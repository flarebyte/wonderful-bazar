"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, advertisments
   Contributor(s):
   Description: 
"""

import string

"""
  Advertisement widget
"""
class AdvertisementWidget(Widget):
    def __init__(self,slogan,url):
        self.init()     
        self.widget ="advertisement"
        self.slogan = slogan
        self.url = url
 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["slogan"] = self.slogan
        r["url"] = self.url
        return r


