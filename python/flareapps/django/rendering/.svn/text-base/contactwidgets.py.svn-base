"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, manage contacts
   Contributor(s):
   Description: 
"""

import string


"""
   http://microformats.org/wiki/geo
"""
class GeographicLocationWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget= "geolocation"
        self.latitude = None
        self.longitude = None

    def setGeographicLocation(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["latitude"] = self.latitude
        r["longitude"] = self.longitude
        return r
        
"""
  
"""
class GeographicAddressWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget= "geoaddress"
        self.addresslines = None
        self.zip_or_postcode = None
        self.city = None
        self.region_or_state = None
        self.country = None
        self.geolocation = None #GeographicLocationWidget
    
    def setGeographicLocation(self,latitude,longitude):
        self.geolocation = GeographicLocationWidget(latitude,longitude)
		
	def setGeographicAddress(self,addresslines,zip_or_postcode,city,region_or_state,country):
        self.addresslines = addresslines
        self.zip_or_postcode = zip_or_postcode
        self.city = city
        self.region_or_state = region_or_state
        self.country = country
		
 
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["addresslines"] = self.addresslines
        r["zip_or_postcode"] = self.zip_or_postcode
        r["city"] = self.city
        r["region_or_state"] = self.region_or_state
        r["country"] = self.country
        r["geolocation"] = self.geolocation
        return r

"""
    widget for transport
"""
class TransportWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="transport"
        self.station_or_stop = None
        self.line = None
        self.walk = None
        self.city = None
        self.geolocation = None
    
    def setGeographicLocation(self,latitude,longitude):
        self.geolocation = GeographicLocationWidget(latitude,longitude)

    def setTransport(self,station_or_stop,line,walk,city):
        self.station_or_stop = station_or_stop
        self.line = line
        self.walk = walk
        self.city = city

    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["station_or_stop"] = self.station_or_stop
        r["line"] = self.line
        r["walk"] = self.walk
        r["city"] = self.city
        r["geolocation"] = self.geolocation
        return r

"""
   Email
"""
class EmailWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="email"
        self.email = None

	def setEmail(self,email):
        self.email = email
		
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["email"] = self.email
        return r

"""
   .tel
"""
class DottelWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="dottel"
        self.dottel = None

	def setDottel(self,dottel):
       self.dottel = dottel
		
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["dottel"] = self.dottel
        return r
 
"""
   widget for telecom address
"""
class TelecomAddressWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="telecomaddress"
        self.countrycode = None
        self.number = None
        self.areacode = None
        self.extension = None
        self.nddp = None #national direct dialing prefix
	
	def setTelecomAddress(self,countrycode,number,areacode,extension,nddp):
        self.countrycode = countrycode
        self.number = number
        self.areacode = areacode
        self.extension = extension
        self.nddp = nddp 
		

    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["countrycode"] = self.countrycode
        r["number"] = self.number
        r["areacode"] = self.areacode
        r["extension"] = self.extension
        r["nddp"] = self.nddp
        return r


"""
	Contact a person or a company using a choice of options: email, phonenumber, ... 
"""
class ContactWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="contact"
        self.emails = [] #[EmailWidget,]
        self.telecoms = [] #[TelecomAddressWidget,]
        self.contactforms = [] #[WebpageWidget,]
        self.dottels = [] #[DottelWidget,]

	def addEmail(self,email):
		neo = EmailWidget()
		neo.setEmail(email)
		self.emails.append(neo)

	def addDottel(self,dottel):
		neo = DottelWidget()
		neo.setDottel(dottel)
		self.dottels.append(neo)
		
	def addTelecomAddress(self,countrycode,number,areacode,extension,nddp):
		neo = TelecomAddressWidget()
		neo.setTelecomAddress(countrycode,number,areacode,extension,nddp)
		self.telecoms.append(neo)

	def addContactForm(self,url,label):
		neo = WebpageWidget()
		neo.setWebpage(url,label)
		self.contactforms.append(neo)


    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["emails"] = self.arrayAsDataModel(self.emails)
        r["telecoms"] = self.arrayAsDataModel(self.telecoms)
        r["contactforms"] = self.arrayAsDataModel(self.contactforms)
        r["dottels"] = self.arrayAsDataModel(self.dottels)
        return r


