"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Admin for the homepage module
   Creator(s):Olivier Huin
   Subject: Administration for the homepage module
   Contributor(s):
   Description:  
"""

from flareteam.homepage.models import *
from django.contrib import admin

class SectionAdmin(admin.ModelAdmin):
	list_display = ['title','slug','locale']

admin.site.register(Section,SectionAdmin)

class NavigationAdmin(admin.ModelAdmin):
	list_display = ['headline','locale']

admin.site.register(Navigation,NavigationAdmin)





