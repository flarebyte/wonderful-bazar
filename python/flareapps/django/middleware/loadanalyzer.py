"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: middleware which analyzes the load. This analysis should facilitate:
        * detecting a risky level of load possibly caused by a "Denial of Service Attack" or a "Slashdot effect". In most cases, an alert should be sent to the administrator.
        * identifying a returning user.
        * capture the user surfing profile: frequent access (broadband)
   Creator(s):Olivier Huin
   Subject:Load analyzer middleware
   Contributor(s):
   Description: 
"""

from django.core.cache import cache
import time
import logging
import string

hourly_timeout=3600
IP_KEY="HTTP_X_FORWARDED_FOR"
#IP_KEY="REMOTE_ADDR"

"""
Configuration for the load
"""
class LoadConfiguration(object):
    def setMinutelyThreshold(self,critical_threshold,thresholds):
        self.thresholds_minutely = thresholds
        self.critical_threshold_minutely = critical_threshold

    def setHourlyThreshold(self,critical_threshold,thresholds):
        self.thresholds_hourly = thresholds
        self.critical_threshold_hourly = critical_threshold
    
    def setLevels(self,levels):
        self.levels = levels
    
    def isHourlyCritical(self,hourlyLoad):
        return hourlyLoad>self.critical_threshold_hourly

    def isMinutelyCritical(self,minutelyLoad):
        return minutelyLoad>self.critical_threshold_minutely
        
    def getLevelForHourlyLoad(self, hourlyLoad):
         if (hourlyLoad<self.thresholds_hourly[0]):
            return self.levels[0]
         if (hourlyLoad<self.thresholds_hourly[1]):
            return self.levels[1]
         if (hourlyLoad<self.thresholds_hourly[2]):
            return self.levels[2]
         return self.levels[3]        

    def getLevelForMinutelyLoad(self, minutelyLoad):
         if (minutelyLoad<self.thresholds_minutely[0]):
            return self.levels[0]
         if (minutelyLoad<self.thresholds_minutely[1]):
            return self.levels[1]
         if (minutelyLoad<self.thresholds_minutely[2]):
            return self.levels[2]
         return self.levels[3]
       


"""
Class to record the actual load
"""
class ActualLoad(object):
    def __init__(self,conf):
        self.conf = conf
        self.counter = 1
        self.started = time.time()
        self.loadbyhour= None
        self.minutecounter = 1
        self.minute=time.time()//60
        self.loadbyminute= None
    def increment(self):
        self.counter = self.counter + 1
        self.loadbyhour =  (3600 * self.counter) // (time.time()-self.started)
        if (self.minute==time.time()//60)
            self.minutecounter =  self.minutecounter + 1
        else:
            #save previous loadbyminute and reset counter           
            self.loadbyminute = self.minutecounter
            self.minutecounter = 1
            self.minute=time.time()//60
    
    def getHourlyLevel(self):
        return self.conf.getLevelForHourlyLoad(self.loadbyhour)       
 
    def getMinutelyLevel(self):
        return self.conf.getLevelForMinutelyLoad(self.loadbyminute)

    def isHourlyCritical(self):
        return self.conf.isHourlyCritical(self.loadbyhour)
    
    def isMinutelyCritical(self):
         return self.conf.isMinutelyCritical(self.loadbyminute)    
    
    def __unicode__(self):
        "load/hour: %d load/minute: %d" % (self.loadbyhour,self.loadbyminute)  `   
        
        

"""
   Middleware for the analyze of the current overall and the user load. 
   If the load reaches a critical level, an error will be thrown, in order to avoid to block the server.
   Flag the request with the colours green,yellow,orange,red or black to represent the level of load.
   Decorate the request:
   * load_overall_hourly: colour depending on the overall load in the last hour.
   * load_overall_minutely: colour depending on the overall load in the last minute.
   * load_user_hourly: colour depending on the load for the current user in the last hour.
   * load_user_minutel: colour depending on the load for the current user in the last hour.
   * returningUser: True/False
