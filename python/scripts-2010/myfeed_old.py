import os, sys, urllib, re, string
import tempfile
from math import sin,cos,atan,acos,asin,atan2,sqrt,pi, modf
import time
import feedparser
		
class MyFeed:

	def __init__(self,url):
		self.url = url
		self.content=""

	def readfeed(self):
		try:
			f = urllib.urlopen(self.url)
			self.content = f.read()
			f.close()
		except IOError:
			print "cannot retrieve web page for", self.url
	
	def parsefeed(self):
		self.readfeed()
			
	def betweenTags(self, startTag,endTag, html):
		r = ""
		start = html.find(startTag)
		if (start>-1):
			end = html.find(endTag,start)
			if (end==-1):
				return r
			r = html[start+len(startTag):end]
			r=r.replace("<br/>","\n")
			r=r.replace("<p>","")
			r=r.replace("</p>","")
			r=r.replace("&amp;"," and ")
		return r

	def save_to_summary(self):
		fout = open("feed-summary.txt","w")
		fout.write(self.content)
		fout.close()
		
#zdnet= MyFeed("http://feeds2.feedburner.com/zdnetuk/highlights")


retrieve()