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
import mondriancss
import datautils, devutils, datasource
from collections import defaultdict
from export import MediaExporter

NAME_ID=">>>[selector-name]"
		
class Stylesheet(MediaExporter):
	
	def __init__(self):
		self.initialize()
	
	def upload(self):
		if (self.conn==None):
			self.connect()
		if (self.conn==None):
			return False
		stylesheet=mondriancss.get_stylesheet()
		css=self.create_css(stylesheet)
		self.upload_css("base",css)	
		
	def create_css(self,stylesheet):
		r = ""
		for selector in stylesheet:
			name = selector.pop(NAME_ID)
			r+="%s{" % name
			for k in selector:
				r+="%s:%s;" % (k,selector[k])
			r+="}\n"
		return r
				
		


stylesheet=Stylesheet()
stylesheet.upload()

		
	
