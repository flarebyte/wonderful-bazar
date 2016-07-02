"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Database the mobile/desktop devices 
   This database should be used to generate a summary for the site player
   Creator(s):Olivier Huin
   Subject:Database of the mobile/desktop devices 
   Contributor(s):
   Description: 
"""

from django.db import models
from django.utils import simplejson as json
import random
import string

"""
   Description: Base class for the device features
"""
class AbstractDeviceFeature(models.Model):
    slug = models.SlugField(primary_key=True, max_length=15, help_text="ex: java-1.5") #less than 2^4
    compact_slug = models.SlugField(db_index=True, unique=True, max_length=3, help_text="ex: AB") #
    title = models.CharField(max_length=63, db_index=True)
    description = models.CharField(max_length=255)
    ranking = models.PositiveIntegerField(help_text="The higher the ranking, the better the feature")
    era1 = models.BooleanField(help_text="To be supported on the future generation")
    era2 = models.BooleanField(help_text="To be supported on the recent generation")
    era3 = models.BooleanField(help_text="To be supported on the old generation")
    def __unicode__(self):
        return self.slug + " ("+ str(self.ranking)+") : "+ self.title
    def asDict(self):
        return {"slug":self.slug,"compact_slug":self.compact_slug,"title":self.title, "ranking":self.ranking,"era1":self.era1,"era2":self.era2,"era3":self.era3}
    class Meta:
        abstract = True
    


"""
   Description: Dummy Manager for the device specs
"""
class DummyDeviceSpecsManager(models.Manager):
    """
    Description: For each capabilties create a number of dummy records
    """
    def populate(self,specs_number,pk_number):
        self.genEntities(pk_number,DeviceVendor)
        self.genEntities(pk_number,DeviceOS)
        self.genEntities(pk_number,Markup)
        self.genEntities(pk_number,ImageFormat,True)
        self.genEntities(pk_number,InputDevice)
        self.genEntities(pk_number,ScriptSupport,True)
        self.genEntities(pk_number,AudioPlayer,True)
        self.genEntities(pk_number,StreamingSupport,True)
        self.genEntities(pk_number,VideoPlayer,True)
        self.genEntities(pk_number,DigitalRightsManagement,True)
        self.genEntities(pk_number,NetworkProtocols,True)
        self.genEntities(pk_number,FlashSupport,True)
        self.genEntities(pk_number,JavaSupport,True)
        self.genEntities(pk_number,URIScheme)
        self.genDeviceSpecs(specs_number,pk_number)
       
    def genEntities(self,pk_number,entity,optional=False):
        print "Generating dummies", entity,pk_number
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if optional:        
            no = entity()
            no.slug = "_"
            no.compact_slug = "_"
            no.description="no available"
            no.ranking = 100
            no.era1=True
            no.era2=True
            no.era3=True
            no.save()        
        for i in range(1, pk_number):
            r = entity()
            prefix = r.__class__.__name__.lower()[0:6]
            r.slug=prefix+"-"+str(i)
            r.compact_slug = alphabet[i]
            print "---Generating dummies", r.slug        
            r.title=r.__class__.__name__+"-title-"+str(i)
            r.description=r.__class__.__name__+"-description-"+str(i)
            r.ranking = random.randint(1, 100)
            r.era1 = (random.randint(1, 100)<35)
            r.era2 = (random.randint(1, 100)<25)
            r.era3 = (random.randint(1, 100)<20)
            r.save()
   
    def genDeviceSpecs(self,specs_number,pk_number):
        print "Generating dummies device specs", specs_number,pk_number        
        for i in range(1, specs_number):
            print "....Generating dummies device specs",i       
            r = DeviceSpecs()            
            prefix = r.__class__.__name__.lower()[0:9]
            r.slug = prefix+"-"+str(i)
            r.model = r.__class__.__name__+"-model-"+str(i)
            r.screen_width = random.randint(60, 2000)
            r.screen_height = random.randint(60, 2000)
            r.usable_display_width = random.randint(60, 2000)
            r.usable_display_height = random.randint(60, 2000)
            r.screen_color_depth = random.randint(2, 32)
            r.https = (random.randint(1, 100)<30)
            r.cookie = (random.randint(1, 100)<40)
            r.memory_limit_markup = random.randint(10000, 30000)
            r.memory_limit_embedded_media = random.randint(10000, 30000)
            r.memory_limit_download = random.randint(10000, 30000)
            r.device_vendor = DeviceVendor.objects.all()[random.randint(1, pk_number-2)]
            r.device_os = DeviceOS.objects.all()[random.randint(1, pk_number-2)]
            r.save() #Many To Many requires to save this first  
            for o in Markup.objects.all():
                if random.randint(1,100)<20:
                    r.markups.add(o)        
            for o in ImageFormat.objects.all():
                if random.randint(1,100)<20:
                    r.image_formats.add(o)        
            for o in InputDevice.objects.all():
                if random.randint(1,100)<20:
                    r.input_devices.add(o)        
            for o in ScriptSupport.objects.all():
                if random.randint(1,100)<20:
                    r.scripts.add(o)        
            for o in AudioPlayer.objects.all():
                if random.randint(1,100)<20:
                    r.audios.add(o)        
            for o in StreamingSupport.objects.all():
                if random.randint(1,100)<20:
                    r.streamings.add(o)        
            for o in VideoPlayer.objects.all():
                if random.randint(1,100)<20:
                    r.videos.add(o)        
            for o in DigitalRightsManagement.objects.all():
                if random.randint(1,100)<20:
                    r.drms.add(o)        
            for o in NetworkProtocols.objects.all():
                if random.randint(1,100)<20:
                    r.network_protocols.add(o)        
            for o in FlashSupport.objects.all():
                if random.randint(1,100)<20:
                    r.flashs.add(o)        
            for o in JavaSupport.objects.all():
                if random.randint(1,100)<20:
                    r.javas.add(o)        
            for o in URIScheme.objects.all():
                if random.randint(1,100)<20:
                    r.uri_schemes.add(o)        
            r.save()
            #Create a few user agents for this DeviceSpecs
            for k in range(0,random.randint(1,5)):
                ua = UserAgent()
                ua.ua = "user-agent-string"+str(i)+"-"+str(k)
                ua.device_specs = r
                ua.save()

    
"""
   Description: Describe the capabilities for a given device
