#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="olivierhuin"
__date__ ="$Oct 6, 2009 9:37:06 PM$"

if __name__ == "__main__":
    print "Hello World";

from amazon import S3
from django.conf import settings
from django.db import models
from mimetypes import guess_type
from django.core import validators
from django import oldforms
from django.dispatch import dispatcher
from django.utils.functional import curry
from django.utils.translation import gettext_lazy
from django.db.models import signals
from PIL import Image
from StringIO import StringIO
import os

conn = S3.AWSAuthConnection(settings.AWS_ACCESS_KEY_ID,
                            settings.AWS_SECRET_ACCESS_KEY)
generator = S3.QueryStringAuthGenerator(settings.AWS_ACCESS_KEY_ID,
                                        settings.AWS_SECRET_ACCESS_KEY)

class S3FileField(models.FileField):
    def __init__(self, verbose_name=None, name=None, bucket='', is_image=False, **kwargs):
        models.FileField.__init__(self, verbose_name, name, upload_to="s3", **kwargs)
        self.bucket = bucket
        self.is_image = is_image

    def get_manipulator_fields(self, opts, manipulator, change, name_prefix='', rel=False, follow=True):
        field_list = models.Field.get_manipulator_fields(self, opts, manipulator, change, name_prefix, rel, follow)
        if not self.blank:
            if rel:
                # This validator makes sure FileFields work in a related context.
                class RequiredFileField(object):
                    def __init__(self, other_field_names, other_file_field_name):
                        self.other_field_names = other_field_names
                        self.other_file_field_name = other_file_field_name
                        self.always_test = True
                    def __call__(self, field_data, all_data):
                        if not all_data.get(self.other_file_field_name, False):
                            c = validators.RequiredIfOtherFieldsGiven(self.other_field_names, gettext_lazy("This field is required."))
                            c(field_data, all_data)
                # First, get the core fields, if any.
                core_field_names = []
                for f in opts.fields:
                    if f.core and f != self:
                        core_field_names.extend(f.get_manipulator_field_names(name_prefix))
                # Now, if there are any, add the validator to this FormField.
                if core_field_names:
                    field_list[0].validator_list.append(RequiredFileField(core_field_names, field_list[1].field_name))
            else:
                v = validators.RequiredIfOtherFieldNotGiven(field_list[1].field_name, gettext_lazy("This field is required."))
                v.always_test = True
                field_list[0].validator_list.append(v)
                field_list[0].is_required = field_list[1].is_required = False

        return field_list

    def get_internal_type(self):
        return "FileField"

    def contribute_to_class(self, cls, name):
        super(S3FileField, self).contribute_to_class(cls, name)
        models.CharField(maxlength=200, blank=self.blank, null=self.null).contribute_to_class(cls, "%s_key"%(self.name))
        models.CharField(maxlength=200, blank=self.blank, null=self.null, default=(self.bucket or settings.DEFAULT_BUCKET)).contribute_to_class(cls, "%s_bucket"%(self.name))
        models.CharField(maxlength=200, blank=True, null=True, default="").contribute_to_class(cls, "%s_content_type"%(self.name))
        models.IntegerField(blank=True, null=True).contribute_to_class(cls, "%s_size"%(self.name))
        if self.is_image:
            models.IntegerField(blank=True, null=True).contribute_to_class(cls, "%s_width"%(self.name))
            models.IntegerField(blank=True, null=True).contribute_to_class(cls, "%s_height"%(self.name))

        # Getter for the file url
        def get_url(instance, field):
            return field.get_url(instance)
        setattr(cls, 'get_%s_url' % self.name, curry(get_url, field=self))

        dispatcher.connect(self.delete_file, signal=signals.post_delete, sender=cls)

    def delete_file(self, instance):
        if getattr(instance, self.attname):
            bucket = self.get_bucket(instance)
            key = self.get_key(instance)
            conn.delete(bucket, key)

    def get_url(self, instance):
        bucket = self.get_bucket(instance)
        key = self.get_key(instance)
        if bucket and key:
            url = generator.make_bare_url(bucket, key)
            return url
        return None

    def get_bucket(self, instance):
        return getattr(instance, "%s_bucket"%self.name)

    def set_bucket(self, instance, bucket):
        setattr(instance, "%s_bucket"%self.name, bucket)

    def get_key(self, instance):
        return getattr(instance, "%s_key"%self.name)

    def set_key(self, instance, key):
        setattr(instance, "%s_key"%self.name, key)

    def get_content_type(self, instance):
        return getattr(instance, "%s_content_type"%self.name)

    def set_content_type(self, instance, content_type):
        setattr(instance, "%s_content_type"%self.name, content_type)

    def get_size(self, instance):
        return getattr(instance, "%s_size"%self.name)

    def set_size(self, instance, size):
        setattr(instance, "%s_size"%self.name, size)

    def get_filename(self, instance):
        return getattr(instance, self.name)

    def set_filename(self, instance, filename):
        setattr(instance, self.name, filename)

    def get_width(self, instance):
        return getattr(instance, "%s_width"%self.name)

    def set_width(self, instance, width):
        setattr(instance, "%s_width"%self.name, width)

    def get_height(self, instance):
        return getattr(instance, "%s_height"%self.name)

    def set_height(self, instance, height):
        setattr(instance, "%s_height"%self.name, height)

    def get_manipulator_field_objs(self):
        if self.is_image: uploadType = oldforms.ImageUploadField
        else: uploadType = oldforms.FileUploadField
        return [uploadType, oldforms.HiddenField]

    def get_manipulator_field_names(self, name_prefix):
        return [name_prefix + self.name + '_file', name_prefix + self.name]

    def save_file(self, new_data, new_object, original_object, change, rel, save=True):
        upload_field_name = self.get_manipulator_field_names('')[0]
        if new_data.get(upload_field_name, False):
            if rel:
                new_content = new_data[upload_field_name][0]["content"]
                new_filename = new_data[upload_field_name][0]["filename"]
            else:
                new_content = new_data[upload_field_name]["content"]
                new_filename = new_data[upload_field_name]["filename"]

            self.set_filename(new_object, new_filename)
            self.set_size(new_object, len(new_content))

            key = new_data["%s_key"%self.name]
            if not key:
                key = "_".join((new_object.__class__.__name__.lower(), str(new_object.id), self.name))
                self.set_key(new_object, key)
            bucket = new_data["%s_bucket"%self.name]
            if not bucket:
                bucket = self.bucket
            content_type = new_data["%s_content_type"%self.name]
            if new_filename and not content_type:
                content_type = guess_type(new_filename)[0]
                if not content_type:
                    content_type = "application/x-octet-stream"
            conn.put(bucket, key, S3.S3Object(new_content),
                     { 'x-amz-acl': 'public-read' , 'Content-Type': content_type})

            if self.is_image:
                # Calculate image width/height
                img = Image.open(StringIO(new_content))
                width, height = img.size
                self.set_width(new_object, width)
                self.set_height(new_object, height)
