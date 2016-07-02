#!/usr/bin/env python
# encoding: utf-8
"""
tango-normalize-grey.py filename

Created by Olivier on 2012-12-28.
Copyright (c) 2012 Flarebyte.com Ltd. All rights reserved.
"""

import sys
import os
import re


def normalize(filename):
  (root, ext)=os.path.splitext(filename)
  filename2 = root + "-norm"+ ext
  print "Normalizing ", filename2
  f=open(filename, 'r')
  text = f.read()
  o = open(filename2, 'w')
  colors = list(set(re.findall(r'#[0-9a-f]{6}', text)))
  print "colors ", colors
  for color in colors:
     text = text.replace(color, tangolize(color))
  o.write(text)

def tangolize(color):
  hexstr = color.strip('#')
  r, g, b = int(hexstr[:2], 16), int(hexstr[2:4], 16), int(hexstr[4:], 16)
  gray = r + g + b
  maximum = 0xff+0xff+0xff
  quot = 1.0 * gray/maximum
  div = 1.0 /6
  if quot>5*div:
    return "#eeeeec"
  if quot>4*div:	
    return "#d3d7cf"
  if quot>3*div:
    return "#babdb6"
  if quot>2*div:
    return "#888a85"
  if quot>1*div:
    return "#555753"
  if quot>0:
    return "#2e3436"
  
  return "#000000"

if __name__ == '__main__':
  filename=sys.argv[1]
  normalize(filename)


