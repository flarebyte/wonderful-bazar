#!/usr/bin/env python

from xhtmlmprenderer import XhtmlmpRenderer
from widgets import *
import unittest
import re


"""

"""
class XhtmlmpRendererTestCase(unittest.TestCase):
    def generateLoremIpsumTextile(self):
        file = open("lorem-ipsum-textile.txt")
        r =  file.readlines(10000)
        file.close()
        return r

    #Location and map widgets 
    def geoWidget(self):
        return GeographicLocationWidget(53.800651,-4.064941)

    def geographicAddressWidget(self):
        return GeographicAddressWidget(["Bankside"],"SE1 9TG","London",None,"GB")

    #Transport widgets    
    def tubeWidget(self):
        r = TransportWidget("Mansion House","District and Circle Line",10,"London")
        r.kind="tube"
        return r

    def busWidget(self):
        r = TransportWidget("Blackfriars Bridge Road","Crystal Palace to King's Cross via Farringdon Road",10,"London")
        r.kind="bus"
        return r

    def taxiWidget(self):
        r = TransportWidget("West Entrance on Holland Street",None,10,"London")
        r.kind="taxi"
        return r

    #conversation widgets   
    def emailWidget(self):
        return EmailWidget("visiting.modern@tate.org.uk")

    def dottelWidget(self):
        return DottelWidget("http://amazon.tel/")

    def telecomAddressWidget(self):
        return TelecomAddressWidget("44","02078878888","0207",None,"0")

    #Links    
    def websiteWidget(self):
        return WebpageWidget("http://www.tate.org.uk","tate.org.uk")

    #Time widgets
    def openhoursWidget(self):
        return {"widget":"openhours","mon-fri": ["10.00","18.00"],"sat": ["10.00","18.00"]}

    def closeddaysWidget(self):
        return DatesWidget(["25/12","26/12"])

    def eventWidget(self):
        return {"widget":"time/event","date": "", "time": 5}

    def lastupdatedWidget(self):
        return DateTimeWidget("21/01/2008","12:03")
 
    def durationWidget(self):
        return DurationWidget(5,23,5)
    
    #Cost and rate    
    def admissionWidget(self):
        return PriceWidget(10,"pounds")

    def priceWidget(self):
        return PriceWidget(10.50,"pounds")

    #Article content    
    def quoteWidget(self):
        return QuoteWidget("I hope my decision to step down goes some way to showing my constituents how sorry I am about my own situation")

    def titleWidget(self):
        return TitleWidget("Tory MP to stand down at election")

    def imageWidget(self):
        return PictureWidget("[tory-mp]","Andrew MacKay and his wife Julie Kirkbride are both MPs","Andrew MacKay")

    def videoWidget(self):
        return MediaWidget("[tory-mp]","Mr Mackay saying he would stand for reselection - 22 May 2009","Andrew MacKay")

    def audioWidget(self):
        return MediaWidget("[tory-mp]","Mr Mackay saying he would stand for reselection - 22 May 2009","Andrew MacKay")
 
    def authorWidget(self):
        return PersonNameWidget("Mr","Oscar",None,"Wilde",None,None)

    def reviewWidget(self):
        return ReviewWidget("summary","description","10/10/2008",PersonNameWidget("Mr","Oscar",None,"Wilde",None,None))

    def ratingWidget(self):
        return RatingWidget(3.51)

   #Weather widget
   #http://developer.yahoo.com/weather/
    def weatherWidget(self):
        return WeatherWidget(22.1,800.0,70.0,"windy",None)

    def windWidget(self):
        return {"widget":"wind","chill/degrees":10.5,"direction/degrees":10, "pressure/mb": 1000,"rising":1 }

    def atmosphereWidget(self):
        return {"widget":"atmosphere","chill/degrees":10.5,"direction/degrees":10, "pressure/mb": 1000,"rising":1 }
 
    def astronomyWidget(self):
        return {"widget":"astronomy","chill/degrees":10.5,"direction/degrees":10, "pressure/mb": 1000,"rising":1 }

   #Advertisement
   #The advertisements are targetted to leisure users and limited to the following industries:
   # Auction houses, Clothing companies, Cosmetics companies, Gambling companies
   # Entertainment companies: Amusement park companies, Film companies, Sports event promotion companies, Leisure companies
   # Brand name food products,Restaurants, For-profit universities and colleges, Museum companies, 
   # Photography companies, Printing companies, Publishing companies,
   # Real estate companies, Research support companies, 
   # Transport companies, Travel and holiday companies, 
   
    def advertisementWidget(self):
        return AdvertisementWidget("make IT simple","http://www.flarebyte.com")

   #Personalisation`   
    def themeWidget(self):
        return {"widget":"theme","theme":"gothic"}

    def accessibilityWidget(self):
        return AccessibilityWidget()

    def localeWidget(self):
        return {"widget":"locale","locale":"en","country":"gb"}

    def timezoneWidget(self):
        return {"widget":"timezone","timezone":+10}

   #Art widgets
   	def artistWidget(self):
	   r = ArtistWidget("Fancisco Goya","Francisco Jose de Goya y Lucientes","ES",SpaceDateWidget("30-03-1746","Fuendetodos","ES"),SpaceDateWidget"16-04-1828","Bordeaux","FR"))
	   r.fields=["Painting", "Printmaking"]
	   return r

	def artistStyleWidget(self):
		return {"widget":"artiststyle","style":"Dramatic, figurative painting, bold free-flowing technique, drawings, and etchings depict dark satirical, and macabre, visions of human suffering."}

	def artistFactsWidget(self):
		return {"widget":"artistfact","facts":[""]}

	def masterworkWidget(self):
		return {"widget":"masterwork","title":"La maja desnuda","created":"1797-1800","place":"museodelprado"}


	"""
	100 richest cities:
	tokyo,newyork,losangeles,chicago,paris,london,osaka,mexico,philadelphia,washingtondc,boston,dallas,
	buenosaires,hongkong,sanfrancisco,atlanta,houston,miami,sãopaulo,seoul,toronto,detroit,madrid,seattle,
	moscow,sydney,phoenix,minneapolis,sandiego,riodejaneiro,barcelona,shanghai,melbourne,istanbul,denver,
	singapore,taipei,mumbai,rome,montreal,milan,baltimore,metromanila,stlouis,beijing,cairo,jakarta,stpetersburg,
	pusan,kolkata,vienna,delhi,telaviv,santiago,cleveland,bangkok,tehran,portland,bogotá,stpetersburg,guangzhou,
	pittsburgh,riyadh,lisbon,vancouver,johannesburg,monterrey,stockholm,capetown,berlin,athens,birmingham,fukuoka,
	manchester,lima,belohorizonte,guadalajara,hamburg,turin,lyon,jeddah,karachi,dhaka,munich,dublin,leeds,warsaw,
	tianjin,bangalore,portoalegre,helsinki,naples,budapest,zurich,ankara,amsterdam,auckland,copenhagen,recife,rotterdam

	"""


	"""
	URL Concepts: 
		- each URL must be very short in order to be easily copied and sent by SMS.
		- if possible each URL should be meaningful.
		- Each document should have an unique ID. Even when the type is different, the ids should be different.
	URL permanent links:
	topic link: updated with the latest news, often bookmarked by users or websites + feed ex: /drawing/ or /drawing/subject/
	major link: updated with the latest news, often bookmarked by users or websites. ex: /place/tatemodern/ or /tatemodern/
	oneshoot link: rarely updated. Base [alphabet-vowels] starting with number(year).bitcheck=no, predictable=yes Example: /4wRpWj 
	unique ID:gold=/1aA,silver=/1aAB,bronze=/1aABC. First 2 characters=520 types=520 tables
	rss.flarebyte.com/
	
	
	----
	[topic]/[search|who|what|where|when|why|how]{asc,desc}
	[topic]/[people=p=1|subject=s=2|place=l=3|event=e=4|analysis=a=5|technique=t=6]
	[topic]/[mail|feedback]
	[topic]/[highlight|popular|editor|thread|photo|video|]
	[topic]/[.rss|.atom]
	[topic,city]
	[topic,country]
	[topic,city,country]
	[topic]?l="fr"
	----
	Document types:
	people.item,people.list,
	subject.item,subject.list
	place.item,place.list
	event.item,event.list
	analysis.item,analysis.list
	technique.item,technique.list
	
	----
	/p/pablopicasso,/people/picasso/
	/l/tatemodern/,/place/tate,liverpool/
	/s/impressionism/,/subject/4wRpWj/
	/44wRpWj,/event/goodfriday,london/,/event/boxingday,newyork/,/e/today,/e/tomorrow,lyon
	:::today,tonight,tomorrow,week,weekend,month,quarter 
	/54wRpWj,/analysis/4wRpWj
	/64wRpWj,/technique/
	----

	/drawing/,
	/illustration/
	/painting/
	/printmaking/
	/sculpture/
	/architecture/
	/garden/
	/installation/
	/filmmaking/
	/photo/
	/conceptual/
	/mixmedia/
	/craft/
	/deco/
	/fashion/
	/digital/
	/graphic/
	/etching/
	/litho/
	/screen/
	/comic/
	/typo/
	/alternative/
	/street/
	----
	/restaurant/
	/bar/
	/hotel/
	
	----
	---Advertising---
	SEO: robot should exclude ads.
	discover deal(1 £/month). Round robin ads. Old ads should be deleted. :
		/discover/121
	bronze deal (25 £/month). Free mobile hosting. Inline bottom ads.
		/ads/dior
		/ads/dior3
	silver deal (250 £/month).  Free mobile hosting. Banner ads.
	Choice of root: ads,brand,tm,ltd,plc,co
		/tm/dior
		/tm/dior/poison
		/tm/dior/jadore
		/tm/dior/dolcevita
	gold deal (from 2500 £/month)
		/dior.mobi/poison
		...customization of the mobile site ...
	
	
	/brand/sony
	
	
	----
	/search/q="query"&hl="en". This should use open search.
	/who/
	/what/
	/where/
	/when/
	/why/
	/how/
	/api/
	----
	/highlight/
	/opening/
	/buzz/
	/alert/
	----
	/mail/from="07998436"&to="olivier@flarebyte.com"&l="gb"&subj="subject"&msg="what do you think ?"
	/mail/from="07998436"&to="olivier@flarebyte.com"&l="gb"&cat="001"
	/feedback/
	/about/
	/help/
	/faq/
	/subscribe/
	/privacy/
	/terms/
	/advertise/
	/perso/
	/flarebyte/
	/quiz/
	/share/
	
	"""
		

	"""
	---On all mobile pages---
	[Logo-Visual art]
	[Advertisement]
	----
	(Who)(What)(Where)(When)(Why)(How)
	[Search]
	----
	: (Drawing)(Illustration)(Painting)(Printmaking)(Sculpture)
	: (Architecture)(Garden design)(Installation art)
	: (Filmmaking)(Photography)(Conceptual art)(Mixed media)
	: (Craft)(Decorative art)(Fashion design) 
	: (Digital Art)(Graphic design)
	: (Etching)(Lithography)(Screen-printing)=>Printmaking
	: (Comics)(Typography)
	: (Alternative Art)(Street Art)
	----
	(Send to friend)(Talk to us=feedback)(Help)(Subscribe)(Privacy Policy)
	(Copyright © 2009, Flarebyte.com Ltd All rights reserved. powered by Flarebyte.com Ltd)
	(Personalisation)
	"""

	"""
	[Highlights]
	[Openings]
	[Previews]
	[Buzz]
	[Alerts:Weather,Transport]
	"""
	def widgetsHomepage(self):
		r = Widgets()
		r.addWidget(self.weatherWidget())
		return r
	
	"""
	[Title]
	[Plain text 1/7]
	[Photos]
	[Widgets:who,what,where,when]
	"""
	def widgetsArticle(self):
		r = Widgets()
		r.addWidget(self.weatherWidget())
		return r

	"""
	ex: Painting
	[Highlights]
	[Openings]
	[Buzz]
	[A-Z][Calendar/Events]
	[Search]
	"""
	def widgetsSection(self):
		r = Widgets()
		r.addWidget(self.weatherWidget())
		return r

	
	def testXhtmlmpRenderer(self):
        lorem_ipsum = self.generateLoremIpsumTextile()
        contents=[lorem_ipsum,lorem_ipsum,lorem_ipsum]        
        widgets =self.videoWidget()
        context = {"width":80, "theme":"gothic"}
        renderer = XhtmlmpRenderer(None)
        page =  renderer.render(contents,widgets,context)
        print page
        self.assertNotEqual(None,page)


if __name__ == "__main__":
    unittest.main()

