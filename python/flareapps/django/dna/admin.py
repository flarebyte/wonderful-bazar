"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Admin for the DNA module
   Creator(s):Olivier Huin
   Subject:Models for DNA
   Contributor(s):
   Description:  
"""

from flareteam.dna.models import *
from django.contrib import admin

class VersionAdmin(admin.ModelAdmin):
	list_display = ['label','active','date_time']

admin.site.register(Version,VersionAdmin)

class LanguageAdmin(admin.ModelAdmin):
	list_display = ['hierarchy','label']

admin.site.register(Language,LanguageAdmin)

class BusinessModelAdmin(admin.ModelAdmin):
	list_display = ['hierarchy','label']

admin.site.register(BusinessModel,BusinessModelAdmin)

class BusinessVocabularyAdmin(admin.ModelAdmin):
	list_display = ['short_name','label']

admin.site.register(BusinessVocabulary,BusinessVocabularyAdmin)





