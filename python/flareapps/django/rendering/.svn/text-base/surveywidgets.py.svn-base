"""
   Copyright (c) 2008-2009 Flarebyte.com Limited. All Rights Reserved.
"""
"""
   Title: Widgets
   Creator(s):Olivier Huin
   Subject:Widgets, for representing surveys, rating
   Contributor(s):
   Description: 
"""

import string

"""
  Rating widget
"""
class RatingWidget(Widget):
    def __init__(self,rating,worst=1.0,best=5.0):
        self.init()     
        self.widget ="rating"
        self.rating = rating
        self.worst = worst
        self.best = best
  
    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["rating"] = self.rating
        r["worst"] = self.worst
        r["best"] = self.best
        return r

"""
  Review widget
"""
class ReviewWidget(Widget):
    def __init__(self,summary,description,dtreviewed,reviewer):
        self.init()     
        self.widget ="review"
        self.summary = summary
        self.description = description
        self.dtreviewed = dtreviewed
        self.reviewer = reviewer
        self.ratings = []
    
    def addRating(self,rating):
        self.ratings.append(rating)

    def asDataModel(self):
        r = Widget.asDataModel(self)        
        r["rating"] = self.rating
        r["worst"] = self.worst
        r["best"] = self.best
        r["reviewer"] = self.reviewer
        r["ratings"] = self.ratings
        return r


