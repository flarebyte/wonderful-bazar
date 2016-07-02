#! /usr/bin/python
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "olivierhuin"
__date__ = "$Sep 17, 2009 10:34:28 PM$"

if __name__ == "__main__":
    print "Hello World";

import s3
from common.services import Service
from django.utils import simplejson as json


class S3Storage(Service):
    """
    Base class for the S3 storage service
    """
    def __init__(self):
        self.connection = None
        self.generator = None

    def get_connection(self):
        if (self.connection is not None):
            return self.connection
        self.connection = s3.AWSAuthConnection(self.configuration["aws_access_key_id"], self.configuration["aws_secret_access_key"])
        return self.connection

    def get_generator(self):
        if (self.generator is not None):
            return self.generator
        self.generator = s3.QueryStringAuthGenerator(self.configuration["aws_access_key_id"], self.configuration["aws_secret_access_key"])
        return self.generator

    def get_new_generator(self, expiration_in_sec):
        r = s3.QueryStringAuthGenerator(self.configuration["aws_access_key_id"], self.configuration["aws_secret_access_key"])
        r.set_expires_in(expiration_in_sec)
        return r

    def is_http_response_successful(self,response):
        if response.http_response.status< 300:
            return True
        else:
            return False

    def log_http_response_failure(self, response):
        self.logger.warning(response.message)


class PutObjectService(S3Storage):
    """
    This service allows to publish an object the cloud
    """
    def __init__(self):
       super(self).__init__()
    
    def perform(self,  **kwargs):
        bucket_name = self.get_param_or_conf("bucket_name", kwargs)
        key_name = self.get_param("key_name", kwargs)
        content = self.get_param("content", kwargs)
        content_type = self.get_param_or_conf("content_type", kwargs)
        access_control_list = self.get_param_or_conf("access_control_list", kwargs)
        metadata={'x-amz-acl': access_control_list , 'Content-Type': content_type}
        headers={'Content-Type': content_type}
        self.put_object(bucket_name, key_name, content, content_type)
        
    def put_object(self, bucket_name, key_name, content, metadata, headers):
        response = self.get_connection.put(bucket_name, key_name, s3.S3Object(content,metadata),headers)

        if (self.is_http_response_successful(response)):
            self.logger.info("PutObjectService: %s, %s, %s ",bucket_name, key_name, content_type)
        else:
            self.log_http_response_failure(response)
       

class GetObjectService(Storage):

   def perform(self, ** kwargs):
       bucket_name = self.get_param_or_conf("bucket_name", kwargs)
       key_name = self.get_param("key_name", "", kwargs)
       self.get_object(bucket_name, key_name)

   def get_object(self, bucket_name, key_name):
       return self.get_connection.get(bucket_name, key_name).object.data

class GetURLService(S3Storage):

   def perform(self, ** kwargs):
       bucket_name = self.get_param_or_conf("bucket_name", kwargs)
       key_name = self.get_param("key_name", "", kwargs)
       self.get_URL(bucket_name, key_name)

   def get_URL(self, bucket_name, key_name):
       return self.get_generator.make_bare_url(bucket_name, key_name + '-public')

class GetExpirableURLService(S3Storage):

   def perform(self, ** kwargs):
       bucket_name = self.get_param_or_conf("bucket_name", kwargs)
       key_name = self.get_param("key_name", "", kwargs)
       expiration_in_s = self.get_param("expiration_in_s", 3600, kwargs)
       self.get_expirable_URL(bucket_name, key_name, expiration_in_s)

   def get_expirable_URL(self, bucket_name, key_name, expiration_in_s):
       self.get_new_generator(expiration_in_s).get(bucket_name, key_name)

class DeleteObjectService(S3Storage):

   def perform(self, ** kwargs):
       bucket_name = self.get_param_or_conf("bucket_name", kwargs)
       key_name = self.get_param("key_name", "", kwargs)
       self.delete_object(bucket_name, key_name)

   def delete_object(self, bucket_name, key_name):
       return self.get_connection.delete(bucket_name, key_name).message


   def storage_strategy_resolver(strategy):
       """ Example: ws:put/xml/expirable/private """
       parts = strategy.split("/")

   if (parts[0] == "ws:put"):

   if ("expirable" in parts):
   return None

   if ("private" in parts):
   return None

   if (parts[0] == "ws:get"):


   if (parts[0] == "ws:delete")

   if ("json" in parts):
            return None

    if ("xml" in parts):
            return None


 