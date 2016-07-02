"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".
TODO: to transform this in unit test
Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
import re

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}


def printmatch(myregex,testtext):
    match =  myregex.match(testtext) 
    if match is None:
        print "---no match---",testtext
    else:    
        print '<Match: %r, groups=%r>' % (match.group(), match.groups())

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


#should not match
printmatch(regex_ImageURLField,"/flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594.png")
printmatch(regex_ImageURLField,"http://10.12.25.26/flarebyte/en/png/company/8/java.applications-594x594-svg")
printmatch(regex_ImageURLField,"http://flarebyte.com")
printmatch(regex_ImageURLField,"http://localhost:8000/admin/")
printmatch(regex_ImageURLField,"{media}/flarebyte/{locale}/{ext}/{size}/company/contact/java-applications.help")

print "--should match>>>"

#should match
printmatch(regex_ImageURLField,"http://flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594.png")
printmatch(regex_ImageURLField,"https://flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594.gif")
printmatch(regex_ImageURLField,"http://flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594.jpg")
printmatch(regex_ImageURLField,"http://10.12.25.26/flarebyte/en/png/company/8/java.applications-594x594.gif")
printmatch(regex_ImageURLField,"http://10.12.25.26/flarebyte/en/png/company/8/java.applications-594x594.svg")
printmatch(regex_ImageURLField,"http://newsimg.bbc.co.uk/media/images/45437000/jpg/_45437564_tom1.jpg")
printmatch(regex_ImageURLField,"{media}/flarebyte/{locale}/{ext}/{size}/company/contact/java-applicati.ons-{size}.{ext}")

#-----------------

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

print "\n\n\n"

#should not match
printmatch(regex_PageURLField,"/flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594.png")
printmatch(regex_PageURLField,"http://10.12.25.26/flarebyte/en/png/company/8/java.applications-594x594-svg")
printmatch(regex_PageURLField,"http://flarebyte.com")
printmatch(regex_PageURLField,"http://localhost:8000/admin/")
printmatch(regex_PageURLField,"{media}/flarebyte/{locale}/{ext}/{size}/company/contact/java-applications.help")

print "--should match>>>"

#should match
printmatch(regex_PageURLField,"http://flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594.png")
printmatch(regex_PageURLField,"https://flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594.gif")
printmatch(regex_PageURLField,"http://flairbyte.com/flarebyte/en/png/company/8/java.applications-594x594")
printmatch(regex_PageURLField,"http://10.12.25.26/flarebyte/en/png/company/8/java.applications-594x594.g")
printmatch(regex_PageURLField,"http://10.12.25.26/flarebyte/en/png/company/8/java.applications-594x594.svg")
printmatch(regex_PageURLField,"http://newsimg.bbc.co.uk/media/images/45437000/jpg/_45437564_tom1.jpg")
printmatch(regex_PageURLField,"{xhtml}/flarebyte/{locale}/{size}/{options}/company/contact/java-applicati.ons")
