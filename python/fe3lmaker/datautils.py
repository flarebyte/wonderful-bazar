#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-02-08.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys, re
import os

from math import sin,cos,atan,acos,asin,atan2,sqrt,pi, modf
from operator import itemgetter
from collections import defaultdict
from stemming.porter2 import stem


nauticalMilePerLat = 60.00721
nauticalMilePerLongitude = 60.10793

rad = pi / 180.0

milesPerNauticalMile = 1.15078
kmsPerNauticalMile = 1.85200

degreeInMiles = milesPerNauticalMile * 60
degreeInKms = kmsPerNauticalMile * 60

earthradius = 6371.0

average_walking_speed_min_per_km = 60.0/3.3
gb_miles_per_km=0.621371192



LINK_HREF,LINK_TEXT,LINK_CSS_CLASS=range(3)

def get_distance_by_haversine(loc1, loc2):
   "Haversine formula - give coordinates as (lat_decimal,lon_decimal) tuples"
   "Adapted from code & formulas by David Z. Creemer and others"

   lat1, lon1 = loc1
   lat2, lon2 = loc2

   # convert to radians
   lon1 = lon1 * pi / 180.0
   lon2 = lon2 * pi / 180.0
   lat1 = lat1 * pi / 180.0
   lat2 = lat2 * pi / 180.0

   # haversine formula
   dlon = lon2 - lon1
   dlat = lat2 - lat1
   a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2.0))**2
   c = 2.0 * atan2(sqrt(a), sqrt(1.0-a))
   km = earthradius * c
   return km

def create_index(datadict,column_id):
	r = {}
	for myuuid in datadict:
		column_value=datadict[myuuid][column_id]
		r[column_value]=myuuid
	return r

def create_slug_index(datadict):
	r = create_index(datadict,ENTITY_SLUG)
	return r

def create_search_index(datadict):
	r = {}
	for myuuid in datadict:
		search_values=datadict[myuuid][ENTITY_SEARCH]
		isearch_list=searchify_list(search_values)
		for isearch in isearch_list:
			r[isearch]=myuuid
	return r
	
def simplify(name):
	r = re.sub("[^A-Za-z0-9]","",name)
	r = r.lower()
	return r

def searchify(name):
	if not name:
		return None
	r = name.lower()
	r = re.sub("[^a-z0-9]"," ",r)
	r = re.sub("(\W|^)((a)|(the))(\W|$)"," ",r)
	r = re.sub("\s+"," ",r)
	words=r.split()
	stemmed_words=list(stem(w) for w in words)
	r = "".join(stemmed_words)
	return r

def searchify_list(searches):
	if not searches:
		return None
	r = list(searchify(search) for search in searches)
	return r

def slugify(name):
	r = re.sub("[^A-Za-z0-9]","",name)
	return r

def find_non_ascii(text):
	r = re.findall("[^A-Za-z0-9-\s,.']",text)
	return r

REGEX_UUID=re.compile("[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}")	
def find_uuids(text):
	return REGEX_UUID.findall(text)

		
def levenshtein(s, t):
	# http://en.wikibooks.org/wiki/Algorithm_implementation/Strings/Levenshtein_distance#Python
    s = ' ' + s
    t = ' ' + t
    d = {}
    S = len(s)
    T = len(t)
    for i in range(S):
        d[i, 0] = i
    for j in range (T):
        d[0, j] = j
    for j in range(1,T):
        for i in range(1,S):
            if s[i] == t[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j] + 1, d[i, j-1] + 1, d[i-1, j-1] + 1)
    return d[S-1, T-1]


def search_levenshtein_suggestions(datadict,column_id,searchterm,threshold):
	r = []
	for myuuid in datadict:
		column_value=datadict[myuuid][column_id]
		lv = levenshtein(simplify(searchterm),simplify(column_value))
		if (lv<threshold):
			r.append(myuuid)
	return r


def soundex(name, len=4):
    """ soundex module conforming to Knuth's algorithm
        implementation 2000-12-24 by Gregory Jorgensen
        public domain
    """

    # digits holds the soundex values for the alphabet
    digits = '01230120022455012623010202'
    sndx = ''
    fc = ''

    # translate alpha chars in name to soundex digits
    for c in name.upper():
        if c.isalpha():
            if not fc: fc = c   # remember first letter
            d = digits[ord(c)-ord('A')]
            # duplicate consecutive soundex digits are skipped
            if not sndx or (d != sndx[-1]):
                sndx += d

    # replace first digit with first alpha character
    sndx = fc + sndx[1:]

    # remove all 0s from the soundex code
    sndx = sndx.replace('0','')

    # return soundex code padded to len characters
    return (sndx + (len * '0'))[:len]


