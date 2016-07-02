#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-02-08.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys, re
import os,indexes
from datetime import datetime
from collections import defaultdict
import datautils, uuid

def digitify(uuid, digits=4):
	r = re.sub("[^0-9]","",uuid)
	return r[0:digits]


def beautify_list(mylist):
	r = ",\n".join([beautify(item) for item in mylist])
	return "["+r+"]"

def beautify_tuple(mytuple):
	size=len(mytuple)
	mylist=list(mytuple)
	if mylist[1]=="uuid":
		myuuid = str(uuid.uuid4())
		short_uuids=myuuid.split("-")
		shortid=short_uuids[1]
		mylist[1]=myuuid
		if mylist[0]=="shortid":
			mylist[0]=shortid
	for i in range(size):
		v = mylist[i]
		if type(v)==str:
			mylist[i]=v.strip()	
	mynewtuple=tuple(mylist)
	r = str(mynewtuple)
	return r

def beautify(stuff):
	if (type(stuff)==list):
		r = beautify_list(stuff)
	elif (type(stuff)==tuple):
		r = beautify_tuple(stuff)
	else:
		r = str(stuff)
	return r
	
ACCENT_REMOVAL_DICT={
   "\xC3\x80" : "A",   "\xC3\x81" : "A",   "\xC3\x82" : "A",   "\xC3\x83" : "A",
      "\xC3\x84" : "A",   "\xC3\x85" : "A",   "\xC3\x86" : "AE",  "\xC3\x87" : "C",
      "\xC3\x88" : "E",   "\xC3\x89" : "E",   "\xC3\x8A" : "E",   "\xC3\x8B" : "E",
      "\xC3\x8C" : "I",   "\xC3\x8D" : "I",   "\xC3\x8E" : "I",   "\xC3\x8F" : "I",
      "\xC3\x90" : "D",   "\xC3\x91" : "N",   "\xC3\x92" : "O",   "\xC3\x93" : "O",
      "\xC3\x94" : "O",   "\xC3\x95" : "O",   "\xC3\x96" : "O",   "\xC3\x98" : "O",
      "\xC3\x99" : "U",   "\xC3\x9A" : "U",   "\xC3\x9B" : "U",   "\xC3\x9C" : "U",
      "\xC3\x9D" : "Y",   "\xC3\x9E" : "P",   "\xC3\x9F" : "ss",
      "\xC3\xA0" : "a",   "\xC3\xA1" : "a",   "\xC3\xA2" : "a",   "\xC3\xA3" : "a",
      "\xC3\xA4" : "a",   "\xC3\xA5" : "a",   "\xC3\xA6" : "ae",  "\xC3\xA7" : "c",
      "\xC3\xA8" : "e",   "\xC3\xA9" : "e",   "\xC3\xAA" : "e",   "\xC3\xAB" : "e",
      "\xC3\xAC" : "i",   "\xC3\xAD" : "i",   "\xC3\xAE" : "i",   "\xC3\xAF" : "i",
      "\xC3\xB0" : "o",   "\xC3\xB1" : "n",   "\xC3\xB2" : "o",   "\xC3\xB3" : "o",
      "\xC3\xB4" : "o",   "\xC3\xB5" : "o",   "\xC3\xB6" : "o",   "\xC3\xB8" : "o",
      "\xC3\xB9" : "u",   "\xC3\xBA" : "u",   "\xC3\xBB" : "u",   "\xC3\xBC" : "u",
      "\xC3\xBD" : "y",   "\xC3\xBE" : "p",   "\xC3\xBF" : "y",
      "\xC4\x80" : "A",   "\xC4\x81" : "a",   "\xC4\x82" : "A",   "\xC4\x83" : "a",
      "\xC4\x84" : "A",   "\xC4\x85" : "a",   "\xC4\x86" : "C",   "\xC4\x87" : "c",
      "\xC4\x88" : "C",   "\xC4\x89" : "c",   "\xC4\x8A" : "C",   "\xC4\x8B" : "c",
      "\xC4\x8C" : "C",   "\xC4\x8D" : "c",   "\xC4\x8E" : "D",   "\xC4\x8F" : "d",
      "\xC4\x90" : "D",   "\xC4\x91" : "d",   "\xC4\x92" : "E",   "\xC4\x93" : "e",
      "\xC4\x94" : "E",   "\xC4\x95" : "e",   "\xC4\x96" : "E",   "\xC4\x97" : "e",
      "\xC4\x98" : "E",   "\xC4\x99" : "e",   "\xC4\x9A" : "E",   "\xC4\x9B" : "e",
      "\xC4\x9C" : "G",   "\xC4\x9D" : "g",   "\xC4\x9E" : "G",   "\xC4\x9F" : "g",
      "\xC4\xA0" : "G",   "\xC4\xA1" : "g",   "\xC4\xA2" : "G",   "\xC4\xA3" : "g",
      "\xC4\xA4" : "H",   "\xC4\xA5" : "h",   "\xC4\xA6" : "H",   "\xC4\xA7" : "h",
      "\xC4\xA8" : "I",   "\xC4\xA9" : "i",   "\xC4\xAA" : "I",   "\xC4\xAB" : "i",
      "\xC4\xAC" : "I",   "\xC4\xAD" : "i",   "\xC4\xAE" : "I",   "\xC4\xAF" : "i",
      "\xC4\xB0" : "I",   "\xC4\xB1" : "i",   "\xC4\xB2" : "IJ",  "\xC4\xB3" : "ij",
      "\xC4\xB4" : "J",   "\xC4\xB5" : "j",   "\xC4\xB6" : "K",   "\xC4\xB7" : "k",
      "\xC4\xB8" : "k",   "\xC4\xB9" : "L",   "\xC4\xBA" : "l",   "\xC4\xBB" : "L",
      "\xC4\xBC" : "l",   "\xC4\xBD" : "L",   "\xC4\xBE" : "l",   "\xC4\xBF" : "L",
      "\xC5\x80" : "l",   "\xC5\x81" : "L",   "\xC5\x82" : "l",   "\xC5\x83" : "N",
      "\xC5\x84" : "n",   "\xC5\x85" : "N",   "\xC5\x86" : "n",   "\xC5\x87" : "N",
      "\xC5\x88" : "n",   "\xC5\x89" : "n",   "\xC5\x8A" : "N",   "\xC5\x8B" : "n",
      "\xC5\x8C" : "O",   "\xC5\x8D" : "o",   "\xC5\x8E" : "O",   "\xC5\x8F" : "o",
      "\xC5\x90" : "O",   "\xC5\x91" : "o",   "\xC5\x92" : "CE",  "\xC5\x93" : "ce",
      "\xC5\x94" : "R",   "\xC5\x95" : "r",   "\xC5\x96" : "R",   "\xC5\x97" : "r",
      "\xC5\x98" : "R",   "\xC5\x99" : "r",   "\xC5\x9A" : "S",   "\xC5\x9B" : "s",
      "\xC5\x9C" : "S",   "\xC5\x9D" : "s",   "\xC5\x9E" : "S",   "\xC5\x9F" : "s",
      "\xC5\xA0" : "S",   "\xC5\xA1" : "s",   "\xC5\xA2" : "T",   "\xC5\xA3" : "t",
      "\xC5\xA4" : "T",   "\xC5\xA5" : "t",   "\xC5\xA6" : "T",   "\xC5\xA7" : "t",
      "\xC5\xA8" : "U",   "\xC5\xA9" : "u",   "\xC5\xAA" : "U",   "\xC5\xAB" : "u",
      "\xC5\xAC" : "U",   "\xC5\xAD" : "u",   "\xC5\xAE" : "U",   "\xC5\xAF" : "u",
      "\xC5\xB0" : "U",   "\xC5\xB1" : "u",   "\xC5\xB2" : "U",   "\xC5\xB3" : "u",
      "\xC5\xB4" : "W",   "\xC5\xB5" : "w",   "\xC5\xB6" : "Y",   "\xC5\xB7" : "y",
      "\xC5\xB8" : "Y",   "\xC5\xB9" : "Z",   "\xC5\xBA" : "z",   "\xC5\xBB" : "Z",
      "\xC5\xBC" : "z",   "\xC5\xBD" : "Z",   "\xC5\xBE" : "z",   "\xC6\x8F" : "E",
      "\xC6\xA0" : "O",   "\xC6\xA1" : "o",   "\xC6\xAF" : "U",   "\xC6\xB0" : "u",
      "\xC7\x8D" : "A",   "\xC7\x8E" : "a",   "\xC7\x8F" : "I",
      "\xC7\x90" : "i",   "\xC7\x91" : "O",   "\xC7\x92" : "o",   "\xC7\x93" : "U",
      "\xC7\x94" : "u",   "\xC7\x95" : "U",   "\xC7\x96" : "u",   "\xC7\x97" : "U",
      "\xC7\x98" : "u",   "\xC7\x99" : "U",   "\xC7\x9A" : "u",   "\xC7\x9B" : "U",
      "\xC7\x9C" : "u",
      "\xC7\xBA" : "A",   "\xC7\xBB" : "a",   "\xC7\xBC" : "AE",  "\xC7\xBD" : "ae",
      "\xC7\xBE" : "O",   "\xC7\xBF" : "o",
      "\xC9\x99" : "e",

      "\xC2\x82" : ",",    
      "\xC2\x84" : ",,",       
      "\xC2\x85" : "...",      
      "\xC2\x88" : "^",        
      "\xC2\x91" : "\x27",     # Forward single quote
      "\xC2\x92" : "\x27",     # Reverse single quote
      "\xC2\x93" : "\x22",     # Forward double quote
      "\xC2\x94" : "\x22",     # Reverse double quote
      "\xC2\x96" : "-",        # High hyphen
      "\xC2\x97" : "--",       # Double hyphen
      "\xC2\xA6" : "|",        # Split vertical bar
      "\xC2\xAB" : "<<",       # Double less than
      "\xC2\xBB" : ">>",       # Double greater than
      "\xC2\xBC" : "1/4",      # one quarter
      "\xC2\xBD" : "1/2",      # one half
      "\xC2\xBE" : "3/4",      # three quarters

      "\xCA\xBF" : "\x27",     # c-single quote
      "\xCC\xA8" : "",         # modifier - under curve
      "\xCC\xB1" : ""          # modifier - under line
}
def accent_removal(text):
	#r = text.maketrans(NON_ASCII,AS_ASCII)
	r = text
	for key in ACCENT_REMOVAL_DICT:
		r=r.replace(key.lower(),ACCENT_REMOVAL_DICT[key])
	return r