"""
class LoadAnalyzerMiddleware(object):
    __init__(self):
        #Load the configurations thresholds
        #TODO: load confs from settings        
        self.loadConf = LoadConfiguration()
        self.loadConf.setLevels(("green","yellow","orange","red","black"))
        self.loadConf.setHourlyThreshold(3600*100,(720, 3600, 3600*10,3600*100))
        self.loadConf.setMinutelyThreshold(60*100,(12,60,60*10,60*100))
        self.loadUserConf = LoadConfiguration()
        self.loadUserConf.setLevels(("green","yellow","orange","red","black"))
        self.loadUserConf.setHourlyThreshold(3600*10,(720, 360, 3600,3600*10))
        self.loadUserConf.setMinutelyThreshold(60*10,(6,20,60,60*10))
        
        #open a file for load statistics
        self.statsfile = open('load-analyzer-middleware.csv','a')
        self.statsfile.write("year,month,weekday,day,hour,time,userid,loadbyhour,loadbyminute,userloadbyhour,userloadbyminute\n")

   """
    Warning: the load analyzer does not attempt to synchronize threads and as a consequence may be inaccurate.
    However, this should be an issue in most cases.    
    """
    def writeToStatistics(self,userid,loadbyhour,loadbyminute,userloadbyhour,userloadbyminute):
        #year,month,weekday,day,hour,hour-time
        dt = time.strftime("%Y,%m,%w,%d,%H,%H:%M,", time.localtime())
        self.statsfile.write(dt+string.join((userid,loadbyhour,loadbyminute,userloadbyhour,userloadbyminute),",")+"\n")
         
    def process_request(self, request):
    """
    Warning: the load analyzer does not attempt to synchronize threads and as a consequence may be inaccurate.
    However, this should be an issue in most cases.    
    """
        #hourly load: update
        load = cache.get('LoadAnalyzerMiddleware.load')
        if (load==None):
            #initialize load record
            load = ActualLoad(self.loadConf)            
            cache.set('LoadAnalyzerMiddleware.load',load,hourly_timeout)
        else:
            #increment load record
            load.increment()
            cache.set('LoadAnalyzerMiddleware.load',load,hourly_timeout)
        
        
        #Takes action if the global load is too high 
        if (load.isHourlyCritical()):
            logging.critical("LoadAnalyzerMiddleware.process_request: hourly critical level reached %d" %(load) )
            return HttpResponseServerError(status=503)
        if (load.isMinutelyCritical()):
            logging.critical("LoadAnalyzerMiddleware.process_request: minutely critical level reached %d" %(load) )
            return HttpResponseServerError(503)

        #Store the overall load level
        request.load_overall_hourly= load.getHourlyLevel()
        request.load_overall_minutely= load.getMinutelyLevel()
        
        #Initialize the user load
        request.load_user_hourly= None
        request.load_user_minutely= None
        
        #Record the load for the current user
        #If a session cookie as been defined, we should this...
        #Otherwise, let's base this on the IP and in the future, we may combine it with the user agent
        if (not request.has_key[IP_KEY]):
            logging.info("LoadAnalyzerMiddleware.process_request: no IP available ! Exit.")            
            #Load remains then undefined
            return None
        
        #if the IP address exists, let's use it 
        userId =  request.META[IP_KEY].lower()
         #hourly load: update
        userload = cache.get('LoadAnalyzerMiddleware.'+userId)
        if (load==None):
            #initialize load record
            userload = ActualLoad(self.loadUserConf)            
            cache.set('LoadAnalyzerMiddleware.'+userId,userload,hourly_timeout)
            request.returningUser=False
        else:
            #increment load record
            userload.increment()
            cache.set('LoadAnalyzerMiddleware.'+userId,userload,hourly_timeout)
            request.returningUser=True

        #Takes action if the user load is too high 
        if (userload.isHourlyCritical()):
            logging.critical("LoadAnalyzerMiddleware.process_request: user hourly critical level reached %d for user %s" %(userload,userId) )
            return HttpResponseServerError(status=503)
        if (userload.isMinutelyCritical()):
            logging.critical("LoadAnalyzerMiddleware.process_request: user minutely critical level reached %d for user %s" %(userload,userId) )
            return HttpResponseServerError(503)

        #Store the user load level
        request.load_user_hourly= userload.getHourlyLevel()
        request.load_user_minutely= userload.getMinutelyLevel()

        self.writeToStatistics(load.loadbyhour,load.loadbyminute,userload.loadbyhour,userload.loadbyminute)
        
        logging.debug("LoadAnalyzerMiddleware.process_request: userid=%s load_overall_hourly=%s load_overall_minutely=%S load_user_hourly=%s load_user_minutely=%s " %          (userId,request.load_overall_hourly,request.load_overall_minutely,request.load_user_hourly,request.load_user_minutely) )

   
           




            
 
