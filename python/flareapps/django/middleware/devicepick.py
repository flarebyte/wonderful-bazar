"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Middleware to manage mobile devices 
   The middleware allows to select the most suitable for a specific device
   Creator(s):Olivier Huin
   Subject:Middleware to manage mobile devices 
   Contributor(s):
   Description: 
"""

import re
import string
import os.path
from django.utils import simplejson as json



# list of mobile User Agents...deprecated ...to delete
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]

"""
Swap dictionary: keys become values, and values become keys.
"""
def swap_dictionary(original_dict):
	return dict([(v, k) for (k, v) in original_dict.iteritems()])
	

device_markup_to_id={"wml":"w","xhtml-mp":"m","html":"h","xhtml":"x"}
device_images_to_id={"jpeg,png":"p","jpeg,gif":"g","jpeg":"j"}
device_layout_to_id={"landscape":"l","portrait":"p","square":"s"}
device_id_to_markup=swap_dictionary(device_markup_to_id)
device_id_to_images=swap_dictionary(device_images_to_id)
device_id_to_layout=swap_dictionary(device_layout_to_id)

re_restyled = re.compile("/[cr]\d{1,3}[qwrtpsdfghjklzxcvbnm]{2}[0-9]{2}/") #cookie+width+markup+image+script+flash+layout
re_browser = re.compile("(((firefox|khtml)/\d+)|(msie\s\d+)|(safari/\d))") #detect Firefox/1.5 KHTML/4.0.5 MSIE 4.01; Safari/525.21 

	

"""
	This value object handles multiple representations of a device profile (explicit and profile gene).
	Default or unknown fields are stored as _ or None
	Note: Make sure that all fields are calculated after creation in order to benefit any later caching.
"""
class DeviceProfile(object):
	def __init__(self):
		pass
	def reset(self):
		self.cookie=None
		self.markup=None
		self.width=None
		self.images=None
		self.javascript=None
		self.flash=None
		self.layout=None
		self.profileGene=None
		#self.sequence=None , #the sequence should not have to be stored
		
	"""
		Create a profile gene string from the internal fields
	"""
	def createProfileGene(self):
		cookie_id= (self.cookie and "c") or "r"
		if (self.markup == None):
			markup_id = "_"
		else:
			markup_id=device_markup_to_id[self.markup]
		if (self.width == None):
			width_id = "00"
		else:
			width_id = str(self.width)
		if (self.javascript == None):
			javascript_id = "_"
		else:
			javascript_id = str(self.javascript)
		if (self.flash == None):
			flash_id = "_"
		else:
			flash_id = str(self.flash)
		if (self.images == None):
			images_id = "_"
		else:
			images_id=device_images_to_id[self.images]
		if (self.layout == None):
			layout_id = "_"
		else:
			layout_id=device_layout_to_id[self.layout]
		self.profileGene="".join([cookie_id,width_id,markup_id,images_id,javascript_id,flash_id,layout_id])

	"""
		The device sequence contains all the device profile features as a sequence. 
		This sequence is usually returned depending on the user agent.
	"""
	def createFromDeviceSequence(self,sequence):
		self.reset()		
		self.cookie=sequence[0]
		self.width=sequence[1]
		self.markup=sequence[2]
		self.images=sequence[3]
		self.javascript=sequence[4]
		self.flash=sequence[5]
		self.layout=sequence[6]
		self.createProfileGene()	
		#markup=list of sequences			

	"""
		The profile gene is a compact string representing the device profile which can be stored in a cookie.
	"""
	def createFromProfileGene(self,profileGene):
		self.profileGene=profileGene		
		self.reset()		
		if (profileGene[0] != "_"):		   
			self.cookie = (profileGene[0]=='c')
		self.width=int(profile[1:len(profileGene)-5])
		if (self.width==0):
			self.width=None		   
		if (profileGene[-5] != "_"):		
			self.markup = device_id_to_markup[profileGene[-5]]
		if (profileGene[-4] != "_"):		
			self.images = device_id_to_images[profileGene[-4]]
		if (profileGene[-3] != "_"):		
			self.javascript = int(profileGene[-3])
		if (profileGene[-2] != "_"):		
			self.flash = int(profileGene[-2])
		if (profileGene[-1] != "_"):		
			self.layout = device_id_to_layout[profileGene[-1]]
	
	def __unicode__(self):
		return self.profileGene 
	
"""
   Middleware for picking the right device profile. 
   Output: Decorate the request with device_profile and device_agent

	Uses cases:
   * ReturningUser: use the path to determine the device profile
   * | user agent | http accept | Action |
   * | __________ | YES			|		 |
   * | YES		  | ___________ |		 |
   * | YES		  | YES			|		 |
 