def key_value_row(key,value,comment=None):
	if comment==None:
		r = ''.join(['"',key,'":'+str(value),",\n"])
	else:
		r = ''.join(['"',key,'":'+str(value),", # ",comment,"\n"])
	return r
	
def save_additions(entitydict,customdict,defaulttuple="()",label_id=datautils.ENTITY_LABEL,filename="out.py"):
	fout = open (filename,"w")
	for k in entitydict:
		if k in customdict:
			data = beautify(customdict[k])
		else:
			data = defaulttuple
		s = ''.join(['"',k,'":'+data,", # ",entitydict[k][label_id],"\n"])
		fout.write(s)
	fout.close()

def save_highlights(entitydict,customdict,defaulttuple="()",filename="out.py"):
	label_id=datautils.ENTITY_LABEL
	fout = open (filename,"w")
	for k in entitydict:
		if k in customdict:
			data = beautify(customdict[k])
		else:
			data = defaulttuple
		comments = [entitydict[k][label_id]]
		#if indexutils.find_uuids(data):
			#comments2 = '\n"""\n'+indexutils.labelify(data)+ '\n"""\n'
		comments2=""
		comments.append(comments2)
		comment = ",".join(comments)
		s = ''.join(['"',k,'":'+data,", # ",comment,"\n"])
		fout.write(s)
	fout.close()

