#!/usr/bin/env python
# encoding: utf-8
"""
datasource.py

Created by Olivier Huin on 2010-03-29.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import simplejson as json

import urllib
import ds_settings
import datetime


def json_to_py(text):
	r= json.loads(text)
	return r

def convert_header_date_to_datetime(header_date):
		"""
		Mon, 12 Apr 2010 21:49:57 GMT
		-> 2010-04-12T21:38Z
		"""
		if not header_date:
			return None
		try:
			date_in=header_date.split(",")[1]
			date_in=date_in.replace(" GMT","")
			date_in= datetime.datetime.strptime(date_in.strip(), "%d %b %Y %H:%M:%S")
			r=date_in
			return r
		except:
			return None

def download_public_json(key):
		url=ds_settings.SUPERSONIC_URL+ds_settings.SUPERSONIC_KEY+key+".json"
		furl = urllib.urlopen(url)
		page = furl.read()
		info = furl.info()
		content_type=info.get("Content-Type")
		content_date=info.get("Date")
		content_etag=info.get("Etag")
		print content_etag
		print convert_header_date_to_datetime(content_date)
		success=False
		if "application/json" in content_type:
			success=True
		furl.close()
		if not success:
			return None
		r = json_to_py(page)
		return r

def download_uuid(uuid):
		return download_public_json("/uuid/"+uuid)

def download_slug(slug):
		return download_public_json("/slug/"+slug)

def download_shortid(shortid):
		return download_public_json("/shortid/"+shortid)

def download_feed(feedname):
		return download_public_json("/feed/"+feedname)

def download_service(servicename):
		return download_public_json("/service/"+servicename)

def download_search(servicename):
		return download_public_json("/search/"+servicename)

