#!/usr/bin/env python
# encoding: utf-8
"""
Created by Olivier Huin on 2010-05-08.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os

import sys
import os
import S3
import time
import csv, uuid
import simplejson as json
import datautils, devutils, datasource
from collections import defaultdict

supersonic={"aws_access_key_id": '1P495TGNK68S9TQA57G2',"aws_secret_access_key": "1g4YLGZOkDBAtNoevA84JPfzk3XyPKMWruIZGkVq",
"bucket_name":"supersonic.flairbyte.com","camouflage_key":"fb502a68b7a25e42d8b7b205fd3444b31e"}

	
class DatasourceWriter:
	
	def __init__(self):
		pass
		
	def jsonify(self,mydict):
		return json.dumps(mydict)

	def connect(self,settings):
		self.access_key_id = settings["aws_access_key_id"]
		self.secret_access_key = settings["aws_secret_access_key"]
		self.bucket_name = settings["bucket_name"]
		self.camouflage_key = settings["camouflage_key"]
		self.conn = S3.AWSAuthConnection(self.access_key_id, self.secret_access_key)
		if (self.conn.check_bucket_exists(self.bucket_name).status == 200):
			print '----- Bucket OK: '+self.bucket_name
			return True
		else:
			print '----- Bucket not found: '+self.bucket_name
			return False
		
	def upload_public_json(self,domain,channel,key,version,mydict):
		path="%s/%s/%s/%d/%s.json" %(domain,self.camouflage_key,channel,version,key)
		print "---- Upload json for key: "+ path
		json = self.jsonify(mydict)
		print "---- Upload json: "+ str(len(json))
		
		message = self.conn.put(self.bucket_name,path, S3.S3Object(json),{ 'x-amz-acl': 'public-read' , 'Content-Type': 'application/json' }).message
		if (message.find("200 ")>-1):
			return True
		else:
			print message
			return False
			