def create_soundex_index(datadict,column_id):
	r = {}
	for myuuid in datadict:
		column_value=datadict[myuuid][column_id]
		soundex_value = soundex(column_value)
		if (r.has_key(soundex_value)):
			r[soundex_value].append(myuuid)
		else:
			r[soundex_value]=[myuuid]
	return r


def search_soundex_suggestions(datadict,searchterm):	
	soundex_searchterm = soundex(searchterm)
	if (datadict.has_key(soundex_searchterm)):
		return datadict[soundex_searchterm]
	else:
		return []

def search_geo_nearest(datadict,column_id,geolocation,km):
	r = []
	for myuuid in datadict:
		geo_value=datadict[myuuid][column_id]
		distance_km = get_distance_by_haversine(geolocation,geo_value)
		if (distance_km>km):
			continue
		r.append(myuuid)
	return r

def search_geo_nearest_many(geo_entities,geolocation,min=4):
	delta_km=0.1
	max_slot=20
	slots = defaultdict(list)
	for myuuid in geo_entities:
		geo_value=geo_entities[myuuid][0:2]
		distance_km = get_distance_by_haversine(geolocation,geo_value)
		slot = int (distance_km/delta_km)
		if (slot>max_slot):
			continue
		slots[slot].append(myuuid)
	r =[]
	for slott in slots:
		r.extend(slots[slott])
		if (len(r)>=min):
			break		
	return r
	
	
def select_rows_from_UUID(datadict,uuids):
	if (uuids==None):
		return None
	r = []
	for uuid in uuids:
		row = datadict[uuid]+(uuid,)
		r.append(row)
	return r

def sort_rows(rows,column_id1,reverse=False):
	rows.sort(key=itemgetter(column_id1),reverse=reverse)
	return rows

def sort_rows3(rows,column_id1,column_id2,column_id3,reverse=False):
	rows.sort(key=itemgetter(column_id1,column_id2,column_id3),reverse=reverse)
	return rows

def prefix_dict(mydict,prefix):
	if (mydict==None):
		return None
	r ={}
	for key in mydict:
		r[prefix+"_"+key]=mydict[key]
	return r
#-------------------------------------------------------------------------
AS_DICT_MODES=("full","ref")

ENTITY_SHORTID,ENTITY_UUID,ENTITY_SLUG,ENTITY_LABEL,ENTITY_SEARCH=range(5)
ENTITY_COLUMNS=("shortid","uuid","slug","label","search")

def get_entity_as_dict(row,datamode="ref"):
	if not row:
		return None
	r = None
	if datamode=="full":
		r = {
		ENTITY_COLUMNS[ENTITY_SHORTID]: row[ENTITY_SHORTID],
		ENTITY_COLUMNS[ENTITY_UUID]: row[ENTITY_UUID],
		ENTITY_COLUMNS[ENTITY_SLUG]: row[ENTITY_SLUG],
		ENTITY_COLUMNS[ENTITY_LABEL]: row[ENTITY_LABEL],
		ENTITY_COLUMNS[ENTITY_SEARCH]: row[ENTITY_SEARCH],
		}
	elif datamode=="ref":
		r = {
		ENTITY_COLUMNS[ENTITY_SHORTID]: row[ENTITY_SHORTID],
		ENTITY_COLUMNS[ENTITY_SLUG]: row[ENTITY_SLUG],
		ENTITY_COLUMNS[ENTITY_LABEL]: row[ENTITY_LABEL],
		}
	else:
		raise NameError('Unknown datamode %s ' % datamode)
	return r

def get_slug(row):
	if not row:
		return None
	return row[ENTITY_SLUG]

def get_shortid(row):
	if not row:
		return None
	return row[ENTITY_SHORTID]

def get_label(row):
	if not row:
		return None
	return row[ENTITY_LABEL]

	
PLACE_LATITUDE,PLACE_LONGITUDE,PLACE_GEOHASH=range(3)
PLACE_COLUMNS=("latitude","longitude","geohash")

