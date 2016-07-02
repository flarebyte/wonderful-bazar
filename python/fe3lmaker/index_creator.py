#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-02-22.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
from devutils import IndexCreation, SearchIndexCreation
import museums,arttopics,timeperiods,artists

def create_main_index():
	icreation = IndexCreation()
	icreation.open()
	icreation.write_entities(museums.museums,"/","museum")
	icreation.write_entities_parts(museums.museums,museums.museums_sections,"/","museum-section")
	icreation.write_entities(arttopics.arttopics,"/","art-topic")
	icreation.write_entities(timeperiods.timeperiods,"/","time-period")
	icreation.close()

	isearch=SearchIndexCreation()
	isearch.open()
	isearch.write_entities(museums.museums)
	isearch.write_entities(arttopics.arttopics)
	isearch.write_entities(timeperiods.timeperiods)
	isearch.sort()
	isearch.save()
	isearch.close()

"""
Artists
"""

def create_artists_index():
	artists_icreation = IndexCreation("indexes_artists.py")
	artists_icreation.open()
	artists_icreation.write_entities(artists.artists,"/artist/","artist")
	artists_icreation.close()

	artists_isearch=SearchIndexCreation("searchindexes_artists.py")
	artists_isearch.open()
	artists_isearch.write_entities(artists.artists)
	artists_isearch.sort()
	artists_isearch.save()
	artists_isearch.close()

create_artists_index()
