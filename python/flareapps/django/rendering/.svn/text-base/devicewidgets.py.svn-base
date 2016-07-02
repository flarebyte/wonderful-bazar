"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing devices
   Contributor(s):
   Description: 
"""

import string

"""
  Accessibility widget
"""
class AccessibilityWidget(Widget):
    def __init__(self,theme="default",font="Verdanna",textsize=0,textspacing=0):
        self.init()     
        self.widget ="accessibility"
        self.theme = theme
        self.font = font
        self.textsize = textsize
        self.textspacing = textspacing
 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["theme"] = self.theme
        r["font"] = self.font
        r["textsize"] = self.textsize
        r["textspacing"] = self.textspacing
        return r

"""
  Mobile Profile widget
"""
class MobileProfileWidget(Widget):
    def __init__(self,cookie,markup,width,image,orientation):
        self.init()     
        self.widget ="mobileprofile"
        self.slogan = slogan
        self.cookie = cookie
        self.markup = markup
        self.width = width
        self.image = image
        self.orientation = orientation
 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["cookie"] = self.cookie
        r["markup"] = self.markup
        r["width"] = self.width
        r["markup"] = self.markup
        r["image"] = self.image
        r["orientation"] = self.orientation
        return r