def get_entity_geo_as_dict(row):
	if not row:
		return None
	r = {
	PLACE_COLUMNS[PLACE_LATITUDE]: row[PLACE_LATITUDE],
	PLACE_COLUMNS[PLACE_LONGITUDE]: row[PLACE_LONGITUDE],
	PLACE_COLUMNS[PLACE_GEOHASH]: row[PLACE_GEOHASH],
	}
	return {"geo":r}

GEO_ADDRESS_LINES,GEO_ADDRESS_POSTCODE,GEO_ADDRESS_CITY,GEO_ADDRESS_REGION_OR_STATE,GEO_ADDRESS_COUNTRY=range(5)
GEO_ADDRESS_COLUMNS=("lines","postcode","city","region_or_state","country")

def get_entity_geo_address_as_dict(row):
	if not row:
		return None
	r = {
	GEO_ADDRESS_COLUMNS[GEO_ADDRESS_LINES]: row[GEO_ADDRESS_LINES],
	GEO_ADDRESS_COLUMNS[GEO_ADDRESS_POSTCODE]: row[GEO_ADDRESS_POSTCODE],
	GEO_ADDRESS_COLUMNS[GEO_ADDRESS_CITY]: row[GEO_ADDRESS_CITY],
	GEO_ADDRESS_COLUMNS[GEO_ADDRESS_REGION_OR_STATE]: row[GEO_ADDRESS_REGION_OR_STATE],
	GEO_ADDRESS_COLUMNS[GEO_ADDRESS_COUNTRY]: row[GEO_ADDRESS_COUNTRY],
	}
	return {"geo_address": r}

LINK_HREF,LINK_TEXT,LINK_CSS_CLASS=range(3)
LINK_COLUMNS=("href","label","css-class")

CLOUD_HREF,CLOUD_TEXT,CLOUD_RANK=range(3)
CLOUD_COLUMNS=("href","label","rank")

def get_clouds_as_dict(row):
	if not row:
		return None
	r = []
	for item in row:
		cloud ={
		CLOUD_COLUMNS[CLOUD_HREF]: item[CLOUD_HREF],
		CLOUD_COLUMNS[CLOUD_TEXT]: item[CLOUD_TEXT],
		CLOUD_COLUMNS[CLOUD_RANK]: item[CLOUD_RANK]
		}
		r.append(cloud)
	return {"cloud_list":r}

BREADCRUMB_HREF,BREADCRUMB_TEXT=range(2)
BREADCRUMB_COLUMNS=("href","label")

def get_breadcrumbs_as_dict(row):
	if not row:
		return None
	r = []
	for item in row:
		cloud ={
		BREADCRUMB_COLUMNS[BREADCRUMB_HREF]: item[BREADCRUMB_HREF],
		BREADCRUMB_COLUMNS[BREADCRUMB_TEXT]: item[BREADCRUMB_TEXT],
		}
		r.append(cloud)
	return {"breadcrumb_list":r}

SCHEDULE_MONDAY,SCHEDULE_TUESDAY,SCHEDULE_WEDNESDAY,SCHEDULE_THURSDAY,SCHEDULE_FRIDAY,SCHEDULE_SATURDAY,SCHEDULE_SUNDAY=range(7)

SCHEDULE_PERIOD_DATE_START,SCHEDULE_PERIOD_DATE_END=range(2)
SCHEDULE_PERIOD_COLUMNS=("date_start","date_end")

def get_schedule_period_as_dict(row):
	if not row:
		return None
	r = {
	SCHEDULE_PERIOD_COLUMNS[SCHEDULE_PERIOD_DATE_START]: row[SCHEDULE_PERIOD_DATE_START],
	SCHEDULE_PERIOD_COLUMNS[SCHEDULE_PERIOD_DATE_END]: row[SCHEDULE_PERIOD_DATE_END],
	}
	return {"period":r}

EVENT_DATE_START,EVENT_TIME_START,EVENT_DATE_END,EVENT_TIME_END,EVENT_DURATION=range(5)
EVENT_COLUMNS=("date_start","time_start","date_end","time_end","duration")

def get_event_as_dict(row):
	if not row:
		return None
	r = {
	EVENT_COLUMNS[EVENT_DATE_START]: row[EVENT_DATE_START],
	EVENT_COLUMNS[EVENT_TIME_START]: row[EVENT_TIME_START],
	EVENT_COLUMNS[EVENT_DATE_END]: row[EVENT_DATE_END],
	EVENT_COLUMNS[EVENT_TIME_END]: row[EVENT_TIME_END],
	EVENT_COLUMNS[EVENT_DURATION]: row[EVENT_DURATION],
	}
	return {"event":r}


