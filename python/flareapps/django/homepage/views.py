# Create your views here.

from django.http import HttpResponse
from flareteam.homepage.models import Navigation
from flareteam.homepage.models import Section
from django.template import Context, loader
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request,locale):
    navigation = Navigation.objects.get(locale=locale)
    t = loader.get_template('homepage/index.html')
    c = Context({
        'navigation': navigation,
        'copyright':"Copyright (c) 2008-2009 Flarebyte.com Limited.",
        'icon':"http://flarebyte.com/flarebyte.logo.icon-16x16.png",
        'css':"http://flairbyte.com/flarebyte/en/css/8/", })
    return HttpResponse(t.render(c))

def section(request,locale,section):
    navigation = Navigation.objects.get(locale=locale)
    section = Section.objects.get(locale=locale,slug=section)
    t = loader.get_template('homepage/section.html')
    c = Context({
        'navigation': navigation,
        'section': section,
        'copyright':"Copyright (c) 2008-2009 Flarebyte.com Limited.",
        'icon':"http://flarebyte.com/flarebyte.logo.icon-16x16.png",
        'css':"http://flairbyte.com/flarebyte/en/css/8/", })
    return HttpResponse(t.render(c))

