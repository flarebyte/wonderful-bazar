"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing encyclopedia style site
   Contributor(s):
   Description: 
"""

import string


"""
CYCLOPEDIA 
"""

"""
  Page widget
  represents a mobile web page
"""
class CyclopediaPageWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="cyclopediapage"
		self.slug = None
		self.uid = None #24yueT
        self.title = None #string
		self.summary=None #string
		self.bulletpoints=[] #[string,string]
        self.created = None #DateTimeWidget
        self.updated = None #DateTimeWidget
        self.thumbnail = None #[PictureWidget]
        self.pictures = [] #[PictureWidget]
        self.medias = [] #[MediaWidget]
		
	def setCreated(self,year,month,day,hour,minute):
		self.created = DateTimeWidget()
		self.created.setDateTime(year,month,day,hour,minute)
        return self.created		

	def setUpdated(self,year,month,day,hour,minute):
		self.updated = DateTimeWidget()
		self.updated.setDateTime(year,month,day,hour,minute)
        return self.updated	

	def setSummary(self,summary):
		self.summary = summary
		
	def addBulletPoints(self,bulletpoint):
		self.bulletpoints.append(bulletpoint)
	
	def setIdentifiers(self,slug,uid):
		self.slug = slug
		self.uid = uid
	
	def setTitle(self,title):
		self.title = title
	
	def setThumbnail(self,url,label,alt):
		self.thumbnail = PictureWidget()
		self.thumbnail.setDescription(url,label,alt)
        return self.thumbnail

	def addPicture(self,url,label,alt):
		picture = PictureWidget()
		picture.setDescription(url,label,alt)
		self.pictures.append(picture)
        return picture

	def addMedia(self,url,label,alt):
		media = MediaWidget()
		media.setDescription(url,label,alt)
		self.medias.append(media)
        return media

	def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["slug"] = self.slug
        r["uid"] = self.uid
        r["title"] = self.title
        r["summary"] = self.summary
        r["bulletpoints"] = self.bulletpoints
        r["created"] = self.created.asDataModel()
        r["updated"] = self.updated.asDataModel()
        r["thumbnail"] = self.thumbnail.asDataModel()
        r["pictures"] = self.arrayAsDataModel(self.pictures)
        r["medias"] =  self.arrayAsDataModel(self.medias)
        return r

"""
  Topic widget
  Represents a topic: Ex: Sculpture
"""
class CyclopediaTopicWidget(CyclopediaPageWidget):
    def __init__(self):
        self.init()     
        self.widget ="cyclopediatopic"
		self.items = items

	def asDataModel(self):
        r = CyclopediaPageWidget.asDataModel(self)        
        r["items"] = self.items
        return r


"""
  Masterwork widget
"""
class MasterworkWidget(CyclopediaPageWidget):
    def __init__(self):
        self.init()     
        self.widget ="masterwork"
        self.placeofcreation = None

	def setPlaceOfCreation(self,year,city,country):
		self.placeofcreation = SpaceYearWidget()
		self.placeofcreation.setSpaceYear(year,city,country)
        return self.placeofcreation
		
	def asDataModel(self):
        r = CyclopediaPageWidget.asDataModel(self)        
        r["placeofcreation"] = self.placeofcreation.asDataModel()
        return r

"""
  Personality widget
"""
class PersonalityWidget(CyclopediaPageWidget):
    def __init__(self):
        self.init()     
        self.widget ="personality"
        self.birthname = None
		self.personalityname = None
        self.nationality = None
        self.born = None #SpaceDateWidget
        self.died = None #SpaceDateWidget
        self.age = None #integer
		self.fields=[] #[LinkWidget,LinkWidget]
		self.movements=[] #[LinkWidget,LinkWidget]
		self.influences=[] #[LinkWidget,...
		self.masterworks=[] #[MasterworkWidget,...

	def setBorn(self,year,city,country):
		self.born = SpaceYearWidget()
		self.born.setSpaceYear(year,city,country)
        return self.born
	
	def setDied(self,year,city,country):
		self.died = SpaceYearWidget()
		self.died.setSpaceYear(year,city,country)
        return self.died

	def setBirthName(self, birthname):
		self.birthname = birthname

	def setPersonalityName(self, personalityname):
		self.personalityname = personalityname

	def setNationality(self,country):
		self.nationality = country
	
	def addInfluence(self,slug,uid,label,icon):
		link = LinkWidget() 
		link.setLink(self,slug,uid,label,icon)	
		self.influences.append(link)
        return link

	def addMovement(self,slug,uid,label,icon):
		link = LinkWidget() 
		link.setLink(self,slug,uid,label,icon)	
		self.movements.append(link)
        return link

	def addField(self,slug,uid,label,icon):
		link = LinkWidget() 
		link.setLink(self,slug,uid,label,icon)	
		self.fields.append(link)
        return link

	def addMasterwork(self):
        r = MasterworkWidget()    		
        self.masterworks.append(r)
        return r

    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["birthname"] = self.birthname
        r["personalityname"] = self.personalityname
        r["nationality"] = self.nationality
        r["born"] = self.born.asDataModel()
        r["died"] = self.died.asDataModel()
        r["age"] = self.age
        r["fields"] = self.arrayAsDataModel(self.fields)
        r["movements"] = self.arrayAsDataModel(self.movements)
        r["influences"] = self.arrayAsDataModel(self.influences)
        r["masterworks"] = self.arrayAsDataModel(self.masterworks)
		
        return r
		
"""
  Place widget
