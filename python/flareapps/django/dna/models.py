"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Models for the DNA module
   Creator(s):Olivier Huin
   Subject:Models for DNA
   Contributor(s):
   Description: Version, Language, BusinessModel, BusinessVocabulary, TechnicalVerb, TechnicalVocabulary 
"""
from django.db import models
from django.template.defaultfilters import slugify

#Version of template
class Version(models.Model):
	#auth_group = models.ForeignKey(Group,verbose_name="user access group", help_text="group which has the permission to access the document")
	label =  models.CharField(max_length=63)	
	date_time = models.DateTimeField(auto_now=True)
	active = models.BooleanField(help_text="yes means visible in normal searches") #yes if active, otherwise archived
	template = models.BooleanField(help_text="yes means that the documents are templates") #yes if this is a template	
	def __unicode__(self):
		return self.label	
	class Meta:	
		verbose_name = "document version"
		ordering = ["label"]


#Example Python, Django, PHP,ANT ..., let's try to avoid to serialize xml with xml
class Language(models.Model):
	hierarchy = models.CharField(max_length=127, unique=True, help_text="Ex: java.jboss.seam:1")
	label = models.CharField(max_length=63)
	file_extension = models.CharField(max_length=7, help_text="Ex: .java")
	def __unicode__(self):
		return self.label	
	class Meta:	
		verbose_name = "programming language"
		verbose_name_plural = "programming languages"
		ordering = ["hierarchy"]

#-------------------------------- Business glossary ----------------------------------

#Example: Accountancy
class BusinessModel(models.Model):
	version = models.ForeignKey(Version)
	hierarchy = models.CharField(max_length=255, unique=True, help_text="hierarchical unique name. flarebyte.accountancy.paye")
	short_name = models.CharField(max_length=31, help_text="short name. Ex: Camel Case")
	label = models.CharField(max_length=63, help_text="label for the business model")
	short_name_plural = models.CharField(max_length=31, help_text="short name (plural). Ex: Camel Cases")
	label_plural = models.CharField(max_length=63, help_text="label for the business model")
	def __unicode__(self):
		return self.label	
	class Meta:	
		verbose_name = "business model"
		verbose_name_plural = "business models"
		ordering = ["hierarchy"]
	

# Example: telephone, email, ...
class BusinessVocabulary(models.Model):
	model = models.ForeignKey(BusinessModel)
	version = models.ForeignKey(Version)
	short_name = models.CharField(max_length=31, help_text="short name. Ex: Camel Case")
	short_name_plural = models.CharField(max_length=31, help_text="short name(plural). Ex: Camel Cases")
	label = models.CharField(max_length=63, help_text="label for the business vocabulary")
	label_plural = models.CharField(max_length=63, help_text="label (plural) for the business vocabulary")
	examples = models.CharField(max_length=255, help_text="Examples for your vocabulary")
	def __unicode__(self):
		return self.short_name + ": " + self.label	
	class Meta:	
		verbose_name = "business vocabulary"
		verbose_name_plural = "business glossary"
		ordering = ["short_name"]


#Example: get, set, find, send, save, store
class TechnicalVerb(models.Model):
	version = models.ForeignKey(Version)
	short_name = models.CharField(max_length=31, help_text="short name. Ex: Camel Case")
	label = models.CharField(max_length=63, help_text="label for the technical verb")
	def __unicode__(self):
		return self.label	
	class Meta:	
		verbose_name = "technical verb"
		verbose_name_plural = "technical verbs"
		ordering = ["label"]

#Example: short, fast, type, date, date time (dt),
class TechnicalVocabulary(models.Model):
	version = models.ForeignKey(Version)
	abbreviation = models.CharField(max_length=15, help_text="abbreviation: Ex: dt for date time")
	short_name = models.CharField(max_length=31, help_text="short name. Ex: Camel Case")
	label = models.CharField(max_length=63, help_text="label for the technical vocabulary")
	def __unicode__(self):
		return self.label	
	class Meta:	
		verbose_name = "technical vocabulary"
		verbose_name_plural = "technical glossary"
		ordering = ["label"]

