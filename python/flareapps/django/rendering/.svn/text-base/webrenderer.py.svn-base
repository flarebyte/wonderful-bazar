"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Middleware to capture the request calls
   Creator(s):Olivier Huin
   Subject:Middleware to mcapture the request calls
   Contributor(s):
   Description: 
"""

import re
import string
import os.path
from django.utils import simplejson as json

class RequestsJournalMiddleware(object):

	def __init__(self):
	"""
	Process the request.
	"""
        #open a file for load statistics
        self.journal = open('requests-journal.json','a')

	def process_request(self, request):
		json.dumps(request, self.journal, sort_keys=True, indent=1, skipkeys=True)




            
 