"""
class PlaceWidget(CyclopediaPageWidget):
    def __init__(self):
        self.init()     
        self.widget ="museum"
        self.geoaddress = None #GeographicAddressWidget
        self.transports = [] #[TransportWidget,TransportWidget]
        self.website = None #WebpageWidget
        self.mobilesite = None #WebpageWidget
		self.contact = None #ContactWidget
		self.rates = [] #[PriceWidget]
		self.wheelchair=False
		self.childfriendly=False
		self.weeklyopentimes = [] #WeeklyOpenTimeWidget
   
    def setGeographicAddress(self,addresslines,zip_or_postcode,city,region_or_state,country):
		self.geoaddress =  GeographicAddressWidget()
		self.geoaddress.setGeographicAddress(addresslines,zip_or_postcode,city,region_or_state,country)
	
	def addTransport(self,station_or_stop,line,walk,city):
		neo = TransportWidget()
		neo.setTransport(station_or_stop,line,walk,city)
		self.transports.append(neo)
		
    def setWebSite(self,url,label):
        self.website = WebpageWidget()
        self.website.setWebpage(url,label)
        return self.website

    def setMobileSite(self,url,label):
        self.mobilesite = WebpageWidget()
        self.mobilesite.setWebpage(url,label)
        return self.mobilesite

    def setContact(self):
        self.contact = ContactWidget()
        return self.contact

	def addRate(self,price,currency,tag1):
		neo = PriceWidget()
		neo.setPrice(price,currency)
        neo.setTags(tag1,None,None)
		self.rates.append(neo)
        return neo
    
    def setFacilities(self,wheelchair,childfriendly):
		self.wheelchair=wheelchair
		self.childfriendly=childfriendly

	def addWeeklyOpenTime(self):
		neo = WeeklyOpenTimeWidget()
		self.weeklyopentimes.append(neo)
        return neo

	def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["geoaddress"] = self.geoaddress.asDataModel()
        r["transports"] = self.arrayAsDataModel(self.transports)
        r["website"] = self.website.asDataModel()
        r["mobilesite"] = self.mobilesite.asDataModel()
        r["contact"] = self.contact.asDataModel()
        r["rates"] = self.arrayAsDataModel(self.rates)
        r["wheelchair"] = self.wheelchair
        r["childfriendly"] = self.childfriendly
        r["weeklyopentimes"] = self.arrayAsDataModel(self.weeklyopentimes)
        return r

"""
  One Time Event widget
"""
class OneTimeEventWidget(PlaceWidget):
    def __init__(self):
        self.init()     
        self.widget ="onetimeevent"
        self.datetime =None #DateTimeWidget
		self.duration = None #DurationWidget
 	
    def setDateTime(self,year,month,day,hour,minute)	
        self.datetime = DateTimeWidget()
        self.datetime.setDateTime(year,month,day,hour,minute)
        return self.datetime

    def setDuration(self,hours,minutes,seconds):
        self.duration = DurationWidget()
        self.duration.setDuration(hours,minutes,seconds)
        return self.duration

    def asDataModel(self):
        r = PlaceWidget.asDataModel(self)        
        r["datetime"] = self.datetime.asDataModel()
        r["duration"] = self.duration.asDataModel()

        return r


"""
  Show widget
"""
class ShowWidget(PlaceWidget):
    def __init__(self):
        self.init()     
        self.widget ="show"
        self.dateperiod =None #DatePeriodWidget

    def setDatePeriod(self)	
        self.dateperiod = DatePeriodWidget()
        return self.dateperiod
 
    def asDataModel(self):
        r = PlaceWidget.asDataModel(self)        
        r["dateperiod"] = self.dateperiod.asDataModel()
        return r

