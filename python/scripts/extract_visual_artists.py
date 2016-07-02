#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-03-20.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import re
import devutils, uuid, datautils
import artists 

RE_GUID=re.compile("^(.+)/guid/")

def process():
	fin = open ("visual_artist.tsv")
	r = {}
	lines = fin.readlines()
	for line in lines:
		m = RE_GUID.search(line)
		if m:
			artist = m.group(1)
			artist=artist.strip()
			myuuid = str(uuid.uuid4())
			mytuple = (devutils.digitify(myuuid,7), myuuid, datautils.slugify(artist), artist, [artist])
			r[myuuid]=mytuple	
	fin.close()
	devutils.save_entities(r)

def reindex():
	newartists=devutils.risk_slugify_entities(artists.artists)
	devutils.save_entities(newartists)

reindex()