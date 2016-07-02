#!/usr/bin/env python
# encoding: utf-8
"""
memoire.py

Created by Olivier Huin on 2010-04-04.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import re

RE_MEMORY=re.compile("^\s*(\d+)\s")


def read_memoire():
	fin = open("memoire.txt")
	lines = fin.readlines()
	fin.close()
	mems = []
	for line in lines:
		m=RE_MEMORY.search(line)
		if m:
			mems.append(int(m.group()))
	total= sum(mems)
	return total

print read_memoire()