def save_entities(entitydict,addrows=0,filename="out.py"):
	for i in range(addrows):
		myuuid = str(uuid.uuid4())
		short_uuids=myuuid.split("-")
		shortid=short_uuids[1]
		mytuple=(shortid,myuuid,None,"",[])
		entitydict[myuuid]=mytuple		
	fout = open (filename,"w")
	fout.write("#!/usr/bin/env python\n")
	fout.write("# encoding: utf-8\n")
	fout.write("\n")	
	fout.write("entities={\n")
	for k in entitydict:
		s = key_value_row(k,entitydict[k])
		fout.write(s)
	fout.write("}\n")			
	fout.close()

def save_links_to_html(entitydict,linksdict,urlprefix="",htmlfile="links.html"):
	fout = open (htmlfile,"w")
	fout.write("<html><head></head><body><ul>")
	for uuid in linksdict:
		link = urlprefix+linksdict[uuid]
		s = '<li><a href="%s">%s</a></li>' % (link,link)
		fout.write(s)
	fout.write("</ul></body></head>")
	fout.close()

def label(uuid):
	return indexes.indexes.get(uuid)

	
class IndexCreation:
	def __init__(self,indexfile="indexes.py"):
		self.indexfile=indexfile
	def open(self):
		self.fout = open(self.indexfile,"w")
		self.fout.write("#!/usr/bin/env python\n")
		self.fout.write("# encoding: utf-8\n")
		self.fout.write("\n")	
		self.fout.write("indexes={\n")
	def close(self):
		self.fout.write("}\n")			
		self.fout.close()
	def write_entities(self,entitiesdict,urlprefix="/",css_class=""):
		for uuid in entitiesdict:
			entity = entitiesdict[uuid]
			myindex=(urlprefix+entity[datautils.ENTITY_SLUG],entity[datautils.ENTITY_LABEL],css_class)
			s=key_value_row(uuid,myindex)
			self.fout.write(s)
	
	def write_entities_parts(self,entitiesdict,entitiespartsdict,urlprefix="/",css_class=""):
		for uuid in entitiespartsdict:
			parts=entitiespartsdict[uuid]
			entity=entitiesdict[uuid]
			for part in parts:
				partuuid=part[datautils.ENTITY_UUID]
				myindex=(urlprefix+entity[datautils.ENTITY_SLUG]+"/"+part[datautils.ENTITY_SHORTID],part[datautils.ENTITY_LABEL],css_class)
				s=key_value_row(partuuid,myindex)
				self.fout.write(s)


