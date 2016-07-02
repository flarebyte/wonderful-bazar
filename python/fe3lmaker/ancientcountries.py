#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-03-08.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import devutils

ancientcountries={
"f4e5baf6-7382-4eee-ae1b-9a3ecd9657a5":('7382', 'f4e5baf6-7382-4eee-ae1b-9a3ecd9657a5', 'GoldCoast', 'Gold Coast', ['Gold Coast']),
"ca3b860c-f3e5-4ae1-910c-f763ebba26c9":('f3e5', 'ca3b860c-f3e5-4ae1-910c-f763ebba26c9', 'SouthernRhodesia', 'Southern Rhodesia', ['Southern Rhodesia']),
"7963355f-0edc-4fa2-869d-0440507a543e":('0edc', '7963355f-0edc-4fa2-869d-0440507a543e', 'KhmerRepublic', 'Khmer Republic', ['Khmer Republic']),
"11fdc8b3-2674-466e-a7ec-ee8e3205309b":('2674', '11fdc8b3-2674-466e-a7ec-ee8e3205309b', 'Zaire', 'Zaire', ['Zaire']),
"a1f3e4e8-a443-4cfa-8d82-555474f81fb7":('a443', 'a1f3e4e8-a443-4cfa-8d82-555474f81fb7', 'FrenchSudan', 'French Sudan', ['French Sudan']),
"e97aa734-da5e-41ce-baaa-c9d26988f6b7":('da5e', 'e97aa734-da5e-41ce-baaa-c9d26988f6b7', 'Abyssinia', 'Abyssinia', ['Abyssinia']),
"83962683-c8c2-4dbc-8122-2221fb7c49aa":('c8c2', '83962683-c8c2-4dbc-8122-2221fb7c49aa', 'FederalRepublicOfYugoslavia', 'Federal Republic of Yugoslavia', ['Federal Republic of Yugoslavia']),
"44a02a36-3443-4aae-84e2-04b50eb077cf":('3443', '44a02a36-3443-4aae-84e2-04b50eb077cf', 'Siam', 'Siam', ['Siam']),
"d0aacd93-f4fd-4ac7-aaf7-163a696109e7":('f4fd', 'd0aacd93-f4fd-4ac7-aaf7-163a696109e7', 'ElliceIslands', 'Ellice Islands', ['Ellice Islands']),
"b877b6b2-5ba1-4fbd-966a-c67cba8fe41c":('5ba1', 'b877b6b2-5ba1-4fbd-966a-c67cba8fe41c', 'NewGranada', 'New Granada', ['New Granada']),
"3c01fc19-635d-4523-8f89-0ca4bc3aaeee":('635d', '3c01fc19-635d-4523-8f89-0ca4bc3aaeee', 'Dahomey', 'Dahomey', ['Dahomey']),
"7cfd1b8d-b246-437a-b380-7d0270aa2091":('b246', '7cfd1b8d-b246-437a-b380-7d0270aa2091', 'GilbertIslands', 'Gilbert Islands', ['Gilbert Islands']),
"f0b638a7-cd35-4778-86bb-de44f1ec46c3":('cd35', 'f0b638a7-cd35-4778-86bb-de44f1ec46c3', 'NewHebrides', 'New Hebrides', ['New Hebrides']),
"8a7728da-8501-47c3-9a81-fb7ff540b214":('8501', '8a7728da-8501-47c3-9a81-fb7ff540b214', 'Burma', 'Burma', ['Burma']),
"8af5ab2e-e571-4d46-86bd-24394c542cf1":('e571', '8af5ab2e-e571-4d46-86bd-24394c542cf1', 'NorthernRhodesia', 'Northern Rhodesia', ['Northern Rhodesia']),
"9cacb4d3-81b0-4cd2-ae77-335299fda53a":('81b0', '9cacb4d3-81b0-4cd2-ae77-335299fda53a', 'French Somaliland', 'French Somaliland', ['French Somaliland']),
"7f5eb6c8-f44a-403c-b8d2-c66b744c4c97":('f44a', '7f5eb6c8-f44a-403c-b8d2-c66b744c4c97', 'Eire', 'Eire', ['Eire']),
"f542406b-63e6-4d4d-95e0-066aa0b4f18c":('63e6', 'f542406b-63e6-4d4d-95e0-066aa0b4f18c', 'Persia', 'Persia', ['Persia']),
"01bc403f-33ca-4726-95ef-163ad33ebb76":('33ca', '01bc403f-33ca-4726-95ef-163ad33ebb76', 'Ceylon', 'Ceylon', ['Ceylon']),
"8c445cf0-d961-4ce4-9bf6-d9785dfadf6a":('d961', '8c445cf0-d961-4ce4-9bf6-d9785dfadf6a', 'UpperVolta', 'Upper Volta', ['Upper Volta']),
"9e2fbf5a-0419-463d-86ce-a773406d67be":('0419', '9e2fbf5a-0419-463d-86ce-a773406d67be', 'UbangiShari', 'Ubangi Shari', ['Ubangi Shari']),
"28ab8fe9-5d57-409c-86a0-49c565742547":('5d57', '28ab8fe9-5d57-409c-86a0-49c565742547', 'NewSpain', 'New Spain', ['New Spain']),
"d58b7a21-25cb-4aed-9f70-2b004f8841b2":('25cb', 'd58b7a21-25cb-4aed-9f70-2b004f8841b2', 'Kampuchea', 'Kampuchea', ['Kampuchea']),
"a3c98b0e-a523-42d5-a8c0-0f6bcdeb30bc":('a523', 'a3c98b0e-a523-42d5-a8c0-0f6bcdeb30bc', 'Malaya', 'Malaya', ['Malaya']),
"61957eea-4d1c-4dae-8b5e-b5444e375583":('4d1c', '61957eea-4d1c-4dae-8b5e-b5444e375583', 'BritishHonduras', 'British Honduras', ['British Honduras']),
"c58168a9-1109-47ef-9114-80e2d120a52d":('1109', 'c58168a9-1109-47ef-9114-80e2d120a52d', 'BritishMandateOfPalestine', 'British Mandate of Palestine', ['British Mandate of Palestine']),
"e3afdef4-6355-4777-9964-d03b0c88c55f":('6355', 'e3afdef4-6355-4777-9964-d03b0c88c55f', 'Moldavia', 'Moldavia', ['Moldavia']),
}
