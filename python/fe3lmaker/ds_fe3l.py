#!/usr/bin/env python
# encoding: utf-8
"""
ds_fe3l.py

Created by Olivier Huin on 2010-04-03.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import datasource

def download_tubes():
	r = datasource.download_feed("tubes")
	return r
	
def download_museum(slug,usecache=True):
	r = datasource.download_slug(slug)
	return r

def download_museum_events(slug,usecache=True):
	key=slug+"/evt"
	r = datasource.download_slug(key)
	return r

def download_museum_restaurants(slug,usecache=True):
	key=slug+"/res"
	r = datasource.download_slug(key)
	return r

def upload_cache(mydict):
	from export import Exporter
	exporter = Exporter()
	exporter.connect()
	exporter.upload_slug("cache/TateModern",mydict)

def find_color_for_tube(tube_shortid,tubesfeed):
	root=tubesfeed["tubesfeed"]
	orange=root.get("orange")
	if orange:
		for tube in orange:
			if tube_shortid==tube["tube"]["shortid"]:
				return "orange"
	red=root.get("red")
	if red:
		for tube in red:
			if tube_shortid==tube["tube"]["shortid"]:
				return "red"
	return "green"

def merge_with_tube_news(museum,tubes):
	tube_list=museum["museum"]["tube_list"]
	for tube in tube_list:
		shortid=tube["tube"]["shortid"]
		status=find_color_for_tube(shortid,tubes)
		tube["tube"]["travelstatus"]=status

download_museum("TateModern")