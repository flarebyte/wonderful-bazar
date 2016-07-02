import os, sys, urllib, re, string
import tempfile
from math import sin,cos,atan,acos,asin,atan2,sqrt,pi, modf
import time
import feedparser
from datetime import datetime
from time import mktime
import codecs

insidetag=re.compile("<p/>")

def clean(html):
	return insidetag.sub("",html)
		
class MyFeeds:
	def __init__(self,urls):
		self.urls = urls
		self.latest=[]
	def reset(self):
		self.latest=[]
	def parse(self,url):
		feeder = feedparser.parse(url)
		now = datetime.now()
		for entry in feeder.entries:
			dt = datetime.fromtimestamp(mktime(entry.updated_parsed))
			diff = now-dt
			row=(entry.id,entry.title,entry.link,diff)
			self.latest.append(row)
	def parse_all(self):
		for url in self.urls:
			self.parse(url)
		
	def format_row(self,row):
		r = row[1]+"\n"+row[0]+"\n"+row[2]+"\n"+str(row[3])+"\n"+"\n"
		return r
			
	def save(self):
		fout = codecs.open("feed-summary.txt","w","utf-8")
		for entry in self.latest:
			fout.write(self.format_row(entry))
			fout.write("\n")
		fout.close()

all_feeds=['http://feeds2.feedburner.com/zdnetuk/highlights',
"http://rss.slashdot.org/Slashdot/slashdot",
"http://feeds.delicious.com/v2/rss/popular/development?count=15"]
feeds=MyFeeds(all_feeds)
feeds.parse_all()
feeds.save()



