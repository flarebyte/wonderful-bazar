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
from datasource.dswriter import DatasourceWriter

VERSION=1

def build_dsWriter():
	supersonic={"aws_access_key_id": '1P495TGNK68S9TQA57G2',"aws_secret_access_key": "1g4YLGZOkDBAtNoevA84JPfzk3XyPKMWruIZGkVq",
	"bucket_name":"supersonic.flairbyte.com","camouflage_key":"fb502a68b7a25e42d8b7b205fd3444b31e"}
	r = DatasourceWriter()
	r.connect(supersonic)
	return r
		
class Preferences:
	
	def __init__(self):
		self.dsWriter=build_dsWriter()
		self.prefs_spreadsheet=PreferencesSpreadsheet()
	
	def upload(self):
		self.prefs_spreadsheet.load_csv()
		print self.upload_preferences()
	
	def upload_preferences(self):
		for page in self.create_all_pref_pages():
			slug="prefs/"+page["slug"]
			self.dsWriter.upload_public_json("fe3l","service",slug,VERSION,page)
		index_prefs=self.create_prefs()
		self.dsWriter.upload_public_json("fe3l","service","prefs",VERSION,index_prefs)
	
	def create_all_pref_pages(self):
		r = self.prefs_spreadsheet.get_preferences_as_dict()
		return r
		
	def create_prefs(self):
		pages = self.prefs_spreadsheet.get_preferences_as_dict()
		page_list=[]
		for page in pages:
			current_page = {"label": page["label"],"slug": page["slug"],"summary": page["summary"]}	
			page_list.append(current_page)
		r={"slug":"prefs","label":"Preferences","page_list":page_list,"breadcrumb_list":[]}
		return r
		
class PreferencesSpreadsheet:
	def __init__(self):
		self.filename="/Users/olivierhuin/Desktop/preferences.csv"
			
	def load_csv(self):
		prefsreader = csv.reader(open(self.filename))
		headers=prefsreader.next()
		self.pages=[]
		current_page=None
		current_sections = None
		current_section=None
		current_keyvalues=None
		current_operation=None
		for row in prefsreader:
			key,value,cookie,operation,label,page,section,summary,page_summary,stop=row
			if not value:
				continue
			if page:
				current_sections=[]
				current_page={"label": page,"slug": datautils.slugify(page.lower()),"summary": page_summary,"section_list":current_sections,"breadcrumb_list":[{"href":"/prefs","label":"Preferences"}]}
				self.pages.append(current_page)
			if section:
				current_operation=operation
				current_keyvalues=[]
				if current_operation=="select_one":
					current_section={"label": section,"cookie":cookie,"operation":operation,"key":key, "pref_list": current_keyvalues}
				if current_operation=="yes_no":
					current_section={"label": section,"cookie":cookie,"operation":operation,"pref_list": current_keyvalues}
				
				current_sections.append(current_section)
			
			if current_operation=="select_one":
				current_keyvalues.append({"value":value,"label":label, "summary":summary})
			if current_operation=="yes_no":
				label_yes,label_no=label.split("/")
				current_keyvalues.append({"key":key,"label_yes":label_yes,"label_no":label_no, "summary":summary})
			
											
	def get_preferences_as_dict(self):
		return self.pages

prefs=Preferences()
prefs.upload()

		
	
