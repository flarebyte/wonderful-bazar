"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Custom_fields
   Creator(s):Olivier Huin
   Subject:Models for homepage
   Contributor(s):
   Description: 
"""


import re
from django.forms.fields import RegexField
from django.utils.translation import ugettext as _

regex_ImageURLField = re.compile(
    r'(^https?://' # http:// or https://
    r'(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,6}|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:[A-Z0-9-/._]+)' #image path
    r'(?:\.png|\.jpg|\.gif|\.svg)$)|' # or with placeholders
    r'(^\{media\}/\S+/\{locale\}/\{ext\}/\{size\}/' # {media}/application/{locale}/{ext}/{size}/
    r'(?:[A-Z0-9-/._]+)' #image path
    r'(?:\-\{size\}\.\{ext\})$)' #-{size}.{ext}
    , re.IGNORECASE)

"""
   ImageURLField: 
 """
class ImageURLField(RegexField):
    default_error_messages = {
        'invalid': _(u'Enter a valid URL.'),
        'invalid_link': _(u'This URL appears to be a broken link.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(ImageURLField, self).__init__(regex_ImageURLField, max_length, min_length, *args,**kwargs)
 
    def clean(self, value):
        value = super(ImageURLField, self).clean(value)
        return value

regex_PageURLField = re.compile(
    r'(^https?://' # http:// or https://
    r'(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,6}|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:[A-Z0-9-/._]+$))|' #image path
    r'(^\{xhtml\}/\S+/\{locale\}/\{size\}/\{options\}/' # {xhtml}/flarebyte/{locale}/{size}/{options}/
    r'(?:[A-Z0-9-/._]+)$)' #image path
    , re.IGNORECASE)

"""
   PageURLField: 
 """
class PageURLField(RegexField):
    default_error_messages = {
        'invalid': _(u'Enter a valid URL.'),
        'invalid_link': _(u'This URL appears to be a broken link.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(PageURLField, self).__init__(regex_PageURLField, max_length, min_length, *args,**kwargs)
 
    def clean(self, value):
        value = super(PageURLField, self).clean(value)
        return value

