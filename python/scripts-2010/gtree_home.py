import os, sys, urllib, re, string
import tempfile
import smtplib
from email.mime.text import MIMEText


#url="http://www.gumtree.com/london/90/16959190.html"
#urlhome="http://www.gumtree.com/cgi-bin/list_postings.pl?posting_cat=2511&search_terms=&min_price=400&max_price=650&num_bedrooms_3=Y&advertiser_type_1=Y"
urlhome="http://www.gumtree.com/cgi-bin/list_postings.pl?posting_cat=2509&search_terms=&min_price=150&max_price=250&room_type_2=Y"

class Gtree:

	def __init__(self):
		pass

	def readHomepage(self):
		fhome = urllib.urlopen(urlhome)
		home = fhome.read()
		fhome.close()
		r = self.allLinks(home)
		return r
		
		

	def readpage(self,url):
		try:
			f = urllib.urlopen(url)
			s = f.read()
			f.close()
			ad= self.betweenTags('<div id="desc">','</div>',s)
			phone = self.betweenTags('<li class="phone">','</li>',s)
			phone=re.sub("<[^>]+>", "", phone)
			location = self.betweenTags('<div id="location">','</div>',s)
			location=re.sub("<[^>]+>", "", location)
			title = self.betweenTags('<h2>','</h2>',s)
			title=re.sub("<[^>]+>", "", title)
			gmap = self.betweenTags('<img src="http://maps.google.com/staticmap?','/>',s)
			if gmap:
				gmap = self.betweenTags('&markers=','"',gmap)
			r = self.extractInfo(ad)
			if title:
				price=self.betweenTags('\xa3','pw',s)
				if price:
					try:
						r["price"]=int(price)
					except ValueError:
						r["price"]=0
			if phone:
				r["phone"]=phone
			if location:
				r["location"]=location
			if title:
				r["title"]=title	
			if gmap:
				r["gmap"]=gmap
			#r["ad"]=ad	
			return r
		except IOError:
			print "cannot retrieve web page for", url
	
	def betweenTags(self, startTag,endTag, html):
		start = html.find(startTag)
		if start:
			end = html.find(endTag,start)
			r = html[start+len(startTag):end]
			r=r.replace("<br/>","\n")
			r=r.replace("<p>","")
			r=r.replace("</p>","")
			r=r.replace("&amp;"," and ")
		return r
	
	def allLinks(self, html):
		r = []
		start = start = html.find("<h5>")
		while (start>0):
			end = html.find("</h5>",start)
			h5 = html[start+len("<h5>"):end]
			if h5:
				h5 = self.betweenTags('href="','">',h5)
				if not h5.startswith("http://www.gumtree.com"):
					h5 = "http://www.gumtree.com"+h5
				r.append(h5)
			start = start = html.find("<h5>",end)
		
		return r	
	
	def extractInfo(self,text):
		r1 = text.lower()
		r = {}
		if ("washing machine") in r1:
			r["washing-machine"]=True
		return r
		
	def latest(self):
		r = []
		links = self.readHomepage()
		for link in links:
			page = self.readpage(link)
			r.append(page)
		return r

			
gtree = Gtree()
mylog = open ( 'D:/data/temp/gtree.log', 'w' ) 
mylog.write(str(gtree.latest()))
mylog.close()
#gtree.latest()
#print gtree.readage(url)

