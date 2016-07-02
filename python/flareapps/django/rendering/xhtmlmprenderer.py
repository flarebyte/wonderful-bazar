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

class XhtmlmpRenderer(object):

	def __init__(self,config):
		self.config = config
		
	
	"""
	Render the page
	skeleton: the permanent part of the model (could be cached)
	spirit: the contextual part of the model
	"""
	def render(self,contents,widgets,context):
		return None