"""
class DeviceSpecs(models.Model):
    slug = models.SlugField(primary_key=True, max_length=15) #less than 2^4
    model = models.CharField(max_length=63, db_index=True)
    screen_width = models.PositiveIntegerField(default = 0, db_index=True, help_text="The total number of addressable pixels in the horizontal direction when held in its default orientation.")
    screen_height = models.PositiveIntegerField(default = 0,db_index=True, help_text="The total number of addressable pixels in the vertical direction when held in its default orientation.")
    usable_display_width = models.PositiveIntegerField(default = 0,db_index=True, help_text="The total number of usable addressable pixels in the horizontal direction.")
    usable_display_height = models.PositiveIntegerField(default = 0,db_index=True, help_text="The total number of usable addressable pixels in the vertical direction.")
    screen_color_depth = models.PositiveIntegerField(default = 0,db_index=True, help_text="The color depth of a display.")
    https = models.BooleanField(default = False,help_text="The web browser supports the SSL protocol.")
    cookie = models.BooleanField(default = True,help_text="ability of a client to store cookies and send them when appropriate.")
    memory_limit_markup = models.PositiveIntegerField(default = 0,help_text="Describes the maximum size in Kilobytes for markup in a web page. Media is treated separately.")
    memory_limit_embedded_media = models.PositiveIntegerField(default = 0,help_text="Describes the maximum size in Kilobytes for media files embedded in a web page.")
    memory_limit_download = models.PositiveIntegerField(default = 0, help_text="Describes the maximum size in Kilobytes for downloaded from a web page and stored locally (e.g. a ringtone or an image).")
    device_vendor = models.ForeignKey('DeviceVendor',db_index=True)    
    device_os = models.ForeignKey('DeviceOS',db_index=True)    
    #Supported features many to many   
    markups = models.ManyToManyField('Markup',db_index=True)    
    image_formats = models.ManyToManyField('ImageFormat')    
    input_devices = models.ManyToManyField('InputDevice')    
    scripts = models.ManyToManyField('ScriptSupport')    
    audios = models.ManyToManyField('AudioPlayer')    
    streamings = models.ManyToManyField('StreamingSupport')    
    videos = models.ManyToManyField('VideoPlayer')    
    drms = models.ManyToManyField('DigitalRightsManagement')    
    network_protocols = models.ManyToManyField('NetworkProtocols')    
    flashs = models.ManyToManyField('FlashSupport')    
    javas = models.ManyToManyField('JavaSupport')    
    uri_schemes = models.ManyToManyField('URIScheme')
    dummies =  DummyDeviceSpecsManager()   
    objects =  models.Manager()   
    def __unicode__(self):
        return self.slug + " : "+ self.model

"""
   Description: Describe the capabilities for a given device
