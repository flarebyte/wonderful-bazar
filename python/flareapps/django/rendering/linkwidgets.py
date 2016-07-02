"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing web links
   Contributor(s):
   Description: 
"""

import string

"""
   Internal link
"""
class LinkWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="link"
        self.slug = None
        self.uid = None
        self.label = None
		self.icon = None

	def setLink(self,slug,uid,label,icon):
       self.slug = slug
       self.uid = uid
       self.label = label
	   self.icon=icon
	
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["slug"] = self.slug
        r["uid"] = self.uid
        r["label"] = self.label
        r["icon"] = self.icon
        return r

"""
   Web page
"""
class WebpageWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="webpage"
        self.url = None
        self.label = None
	
	def setWebpage(self,url,label):
        self.url = url
        self.label = label

    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["url"] = self.url
        r["label"] = self.label
        return r

"""
  Picture widget
"""
class PictureWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="picture"
        self.url = None
        self.label = None
        self.alt = None
	
	def setDescription(self,url,label,alt):
        self.url = url
        self.label = label
        self.alt = alt
	
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["url"] = self.url
        r["label"] = self.label
        r["alt"] = self.alt
        return r

"""
  Media widget
"""
class MediaWidget(Widget):
    def __init__(self,url,label,alt):
        self.init()     
        self.widget ="media"
        self.url = None
        self.label = None
        self.alt = None

	def setDescription(self,url,label,alt):
        self.url = url
        self.label = label
        self.alt = alt

    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["url"] = self.url
        r["label"] = self.label
        r["alt"] = self.alt
        return r


