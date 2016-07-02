"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing temporal info
   Description: 
"""

import string
from datetime import datetime

months_en = ("January","February","March","April","May","June","July","August","September","October","November","December")
months_fr = ("Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre")

import basewidgets

"""
  Date widget
"""
class DateWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="date"
		self.year = None
		self.month = None
		self.monthname = None
		self.day = None
		self.isoweekday = None

  	def setDate(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
		#calculate day of week
		date = datetime.date(year,month,day)
		self.isoweekday = date.isoweekday()

  	def setTime(self,hour,minute):
		self.hour = hour
		self.minute = minute
	
	def setDateTime(self,year,month,day,hour,minute):
		self.setDate(year,month,day)
		self.setTime(hour,minute)
		
	def localize(self,locale):
		if (locale=="en"):
			self.monthname = months_en[self.month]
		if (locale=="fr"):
			self.monthname = months_fr[self.month]

	def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["year"] = self.year
        r["month"] = self.month
        r["monthname"] = self.monthname
        r["day"] = self.day
        r["isoweekday"] = self.isoweekday
        return r


"""
  Date Time widget
"""
class DateTimeWidget(DateWidget):
    def __init__(self):
        self.init()     
        self.widget ="datetime"
		self.hour = None
		self.minute =  None

  	def setTime(self,hour,minute):
		self.hour = hour
		self.minute = minute

	def asDataModel(self):
        r = DateWidget.asDataModel(self)        
        r["hour"] = self.hour
        r["minute"] = self.minute
        return r
		
"""
  Date Time widget
"""
class TimeWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="time"
		self.hour = None
		self.minute =  None

  	def setTime(self,hour,minute):
		self.hour = hour
		self.minute = minute

	def asDataModel(self):
        r = DateWidget.asDataModel(self)        
        r["hour"] = self.hour
        r["minute"] = self.minute
        return r		

"""
  Automatic Date widget
  ex: +1, +2, 
  means today + 1 day ...
"""
class AutoDateWidget(Widget):
    def __init__(self,add):
        self.init()     
        self.widget ="autodate"
        self.add = add
  
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["add"] = self.add
        return r

"""
  Date Period widget
"""
class DatePeriodWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="dateperiod"
        self.beginningdate = None #DateWidget
		self.endingdate = None #DateWidget
		#self.period #in days
	
	def setBeginningDate(self,year,month,day):
		 self.beginningdate = DateWidget()
		 self.beginningdate.setDate(year,month,day)
		 
	def setEndingDate(self,year,month,day):
		 self.endingdate = DateWidget()
		 self.endingdate.setDate(year,month,day)
		 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["beginningdate"] = beginningdate.asDataModel()
        r["endingdate"] = endingdate.asDataModel()
        return r

"""
  Time Period widget
"""
class TimePeriodWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="timeperiod"
        self.beginningtime = None #TimeWidget
		self.endingtime = None #TimeWidget

	def setBeginningTime(self,hour,minute):
		 self.beginningtime = TimeWidget()
		 self.beginningtime.setTime(hour,minute)
		 
	def setEndingTime(self,hour,minute):
		 self.endingtime = TimeWidget()
		 self.endingtime.setTime(hour,minute)
		 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["beginningtime"] = beginningtime.asDataModel()
        r["endingtime"] = endingtime.asDataModel()
        return r


"""
  Duration widget
"""
class DurationWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="duration"
        self.hours = None
        self.minutes = None
        self.seconds = None
	
	def setDuration(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
  
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["hours"] = self.hours
        r["minutes"] = self.minutes
        r["seconds"] = self.seconds
        return r

"""
  Time widget
"""
class WeeklyOpenTimeWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="weeklyopentime"
		self.mon = False
		self.tue = False
		self.wed = False
		self.thu = False
		self.fri = False
		self.sat = False
		self.sun = False
        self.timeperiod = None #TimePeriodWidget
	
	def setTimePeriod(self,hour1,minute1,hour2,minute2):
		 self.timeperiod = TimePeriodWidget()
		 self.timeperiod.setBeginningTime(hour1,minute1)
		 self.timeperiod.setEndingTime(hour2,minute2)
         return self.timeperiod
		 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["mon"] = self.mon
        r["tue"] = self.tue
        r["wed"] = self.wed
        r["thu"] = self.thu
        r["fri"] = self.fri
        r["sat"] = self.sat
        r["sun"] = self.sun
        r["timeperiod"] = self.timeperiod.asDataModel()
        return r

"""
  Space Year widget
"""
class SpaceYearWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="spaceyear"
		self.year = None
		self.city = None
		self.country = None

  	def setSpaceYear(self,year,city,country):
		self.year = year
		self.city = city
		self.country = country

	def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["year"] = self.year
        r["city"] = self.city
        r["country"] = self.country
        return r