"""
class UserAgent(models.Model):
    ua = models.CharField(max_length=200, db_index=True)
    device_specs = models.ForeignKey('DeviceSpecs',db_index=True)          

"""
   Description: Device vendor
   ex: Nokia, LG, Sony Ericsson
"""
class DeviceVendor(AbstractDeviceFeature):
    pass

"""
   Description: 
   ex: OS Symbian, OS Windows
"""
class DeviceOS(AbstractDeviceFeature):
    pass

"""
   Description: Set of mark-up languages a client supports+tyle Sheet languages
   ex: XHTML MP11, XHTML MP12 + css10, css21, wcss10.
"""
class Markup(AbstractDeviceFeature):
    content_type = models.CharField(max_length=63, default="text/html;charset=UTF-8")
    
"""
   Description: Set of image formats a client supports as part of a Web page.
   ex: Jpg, Png, Gif87, Gif89A
"""
class ImageFormat(AbstractDeviceFeature):
    pass

"""
   Description: This table described which input devices are available to the user. 
   Normally most mobile devices such as mobile phones will have a keypad, it is common, though, to have a rocker, a stylus and a touch screen in PDAs, tablets and so on.
   Enumeration of values as follows: keypad, touchScreen, stylus, trackball, clickWheel.

"""
class InputDevice(AbstractDeviceFeature):
    pass

"""
   Description: Manufacturer claim of support of a scripting language or dialect.
   Ex: ecmascript-MP.
"""
class ScriptSupport(AbstractDeviceFeature):
    pass

"""
   Description: Audio player support
   Ex: MIDI Monophonic, ARM, MP3,  ...
"""
class AudioPlayer(AbstractDeviceFeature):
    pass
    
"""
   Description: Streaming support
   Ex: Stream 3GPP H.264 Level 10b, Stream 3GPP AAC LC
"""
class StreamingSupport(models.Model):
    pass

"""
   Description: Video Player support
   Ex: WMV, 
"""
class VideoPlayer(AbstractDeviceFeature):
    pass

"""
   Description: Digital rights management
   Ex: DRM OMA Forward Lock 
"""
class DigitalRightsManagement(AbstractDeviceFeature):
    pass

"""
   Description: Network Protocols
   Ex: CSD, HSCSD,GPRS, EDGE 
"""
class NetworkProtocols(AbstractDeviceFeature):
    pass

"""
   Description: Flash support
   Ex: Flash lite
"""
class FlashSupport(AbstractDeviceFeature):
    pass

"""
   Description: Java support
   Ex: Java 5
"""
class JavaSupport(AbstractDeviceFeature):
    pass

"""
   Description: Java support
   Ex: URI Scheme Tel,URI Scheme SMS
"""
#The ability of the web browser to start a telephone call when a URI is defined with the protocol 'tel' followed by a telephone number (e.g. tel:+35312345678).
#The ability of the web browser to start a new SMS message when a URI is defined with the protocol sms followed by a telephone number (e.g. sms:+35312345678).
#The ability of the web browser to start a new SMS message when a URI is defined with the protocol smsto followed by a telephone number (e.g. smsto:+35312345678).
class URIScheme(AbstractDeviceFeature):
    pass

"""
   Description: Information concerning the package.
   Most of the information should be generated automatically ...
"""
class Package(models.Model):
    slug = models.SlugField(primary_key=True, max_length=31, help_text="ex: slug-compact-regex") #less than 2^5
    value_json = models.TextField()
    def __unicode__(self):
        return self.slug
 

"""
   ----------------------------------------------------------------------------------------------------------------
   ---------------                          PUBLIC TABLES                                      --------------------
   ----------------------------------------------------------------------------------------------------------------