def lenght_compare(x,y):
	if len(x)==len(y):
		return 0
	elif len(x)<len(y):
		return 1
	else: #len(x)<len(y):
		return -1

class SearchIndexCreation:
	def __init__(self,indexfile="searchindexes.py"):
		self.indexfile=indexfile
		self.listofregex = []
	def open(self):
		self.fout = open(self.indexfile,"w")
		self.fout.write("#!/usr/bin/env python\n")
		self.fout.write("# encoding: utf-8\n")
		self.fout.write("\n")	
		self.fout.write("import re\n")	
		self.fout.write("searchindexes=[\n")
	def close(self):
		self.fout.write("]\n")			
		self.fout.close()
	def write_entities(self,entitiesdict):
		re_space=re.compile("[\s.,'-]+")
		for uuid in entitiesdict:
			for term in entitiesdict[uuid][datautils.ENTITY_SEARCH]:
				regex=re_space.sub("\s+",term.lower())
				regex="(^|\W)("+regex+"[s]?)(\W|$)"
				s="(re.compile('"+regex+"', re.IGNORECASE)"+',"\g<1>'+uuid+'\g<3>"),\n'
				self.listofregex.append(s)
	def sort(self):
		self.listofregex.sort(cmp=lenght_compare)
	def save(self):
		for row in self.listofregex:
			self.fout.write(row)
	
				
def check_entity_doublons(entitydict):
	shortids=defaultdict(int)
	slugs=defaultdict(int)
	for uuid in entitydict:
		shortid=entitydict[uuid][datautils.ENTITY_SHORTID]
		slug=entitydict[uuid][datautils.ENTITY_SLUG]
		shortids[shortid]+=1
		slugs[slug]+=1
	r=[]
	for shortid in shortids:
		if shortids[shortid]>1:
			r.append(shortid)
	for slug in slugs:
		if slugs[slug]>1:
			r.append(slug)
	return r

def reindex_entities(entitydict,length_shortid=4,force=False):
	r = {}
	for uuid in entitydict:
		mytuple=entitydict[uuid]
		shortid=entitydict[uuid][datautils.ENTITY_SHORTID]
		search=entitydict[uuid][datautils.ENTITY_SEARCH]
		label=entitydict[uuid][datautils.ENTITY_LABEL]
		if (not shortid) or (force==True):
			shortid=digitify(uuid,length_shortid)
		slug=entitydict[uuid][datautils.ENTITY_SLUG]
		if not slug:
			slug=label
		if not search:
			search=[label]
		newtuple=(shortid,uuid,slug,label,search)
		r[uuid]=newtuple
	return r

def risk_slugify_entities(entitydict):
	r = {}
	for uuid in entitydict:
		mytuple=entitydict[uuid]
		shortid=entitydict[uuid][datautils.ENTITY_SHORTID]
		label=entitydict[uuid][datautils.ENTITY_LABEL]
		is_label_non_ascii = datautils.find_non_ascii(label)
		kiss_label = accent_removal(label)
		is_kiss_non_ascii = datautils.find_non_ascii(kiss_label)
		slug=datautils.slugify(kiss_label)
		search = [label]
		if is_label_non_ascii:
			search.append(kiss_label)
		newtuple=(shortid,uuid,slug,label,search)
		if not is_kiss_non_ascii:
			r[uuid]=newtuple
	return r

class Chronometer:
	def __init__(self):
		self.previous = datetime.now()		
	def freeze(self, text):
		newtime = datetime.now()
		delta = newtime - self.previous
		self.previous = newtime
		return text +" : " +str(delta)
		
		
			


	