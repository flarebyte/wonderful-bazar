"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, base components
   Contributor(s):
   Description: 
"""

import string


"""
   Abstract
"""
class Widget(object):
    def __init__(self):
        self.widget="widget"
        self.kind = None
		self.decorator1 = None #DecoratorWidget
		self.decoration1 = None
		self.decorator2 = None #DecoratorWidget
		self.decoration2 = None
		self.decorator3 = None #DecoratorWidget
		self.decoration3 = None
		self.rank = 1
        self.tag1 = None
        self.tag2 = None
        self.tag3 = None
    
    def asDataModel(self):
        return {"widget":self.widget,"kind":self.kind,"uid":self.uid,"rank":self.rank,"tag1":self.tag1,"tag2":self.tag2,"tag3":self.tag3}

    def arrayAsDataModel(self,items):
        r = []
		for item in items:
			r.append(item.asDataModel())
		return r


	def decorate1(self,uid,params):
		self.decorator1 = DecoratorWidget(uid,params)
	
	def decorate2(self,uid,params):
		self.decorator2 = DecoratorWidget(uid,params)

	def decorate3(self,uid,params):
		self.decorator3 = DecoratorWidget(uid,params)
		
    def setTags(self,tag1,tag2,tag3):
		self.tag1 = tag1
		self.tag2 = tag2
		self.tag3 = tag3

"""
  Decorator widget
  This widget is used as a placeholder to decorate the static data with dynamic data coming from feeds ...
"""
class DecoratorWidget(Widget):
    def __init__(self,uid,params):
        self.init()     
        self.widget ="decorator"
        self.uid = uid
        self.params = params
 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["uid"] = self.uid
        r["params"] = self.params
        return r

"""
   Widgets
"""
class Widgets(Widget):
    def __init__(self):
        self.init()     
        self.widget= "widgets"
        self.widgets={}

    def addWidget(self,name,widget):
        self.widgets[name]=widget
    
    def asDataModel(self):
		return self.widgets