"""

SCREEN_WIDTH_CHOICES = (
    (8, '84 pix'),
    (9, '96 pix'),
    (10, '101 pix'),
    (12, '120-128 pix'),
    (13, '130-132 pix'),
    (17, '176 pix'),
    (20, '208 pix'),
    (22, '220 pix'),
    (24, '240 pix'),
    (32, '320 pix'),
    (48, '480 pix'),
    (64, '640 pix'),#Desktop
    (80, '800 pix'),#Desktop
    (102, '1024 pix'),#Desktop
    (128, '1280 pix'),#Desktop
)
PIXEL_DENSITY_CHOICES = (
    (80, '80 ppi'),
    (120, '120 ppi'),
    (160, '160 ppi'),
    (200, '200 ppi'),
    (240, '240 ppi'),
)
SCREEN_WIDTH_LIST = [8,9,10,12,13,17,20,22,24,32,48,64,80,102,128]
SCREEN_RANGE_LIST = {8:[0,90],9:[90,100],10:[100,120],12:[120,130],
                    13:[130,170],17:[170,200],20:[200,220],22:[220,240],
                    24:[240,320],32:[320,480],48:[480,640],64:[640,800],
                    80:[800,1020],102:[1020,1279],128:[1280,2500]}
SCREEN_WIDTH_ERA1_LIST = [48,64,80,102,128]
SCREEN_WIDTH_ERA2_LIST = [20,22,24,32]
SCREEN_WIDTH_ERA3_LIST = [8,9,10,12,13,17]
COOKIE_LIST = [True,False]                                
COOKIE_SLUG_LIST ={True: "cookie_y",False: "cookie_n"}                                
COOKIE_COMPACT_LIST ={True: "c",False: "r"}                                


"""
   Description: Manager to retrieve BrowserProfile
