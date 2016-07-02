#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-05-03.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import flickr
from export import Exporter


class ImagesExporter(Exporter):
	
	def __init__(self):
		self.initialize()
	
	def upload(self):
		if (self.conn==None):
			self.connect()
		if (self.conn==None):
			return False
		photos=self.search_photos("Tate Modern")
		print self.upload_museum_images("TateModern",photos)

	def upload_museum_images(self,imgslug,mydict):
		slug=imgslug+"/img"
		return self.upload_slug(slug,mydict)
		
	def search_photos(self,text):
	    photos = flickr.photos_search(text=text, per_page=9, extras="owner_name,url_sq, url_t, url_s, url_m, url_o")
	    r = []
	    for photo in photos:
			sizes=photo.getSizes()
			nsizes={}
			for size in sizes:
				nsizes[size["label"].lower()]=size
			photodata = {"owner":{"username":photo.owner.username,"realname": photo.owner.realname},"sizes":nsizes}
			r.append(photodata)
	    return r
	
					
exporter = ImagesExporter()
print exporter.upload()

#quicker to just 'hack' the url
#I don't think this works anymore, a change in url format
