"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Models for the public web site (web1, web2 and mobile). 
   This should be optimized for performances.
   Creator(s):Olivier Huin
   Subject:Models for the site content
   Contributor(s):
   Description: 
"""

from django.db import models
from flareteam.common.flare_dbfields import AutoUuidField,ImageURLField,PageURLField,TitleField,LocaleField
from flareteam.device.models import BrowserProfile,BrowserProfileManager


#verify standard
SECTION_TYPE_CHOICES = (
    (10, 'header'),
    (11, 'header 1'),
    (12, 'header 2'),
    (13, 'header 3'),
    (14, 'header 4'),
    (20, 'keywords'),
    (20, 'author'),
    (30, 'body'),
)


RANKING_CHOICES = (
    (1, 'Overall'),
    (2, 'We love'),
    (3, 'We hate'),
    (4, 'Editor choice'),
    (5, 'Most clicked'),
    (6, 'Most shared'),
)


"""
   Description: 
"""
class WebArticle(models.Model):
    ref = models.ForeignKey('ArticleRef')    
    browser_profile = models.ForeignKey('device.BrowserProfile')
    content = models.TextField(help_text="content to be displayed using the browser profile markup")
    locale =  LocaleField()
 
"""
   Description: Unique reference for a Page document, ignoring the presentation details (xhtml, wap, print, pdf) and the browser profile ...
"""
class ArticleRef(models.Model):
    uuid = AutoUuidField()
    symburl = PageURLField()
    
"""
   Description: Stores all the articles to be searched
"""
class ArticleSearch(models.Model):
    fulltext =  models.TextField() #title, content, author
    section_type =  models.PositiveSmallIntegerField(choices=SECTION_TYPE_CHOICES)
        
    #order by    
    ranking = models.IntegerField() # 1 is bottom of the list; the higher the better.It should take into account the section, the quality of the article, the date ...
    published = models.DateTimeField(editable=True) 

    #return    
    ref = models.ForeignKey('ArticleRef')    

"""
   Description: 
"""
class ArticleRanking(models.Model):
    ref = models.ForeignKey('ArticleRef')    
    ranking = models.SmallIntegerField(choices=RANKING_CHOICES, help_text="The higher the better.") 
    started = models.DateTimeField()
    finished = models.DateTimeField()

"""
   Description: Manager to search article
"""
class ArticleSearchManager(models.Manager):
    pass