"""
class BrowserProfileManager(models.Manager):
    def findByCompactSlug(self, p_compact_slug):
        return BrowserProfile.objects.get(compact_slug=p_compact_slug)
   
    def findByUserAgent(self, user_agent):
        uah = UserAgentHash.objects.get(ua_hash=BrowserProfileManager.userAgentHasher(user_agent))
        if (uah):
            return uah.browser_profile
        else:
            return Null
    """
        Hash a user agent in way which group similar mobile devices together if possible    
    """    
    def userAgentHasher(user_agent):
        return user_agent
    
    """
        Analysis the side tables and generate the tables    
    """    
    def stringclean(self, str):
        r = str        
        r = string.replace(r,"-_-_-_-_-","-")
        r = string.replace(r,"-_-_-_-","-")
        r = string.replace(r,"-_-_-","-")
        r = string.replace(r,"-_-","-")
        r = string.rstrip(r,"-")
        return r
    def populate(self):
        no_script =  ScriptSupport.objects.get(slug="_");
        no_flash =  FlashSupport.objects.get(slug="_")
        no_image =  ImageFormat.objects.get(slug="_")     
        #ERA 1: Advanced mobile device. Accepts Flash and javascript.   
        for markup in Markup.objects.filter(era1=True):
            for img in ImageFormat.objects.filter(era1=True):
                   for width in SCREEN_WIDTH_ERA1_LIST:       
                        #optional features                
                        for script in ScriptSupport.objects.filter(era1=True):
                            for flash in FlashSupport.objects.filter(era1=True):
                                for cookie in COOKIE_LIST:                                
                                    profil = BrowserProfile()                                 
                                    profil.slug = self.stringclean(COOKIE_COMPACT_LIST[cookie]+str(width)+"-"+markup.slug+"-"+img.slug+"-"+script.slug+"-"+flash.slug+"-"+COOKIE_SLUG_LIST[cookie])
                                    profil.compact_slug = COOKIE_COMPACT_LIST[cookie]+str(width)+markup.compact_slug+img.compact_slug+script.compact_slug+flash.compact_slug
                                    profil.response_content_type=markup.content_type
                                    description = {
                                                    'Markup': markup.asDict(), 
                                                    'ImageFormat': img.asDict(),
                                                    'ScriptSupport': script.asDict(),
                                                    'FlashSupport': flash.asDict(),
                                                    'width': width,
                                                    'cookie': cookie
                                                                
                                                   }                                    
                                    profil.description_json = json.dumps(description, sort_keys=True, indent=4)
                                    profil.width = width
                                    profil.cookie=cookie
                                    profil.markup=markup
                                    profil.image_format = img
                                    profil.script = script
                                    profil.flash = flash
                                    profil.ranking = flash.ranking/10+script.ranking+10*img.ranking+100*markup.ranking
                                    print "...saving "+  profil.slug
                                    profil.save()
        #ERA 2: Classic mobile device. No Flash and no javascript.        
        for markup in Markup.objects.filter(era2=True):
            for img in ImageFormat.objects.filter(era2=True):
                   for width in SCREEN_WIDTH_ERA2_LIST:       
                        for cookie in COOKIE_LIST:                                
                            profil = BrowserProfile()                                 
                            profil.slug = self.stringclean(COOKIE_COMPACT_LIST[cookie]+str(width)+"-"+markup.slug+"-"+img.slug+"-"+COOKIE_SLUG_LIST[cookie])
                            profil.compact_slug = COOKIE_COMPACT_LIST[cookie]+str(width)+markup.compact_slug+img.compact_slug
                            profil.response_content_type=markup.slug #should be the real content type
                            description = {
                                'Markup': markup.asDict(), 
                                'ImageFormat': img.asDict(),
                                'ScriptSupport': no_script.asDict(),
                                'FlashSupport': no_flash.asDict(),
                                'width': width,
                                'cookie': cookie                           
                            }                                    
                            profil.description_json = json.dumps(description, sort_keys=True, indent=4)
                            profil.width = width
                            profil.cookie=cookie
                            profil.markup=markup                        
                            profil.image_format = img
                            profil.script = no_script
                            profil.flash = no_flash
                            profil.ranking = 10*img.ranking+100*markup.ranking
                            print "...saving "+  profil.slug
                            profil.save()
        #ERA 3: Classic mobile device. No Flash, no javascript, no image.
        for markup in Markup.objects.filter(era3=True):
              for width in SCREEN_WIDTH_ERA2_LIST:       
                    for cookie in COOKIE_LIST:                                
                          profil = BrowserProfile()                                 
                          profil.slug = self.stringclean(COOKIE_COMPACT_LIST[cookie]+str(width)+"-"+markup.slug+"-"+COOKIE_SLUG_LIST[cookie])
                          profil.compact_slug = COOKIE_COMPACT_LIST[cookie]+str(width)+markup.compact_slug
                          profil.response_content_type=markup.slug #should be the real content type
                          description = {
                            'Markup': markup.asDict(), 
                            'width': width,
                            'ImageFormat': no_image.asDict(),
                            'ScriptSupport': no_script.asDict(),
                            'FlashSupport': no_flash.asDict(),
                            'width': width,
                            'cookie': cookie                          
                          }                                    
                          profil.description_json = json.dumps(description, sort_keys=True, indent=4)
                          profil.width = width
                          profil.cookie=cookie
                          profil.markup=markup                        
                          profil.image_format = no_image
                          profil.script = no_script
                          profil.flash = no_flash
                          profil.ranking = 100*markup.ranking
                          print "...saving "+  profil.slug
                          profil.save()
                                   
                            
                                    
 



           #for o in AudioPlayer.objects.filter(era1=True):
            #for o in StreamingSupport.objects.filter(era1=True):
            #for o in VideoPlayer.objects.filter(era1=True):
            
            #for o in URIScheme.objects.filter(era1=True):
            #for o in NetworkProtocols.objects.filter(era1=True) #if slow, desactivate audio and video
            #for o in InputDevice.objects.filter(era1=True):
            #for o in DigitalRightsManagement.objects.filter(era1=True):
            #for o in JavaSupport.objects.filter(era1=True):


    
    
       



"""
    Description: The list of browser profiles is defined according the statistics about the existing DeviceSpecs
    This table should be used by the player and should contain only a limited number of records
    All theses records should be cached in memory.
    Browsing should occurs on fast http website
