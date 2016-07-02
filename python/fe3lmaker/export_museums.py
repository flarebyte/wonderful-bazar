#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-03-22.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import S3
import time
import csv, uuid
import simplejson as json
import museums
import datautils, devutils, datasource
from collections import defaultdict
from export import Exporter

		
class Museums(Exporter):
	
	def __init__(self):
		self.initialize()
		self.event_spreadsheet=MuseumEventSpreadsheet()
	
	def upload(self):
		if (self.conn==None):
			self.connect()
		if (self.conn==None):
			return False

		self.event_spreadsheet.load_norm_csv()
		self.event_spreadsheet.group_by_place()
		
		uuid="52c859bb-c59b-43c1-9371-af05df1ab638"
		print self.upload_museum(uuid)
		print self.upload_museum_events(uuid)
		#print self.upload_museum_restaurants(uuid)

	def upload_museum(self,uuid):
		mydict=self.create_entity(uuid)
		slug=datautils.get_slug(museums.entities[uuid])
		return self.upload_slug(slug,mydict)
	
	def upload_museum_events(self,uuid):
		mydict=self.create_entity_events(uuid)
		slug=datautils.get_slug(museums.entities[uuid])+"/evt"
		return self.upload_slug(slug,mydict)

	def upload_museum_restaurants(self,uuid):
		mydict=self.create_entity_restaurants(uuid)
		slug=datautils.get_slug(museums.entities[uuid])+"/rest"
		return self.upload_slug(slug,mydict)

	def write_museum(self,uuid):
		mydict=self.create_entity(uuid)
		return self.write_to_file(mydict)
	
	def create_entity(self,uuid):
		r = museums.get_data_as_dict(uuid)
		return r

	def create_entity_restaurants(self,uuid):
		r = museums.get_entity_restaurants(uuid)
		return r

	def create_entity_events(self,uuid):
		r = self.event_spreadsheet.get_event_list_as_dict(uuid)
		return r
	
	def export_to_csv(self):
		reftable_writer = csv.writer(open('museums.csv', 'w'))
		for uuid in museums.entities:
			(entity_shortid,myuuid,entity_slug,entity_label,entity_search)=museums.entities[uuid]
			reftable_writer.writerow([uuid,entity_label])

class MuseumEventSpreadsheet:
	def __init__(self):
		self.filename="/Users/olivierhuin/Desktop/art-exhibitions-london-fe3l-private.csv"
		
	def normalize_place(self, place):
		if not place:
			return None
		uuids = datautils.find_uuids(place)
		place_uuid = uuids[0]
		place_name = museums.entities[place_uuid][2]
		return place_uuid + "/" + place_name
	
	def load_norm_csv(self):
		eventreader = csv.reader(open(self.filename))
		headers=eventreader.next()
		self.events={}
		for row in eventreader:
			entity_shortid,entity_uuid,entity_slug,entity_label,entity_search,event_place,event_start,event_end,event_description=row
			if not entity_uuid:
				entity_uuid = str(uuid.uuid4())
			if not entity_shortid:
				entity_shortid = devutils.digitify(entity_uuid,7)
			event_place=self.normalize_place(event_place)
			newrow=(entity_shortid,entity_uuid,entity_slug,entity_label,entity_search,event_place,event_start,event_end,event_description)
			self.events[entity_uuid]=newrow
					
	def save_csv(self):
		self.load_norm_csv()
		if not self.events:
			return
		event_writer = csv.writer(open('art-exhibitions-london.csv', 'w'))
		headers=("entity_shortid","entity_uuid","entity_slug","entity_label","entity_search","event_place","event_start","event_end","event_description")
		event_writer.writerow(headers)
		for uuid in self.events:
			event_writer.writerow(self.events[uuid])
	
	def group_by_place(self):
		if not self.events:
			return
		self.places = defaultdict(list)
		for uuid in self.events:
			place_uuids=datautils.find_uuids(self.events[uuid][5])
			self.places[place_uuids[0]].append(uuid)
			
			
	def get_event_list_as_dict(self,place_uuid):
		event_uuids=self.places.get(place_uuid)
		if not event_uuids:
			return None
		r = []
		for uuid in event_uuids:
			row=self.events[uuid]
			entity_shortid,entity_uuid,entity_slug,entity_label,entity_search,event_place,event_start,event_end,event_summary=row
			event_dict = datautils.get_entity_as_dict(row[0:5])
			schedule_period = datautils.get_schedule_period_as_dict((event_start,event_end))
			event_dict.update(schedule_period)
			event_dict["official_summary"]=event_summary
			r.append(event_dict)
		return {"events" : r}
			

		
mymuseums = Museums()
mymuseums.upload()
	
