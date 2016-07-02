"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""

__author__="olivierhuin"
__date__ ="$Sep 13, 2009 10:56:31 PM$"

if __name__ == "__main__":
    print "Hello World";

import logging

RESPONSE_TIMES=("memory","fileio","database","network","blink_of_an_eye","fax","eurostar")
SERVICE_LOCATOR_MODE = ("unittest","sandbox","integration","staging","live")

class Service(object):
    """
    Abstract Service class
    """
    def __init__(self):
        self.configuration=None
        self.locator=None
        self.logger = logging.getLogger("Services")

    
    def perform(self,**kwargs):
        pass
        
    def get_param_or_conf(self,name,**kwargs):
        r = kwargs[name]
        if (not r):
            r = self.configuration[name]
        if (not r):
            self.logger.warn("The parameter %s is undefined", name)
            return None
        return r

    def get_param(self,name,**kwargs):
        r = kwargs[name]
        if (not r):
            self.logger.warn("The parameter %s is undefined", name)
            return None
        return r


class NotFoundService(Service):
    def perform(self,**kwargs):
        return None    


class ServiceLocator(object):

    def __init__(self,mode="unittest"):
        self.mode=mode
        self.services={}
        self.resolvers=[]

    def perform(self,strategy,**kwargs):
        return self.find_service(strategy).perform(kwargs)
    
    """ Lazy loading of the service"""
    def find_service(self,strategy):
        if (strategy in services):
            return self.services[strategy]
        r = None
        for resolver in resolvers:
            r = resolver(strategy)
            if r not None:                
                break
        if (r is None):
            r = NotFoundService()
        r.locator=self
        self.services[strategy]=r
        return r


    



    

    



    

    