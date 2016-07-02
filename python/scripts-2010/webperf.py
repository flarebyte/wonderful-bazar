import os, sys, urllib, httplib, re, string
import tempfile
from math import sin,cos,atan,acos,asin,atan2,sqrt,pi, modf
import time


class WebPerf:

	def __init__(self):
		pass

	def urlopen(self,url):
		try:
			f = urllib.urlopen(url)
			s = f.read()
			f.close()
			return s
		except IOError:
			print "cannot retrieve web page for", url

	def urlhead(self,url):
		try:
			conn  = httplib.HTTPConnection("www.stage.bbc.co.uk",timeout=10)
			print conn
			conn.request("GET", "/mobile/search/searchpagev2?q=batman&x=0&y=0")
			print "\n....\n"
			res = conn.getresponse()
			return res
		except IOError:
			print "cannot retrieve web page for", url
			
	def perf_urlopen(self,url):
		t1 = time.time()
		page = self.urlopen(url)
		t2 = time.time()
		delta = (t2 -t1)*1000
		return delta
		
		
perf = WebPerf()
print perf.perf_urlopen("http://www.bbc.co.uk/mobile/ents/")

#perf.urlhead("http://www.bbc.co.uk/mobile/ents/")

