"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Models for the DNA Django module
   Creator(s):Olivier Huin
   Subject:Models for DNA Django module
   Contributor(s):
   Description:  
"""

from flareteam.dnadjango.models import *
from django.contrib import admin

class EntityInline(admin.TabularInline):
    model = Entity
    extra = 2

class ApplicationAdmin(admin.ModelAdmin):
	list_display = ['name','label',"active"]
	inlines = [EntityInline]

admin.site.register(Application,ApplicationAdmin)

class FieldTypeAdmin(admin.ModelAdmin):
	list_display = ['name','label']

admin.site.register(FieldType,FieldTypeAdmin)

class FieldChoicesAdmin(admin.ModelAdmin):
	list_display = ['label']

admin.site.register(FieldChoices,FieldChoicesAdmin)

class EntityFieldInline(admin.StackedInline):
	model = EntityField
	extra = 2
	fk_name = "entity"

class EntityAdmin(admin.ModelAdmin):
	list_filter = ['application']
	inlines = [EntityFieldInline]

admin.site.register(Entity,EntityAdmin)







