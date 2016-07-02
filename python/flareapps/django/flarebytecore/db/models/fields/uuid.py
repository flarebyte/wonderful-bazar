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
import uuid

from django.db.models.fields import CharField
from flareteam.common import flare_formfields 

"""
   AutoUuidField: 
 """
class AutoUuidField(CharField):
    def __init__(self, *args, **kwargs):
        # Set this as a fixed value, we store UUIDs in text.
		kwargs['max_length'] = 36
		kwargs['blank'] = True
		kwargs['primary_key'] = True
		kwargs['editable'] = False
		super(AutoUuidField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return CharField.__name__
    
    def pre_save(self, model_instance, add):
        if add:
            value = str(uuid.uuid1())
            setattr(model_instance, self.attname, value)
            return value
        else:
            value = super(AutoUuidField, self).pre_save(model_instance, add)
            if not value:
                value = str(uuid.uuid1())
                setattr(model_instance, self.attname, value)
        return value

"""
   ImageURLField: 
 """
class ImageURLField(CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_length'] = 200
        CharField.__init__(self, verbose_name, name, **kwargs)

    def get_internal_type(self):
        return CharField.__name__
 

    def formfield(self, **kwargs):
        defaults = {'form_class': flare_formfields.ImageURLField}
        defaults.update(kwargs)
        return super(ImageURLField, self).formfield(**defaults)

"""
   PageURLField: 
 """
class PageURLField(CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_length'] = 200
        CharField.__init__(self, verbose_name, name, **kwargs)

    def get_internal_type(self):
        return CharField.__name__

    def formfield(self, **kwargs):
        defaults = {'form_class': flare_formfields.PageURLField}
        defaults.update(kwargs)
        return super(PageURLField, self).formfield(**defaults)

"""
   TitleField: 
 """
class TitleField(CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_length'] = 63 #less than 2^6
        CharField.__init__(self, verbose_name, name, **kwargs)

    def get_internal_type(self):
        return CharField.__name__

"""
   DescriptionField: 
 """
class DescriptionField(CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_length'] = 250 #less than 2^8
        CharField.__init__(self, verbose_name, name, **kwargs)

    def get_internal_type(self):
        return CharField.__name__


"""
   LocaleField: 
 """
class LocaleField(CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_length'] = 8
        kwargs['help_text'] ="ISO Language Code - ISO Country Code"
        CharField.__init__(self, verbose_name, name, **kwargs)

    def get_internal_type(self):
        return CharField.__name__


