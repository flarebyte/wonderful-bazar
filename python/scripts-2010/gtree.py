import os, sys, urllib, re, string
import tempfile
from math import sin,cos,atan,acos,asin,atan2,sqrt,pi, modf
import time


url="http://www.gumtree.com/london/54/52024554.html"
urlhome="http://www.gumtree.com/cgi-bin/list_postings.pl?posting_cat=2509&search_terms=&min_price=130&max_price=290&room_type_2=Y"

up_lat=51.5370 #Angel/Essex road
down_lat=51.5138
left_lon=-0.1774
right_lon=-0.08709

def simplify(value):
	if value:
		return value
	else:
		return "_"

		
def isInsideLondon(mydict):
	if not "latitude" in mydict:
		return False
	if not "longitude" in mydict:
		return False
	latitude = mydict["latitude"]
	longitude = mydict["longitude"]
	if (latitude<down_lat):
		return False
	if (latitude<down_lat):
		return False
	if (longitude>right_lon):
		return False
	if (longitude<left_lon):
		return False
	return True
		
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
			lat = float(0)
			lon = float(0)
			if gmap:
				gmap = self.betweenTags('&markers=','"',gmap)
				lat,lon = gmap.split(",")
				lat = float(lat)
				lon = float(lon)
			r = self.extractInfo(ad)
			r["url"]=url
			if title:
				pricepw=self.betweenTags('\xa3','pw',s)
				r["pricepw"]=0
				if pricepw:
					try:
						r["pricepw"]=int(pricepw)
					except ValueError:
						r["pricepw"]=0
				pricepcm=self.betweenTags('\xa3','pcm',s)
				if pricepcm:
					try:
						r["pricepcm"]=int(pricepcm)
					except ValueError:
						r["pricepcm"]=0
				else:
					r["pricepcm"]=r["pricepw"]*4.5
			if phone:
				r["phone"]=phone
			if location:
				r["location"]=location
			if title:
				r["title"]=title	
			if gmap:
				r["gmap"]=gmap
				r["latitude"]=lat
				r["longitude"]=lon
			r["ad"]=ad	
			return r
		except IOError:
			print "cannot retrieve web page for", url
	
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
	
	def allLinks(self, html):
		r = []
		start = html.find("<h5>")
		while (start>-1):
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
		features = 0
		if ("washing machine") in r1:
			features+=1
		if ("dishwasher") in r1:
			features+=1
		if ("dryer") in r1:
			features+=1
		if ("wireless") in r1:
			r["wifi"]=True
			features+=1
		if ("wifi") in r1:
			r["wifi"]=True
			features+=1
		if ("broadband") in r1:
			r["wifi"]=True
			features+=1
		if ("includ") in r1:
			r["bills-included"]=True
			features+=1
		r["features"]=features
		return r
		
	def latest(self):
		r = []
		links = self.readHomepage()
		for link in links:
			page = self.readpage(link)
			if (isInsideLondon(page)):
				r.append(page)
		print len(r),"/",len(links)
		return r

	def html(self):
		pages = self.latest()
		r = '<HTML xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-GB"><body>'
		r += '<h4> Last updated: '
		r += time.strftime("%A, %B %d, %H:%M:%S", time.localtime())
		r += '</h4>'
		r += '<table border="1">'
		r += "<tr><td><em>Title</em></td><td><em>Price pcm</em></td><td><em>Price pw</em></td><td><em>Features</em></td><td><em>wifi</em></td><td><em>All included</em></td></tr>"
		for page in pages:
			fields = [page["pricepcm"],page["pricepw"],simplify(page["features"]),simplify(page.has_key("wifi")),simplify(page.has_key("includ"))]
			r += '<tr>'
			tabstart = '<td><a href="$url">$title</a></td>'.replace("$url",page["url"])
			tabstart= tabstart.replace("$title",page["title"])
			r += tabstart
			for field in fields:
				r += '<td>'
				r += str(field)
				r += '</td>'
			r += '</tr>'
		r = r + '</table>'
		r = r + '<ul>'
		for page in pages:
			r += '<li>'
			tabstart = '<a href="$url">$title</a>'.replace("$url",page["url"])
			tabstart= tabstart.replace("$title",page["title"])
			r += tabstart
			r += page["ad"]
			r += '</li>'
		r = r + '</ul>'
		r = r + '</body></html>'
		return r

def generate():
	gtree = Gtree()
	mylog = open ( 'D:/data/temp/gtree.html', 'w' ) 
	mylog.write(str(gtree.html()))
	mylog.close()
	#gtree.latest()
	#print gtree.readage(url)

def mycron():
	while (1==1):
		generate()
		time.sleep(60*20)
	
mycron()
