"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing money
   Contributor(s):
   Description: 
"""

import string


"""
  Price widget
"""
class PriceWidget(Widget):
    def __init__(self):
        self.init()     
        self.widget ="price"
        self.price = None
        self.currency = None
    
    def setPrice(self,price,currency):
        self.price = price
        self.currency = currency
  
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["price"] = self.price
        r["currency"] = self.currency
        return r


