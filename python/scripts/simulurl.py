#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2009-11-05.
Copyright (c) 2009 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os

base="http://fe3l.com/"
"""[people=p=1|subject=s=2|place=l=3|event=e=4|analysis=a=5|technique=t=6] """
suffixes=["p","e"]
"""[topic]/[highlight|popular|editor|thread|photo|video|mail|feedback] """
#suffixes=["h","p","e","t","f","v","m","k"]
""" film,restaurant, bars&pub,hotels, museums, kids, music, classical & opera, art, theatre, comedy, cabaret, dance, books, poetry, clubs, nightlife, gay, lesbian, sport, 
shopping, travel, offers,dating, jobs """
categories={"f":"films","r":"restaurants", "b":"bars&pubs","h":"hotels","m": "museums", "k":"kids", "u":"music", "l":"classical & opera","a":"art", "t":"theatre","y":"comedy",
"c":"cabaret","d":"dance", "b":"books", "p":"poetry", "c":"clubs", "n":"nightlife", "g":"gay&lesbian", "s":"sport", "s":"shopping", "t":"travel","o": "offers","d":"dating", "j":"jobs"}
art_topics=["alternative","architecture","comic","conceptual","craft","deco","digital","drawing","etching","fashion","filmmaking","garden","graphic","illustration","installation",
"litho","mixmedia","painting","photo","printmaking","screen","sculpture","street","typo"]
sorting={"l":"latest","L":"oldest","p":"popular","P":"popular asc","e":"editor"}
richestcities=["tokyo","newyork","losangeles","chicago","paris","london","osaka","mexico","philadelphia","washingtondc","boston","dallas", "buenosaires","hongkong",
"sanfrancisco","atlanta","houston","miami","saopaulo","seoul","toronto","detroit","madrid","seattle", "moscow","sydney","phoenix","minneapolis","sandiego","riodejaneiro",
"barcelona","shanghai","melbourne","istanbul","denver", "singapore","taipei","mumbai","rome","montreal","milan","baltimore","metromanila","stlouis","beijing","cairo",
"jakarta","stpetersburg", "pusan","kolkata","vienna","delhi","telaviv","santiago","cleveland","bangkok","tehran","portland","bogota","guangzhou",
"pittsburgh","riyadh","lisbon","vancouver","johannesburg","monterrey","stockholm","capetown","berlin","athens","birmingham","fukuoka", "manchester","lima",
"belohorizonte","guadalajara","hamburg","turin","lyon","jeddah","karachi","dhaka","munich","dublin","leeds","warsaw", "tianjin","bangalore","portoalegre",
"helsinki","naples","budapest","zurich","ankara","amsterdam","auckland","copenhagen","recife","rotterdam"] 

def topics():
	for art_topic in art_topics:
		url= base+art_topic
		print url, len(url)

def richest_cities():
	max_length=0
	for city in richestcities:
		for k in categories:
			for l in sorting: 
				url= base+city+"/"+k+l
				if (len(url)>30):
					print url, len(url)
				if (len(url)>max_length):
					max_length=len(url)
	print max_length
	


def richest_cities_max():
	max_length=0
	count=0.0
	for city in richestcities:
		url= base+city+"/"
		if (len(url)>26):
			print url, len(url)
			count=count+1
		if (len(url)>max_length):
			max_length=len(url)
						
	print "count, max_length",100*count/len(richestcities), max_length

				
if __name__ == '__main__':
	richest_cities_max()
