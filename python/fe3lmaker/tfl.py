import os, sys, urllib, re, string
import time
import datautils, tubes

URL_TUBE="http://www.tfl.gov.uk/tfl/livetravelnews/realtime/tube/default.html"
URL_TUBE_OFFSET="http://www.tfl.gov.uk/tfl/livetravelnews/realtime/by-date.aspx?offset="
URL_BUS="http://www.tfl.gov.uk/tfl/livetravelnews/realtime/buses/default.html"
URL_BUS_OFFSET="http://www.tfl.gov.uk/tfl/livetravelnews/realtime/buses/default.html"

class DefinitionList(object):
	def __init__(self,html):
		self.html = html
		self.position = 0
		self.list=[]

	def setPosition(self,position):
		self.position = position

	def smaller(self, a,b):
		if (a==None and b==None):
			return 0
		if (a==None):
			return 2
		if (b==None):
			return 1
		if (a<b):
			return 1
		else:
			return 2
		
	def findend(self,tag):
		r = self.html.find(tag,self.position)
		if (r ==-1):
			return None
		return r + len(tag)

	def betweenTags(self, startTag,endTag):
		r = ""
		start = self.findend(startTag)
		if (start==None):
			return None
		end = self.html.find(endTag,start)
		if (end==-1):
			return None
		r = self.html[start:end]
		return r
		
	def hasStartTag(self):
		r = self.html.find("<dt",self.position)
		if (r>-1):
			return True
		r = self.html.find("<dd",self.position)
		if (r>-1):
			return True
		return False 
	
	def parse(self):
		hasnext = self.hasStartTag()
		currentdef = []
		while (hasnext):
			dt = self.findend('<dt>')
			dd = self.findend('<dd>')
			switch = self.smaller(dt,dd)
			if (switch==0):
				hasnext = False
			if (switch == 1):
				dt_value = self.betweenTags('<dt>','</dt>')
				if (len(currentdef)>0):
					self.list.append(currentdef)
				currentdef = [dt_value]
				self.setPosition(self.findend('</dt>'))
				hasnext = self.hasStartTag()
			if (switch == 2):
				dd_value = self.betweenTags('<dd>','</dd>')
				h3=self.betweenTags('<h3>','</h3>')
				currentdef.append(h3)
				self.setPosition(self.findend('</dd>'))
				hasnext = self.hasStartTag()
		if (len(currentdef)>0):
			self.list.append(currentdef)
		return self.list
		
			
		
class Crawler:

	def __init__(self):
		pass

	def readpage(self,url):
		try:
			f = urllib.urlopen(url)
			s = f.read()
			f.close()
			return s
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
	
	def findend(self,tag,html,position):
		r = html.find(tag,position)
		if (r ==-1):
			return None
		return r + len(tag)
		
	def parse_dl(self, html):
		r = []
		dt = html.find('<dt class=')
		while (dt>-1):
			dt_end=html.find("</dt>",dt)
			dd = html.find("<dd>",dt)
			dd_end = html.find("</dd>",dt)
			clazz,dt_value = html[dt+10:dt_end].split(">")
			clazz=clazz.replace('"','')
			item=(clazz,dt_value,html[dd+4:dd_end])
			r.append(item)
			#next
			dt = html.find('<dt class=',dd_end)
		return r
	
	def parse_li(self, html):
		r = []
		start_tag = "<li class="
		end_tag = "</li>"
		li_start = self.findend(start_tag,html,0)
		while (li_start!=None):
			li_end=html.find(end_tag,li_start)
			clazz,li_value = html[li_start:li_end].split(">")
			clazz=clazz.replace('"','')
			item=(clazz,li_value)
			r.append(item)
			#next
			li_start = self.findend(start_tag,html,li_end)
		return r
		

class TubeCrawler(Crawler):
	def __init__(self,offset=0):
		self.offset = offset
		if (offset==0):
			self.url_tube = URL_TUBE
		else:
			self.url_tube = URL_TUBE_OFFSET+str(offset)
		
	def tube_lines(self):
		page = self.readpage(self.url_tube)
		r = {}
		if not page:
			return r
		tubeLines = self.betweenTags('<dl id="lines">','</dl>',page)
		dl = self.parse_dl(tubeLines)
		for line in dl:
			if "Good" in line[2]:
				r[line[0]]=True
			else:
				r[line[0]]=False
		return r

	def tube_stations(self):
		page = self.readpage(self.url_tube)
		if not page:
			return r
		df = DefinitionList(self.betweenTags('<dl id="stations">','</dl>',page))
		return df.parse()
		
	def tube_stations_normalized(self):
		station_status_list = self.tube_stations()
		if not station_status_list:
			return None
		r = [None,None,None,None,station_status_list]
		for station_list in station_status_list:
			status=station_list.pop(0)
			status=status.lower()
			row_nb=tubes.STATUS_GREEN
			if "closed" in status:
				row_nb=tubes.STATUS_RED
			elif "maintenance" in status:
				row_nb=tubes.STATUS_ORANGE
			else:
				row_nb=tubes.STATUS_DEBUG
			uuids=tubes.search_tube_station_UUID_list(station_list)
			station_list.insert(0,status+" / "+str(row_nb))
			r[row_nb]=uuids
		return r

class Bus(Crawler):
	def __init__(self,offset=0):
		self.offset = offset
		if (offset==0):
			self.url_tube = URL_BUS
		else:
			self.url_tube = URL_BUS_OFFSET+str(offset)
		
	def busLines(self):
		page = self.readpage(self.url_tube)
		r = []
		if not page:
			return r
		busLines = self.betweenTags('</form>','<form',page)
		li = self.parse_li(busLines)
		for line in li:
			if (line[0]=="buses"):
				r.append(line[1])
		return r
		
		