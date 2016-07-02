"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Models for the homepage module
   Creator(s):Olivier Huin
   Subject:Models for homepage
   Contributor(s):
   Description: Short-term implementation to be replaced by a more advanced design in the long-term.
"""

from django.db import models
from flareteam.common.flare_dbfields import AutoUuidField,ImageURLField,PageURLField,TitleField,LocaleField

"""
   Description: a section is basically a web page, but the summary can also appear on the homepage 
"""
class Section(models.Model):
	uuid = AutoUuidField()
	slug =  models.SlugField()
	title =  TitleField()
	title_url = PageURLField()
	thumbnail_alt =  TitleField()
	thumbnail_url = ImageURLField()
	summary = models.TextField(help_text="summary for the front page to be displayed using the Textile format")
	content = models.TextField(help_text="content to be displayed using the Textile format")

	#Meta information	
	description =  models.CharField(max_length=127, help_text="meta: description of the section")
	keywords =  models.CharField(max_length=127, help_text="meta: list the keywords")
	created = models.DateTimeField(editable=False, auto_now_add=True) 
	modified = models.DateTimeField(editable=False, auto_now=True)
	locale =  LocaleField()
	def __unicode__(self):
		return self.title	
	class Meta:	
		verbose_name = "homepage section"
		ordering = ["title"]

"""
   Description: a navigation represents a homepage for a specific locale or context
"""
class Navigation(models.Model):
    uuid = AutoUuidField()
    billboard =  TitleField()
    headline =  TitleField()
    copyright =  models.CharField(max_length=127, default = "Copyright (c) 2008-2009 Flarebyte.com Limited. All rights reserved.", help_text="Copyright")
    main_section = models.ForeignKey(Section, related_name="main_sect", help_text="main section to display")

    #list of sections to appear on the homepage    
    section1 = models.ForeignKey(Section, related_name="sect1", help_text="section 1")
    section2 = models.ForeignKey(Section, related_name="sect2",help_text="section 2",null=True)
    section3 = models.ForeignKey(Section, related_name="sect3",help_text="section 3", null=True)
    section4 = models.ForeignKey(Section, related_name="sect4", help_text="section 4", null=True)
    section5 = models.ForeignKey(Section, related_name="sect5",help_text="section 5", null=True)
    section6 = models.ForeignKey(Section, related_name="sect6",help_text="section 6", null=True)

    #list of footers to appear on the homepage    
    footer1 = models.ForeignKey(Section, related_name="foot1", help_text="footer 1")
    footer2 = models.ForeignKey(Section, related_name="foot2",help_text="footer 2", null=True)
    footer3 = models.ForeignKey(Section, related_name="foot3",help_text="footer 3", null=True)
    footer4 = models.ForeignKey(Section, related_name="foot4", help_text="footer 4", null=True)
    footer5 = models.ForeignKey(Section, related_name="foot5",help_text="footer 5", null=True)

    #technical configurations
    favicon =  ImageURLField(help_text="favicon should be 16x16") 
    css =  models.URLField("The css base path")
    xhtml =  models.URLField("The xhtml base path")
    
     
    #Meta information	
    description =  models.CharField(max_length=127, help_text="meta: description of the section")
    keywords =  models.CharField(max_length=127, help_text="meta: list the keywords")
    created = models.DateTimeField(editable=False, auto_now_add=True) 
    modified = models.DateTimeField(editable=False, auto_now=True)
    locale =  LocaleField()

    def __unicode__(self):
        return self.headline	
    class Meta:	
        verbose_name = "homepage navigation"
        ordering = ["locale"]

"""
   Description: a contact-us record allows an anonymous user to post a message.
"""
class Contactus(models.Model):
    uuid = AutoUuidField()
    title =  models.CharField(max_length=15)
    firstname =  models.CharField(max_length=31)
    lastname =  models.CharField(max_length=31)
    company =  models.CharField(max_length=63,blank=True)
    subject =  TitleField()
    email =  models.EmailField()
    message = models.TextField()

    #Meta information
    created = models.DateTimeField(editable=False, auto_now_add=True) 
    modified = models.DateTimeField(editable=False, auto_now=True)
    locale =  LocaleField()

    keywords =  models.CharField(max_length=127, blank=True, help_text="meta: list the keywords") #enter by staff
        
    #request header info, for statistic purposes
    user_agent = models.CharField(max_length=255, blank=True)
    http_accept = models.CharField(max_length=255, blank=True)
    http_language = models.CharField(max_length=255, blank=True)
    ip = models.IPAddressField(blank=True) #to be used against spam and possibly to identify the city

    def __unicode__(self):
        return  "%s %s" % (email, subject)
    class Meta:	
        verbose_name = "Contact Us"
        ordering = ["email"]