EVENT_HREF,EVENT_LABEL,EVENT_IMG,EVENT_ALT=range(4)
EVENT_COLUMNS=("href","label","img","alt")

def get_events_as_dict(row):
	if not row:
		return None
	r = []
	for item in row:
		event ={
		EVENT_COLUMNS[EVENT_HREF]: item[EVENT_HREF],
		EVENT_COLUMNS[EVENT_LABEL]: item[EVENT_LABEL],
		EVENT_COLUMNS[EVENT_IMG]: item[EVENT_IMG],
		EVENT_COLUMNS[EVENT_ALT]: item[EVENT_ALT],
		}
		r.append(event)
	return {"event_list":r}

QUOTE_TEXT,QUOTE_AUTHOR=range(2)
QUOTE_COLUMNS=("quote","author")

def get_quotes_as_dict(row):
	if not row:
		return None
	r = []
	for item in row:
		quote ={
		QUOTE_COLUMNS[QUOTE_TEXT]: item[QUOTE_TEXT],
		QUOTE_COLUMNS[QUOTE_AUTHOR]: item[QUOTE_AUTHOR],
		}
		r.append(quote)
	return {"quote_list":r}
	
EMAIL_KIND,EMAIL_VALUE=range(2)
EMAIL_COLUMNS=("email_type","email_address")

def get_emails_as_dict(row):
	if not row:
		return None
	r = []
	for item in row:
		email ={
		EMAIL_COLUMNS[EMAIL_KIND]: item[EMAIL_KIND],
		EMAIL_COLUMNS[EMAIL_VALUE]: item[EMAIL_VALUE],
		}
		r.append(email)
	return {"email_list":r}

PHONE_KIND,PHONE_VALUE, PHONE_OPENTIMES=range(3)
PHONE_COLUMNS=("phone_type","phone_number","phone_opentimes")

def get_phones_as_dict(row):
	if not row:
		return None
	r = []
	for item in row:
		phone ={
		PHONE_COLUMNS[PHONE_KIND]: item[PHONE_KIND],
		PHONE_COLUMNS[PHONE_VALUE]: item[PHONE_VALUE],
		PHONE_COLUMNS[PHONE_OPENTIMES]: item[PHONE_OPENTIMES],
		}
		r.append(phone)
	return {"phone_list":r}

def get_sections_as_dict(row, datamode="ref"):
	if not row:
		return None
	r = []
	for item in row:
		section = None
		if datamode=="full":
			section ={
			ENTITY_COLUMNS[ENTITY_SHORTID]: item[ENTITY_SHORTID],
			ENTITY_COLUMNS[ENTITY_UUID]: item[ENTITY_UUID],
			ENTITY_COLUMNS[ENTITY_SLUG]: item[ENTITY_SLUG],
			ENTITY_COLUMNS[ENTITY_LABEL]: item[ENTITY_LABEL],
			ENTITY_COLUMNS[ENTITY_SEARCH]: item[ENTITY_SEARCH],
			}
		elif datamode=="ref":
			section ={
			ENTITY_COLUMNS[ENTITY_SHORTID]: item[ENTITY_SHORTID],
			ENTITY_COLUMNS[ENTITY_SLUG]: item[ENTITY_SLUG],
			ENTITY_COLUMNS[ENTITY_LABEL]: item[ENTITY_LABEL],
			}
		else:
			raise NameError('Unknown datamode %s ' % datamode)	
			
		r.append(section)
	return {"section_list":r}

HIGHLIGHTS_WHENS,HIGHLIGHTS_WHERES,HIGHLIGHTS_DESCRIPTION=range(3)
HIGHLIGHTS_COLUMNS=("whens","wheres","description")

def get_highlights_as_dict(row):
	if not row:
		return None
	r = []
	for item in row:
		highlight ={
		HIGHLIGHTS_COLUMNS[HIGHLIGHTS_DESCRIPTION]: item[HIGHLIGHTS_DESCRIPTION],
		}
		r.append(highlight)
	return {"highlight_list":r}

def get_distance_as_dict(loc1, loc2):
	distance_km=get_distance_by_haversine(loc1,loc2)
	if not distance_km:
		return None
	distance_miles=distance_km*gb_miles_per_km
	minutes=distance_km*average_walking_speed_min_per_km
	r = {"kilometers":distance_km,"miles":distance_miles,"minutes":minutes}
	return r
	
	