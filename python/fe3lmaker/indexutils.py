#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-03-08.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import re
from datetime import datetime
import devutils

class Chronometer:
	def __init__(self):
		self.previous = datetime.now()		
	def freeze(self, text):
		newtime = datetime.now()
		delta = newtime - self.previous
		self.previous = newtime
		return text +" : " +str(delta)

chrono = Chronometer()

import indexes,searchindexes, indexes_artists, searchindexes_artists
print chrono.freeze("import")


def uuidify(text):
	si=searchindexes.searchindexes
	si_artists = searchindexes_artists.searchindexes
	for kv in si:
		text=kv[0].sub(kv[1],text)
	for kv in si_artists:
		text=kv[0].sub(kv[1],text)
	return text

def uuidify_list(mylist):
	if not mylist:
		return mylist
	r = []
	for part in mylist:
		part = uuidify(part)
		r.append(part)
	return r	

REGEX_UUID=re.compile("[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}")	
def find_uuids(text):
	return REGEX_UUID.findall(text)
	
def labelify(text):
	uuids=find_uuids(text)
	print chrono.freeze("find_uuids")
	i=indexes.indexes
	print chrono.freeze("load indexes")
	i_artists=indexes_artists.indexes
	for uuid in uuids:
		if uuid in i:
			text=text.replace(uuid,i[uuid][1])
	uuids=find_uuids(text)
	print chrono.freeze("replace_index")
	for uuid in uuids:
		if uuid in i_artists:
			text=text.replace(uuid,i_artists[uuid][1])
	print chrono.freeze("replace_artists")
	return text

def uuidify_highlights(entitiespartsdict):	
	r={}
	for uuid in entitiespartsdict:
		mylist=entitiespartsdict[uuid]
		if not mylist:
			continue
		newlist=[]
		for mytuple in mylist:
			whens=mytuple[0]
			wheres=mytuple[1]
			what=mytuple[2]
			newwhens=uuidify_list(whens)
			newwheres=uuidify_list(wheres)
			what=uuidify(what)
			newtuple=(newwhens,newwheres,what)
			newlist.append(newtuple)
		r[uuid]=newlist
	return r

def get_label(uuid):
	mytuple = indexes.indexes.get(uuid)
	if not mytuple:
		return None
	return mytuple[1]
	
