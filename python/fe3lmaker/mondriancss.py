#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-04-18.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os

	
FONTS="Gill Sans, Helvetica, Verdana,Arial"
LIST_MARGIN="1em 1em 1em 10px"
LIST_PADDING_LEFT="10px"
LIST_MARGIN_TOPBOTTOM="0.3em"
BACKGROUND_COLOR="#b0c4de"
NAME_ID=">>>[selector-name]"
font_color="#2e3436"
fontb_color="#555753"
fontbg_color="#F6F6F6"


def padding_std(top,bottom,left=8,right=8):
	r = "%fem %fpx %fem %fpx" % (top,left,bottom,right)
	return r

def margin_std(top,bottom):
	r = "%fem -8px %fem -8px" % (top,bottom)
	return r
	
def font_size(index):
	maxi=5
	v = 1.0
	for i in range(maxi-index):
		v = v * 1.2
	r = "%.2fem" % (v)
	return r
		
	
def clone(mydict,name):
	r = mydict.copy()
	r[NAME_ID]=name
	return r

def mondrian_css(theme): 
	maincolor=theme["maincolor"]
	bgcolor=theme["bgcolor"]
	font_color=theme["font_color"]
	fontb_color=theme["fontb_color"]
	fontbg_color=theme["fontbg_color"]
	SEPARATOR_LINE="1px solid %s" % (maincolor)
	stylesheet=[]	
	h1_top_aligned= {
		NAME_ID:"h1.top-aligned",
		"font-size":font_size(1),
		"padding":padding_std(0.3,0.3),
		"margin":margin_std(0,0.5),
		"font-weight":"bold",
		"color": bgcolor,
		"background-color":maincolor,
	}
	stylesheet.append(h1_top_aligned)
	
	h1={
		NAME_ID:"h1",
		"font-size":font_size(1),
		"padding":padding_std(0.3,0.3),
		"margin":margin_std(0.2,0.3),
		"color": bgcolor,
		"background-color":maincolor,
		"border-top":SEPARATOR_LINE,
	}
	stylesheet.append(h1)

	h2={
		NAME_ID:"h2",
		"font-size":font_size(2),
		"padding":padding_std(0,0,4),
		"margin":margin_std(0.2,0.3),
		"border-bottom":SEPARATOR_LINE,
		"color": bgcolor,
		"background-color":maincolor,
		"clear": "both",
	}
	stylesheet.append(h2)

	h3=clone(h2,"h3")
	h3["font-size"]=font_size(3)
	stylesheet.append(h3)

	h4=clone(h3,"h4")
	h4["font-size"]=font_size(4)
	h4["color"]=maincolor
	h4["background-color"]=bgcolor
	stylesheet.append(h4)


	""" ---------------------- Basic elements ----------------- """

	body={
		NAME_ID:"body",
		"color": font_color,
		"font-size": "100%",
		"font-weight": "normal",
		"font-family": FONTS,
	}
	stylesheet.append(body)

	p={
		NAME_ID:"p",
		"line-height": "125%",
		"margin-top": "0.2em",
		"margin-bottom": "0.8em",
		"clear": "both",
	}
	stylesheet.append(p)

	footer_p={
		NAME_ID:"#footer p",
		"color": font_color,
		"font-size": ".8em",
		"margin": margin_std(0,0),
		"padding": "0em",
	}
	stylesheet.append(footer_p)

	strong = {
		NAME_ID:"strong",
		"font-weight": "bolder",
	}
	stylesheet.append(strong)
	
	em = {
		NAME_ID:"em",
		"font-style": "italic",
	}
	stylesheet.append(em)

	""" ---------------------- Containers ----------------- """

	wrap={
		NAME_ID:"#wrap",
		"width":"100%",
		"overflow":"hidden",
		"position":"absolute",
		"left":"0",
		"padding":"0",
		"background-color":bgcolor,
	}
	stylesheet.append(wrap)

	content={
		NAME_ID:"#content",
		"margin":"8px 8px 8px 8px",
	}
	stylesheet.append(content)

	footer={
		NAME_ID:"#footer",
		"padding":".7em 0em",
		"color": "white",
		"background-color":font_color,
		"clear":"both",
		"height":"3em",
	}
	stylesheet.append(footer)

	""" ---------------- Navigations --------------- """

	breadcrumbs={
		NAME_ID:"ul.breadcrumbs",
		"padding": padding_std(0.5,0.5),
		"margin": margin_std(0,0),
		"font-size": "80%",
		"list-style-type":"none",
		}
	stylesheet.append(breadcrumbs)

	breadcrumbs_li={
		NAME_ID:"ul.breadcrumbs li",
		"display":"inline",
		"line-height":"1.5em",
		}
	stylesheet.append(breadcrumbs_li)

	""" Rating """

	div_rating_span = {
		NAME_ID:"div.rating span",
		"float": "right",
		"padding-top": "0.4em",
	}
	stylesheet.append(div_rating_span)

	div_rating = {
		NAME_ID:"div.rating",
		"width": "150px",
		"height": "24px",
		"background": "url(http://media.flairbyte.com/fe3l/falcon/png/sprite-rating.png) no-repeat 0px 0px",
		"margin-bottom": "1em",
	}
	stylesheet.append(div_rating)

	for i in range(6):
		star={
		NAME_ID:"div.stars-%d" % (i),
		"background-position": "left %dpx" % (-i*25),
		}
		stylesheet.append(star)

	div_top = {
		NAME_ID:"div.top",
		"font-size": ".9em",
		"background": "url(http://media.flairbyte.com/fe3l/falcon/png/img-top.png) no-repeat 10px center",
		"border-bottom": SEPARATOR_LINE,
		"border-top": SEPARATOR_LINE,
		"padding": ".3em 2.2em .3em 2.2em",
		"margin": "0.5em -10px 0.5em -10px",
		"clear": "both",
	}
	stylesheet.append(div_top)

	div_top_a = {
		NAME_ID:"div.top a",
		"color": "",
		"text-decoration": "none",
		"width": "100%",
		"display": "block",
	}
	stylesheet.append(div_top_a)

	""" FOOTER OR ADMIN NAV """

	ul_nav_footer = {
		NAME_ID:"ul.nav-footer",
		"display": "block",
		"color":maincolor,
		"padding": "0em .5em .5em 8px",
		"font-size": ".85em",
		"height": "2em",
	}
	stylesheet.append(ul_nav_footer)

	ul_nav_footer_li = {
		NAME_ID:"ul.nav-footer li",
		"display": "inline",
		"line-height": "1.5em",
		"float": "left",
	}
	stylesheet.append(ul_nav_footer_li)

	ul_nav_footer_li_a = {
		NAME_ID:"ul.nav-footer li a",
		"padding-right": "0.5em",
		"padding-left": "0.5em",
		"border-right": SEPARATOR_LINE,
		"text-decoration": "none",
	}
	stylesheet.append(ul_nav_footer_li_a)

	ul_nav_footer_li_last_a = {
		NAME_ID:"ul.nav-footer li.last a",
		"border-right": "none",
		"padding-right": "0",
	}
	stylesheet.append(ul_nav_footer_li_last_a)

	ul_nav_footer_li_first_a = {
		NAME_ID:"ul.nav-footer li.first a",
		"padding-left": "0",
	}
	stylesheet.append(ul_nav_footer_li_first_a)


	ul_nav_footer_a = {
		NAME_ID:"ul.nav-footer a",
		"color": bgcolor,
	}
	stylesheet.append(ul_nav_footer_a)

	ul_nav_footer_li_a_hover = {
		NAME_ID:'ul.nav-footer a:hover',
		"color": maincolor,
		"background-color": bgcolor,
		"outline": "none",
	}
	stylesheet.append(ul_nav_footer_li_a_hover)

	""" ------------- Advertisements ------------------"""

	advertisement = {
		NAME_ID:".advertisement",
		"padding": "0",
		"margin": "0.5em 0 0.5em 0",
		"width": "100%",
	}
	stylesheet.append(advertisement)

	advertisement_p = {
		NAME_ID:".advertisement p",
		"border": SEPARATOR_LINE,
		"padding": "0.4em 0.4em",
		"background-color": fontbg_color,
		"margin-bottom": "0",
		"margin-top": "0",
	}
	stylesheet.append(advertisement_p)

	advertisement_span = {
		NAME_ID:".advertisement span",
		"text-transform": "uppercase",
		"padding": "0",
		"float": "right",
		"font-size": "0.7em",
		"color": fontb_color,
		"padding-bottom": "0.3em",
	}
	stylesheet.append(advertisement_span)

	""" ------------- Branding ------------------"""

	header_div_branding = {
		NAME_ID:"#header div.branding",
		"height": "68px",
		"background": "",
		"display": "block",
		"width": "100%",
		"overflow": "hidden",
	}
	stylesheet.append(header_div_branding)

	header_div_branding_img = {
		NAME_ID:"#header div.branding img",
		"padding-top": "20px",
		"padding-left": "10px",
	}
	stylesheet.append(header_div_branding_img)

	header_div_branding_a = {
		NAME_ID:"#header div.branding a",
		"width": "100%",
		"height": "68px",
		"display": "block",
		"background-image": "none",
		"padding-right": "none",
	}
	stylesheet.append(header_div_branding_a)

	header_div_branding_p = {
		NAME_ID:"#header div.branding p",
		"text-indent": "-5000px",
	}
	stylesheet.append(header_div_branding_p)

	""" ------------- Links ------------------"""
	a = {
		NAME_ID:"a",
		"color":font_color,
	}
	stylesheet.append(a)
	
	a_hover = {
		NAME_ID:"a:hover",
		"color":bgcolor,
		"background-color":font_color,
	}
	stylesheet.append(a_hover)

	a_external = {
		NAME_ID:"a.external",
		"background": "url(http://media.flairbyte.com/fe3l/falcon/png/img-link-external.png) no-repeat right top",
		"padding-right": "1em",
	}
	stylesheet.append(a_external)

	a_ical = {
		NAME_ID:"a.ical",
		"background": "url(http://media.flairbyte.com/fe3l/falcon/png/img-link-ical.png) no-repeat right top",
		"padding-right": "1em",
	}
	stylesheet.append(a_ical)

	mail_to = {
		NAME_ID:'a[href^="mailto:"]',
		"background": "url(http://media.flairbyte.com/fe3l/falcon/png/img-link-email.png) no-repeat right top",
		"padding-right": "1em",
	}
	stylesheet.append(mail_to)

	tel = {
		NAME_ID:'a[href^="tel:"]',
		"background": "url(http://media.flairbyte.com/fe3l/falcon/png/img-link-tel.png) no-repeat right top",
		"padding-right": "1em",
	}
	stylesheet.append(tel)

	sms = {
		NAME_ID:'a[href^="sms:"]',
		"background": "url(http://media.flairbyte.com/fe3l/falcon/png/img-link-sms.png) no-repeat right top",
		"padding-right": "1em",
	}
	stylesheet.append(sms)
	
	""" ----------------------- CLOUDS ------------------------ """
	ul_list_cloud = {
		NAME_ID:'ul.list-cloud',
		"list-style-type": "none",
		"color": font_color,
	}
	stylesheet.append(ul_list_cloud)
	for i in range(5):
		height=0.8+i*0.15
		li_cloudn = {
			NAME_ID:'li.cloud'+str(i),
			"display": "block",
			"font-size": "%fem" % (height),
		}
		stylesheet.append(li_cloudn)
	
	ul_list_cloud_a = {
		NAME_ID:'ul.list-cloud a',
		"display": "block",
		"text-decoration": "none",
	}
	stylesheet.append(ul_list_cloud_a)
	
	ul_list_cloud_a_hover = {
		NAME_ID:'ul.list-cloud a:hover',
		"color": bgcolor,
		"background-color": maincolor,
		"outline": "none",
	}
	stylesheet.append(ul_list_cloud_a_hover)

	""" ----------------------- Definition List ------------------------ """
	
	dl = {
		NAME_ID:'dl',
		"margin": margin_std(1,1),
		"padding": "0",
	}
	stylesheet.append(dl)
	
	dt = {
		NAME_ID:'dt',
		"position": "relative",
		"left": "0",
		"top": "0.8em",
		"width": "4em",
		"font-size": "120%",
	}
	stylesheet.append(dt)
	
	dd = {
		NAME_ID:'dd',
		"border-left": SEPARATOR_LINE,
		"margin": "0 0 0 8em",
		"padding": "0em 0 .5em 1em",
	}
	stylesheet.append(dd)

	""" ----------------------- Tubes list ------------------------ """
	ul_tube_list = {
		NAME_ID:"ul.tube-list",
		"display": "block",
		"color":font_color,
		"padding": "0em .5em .5em 8px",
		"height": "2em",
	}
	stylesheet.append(ul_tube_list)

	travelstatus_green = {
		NAME_ID:".travelstatus-green",
		"display": "inline",
		"color":bgcolor,
		"background-color":"#4e9a06",
		"border-right": "1px solid white",
		"padding": padding_std(0,0,4,4),
		"line-height": "1.5em",
		"float": "left",
	}
	stylesheet.append(travelstatus_green)

	travelstatus_orange = {
		NAME_ID:".travelstatus-orange",
		"display": "inline",
		"color":fontb_color,
		"padding": padding_std(0,0,4,4),
		"font-size": "80%",
		"line-height": "1.5em",
		"float": "left",
	}
	stylesheet.append(travelstatus_orange)

	travelstatus_red = {
		NAME_ID:".travelstatus-red",
		"display": "inline",
		"color":fontb_color,
		"padding": padding_std(0,0,4,4),
		"font-size": "70%",
		"line-height": "1.5em",
		"float": "left",
	}
	stylesheet.append(travelstatus_red)
	
	return stylesheet


def get_stylesheet():
	theme_1={"maincolor": "#204a87", "bgcolor": "#eeeeec","font_color":"#2e3436","fontb_color": "#555753","fontbg_color":"#F6F6F6"}
	theme_2={"maincolor": "#d3d7cf", "bgcolor": "#2e3436","font_color":"#3465a4","fontb_color": "white","fontbg_color":"#888a85"}
	return mondrian_css(theme_2)



	
