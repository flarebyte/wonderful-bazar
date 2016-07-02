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

AWS_ACCESS_KEY_ID = '***'
AWS_SECRET_ACCESS_KEY = '***'
SUPERSONIC_KEY = '***'
SUPERSONIC_URL="http://supersonic.flairbyte.com.s3.amazonaws.com/fe3l/"
SUPERSONIC_BUCKET="supersonic.flairbyte.com"
SUPERSONIC_NODE="fe3l/"

MEDIA_URL="http://media.flairbyte.com/fe3l/"
MEDIA_BUCKET="media.flairbyte.com"
MEDIA_NODE="fe3l/"

MONITOR_BUCKET="monitor.flairbyte.com"


class Exporter:

	def __init__(self):
		pass

	def initialize(self):
		self.access_key_id = AWS_ACCESS_KEY_ID
		self.secret_access_key = AWS_SECRET_ACCESS_KEY
		self.bucket_name = SUPERSONIC_BUCKET
		self.conn = None

	def jsonify(self,mydict):
		return json.dumps(mydict)

	def connect(self):
		self.initialize()
		self.conn = S3.AWSAuthConnection(self.access_key_id, self.secret_access_key)
		# self.generator = S3.QueryStringAuthGenerator(self.access_key_id, self.secret_access_key)
		if (self.conn.check_bucket_exists(self.bucket_name).status == 200):
  			print '----- Bucket OK: '+self.bucket_name
			return True
		else:
			print '----- Bucket not found: '+self.bucket_name
			return False

	def write_to_file(self,mydict,myfile="out.js"):
		json = self.jsonify(mydict)
		fout = open(myfile,"w")
		fout.write(json)
		fout.close()

	def upload_public_json(self,key,mydict):
		print "---- Upload json for key: "+ key
		json = self.jsonify(mydict)
		print "---- Upload json: "+ str(len(json))
		message = self.conn.put(self.bucket_name,key, S3.S3Object(json),{ 'x-amz-acl': 'public-read' , 'Content-Type': 'application/json' }).message
		if (message.find("200 ")>-1):
			return True
		else:
			print message
			return False

	def get_logging_status(self):
		response = self.conn.get_bucket_logging(self.bucket_name,{})
		if not response:
			return None
		return response.body

	def enable_logging(self):
		xml='<?xml version="1.0" encoding="UTF-8" ?><BucketLoggingStatus xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><LoggingEnabled><TargetBucket>monitor.flairbyte.com</TargetBucket><TargetPrefix>logging/supersonic.flairbyte.com-</TargetPrefix></LoggingEnabled></BucketLoggingStatus>'
		r=self.conn.put_bucket_logging(self.bucket_name,xml,{})
		return r.body

	def upload_uuid(self,uuid,mydict):
		key = SUPERSONIC_NODE+SUPERSONIC_KEY+"/uuid/"+uuid+".json"
		return self.upload_public_json(key,mydict)

	def upload_slug(self,slug,mydict):
		key = SUPERSONIC_NODE+SUPERSONIC_KEY+"/slug/"+slug+".json"
		return self.upload_public_json(key,mydict)

	def upload_shortid(self,shortid,mydict):
		key = SUPERSONIC_NODE+SUPERSONIC_KEY+"/shortid/"+shortid+".json"
		return self.upload_public_json(key,mydict)

	def upload_feed(self,feedname,mydict):
		key = SUPERSONIC_NODE+SUPERSONIC_KEY+"/feed/"+feedname+".json"
		return self.upload_public_json(key,mydict)

	def upload_service(self,servicename,mydict):
		key = SUPERSONIC_NODE+SUPERSONIC_KEY+"/service/"+servicename+".json"
		return self.upload_public_json(key,mydict)

	def upload_search(self,searchterm,mydict):
		key = SUPERSONIC_NODE+SUPERSONIC_KEY+"/search/"+searchterm+".json"
		return self.upload_public_json(key,mydict)

#-------------------------------------------------------------------------------------------------------------
class MediaExporter:

	def __init__(self):
		pass

	def initialize(self):
		self.access_key_id = AWS_ACCESS_KEY_ID
		self.secret_access_key = AWS_SECRET_ACCESS_KEY
		self.bucket_name = MEDIA_BUCKET
		self.conn = None

	def connect(self):
		self.initialize()
		self.conn = S3.AWSAuthConnection(self.access_key_id, self.secret_access_key)
		# self.generator = S3.QueryStringAuthGenerator(self.access_key_id, self.secret_access_key)
		if (self.conn.check_bucket_exists(self.bucket_name).status == 200):
  			print '----- Bucket OK: '+self.bucket_name
			return True
		else:
			print '----- Bucket not found: '+self.bucket_name
			return False

	def get_logging_status(self):
		response = self.conn.get_bucket_logging(self.bucket_name,{})
		if not response:
			return None
		return response.body

	def enable_logging(self):
		xml='<?xml version="1.0" encoding="UTF-8" ?><BucketLoggingStatus xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><LoggingEnabled><TargetBucket>monitor.flairbyte.com</TargetBucket><TargetPrefix>logging/media.flairbyte.com-</TargetPrefix></LoggingEnabled></BucketLoggingStatus>'
		r=self.conn.put_bucket_logging(self.bucket_name,xml,{})
		return r.body

	def get_acl(self):
		r = self.conn.get_bucket_acl(self.bucket_name,{})
		return r.body

	def set_acl(self):
		fin=open("media.flairbyte.com.acl.xml")
		acl_xml = fin.read()
		fin.close()
		r = self.conn.put_bucket_acl(self.bucket_name,acl_xml,{})
		return r.body

	def upload_css(self,slug,content):
		path=MEDIA_NODE+"css/"+slug+".css"
		message = self.conn.put(self.bucket_name,path, content,{ 'x-amz-acl': 'public-read' , 'Content-Type': 'text/css' }).message
		if (message.find("200 ")>-1):
			return True
		else:
			print message
			return False

#-------------------------------------------------------------------------------------------------------------

class MonitorExporter:

	def __init__(self):
		pass

	def initialize(self):
		self.access_key_id = AWS_ACCESS_KEY_ID
		self.secret_access_key = AWS_SECRET_ACCESS_KEY
		self.bucket_name = MONITOR_BUCKET
		self.conn = None

	def connect(self):
		self.initialize()
		self.conn = S3.AWSAuthConnection(self.access_key_id, self.secret_access_key)
		# self.generator = S3.QueryStringAuthGenerator(self.access_key_id, self.secret_access_key)
		if (self.conn.check_bucket_exists(self.bucket_name).status == 200):
  			print '----- Bucket OK: '+self.bucket_name
			return True
		else:
			print '----- Bucket not found: '+self.bucket_name
			return False

	def get_acl(self):
		r = self.conn.get_bucket_acl(self.bucket_name,{})
		return r.body

	def set_acl(self):
		fin=open("monitor.flairbyte.com.acl.xml")
		acl_xml = fin.read()
		fin.close()
		r = self.conn.put_bucket_acl(self.bucket_name,acl_xml,{})
		return r.body
