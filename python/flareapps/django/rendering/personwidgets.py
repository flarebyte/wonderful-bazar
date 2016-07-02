"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing persons
   Contributor(s):
   Description: 
"""

import string


"""
  Person name widget
"""
class PersonNameWidget(Widget):
    def __init__(self,prefix,givenname,middlename,familyname,preferredname,suffix):
        self.init()     
        self.widget ="personname"
        self.prefix = prefix
        self.givenname = givenname
        self.middlename = middlename
        self.familyname = familyname
        self.preferredname = preferredname
        self.suffix = suffix
  
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["prefix"] = self.prefix
        r["givenname"] = self.givenname
        r["middlename"] = self.middlename
        r["familyname"] = self.familyname
        r["preferredname"] = self.preferredname
        r["suffix"] = self.suffix
        return r

"""
  Personality widget
"""
class PersonalityWidget(PageWidget):
    def __init__(self,personalityname,birthname,nationality,born,died):
        self.init()     
        self.widget ="personality"
        self.birthname = birthname
        self.nationality = nationality
        self.born = born #SpaceDateWidget
        self.died = died #SpaceDateWidget
		self.fields=None #[LinkWidget,LinkWidget]
		self.movements=None #[LinkWidget,LinkWidget]
		self.influences=None #[PersonalityWidget
		


,PersonalityWidget]
		self.masterworks=None #[MasterworkWidget,MasterworkWidget]
		self.awards=None #[string,string]
		
   
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["birthname"] = self.birthname
        r["personalityname"] = self.personalityname
        r["nationality"] = self.nationality
        r["born"] = self.born
        r["died"] = self.died
        r["age"] = self.getAge()
        r["fields"] = self.fields
        r["movements"] = self.movements
        r["influences"] = self.influences
        r["masterworks"] = self.masterworks
        r["artisticstyle"] = self.artisticstyle
        r["facts"] = self.artisticstyle
        return r

	def getAge():
		return 0
		

