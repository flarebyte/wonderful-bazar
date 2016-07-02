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
import datautils, devutils, datasource
from collections import defaultdict
from export import Exporter
import tubes, tfl
from tfl import TubeCrawler

		
class TubeExporter(Exporter):
	
	def __init__(self):
		self.initialize()
	
	def upload(self):
		if (self.conn==None):
			self.connect()
		if (self.conn==None):
			return False
		print self.upload_tubes()
		

	def upload_tubes(self):
		mydict = self.crawl_tubes()
		return self.upload_feed("tubes",mydict)
			
	def crawl_tubes(self):
		crawler = TubeCrawler()
		info=crawler.tube_stations_normalized()
		if not info:
			return None
		(green,orange,red,todebug,crawled)=info
		r = defaultdict(list)
		if crawled:
			r["crawled"]=crawled
		if todebug:
			for uuid in todebug:
				tube_entity=tubes.get_data_as_dict(uuid)
				r["debug"].append(tube_entity)
		if green:
			for uuid in green:
				tube_entity=tubes.get_data_as_dict(uuid)
				r["green"].append(tube_entity)
		if orange:
			for uuid in orange:
				tube_entity=tubes.get_data_as_dict(uuid)
				r["orange"].append(tube_entity)
		if red:
			for uuid in red:
				tube_entity=tubes.get_data_as_dict(uuid)
				r["red"].append(tube_entity)
		return {"tubesfeed": r}

		
exporter = TubeExporter()
print exporter.upload()
	
