"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing weather
   Contributor(s):
   Description: 
"""

import string


"""
  Weather widget
  http://developer.yahoo.com/weather/
"""
class WeatherWidget(Widget):
    def __init__(self,celsius,mbpressure,humidity,condition,pubdate):
        self.init()     
        self.widget ="weather"
        self.celsius = celsius
        self.fahrenheit = (9/5)*celsius+32
        self.mbpressure = mbpressure
        self.humidity = humidity
        self.condition = condition
        self.pubdate = pubdate
 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["celsius"] = self.celsius
        r["fahrenheit"] = self.fahrenheit
        r["mbpressure"] = self.mbpressure
        r["humidity"] = self.humidity
        r["condition"] = self.condition
        r["pubdate"] = self.pubdate
        return r


