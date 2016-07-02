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
#from flareteam.dna import models

RELATIONSHIPS_CHOICES = (
    ('0', 'None'),
    ('1..1', 'OneToOne'),
    ('*..1', 'ManyToOne'),
    ('*..*', 'ManyToMany'),
    ('1R', 'ManyToOne Recursive'),
    ('*R', 'ManyToMany Recursive'),
)

CUSTOM_METHOD_CHOICES = (
    ('__unicode__', 'The __unicode__() method is called whenever you call unicode() on an object.'),
    ('__str__','The __str__() method is called whenever you call str() on an object.'),
    ('LBL', 'Label'),
)

CHAR_LENGTH_CHOICES = (
    (0, 'None'),
    (7, 'abbreviation (7 chars)'),
    (15,'tiny name (15 chars)'),
    (31,'name (31 chars)'),
    (63,'row (63 chars)'),
    (255,'summary (255 chars)'),
)


#Django Application
class Application(models.Model):
	name =  models.CharField(max_length=31)	
	label =  models.CharField(max_length=63)	
	date_time = models.DateTimeField(auto_now=True)
	active = models.BooleanField(help_text="yes means visible in normal searches") #yes if active, otherwise archived
	def __unicode__(self):
		return self.name + ": " + self.label	
	class Meta:	
		verbose_name = "django application"
		verbose_name_plural = "django applications"
		ordering = ["label"]

	
#Field type. Ex: models.IntegerField
class FieldType(models.Model):
	name =  models.CharField(max_length=31, unique=True)	
	label =  models.CharField(max_length=63)
	code =  models.CharField(max_length=255) #Ex: models.CharField
	def __unicode__(self):
		return self.name + ": " + self.label	
	class Meta:	
		verbose_name = "django field type"
		verbose_name_plural = "django field types"
		ordering = ["label"]

#Examples of field choices: ex: cities, titles, etc ..
class FieldChoices(models.Model):
	label =  models.CharField(max_length=63)
	code =  models.TextField()
	def __unicode__(self):
		return self.label	
	class Meta:	
		verbose_name = "django field choices"
		verbose_name_plural = "django field choices list"
		ordering = ["label"]

#Entity or table
class Entity(models.Model):
	application = models.ForeignKey(Application)
	vocabulary = models.ForeignKey("dna.BusinessVocabulary")
	#ordering = models.ForeignKey(EntityField,related_name="ordering",help_text="The default ordering for the object, for use when obtaining lists of objects")
	admin = models.BooleanField(help_text="If False, no default administration interface will be created ",default=True) 
	def __unicode__(self):
		return str(self.vocabulary)
	class Meta:	
		verbose_name = "django entity"
		verbose_name_plural = "django entities"
	

#Entity fields
class EntityField(models.Model):
	entity = models.ForeignKey(Entity)
	vocabulary = models.ForeignKey("dna.BusinessVocabulary")
	length = models.IntegerField(choices=CHAR_LENGTH_CHOICES, default=0)
	field_type = models.ForeignKey(FieldType)
	default = models.CharField(max_length=255)
	choices = models.ForeignKey(FieldChoices)
	null = models.BooleanField(help_text="If True, Django will store empty values as NULL in the database",default=False) 
	blank = models.BooleanField(help_text="If True, the field is allowed to be blank.",default=False) 
	unique = models.BooleanField(help_text="If True, this field must be unique throughout the table",default=False) 
	editable = models.BooleanField(help_text="If False, the field will not be editable in the admin or via forms automatically generated from the model class",default=True) 
	#Relationships
	relationship = models.CharField(max_length=7,choices=RELATIONSHIPS_CHOICES)
	related_entity = models.ForeignKey(Entity,related_name="related_entity",help_text="The class to which the model is related.",null=True)
	though_entity = models.ForeignKey(Entity,related_name="though_entity",help_text="The intermediate model is associated with the ManyToManyField using the through argument to point to the model that will act as an intermediary",null=True)
	class Meta:	
		verbose_name = "django entity field"
		verbose_name_plural = "django entity fields"


#Custom method for the entity
class EntityCustomMethod(models.Model):
	entity = models.ForeignKey(Entity)
	vocabulary = models.ForeignKey("dna.BusinessVocabulary")
	method = models.CharField(max_length=7,choices=CUSTOM_METHOD_CHOICES)
	field1 = models.ForeignKey(EntityField,related_name="field1",null=True)
	field2 = models.ForeignKey(EntityField,related_name="field2",null=True)
	field3 = models.ForeignKey(EntityField,related_name="field3",null=True)
	field4 = models.ForeignKey(EntityField,related_name="field4",null=True)
	field5 = models.ForeignKey(EntityField,related_name="field5",null=True)
	field6 = models.ForeignKey(EntityField,related_name="field6",null=True)
	field7 = models.ForeignKey(EntityField,related_name="field7",null=True)
	field8 = models.ForeignKey(EntityField,related_name="field8",null=True)
	field9 = models.ForeignKey(EntityField,related_name="field9",null=True)
	class Meta:	
		verbose_name = "django model custom method"
		verbose_name_plural = "django model custom methods"

	
	
		


		
	