"""
class BrowserProfile(models.Model):
    slug = models.SlugField(primary_key=True, max_length=63, help_text="ex:xhtml-css-jpg-png") #less than 2^5
    compact_slug = models.SlugField(db_index=True, unique=True, max_length=31, help_text="Used to configure accessibility via the URL ex:en-gb/8fja/") #less than 2^5
    description_json = models.TextField(help_text="Verbose list of features generated automatically in json format")
    #filter
    width = models.PositiveIntegerField(default = 0, help_text="The total number of addressable pixels in the horizontal direction when held in its default orientation.")
    cookie = models.BooleanField(default = True,help_text="ability of a client to store cookies and send them when appropriate.")
    markup = models.ForeignKey('Markup')  
    image_format = models.ForeignKey('ImageFormat')    
    script = models.ForeignKey('ScriptSupport')    
    flash = models.ForeignKey('FlashSupport')    
    ranking = models.PositiveIntegerField(help_text="The higher the ranking, the better the feature")
    #response headers
    response_content_type = models.CharField(max_length=255) #text/html;charset=utf-8
    live = BrowserProfileManager()
    objects =  models.Manager()   

"""
    Description: The list of browser profiles is defined according the statistics about the existing DeviceSpecs
    This table should be used by the player and should contain only a limited number of records
    All theses records should be cached in memory.
    Interactive implies sessions and as secure as possible web applications
"""
class InteractiveProfile(models.Model):
    slug = models.SlugField(primary_key=True, max_length=63, help_text="ex:xhtml-css-jpg-png") #less than 2^5
    compact_slug = models.SlugField(db_index=True, unique=True, max_length=31, help_text="Used to configure accessibility via the URL ex:en-gb/8fja/") #less than 2^5
    description_json = models.TextField(help_text="Verbose list of features generated automatically in json format")
    #response headers
    response_content_type = models.CharField(max_length=255) #text/html;charset=utf-8
    live = BrowserProfileManager()

"""
    Description: The list of browser profiles is defined according the statistics about the existing DeviceSpecs
    This table should be used by the player and should contain only a limited number of records
    All theses records should be cached in memory.
    The multimedia profile should be used to listen to audio and video online
"""
class MultimediaProfile(models.Model):
    slug = models.SlugField(primary_key=True, max_length=63, help_text="ex:xhtml-css-jpg-png") #less than 2^5
    compact_slug = models.SlugField(db_index=True, unique=True, max_length=31, help_text="Used to configure accessibility via the URL ex:en-gb/8fja/") #less than 2^5
    description_json = models.TextField(help_text="Verbose list of features generated automatically in json format")
    #response headers
    response_content_type = models.CharField(max_length=255) #text/html;charset=utf-8
    live = BrowserProfileManager()

"""
   Description: Manager to retrieve BrowserProfile
"""
class UserAgentHashManager(models.Manager):
    def populate(self):
        for bp in BrowserProfile.objects.all():
            #filter all acceptable mobile devices for this BrowserProfile
            for ds in DeviceSpecs.objects.filter(screen_width__gte=SCREEN_RANGE_LIST[bp.width][0])\
            .filter(screen_width__lte=SCREEN_RANGE_LIST[bp.width][1])\
            .filter(markups=bp.markup)\
            .filter(image_formats=bp.image_format)\
            .filter(scripts=bp.script)\
            .filter(flashs=bp.flash)\
            .filter(cookie=bp.cookie):
                print "===Browser Profile=== ", bp.cookie, bp.slug, bp.markup.slug, bp.image_format, bp.script, bp.flash            
                print "=====device==", ds.slug, ds.screen_width
                for ua in UserAgent.objects.filter(device_specs=ds):
                    print "=======user agent==", ua.ua
                    #check if new BrowserProfile is better ranked, and in this case override it
                    if not UserAgentHash.objects.filter(ua_hash=ua.ua) or UserAgentHash.objects.filter(ua_hash=ua.ua).filter(browser_profile__ranking__lte=bp.ranking):
                        print "=======user agent==>", ua.ua
                        uah = UserAgentHash()
                        uah.ua_hash=ua.ua
                        uah.browser_profile=bp
                        uah.save()
                    
                    
                    

"""
   Description: User Agent unique hash created using regular expression
   All theses records should be cached in memory.
"""
class UserAgentHash(models.Model):
    ua_hash = models.CharField(max_length=200, primary_key=True, help_text="Unique id")
    browser_profile = models.ForeignKey('BrowserProfile',db_index=True)          
    live = UserAgentHashManager()
    objects = models.Manager()