"""
class DevicePickMiddleware(object):
	def __init__(self):
		self.DeviceProfileDB = self.loadDeviceProfiles()
		deviceModels = self.loadDeviceModels()
		all_models=string.join(deviceModels, "|")
		self.re_models_semicolons = re.compile("(("+all_models+")[^/;[]*)([/;[]|$)")
		self.re_models_spaces = re.compile("(("+all_models+")[^/\s[]*)([/\s[]|$)")

	"""
	If the user appears to be a returning one, we will try first to parse the url and retrieve the existing settings.
	"""	   
	def process_request_for_returning_user(self, request):
		settings=re_restyled.search(request.path)
		if (settings!=None):
			#use the existing settings to tag the view
			request.DeviceProfile=self.createDeviceProfileFromSettings(settings)
			return None
		
	"""
	Retrieves the probable device model version from the user agent	   
	"""	   
	def extractDeviceAgent(self,user_agent):
		has_semicolons = (user_agent.count(';')>0)
		if (has_semicolons):
			model=self.re_models_semicolons.search(user_agent.replace("(",";").replace(")",";"))
			if (model!=None):
				return model.group(1).strip()
			else:
				return self.extractBrowser(user_agent)
		else:
			model=self.re_models_spaces.search(user_agent.replace("("," ").replace(")"," "))
			if (model!=None):
				return model.group(1).strip()
			else:
				return self.extractBrowser(user_agent)
	"""
	Retrieves the probable browser version from the user agent	   
	"""	   
	def extractBrowser(self,user_agent):
		model=re_browser.search(user_agent)
		if (model!=None):
			return model.group(1).strip()
		else:
			return None


	"""
	Try to retrieve the device sequence from the database
	"""	   
	def lookupDeviceSequenceFromDeviceAgent(self,device_agent):
		if (device_agent == None):
			return None
		if not self.DeviceProfileDB.has_key(device_agent):
			return None
		return self.DeviceProfileDB.get(device_agent)

	"""
	Loads the devices models which will be used to extract the mobile device	
	"""
	def loadDeviceModels(self):
		f = None
		try:
			f = open(os.path.join(os.path.dirname(__file__), 'device-models.txt'))
			ss = f.readlines()
		finally:
			if f:
				f.close()
		return [s.strip() for s in ss if not s.startswith('#')]

	"""
	Loads the devices profiles.
	"""
	def loadDeviceProfiles(self):
		r = None		 
		try:		
			f = None
			f = open(os.path.join(os.path.dirname(__file__), 'device-profile.json'))
			db = f.read()
			r = json.loads(db)
		finally:
			if f:
				f.close()
		return r

	"""
		Try to extract a profile gene or return None   
	"""	   
	def extractProfileGene(self,anystring):
		return re_restyled.search(anystring)

	"""
	  Returns the markup given the http_accept in lower case	
	"""	   
	def markupFromHttpAccept(self,http_accept):
		if (http_accept.count('text/html')>0):
			return "html"
		if (http_accept.count('application/xhtml')>0):
			return "xhtml"
		#mobile device		  
		if (http_accept.count('vnd.wap.wml')>0):
			return "wml"
		if (http_accept.count('vnd.wap.xhtml')>0):
			return "xhtml-mp"
		return None

	"""
	  Returns the best images format given the http_accept in lower case	
	"""	   
	def imagesFromHttpAccept(self,http_accept):
		if (http_accept.count('image/jpeg')==0):
			return None
		if (http_accept.count('image/png')>0):
			return "jpeg,png"
		if (http_accept.count('image/gif')>0):
			return "jpeg,gif"
		return "jpeg"

           
	"""
	Process the request.
	"""
	def process_request(self, request):
		#If the device_profile has already been defined, just exit		  
		if (hasattr(request,"device_profile")):
			return None

		http_accept = None
		user_agent = None
		
		if request.META.has_key("HTTP_ACCEPT"):
			http_accept = request.META["HTTP_ACCEPT"].lower()

		if request.META.has_key("HTTP_USER_AGENT"):
			# Let's try to identify the mobile device
			user_agent = request.META["HTTP_USER_AGENT"].lower()
		
		#Exit if no http_accept nor user_agent		
		if (http_accept == None and user_agent == None):
			request.device_profile=None
			return None
		
		#If only user_agent, try to find it in the database otherwise return None		 
		if (http_accept==None):
			request.device_agent=self.extractDeviceAgent(user_agent)
			device_sequence = self.lookupDeviceSequenceFromDeviceAgent(request.device_agent)
			if (device_sequence==None):
				request.device_profile=None				   
				return None
			request.device_profile=DeviceProfile()
			request.device_profile.createFromDeviceSequence(device_sequence)
			return None

		#If only http_accept		
		if (user_agent==None):
			request.device_agent = None
			#determine markup and images
			markup=self.markupFromHttpAccept(http_accept)
			#We need to know at least the markup			
			if (markup==None):
				request.device_profile = None
				return None		  
			images=self.imagesFromHttpAccept(http_accept)
			device_sequence = [None, None, markup, images, None, None,None]
			request.device_profile=DeviceProfile()
			request.device_profile.createFromDeviceSequence(device_sequence)
			return None
		
		#Both user_agent and http_accept are obviously defined
 
		request.device_agent=self.extractDeviceAgent(user_agent)
		ua_device_sequence = self.lookupDeviceSequenceFromDeviceAgent(request.device_agent)
		markup=self.markupFromHttpAccept(http_accept)
		images=self.imagesFromHttpAccept(http_accept)
 
		#If the user agent is not defined in the database, exit with default		
		if (ua_device_sequence == None):
			if (markup==None):
				request.device_profile=None
				return None
			device_sequence = [None, None, markup, images, None, None,None]
			request.device_profile=DeviceProfile()
			request.device_profile.createFromDeviceSequence(device_sequence)
			return None
	
		#A user agent has been found in the database, let's merge with http_accept values, taking http_accept in priority
		if (markup!=None):
			ua_device_sequence[2]= markup
		if (images!=None):
			ua_device_sequence[3]= images
		
		request.device_profile=DeviceProfile()
		request.device_profile.createFromDeviceSequence(ua_device_sequence)
		return None




            
 
