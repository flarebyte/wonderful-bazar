#!/usr/bin/env python
# encoding: utf-8
"""
museums.py

Created by Olivier Huin on 2009-11-12.
Copyright (c) 2009 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import datautils, devutils, semantics
import geohash


entities={
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":('4798', 'e4798bb2-5b17-471c-9f69-38a9d7e91a68', 'NationalGallery', 'National Gallery', ['National Gallery']),
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":('9324', '1ebf1c9b-9c32-4a80-999a-6f577a29ae50', 'VictoriaAndAlbertMuseum', 'Victoria & Albert Museum', ['Victoria & Albert Museum', 'Victoria And Albert Museum']),
"c3770c23-2986-4e4e-8406-c437e06c01e9":('2986', 'c3770c23-2986-4e4e-8406-c437e06c01e9', 'GeffryeMuseum', 'Geffrye Museum', ['Geffrye Museum']),
"52c859bb-c59b-43c1-9371-af05df1ab638":('8594', '52c859bb-c59b-43c1-9371-af05df1ab638', 'ChurchillMuseum', 'Churchill Museum And Cabinet War Rooms', ['Churchill Museum And Cabinet War Rooms']),
"da6fafd6-bafe-4403-9c2f-e7702b247436":('4403', 'da6fafd6-bafe-4403-9c2f-e7702b247436', 'SirJohnSoanesMuseum', 'Sir John Soanes Museum', ['Sir John Soanes Museum']),
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":('5291', '3e545cbe-5a9b-41dd-8d1d-953168c8472d', 'TateModern', 'Tate Modern', ['Tate Modern']),
"73294388-5a07-48ca-9012-3039a455da63":('5307', '73294388-5a07-48ca-9012-3039a455da63', 'NaturalHistoryMuseum', 'Natural History Museum', ['Natural History Museum']),
"af70fe3b-c49f-429c-ac2d-782e44b80399":('2497', 'af70fe3b-c49f-429c-ac2d-782e44b80399', 'VAMuseumOfChildhood', 'V&A Museum of Childhood', ['V&A Museum of Childhood', 'Victoria And Albert Museum of Childhood']),
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":('4734', 'a3268d2c-47a4-4572-bb62-55b822ba9cb5', 'ScienceMuseum', 'Science Museum', ['Science Museum']),
"1662b8a9-2956-4a57-87e9-f797ea008b09":('2956', '1662b8a9-2956-4a57-87e9-f797ea008b09', 'MuseumOfLondon', 'Museum Of London', ['Museum Of London']),
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":('9152', 'bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1', 'HMSBelfast', 'HMS Belfast', ['HMS Belfast']),
"e241c444-5603-458f-8040-73b1b87c7c3a":('5603', 'e241c444-5603-458f-8040-73b1b87c7c3a', 'NationalPortraitGallery', 'National Portrait Gallery', ['National Portrait Gallery']),
"f156dd09-a605-4e83-9291-cb6e1e539b86":('1605', 'f156dd09-a605-4e83-9291-cb6e1e539b86', 'BritishMuseum', 'British Museum', ['British Museum']),
"7262b139-af2b-4713-b8d1-7aaf5a344e17":('4713', '7262b139-af2b-4713-b8d1-7aaf5a344e17', 'HornimanMuseum', 'Horniman Museum', ['Horniman Museum']),
"874609af-cd08-43a8-9949-06e54bf0da03":('8746', '874609af-cd08-43a8-9949-06e54bf0da03', 'WallaceCollection', 'Wallace Collection', ['Wallace Collection']),
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":('2700', 'dd5d2700-33c9-45e6-a4f7-8c59f0046c26', 'MuseumInDocklands', 'Museum In Docklands', ['Museum In Docklands']),
"aba1c848-0c8d-4b40-a77d-63630e971557":('6363', 'aba1c848-0c8d-4b40-a77d-63630e971557', 'NationalMaritimeMuseum', 'National Maritime Museum', ['National Maritime Museum']),
"4db953be-e9a5-4bec-8099-684013a6a420":('8099', '4db953be-e9a5-4bec-8099-684013a6a420', 'ImperialWarMuseum', 'Imperial War Museum', ['Imperial War Museum']),
"02298ab2-da45-46f9-9f79-6ad906d35868":('5868', '02298ab2-da45-46f9-9f79-6ad906d35868', 'TateBritain', 'Tate Britain', ['Tate Britain'])
}

entities_geo={
"c3770c23-2986-4e4e-8406-c437e06c01e9":(51.531739000000002, -0.076218999999999995, 'gcpvnm06puqu'), # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":(51.502082999999999, -0.129028, 'gcpuvpdj3kje'), # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":(51.517102999999999, -0.116914, 'gcpvj66ugsn9'), # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":(51.508600000000001, -0.1283, 'gcpvj0fe66ux'), # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":(51.495983000000003, -0.176372, 'gcpugyx9f4zx'), # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":(51.481110999999999, -0.0055560000000000002, 'gcpuzgggnw9j'), # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":(51.528888999999999, -0.055, 'gcpvnsxcw3j5'), # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":(51.517705999999997, -0.096808000000000005, 'gcpvjf982hqw'), # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":(51.5075, -0.023611, 'gcpvp2wucvfm'), # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":(51.497500000000002, -0.17472199999999999, 'gcpuunbf8tvc'), # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":(51.517499999999998, -0.153056, 'gcpvhd2x1w11'), # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":(51.519444, -0.126944, 'gcpvj4gd9brw'), # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":(51.440556000000001, -0.060832999999999998, 'gcpuws7wyqxt'), # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":(51.507778000000002, -0.099167000000000005, 'gcpvj8xy91xx'), # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":(51.506661000000001, -0.081250000000000003, 'gcpvn0sb49x8'), # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":(51.496667000000002, -0.17194400000000001, 'gcpuundvc6t2'), # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":(51.495832999999998, -0.108333, 'gcpuvw90gxj1'), # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":(51.490833000000002, -0.127222, 'gcpuvje7gdbr'), # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":(51.509369, -0.12773300000000001, 'gcpvj0fzzd76'), # National Portrait Gallery
}

entities_geo_address={
"c3770c23-2986-4e4e-8406-c437e06c01e9":('136 Kingsland Road', 'E2 8EA', 'London', 'Shoreditch', 'GB'), # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":('Clive Steps,King Charles Street', 'SW1A 2AQ', 'London', '', 'GB'), # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":("13 Lincoln's Inn Fields", 'WC2A 3BP', 'London', '', 'GB'), # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":('Trafalgar Square', 'WC2N 5DN', 'London', '', 'GB'), # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":('Cromwell Road', 'SW7 5BD', 'London', '', 'GB'), # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":('Romney Road', 'SE10 9NF', 'Greenwich London', '', 'GB'), # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":('Cambridge Heath Road', 'E2 9PA', 'London', '', 'GB'), # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":('London Wall', 'EC2Y 5HN', 'London', '', 'GB'), # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":('West India Quay, Canary Wharf', 'E14 4AL', 'London', '', 'GB'), # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":('Exhibition Road, South Kensington', 'SW7 2DD', 'London', '', 'GB'), # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":('Hertford House, Manchester Square', 'W1U 3BN', 'London', '', 'GB'), # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":('Great Russell Street', 'WC1B 3DG', 'London', '', 'GB'), # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":('100 London Rd, Forest Hill', 'SE23 3PQ', 'London', '', 'GB'), # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":('Bankside', 'SE1 9TG', 'London', '', 'GB'), # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":("Morgan's Lane, Tooley Street", 'SE1 2JH', 'London', '', 'GB'), # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":('Cromwell Road', 'SW7 2RL', 'London', '', 'GB'), # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":('Lambeth Road', 'SE1 6HZ', 'London', '', 'GB'), # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":('53 Bankside', 'SE1 9TG', 'London', '', 'GB'), # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":("2 Saint Martin's Place", 'WC2H 0HE', 'London', '', 'GB'), # National Portrait Gallery
}

entities_bus_lines={
"c3770c23-2986-4e4e-8406-c437e06c01e9":['149', '242', '243', '67', '394'], # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":['3', '11', '12', '24', '53', '87', '88', '109', '148', '159', '184', '211', '453'], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":[''], # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":['3', '12', '24', '29', '53', '88', '159', '176', '6', '9', '11', '13', '15', '23', 'x53', '77a', '91', '109', '139'], # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":['14', '49', '70', '74', '345', '360', '414', 'C1'], # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":['177', '180', '188', '199', '286', '386'], # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":['D6', '106', '254', '309', '388', '8', '26', '55', '48'], # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":['4', '8', '25', '56', '100', '25', '172', '242', '521'], # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":['D3', 'D7', 'D8', '277', 'N50', 'D6', '15', '115', '135'], # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":['14', '49', '70', '74', '345', '360', '414', '430', 'C1'], # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":['2', '10', '12', '13', '30', '74', '82', '94', '113', '137', '274'], # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":['1', '7', '8', '19', '25', '38', '55', '98', '242', '10', '14', '24', '29', '73', '134', '390', '59', '68', 'X68', '91', '168', '188'], # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":['176', '185', '197', '356', 'P4', '122', 'P13', '363'], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":['RV1', '45', '63', '100', '381', '344'], # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":['RV1', '17', '21', '35', '40', '43', '47', '133', '141', '149', '343', '381', '521'], # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":['C1', '14', '74', '414'], # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":['1', '3', '12', '45', '53', '59', '63', '68', '100', '159', '168', '171', '172', '176', '188', '344', '360', '453', 'C10'], # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":['2', '3', 'C10', '36', '87', '88', '159', '185', '436', '507'], # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":['24', '29', '176'], # National Portrait Gallery
}

entities_tube_stations={
"c3770c23-2986-4e4e-8406-c437e06c01e9":['b09cb073-2656-4079-b8e6-757300b367bd', '0534ef61-db2a-416f-8f70-6d12bf356d95', '480e2906-9176-4d6a-b14b-3a966a5a4f3f', 'c2ee297b-72ee-4842-9660-fd2ed00d93a2', '78e36286-e750-49ee-927a-4e2bc3134788'], # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":['ccffda41-ad3f-4c1f-b19d-f3dfe244ee96', '4f6eda25-7e30-45ad-80f2-9db2453d262c', '8ec708cb-60c6-4dfa-a66c-2d7220dc7d83', '5e7c3e79-ec13-4840-a499-5c1cef1a6b2f'], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":['1629ea4a-7ee7-4f0c-bb70-231721b53632', '0b7a7fd5-81c8-4f40-b072-ed5bd74eed46', 'ef5e3a08-aee0-4b26-9686-c699bc8d91e6', 'c95d8299-8911-4a67-af90-f945b8d990bb'], # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":['5e7c3e79-ec13-4840-a499-5c1cef1a6b2f', '4a018a17-22e8-4539-b41d-910e4caf4b50', '8ec708cb-60c6-4dfa-a66c-2d7220dc7d83', 'cebe7422-4f0d-435d-9219-0292d950967f'], # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":['88392a34-b5cb-4c76-9e9d-7cfaf4fb944e', 'f15dee6f-5cd2-4ea1-8089-04955c76ff73', '0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4', 'ed39a802-cf23-42a2-8006-cf2ab8a54048'], # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":['68f6f208-ef36-4859-9a85-6440e04d4c63', '46d479d0-c2c8-4893-bf40-41721a7be205', '05da5b28-c40d-4860-92fb-6edf97f64650', '8b275b50-6675-44dc-b9f8-154730faac04'], # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":['480e2906-9176-4d6a-b14b-3a966a5a4f3f', '249dc44e-c5e8-4803-818a-ea54725c2a9d', '742e97bc-26b6-4294-b111-b1301e8760d8', '0534ef61-db2a-416f-8f70-6d12bf356d95'], # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":['e427de05-8e0e-4bb6-99f7-81835be4bee7', '3c1ecf94-d8e2-4e5f-8f54-645e836b3294', 'c2ee297b-72ee-4842-9660-fd2ed00d93a2', '2b13ebcf-2181-451d-b4b0-e53c03ae77f1', '70ab528d-f449-49ff-a03c-33bb16bf7ab7'], # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":['29105288-d523-40cf-99a1-1ef83751460f', '3347e7d7-69a0-405a-86e7-e8f3e620e5a7', 'a67bc448-b939-4d1a-9d9a-840c17b6a496', 'f806f577-3afb-4101-8dec-e8e3435a9cc5', '9f80e0d8-84bb-4474-91b9-c02d59390ddc'], # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":['88392a34-b5cb-4c76-9e9d-7cfaf4fb944e', 'f15dee6f-5cd2-4ea1-8089-04955c76ff73', '0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4', 'ed39a802-cf23-42a2-8006-cf2ab8a54048'], # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":['9713cb92-a9d6-4eb8-9bf9-477860fd02ab', '6ac25ebb-40be-4de4-bb86-c7db73ae823d', 'efb5766a-16a9-434f-8574-1b254726866d', '3dfe2051-c378-4afa-9826-bc94298eb01a'], # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":['2ea2857a-1d56-4fe9-a145-d6031fd660ab', '861ece04-d755-4e24-948c-1990014f49e2', 'd6a59b2a-da2d-4860-9df7-ae60ffabec1d', '1629ea4a-7ee7-4f0c-bb70-231721b53632'], # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":[], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":['30d86bee-6a66-4f65-9b47-dd2a21e5a4f8', 'b194c301-5369-4cd9-ae07-8e454d4ebe69', '70ab528d-f449-49ff-a03c-33bb16bf7ab7', 'b39c2218-4bd9-4c5a-ac76-9483a64e58ec', 'e427de05-8e0e-4bb6-99f7-81835be4bee7'], # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":['5c249c9c-696d-4cbd-a8a3-c87f7029566e', '21ca86c8-b3a9-4040-b088-a2bba3e17c7d', '815ea4ed-f5ee-4f5c-b3ab-3731a03eeed5', 'a5d9ae6f-e2a1-48a0-b671-05fc0c0376d7'], # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":['88392a34-b5cb-4c76-9e9d-7cfaf4fb944e', 'f15dee6f-5cd2-4ea1-8089-04955c76ff73', '0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4', '0d8038c4-2a18-42eb-95e9-b3eba2fbd129'], # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":['e6c6ede6-efc2-4040-9876-932552ce8646', '7f6a1eba-5fd4-43fb-9d86-b60ef44f03d4', 'ff596b51-d851-4cdb-b6ff-3f143a90c862', '9ea06909-e76d-407f-bbf1-06a4e63f454c', 'b194c301-5369-4cd9-ae07-8e454d4ebe69'], # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":['b5ef4219-5d51-49d4-8bd5-2fa1fb9e867c', '8046cf9c-5d92-47ee-b034-32205ba494c6', '4f6eda25-7e30-45ad-80f2-9db2453d262c', 'ccffda41-ad3f-4c1f-b19d-f3dfe244ee96'], # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":['5e7c3e79-ec13-4840-a499-5c1cef1a6b2f', '4a018a17-22e8-4539-b41d-910e4caf4b50', '8ec708cb-60c6-4dfa-a66c-2d7220dc7d83', 'cebe7422-4f0d-435d-9219-0292d950967f', 'ef5e3a08-aee0-4b26-9686-c699bc8d91e6'], # National Portrait Gallery
}

wikipedia_homeurl_en="http://en.wikipedia.org/wiki/"
wikipedia_homeurl_en_mobile="http://en.m.wikipedia.org/wiki/"
entities_wikipedia={
"c3770c23-2986-4e4e-8406-c437e06c01e9":"Geffrye_Museum", # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":"Churchill_museum_and_cabinet_war_rooms", # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":"Sir_John_Soane's_Museum", # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":"National_Gallery_(London)", # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":"Natural_History_Museum", # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":"National_Maritime_Museum", # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":"V&A_Museum_of_Childhood", # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":"Museum_of_london", # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":"Museum_in_docklands", # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":"Science_Museum", # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":"Wallace_Collection", # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":"British_Museum", # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":"Horniman_Museum", # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":"Tate_Modern", # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":"HMS_Belfast", # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":"Victoria_and_Albert_Museum", # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":"Imperial_War_Museum", # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":"Tate_Britain", # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":"National_Portrait_Gallery_(London)", # National Portrait Gallery
}

entities_website={
"c3770c23-2986-4e4e-8406-c437e06c01e9":"http://www.geffrye-museum.org.uk/", # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":"http://cwr.iwm.org.uk/", # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":"http://www.soane.org/", # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":"http://www.nationalgallery.org.uk/", # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":"http://www.nhm.ac.uk/", # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":"http://www.nmm.ac.uk/places/maritime-galleries/", # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":"http://www.vam.ac.uk/moc/", # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":"http://www.museumoflondon.org.uk/English/", # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":"http://www.museumindocklands.org.uk/English/", # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":"http://www.sciencemuseum.org.uk/", # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":"http://www.wallacecollection.org/", # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":"http://www.britishmuseum.org/", # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":"http://www.horniman.ac.uk/", # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":"http://www.tate.org.uk/modern/", # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":"http://hmsbelfast.iwm.org.uk/", # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":"http://www.vam.ac.uk/", # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":"http://london.iwm.org.uk/", # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":"http://www.tate.org.uk/britain/", # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":"http://www.npg.org.uk/", # National Portrait Gallery
}

entities_email={
"c3770c23-2986-4e4e-8406-c437e06c01e9":[("email-general","info@geffrye-museum.org.uk"),("email-booking","bookings@geffrye-museum.org.uk"),("email-shop","jknott@geffrye-museum.org.uk")], # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":[("email-general","cwr@iwm.org.uk")], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":[("email-booking","sbhatti@soane.org.uk")], # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":[("email-general","information@ng-london.org.uk")], # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":[], # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":[("email-booking","bookings@nmm.ac.uk")], # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":[("email-booking","moc@vam.ac.uk")], # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":[("email-booking","info@museumoflondon.org.uk")], # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":[("email-booking","info.docklands@museumoflondon.org.uk")], # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":[("email-feedback","feedback@nmsi.ac.uk")], # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":[("email-general","visiting@wallacecollection.org")], # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":[("email-booking","")], # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":[("email-booking","enquiry@horniman.ac.uk")], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":[("email-booking","visiting.modern@tate.org.uk")], # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":[("email-general","hmsbelfast@iwm.org.uk")], # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":[("email-general","vanda@vam.ac.uk")], # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":[("email-general","mail@iwm.org.uk")], # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":[("email-general","information@britishmuseum.org"),("email-booking","tickets@britishmuseum.org"),("email-membership","friends@britishmuseum.org")], # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":[], # National Portrait Gallery
}

entities_openingtimes={
"c3770c23-2986-4e4e-8406-c437e06c01e9":([], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('12:00', '17:00')]), # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":([('09:30', '18:00')], [('09:30', '18:00')], [('09:30', '18:00')], [('09:30', '18:00')], [('09:30', '18:00')], [('09:30', '18:00')], [('09:30', '18:00')]), # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":([], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], []), # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '21:00')], [('10:00', '18:00')], [('10:00', '18:00')]), # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":([('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')]), # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":([('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')]), # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":([('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '17:45')]), # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')]), # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')]), # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')]), # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":([('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')], [('10:00', '17:00')]), # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":([('10:00', '17:30')], [('10:00', '17:30')], [('10:00', '17:30')], [('10:00', '20:30')], [('10:00', '20:30')], [('10:00', '17:30')], [('10:00', '17:30')]), # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":([('10:30', '17:30')], [('10:30', '17:30')], [('10:30', '17:30')], [('10:30', '17:30')], [('10:30', '17:30')], [('10:30', '17:30')], [('10:30', '17:30')]), # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '22:00')], [('10:00', '22:00')], [('10:00', '18:00')]), # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')]), # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":([('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '17:45')], [('10:00', '22:00')], [('10:00', '17:45')], [('10:00', '17:45')]), # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')]), # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":([('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')], [('10:00', '17:50')]), # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":([('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')], [('10:00', '21:00')], [('10:00', '21:00')], [('10:00', '18:00')], [('10:00', '18:00')]), # National Portrait Gallery
}

entities_phones_openingtimes={
"c3770c23-2986-4e4e-8406-c437e06c01e9":[('general','+44 207 739 9893', None)], # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":[('general','+44 20 7930 6961', None)], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":[('general','+44 20 7405 2107', None)], # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":[('general','+44 20 7747 2885', None)], # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":[('general','+44 20 7942 5011', None)], # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":[('booking', '+44 20 8312 6608 ', ([('10:00', '16:00')], [('10:00', '16:00')], [('10:00', '16:00')], [('10:00', '16:00')], [('10:00', '16:00')], [('10:00', '16:00')], [('10:00', '16:00')]) )], # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":[('general', '+44 20 8983 5200', None)], # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":[('booking', '+44 020 7001 9844', ([('09:15', '18:00')], [('09:15', '18:00')], [('09:15', '18:00')], [('09:15', '18:00')], [('09:15', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')]))], # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":[('booking', '+44 020 7001 9844', ([('09:15', '18:00')], [('09:15', '18:00')], [('09:15', '18:00')], [('09:15', '18:00')], [('09:15', '18:00')], [('10:00', '18:00')], [('10:00', '18:00')]))], # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":[('general', '+44 870 870 4868', None)], # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":[('general', '+44 207 563 9500', None)], # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":[('general', '+44 20 7323 8299', None ),('booking', '+44 20 7323 8181', None ),('membership', '+44 20 7323 8195', None )], # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":[('general', '+44 20 8699 1872', None)], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":[('general', '+44 207 887 8888', None)], # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":[('general','+44 207 940 6300', None)], # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":[('general', '+44 20 7942 2000', None),('membership', '+44 20 7942 2271', None)], # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":[('general','+44 20 7416 5320', None)], # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":[('general', '+44 207 887 8888', None)], # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":[('general', '+44 20 7306 0055 ', None)], # National Portrait Gallery
}
MUSEUM_RATE_ADULT,MUSEUM_RATE_STUDENT,MUSEUM_RATE_KID,MUSEUM_RATE_SENIOR,MUSEUM_RATE_MEMBER=range(5)
MUSEUM_MEMBERSHIP_1ADULT,MUSEUM_MEMBERSHIP_2ADULTS,MUSEUM_MEMBERSHIP_3ADULTS,MUSEUM_MEMBERSHIP_4ADULT=range(4)


entities_sections={
"c3770c23-2986-4e4e-8406-c437e06c01e9":[('176', 'd4aec490-a176-43eb-b284-4abd8b702751', 'PeriodRooms', 'Period Rooms', ['Period Rooms']),
('393', '4b3b2dbc-3be9-4386-9a53-e0a63b33e768', 'SpecialExhibitions', 'Special Exhibitions', ['Special Exhibitions']),
('416', '416929c0-a7b5-46dc-9771-f22e2b54e3da', 'HerbGarden', 'Herb Garden', ['Herb Garden']),
('422', '7729bb41-f017-4220-bbac-348e06094dd1', '17thCenturyPeriodGarden', '17th Century Period Garden', ['17th Century Period Garden']),
('456', 'f2af1f98-bc86-4566-aa99-0604effe8494', '18thCenturyPeriodGarden', '18th Century Period Garden', ['18th Century Period Garden']),
('651', '1fab44bf-d4cf-4a56-a9c5-a651604e9360', '19thCenturyPeriodGarden', '19th Century Period Garden', ['19th Century Period Garden']),
('356', '11e91d7b-8f71-4abc-8d63-96d35616cc38', '20thCenturyPeriodGarden', '20th Century Period Garden', ['20th Century Period Garden']),
('683', 'f71e402b-c354-44c9-bf8a-c683fc5d085b', 'HistoricAlmshouse', 'Historic Almshouse', ['Historic Almshouse']),
('593', '386c9e3b-1d9b-41f6-a9f7-55e8593e83b6', 'Restaurant', 'Restaurant', ['Restaurant']),
('421', '5ed8d1a6-4dc2-40e2-90b6-27b0fed4c2cc', 'Shop', 'Shop', ['Shop']),
('802', 'de7e1f30-dac7-41f7-8025-a116f51ea4ae', 'LectureRoom', 'Lecture Room', ['Lecture Room']),
('276', '22cbf276-ce5b-49a0-a46a-da63edff6fc0', 'DesignCentre', 'Design Centre', ['Design Centre']),
('214', '2ce21478-67fd-4ca6-93d1-09fd8e1ef9fa', 'EducationRooms', 'Education Rooms', ['Education Rooms']),
('902', 'a4365aea-b0d8-4bf2-9024-9b8eaa6890d9', 'IronMongerGraveYard', "IronMongers'GraveYard", ["IronMongers'GraveYard"])], # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":[('e26a', '161edd40-e26a-42ac-92b4-b7857f835420', 'Shop', 'Shop', ['Shop']),
('9434', '2aba31df-9434-4c28-ae1a-eed424e94870', 'Coffee Place', 'Coffee Place', ['Coffee Place'])], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":(), # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":(), # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":(), # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":(), # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":(), # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":(), # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":(), # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":(), # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":(), # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":(), # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":(), # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":(), # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":(), # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":(), # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":(), # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":(), # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":(), # National Portrait Gallery
}

entities_clouds={
"c3770c23-2986-4e4e-8406-c437e06c01e9":[('/2986/bar', 'Bars', 1),
('/2986/evt', 'Events', 1),
('/2986/map', 'Map', 3),
('/2986/img', 'Photos', 3),
('/2986/rest', 'Restaurants', 1),
('/2986/vid', 'Videos', 1),
('/2986/news', 'News', 0),
('/2986/thd', 'Threads', 0)], # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":[('/8594/bar', 'Bars', 1),
('/8594/evt', 'Events', 1),
('/8594/map', 'Map', 3),
('/8594/img', 'Photos', 3),
('/8594/rest', 'Restaurants', 4),
('/8594/vid', 'Videos', 1),
('/8594/news', 'News', 0),
('/8594/thd', 'Threads', 0)], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":[('/4403/bar', 'Bars', 1),
('/4403/evt', 'Events', 1),
('/4403/map', 'Map', 3),
('/4403/img', 'Photos', 3),
('/4403/rest', 'Restaurants', 3),
('/4403/vid', 'Videos', 1),
('/4403/news', 'News', 0),
('/4403/thd', 'Threads', 0)], # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":[('/4798/bar', 'Bars', 1),
('/4798/evt', 'Events', 1),
('/4798/map', 'Map', 3),
('/4798/img', 'Photos', 3),
('/4798/rest', 'Restaurants', 4),
('/4798/vid', 'Videos', 1),
('/4798/news', 'News', 0),
('/4798/thd', 'Threads', 0)], # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":[('/5307/bar', 'Bars', 1),
('/5307/evt', 'Events', 1),
('/5307/map', 'Map', 3),
('/5307/img', 'Photos', 3),
('/5307/rest', 'Restaurants', 5),
('/5307/vid', 'Videos', 1),
('/5307/news', 'News', 0),
('/5307/thd', 'Threads', 0)], # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":[('/6363/bar', 'Bars', 1),
('/6363/evt', 'Events', 1),
('/6363/map', 'Map', 3),
('/6363/img', 'Photos', 3),
('/6363/rest', 'Restaurants', 0),
('/6363/vid', 'Videos', 1),
('/6363/news', 'News', 0),
('/6363/thd', 'Threads', 0)], # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":[('/2497/bar', 'Bars', 1),
('/2497/evt', 'Events', 1),
('/2497/map', 'Map', 3),
('/2497/img', 'Photos', 3),
('/2497/rest', 'Restaurants', 0),
('/2497/vid', 'Videos', 1),
('/2497/news', 'News', 0),
('/2497/thd', 'Threads', 0)], # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":[('/2956/bar', 'Bars', 1),
('/2956/evt', 'Events', 1),
('/2956/map', 'Map', 3),
('/2956/img', 'Photos', 3),
('/2956/rest', 'Restaurants', 3),
('/2956/vid', 'Videos', 1),
('/2956/news', 'News', 0),
('/2956/thd', 'Threads', 0)], # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":[('/2700/bar', 'Bars', 1),
('/2700/evt', 'Events', 1),
('/2700/map', 'Map', 3),
('/2700/img', 'Photos', 3),
('/2700/rest', 'Restaurants', 0),
('/2700/vid', 'Videos', 1),
('/2700/news', 'News', 0),
('/2700/thd', 'Threads', 0)], # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":[('/4734/bar', 'Bars', 1),
('/4734/evt', 'Events', 1),
('/4734/map', 'Map', 3),
('/4734/img', 'Photos', 3),
('/4734/rest', 'Restaurants', 3),
('/4734/vid', 'Videos', 1),
('/4734/news', 'News', 0),
('/4734/thd', 'Threads', 0)], # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":[('/8746/bar', 'Bars', 1),
('/8746/evt', 'Events', 1),
('/8746/map', 'Map', 3),
('/8746/img', 'Photos', 3),
('/8746/rest', 'Restaurants', 5),
('/8746/vid', 'Videos', 1),
('/8746/news', 'News', 0),
('/8746/thd', 'Threads', 0)], # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":[('/1605/bar', 'Bars', 1),
('/1605/evt', 'Events', 1),
('/1605/map', 'Map', 3),
('/1605/img', 'Photos', 3),
('/1605/rest', 'Restaurants', 3),
('/1605/vid', 'Videos', 1),
('/1605/news', 'News', 0),
('/1605/thd', 'Threads', 0)], # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":[('/4713/bar', 'Bars', 1),
('/4713/evt', 'Events', 1),
('/4713/map', 'Map', 3),
('/4713/img', 'Photos', 3),
('/4713/rest', 'Restaurants', 0),
('/4713/vid', 'Videos', 1),
('/4713/news', 'News', 0),
('/4713/thd', 'Threads', 0)], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":[('/5291/bar', 'Bars', 1),
('/5291/evt', 'Events', 1),
('/5291/map', 'Map', 3),
('/5291/img', 'Photos', 3),
('/5291/rest', 'Restaurants', 3),
('/5291/vid', 'Videos', 1),
('/5291/news', 'News', 0),
('/5291/thd', 'Threads', 0)], # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":[('/9152/bar', 'Bars', 1),
('/9152/evt', 'Events', 1),
('/9152/map', 'Map', 3),
('/9152/img', 'Photos', 3),
('/9152/rest', 'Restaurants', 2),
('/9152/vid', 'Videos', 1),
('/9152/news', 'News', 0),
('/9152/thd', 'Threads', 0)], # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":[('/9324/bar', 'Bars', 1),
('/9324/evt', 'Events', 1),
('/9324/map', 'Map', 3),
('/9324/img', 'Photos', 3),
('/9324/rest', 'Restaurants', 3),
('/9324/vid', 'Videos', 1),
('/9324/news', 'News', 0),
('/9324/thd', 'Threads', 0)], # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":[('/8099/bar', 'Bars', 1),
('/8099/evt', 'Events', 1),
('/8099/map', 'Map', 3),
('/8099/img', 'Photos', 3),
('/8099/rest', 'Restaurants', 1),
('/8099/vid', 'Videos', 1),
('/8099/news', 'News', 0),
('/8099/thd', 'Threads', 0)], # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":[('/5868/bar', 'Bars', 1),
('/5868/evt', 'Events', 1),
('/5868/map', 'Map', 3),
('/5868/img', 'Photos', 3),
('/5868/rest', 'Restaurants', 2),
('/5868/vid', 'Videos', 1),
('/5868/news', 'News', 0),
('/5868/thd', 'Threads', 0)], # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":[('/5603/bar', 'Bars', 1),
('/5603/evt', 'Events', 1),
('/5603/map', 'Map', 3),
('/5603/img', 'Photos', 3),
('/5603/rest', 'Restaurants', 4),
('/5603/vid', 'Videos', 1),
('/5603/news', 'News', 0),
('/5603/thd', 'Threads', 0)], # National Portrait Gallery
}

entities_quotes={
"c3770c23-2986-4e4e-8406-c437e06c01e9":None, # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":[("An appeaser is one who feeds a crocodile, hoping it will eat him last.","Winston Churchill"),
("A pessimist sees the difficulty in every opportunity; an optimist sees the opportunity in every difficulty.","Winston Churchill"),
("History will be kind to me for I intend to write it.","Winston Churchill")], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":None, # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":None, # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":None, # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":None, # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":None, # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":None, # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":None, # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":None, # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":None, # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":None, # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":[("Those who use their eyes obtain the most enjoyment and knowledge. Those who look but do not see go away no wiser than when they came.","Frederick Horniman")], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":None, # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":None, # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":None, # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":None, # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":None, # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":None, # National Portrait Gallery
}

entities_events={
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":[("Event 1 is going to be awesome","http://wwww.flarebyte.com","http://flairbyte.com/flarebyte/en/png/logo/8/logo-8.png","Alt Image"),
("Event 2 is going to be awesome","http://wwww.flarebyte.com","http://flairbyte.com/flarebyte/en/png/logo/8/logo-8.png","Alt Image")],
}

#HIGHLIGHT_WHEN, HIGHLIGHT_WHERE, HIGHLIGHT_SUBJECT, HIGHLIGHT_DISTINCTION
entities_highlights={
"c3770c23-2986-4e4e-8406-c437e06c01e9":[(['17C', '18C', '19C', '20C'], ['GB'], 'Furniture, textiles, paintings and decorative arts'),
(['XVII', 'XVIII', 'XIX', 'XX'], ['GB'], 'Evolution of the style of the English middle class interiors'),
(None, None, 'Comprehensive reference library'),
(None, ['GB', 'ASIA'], 'Oriental and English porcelain')], # Geffrye Museum,
"""
[(['XVII', 'XVIII', 'XIX', 'XX'], ['GB'], 'Furniture, textiles, paintings and decorative arts'),
(['XVII', 'XVIII', 'XIX', 'XX'], ['GB'], 'Evolution of the style of the English middle class interiors'),
(None, None, 'Comprehensive reference library'),
(None, ['GB', 'ASIA'], 'Oriental and English porcelain')]
"""

"52c859bb-c59b-43c1-9371-af05df1ab638":[(None,None,"underground operational command and control centre"),
(None,None,"private and public life of Winston Churchill (1874-1965)")
], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":[(None,None,"Sir John Soane's house, museum and library"),
(None,None,"over 30,000 pieces"),
(None,None,"collections of paintings, drawings and antiquities"),
(None,None,"Hogarth's famous Rake's Progress series"),
(None,None,"sarcophagus of Seti I in the basement Crypt"),
], # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":[(None,None,"over 2,300 paintings"),
(None,None,"Duccio, Uccello, van Eyck, Lippi, Mantegna, Botticelli, Durer, Memling, Bellini"),
(None,None,"Leonardo, Cranach, Michelangelo, Raphael, Holbein, Bruegel, Bronzino, Titian, Veronese"),
(None,None,"Caravaggio, Rubens, Poussin, Van Dyck, Velazquez, Claude, Rembrandt, Cuyp, Vermeer"),
(None,None,"Canaletto, Goya, Turner, Constable, Ingres, Degas, Cezanne, Monet, Van Gogh")], # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":[(None,None,"over 70 million items"),
(None,None,"Botany, Entomology, Mineralogy, Palaeontology and Zoology"),
(None,None,"exhibition of dinosaur skeletons")], # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":[(None,None,"two million items"),
(None,None,"maritime art, cartography, manuscripts, ship models and plans, scientific and navigational instruments"),
(None,None,"world's largest maritime historical reference library (100,000 volumes)")], # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":[(None,None,"collection of childhood-related objects"),
(None,None,"toys, dolls, dolls' houses, games, puppets, nursery, children's clothing and furniture")], # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":[(["1C"],None,"The founding of Londinium in AD50"),
(None,None,"Roman London"),
(None,None,"Medieval London"),
(["16C","17C"],None,"War, Plague & Fire (1550s-1660s)")], # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":[(None,None,"story of London's river, port and people"),
(None,None,"collection of historical artefacts, models, and pictures"),
(None,None,"12 galleries")], # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":[(None,None,"over 300,000 items"),
(None,None,"Stephenson's Rocket,Charles Babbage's Difference engine, James Watson's model of DNA")], # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":[(None,None,"25 galleries"),
(None,None,"5,500 objects"),
(["15C","16C","17C","18C","19C"],None,"decorative arts"),
(["18C"],None,"French paintings,furniture, arms & armour, porcelain"),
(None,None,"Paintings,Watercolours and Drawings"),
(None,None,"Furniture, Ceramics"),
(None,None,"European and Oriental Arms and Armour"),
(None,None,"Sculpture, Miniatures"),
(None,None,"Medieval and Renaissance Works of Art"),
(None,None,"Goldsmiths' Work")], # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":[(None,None,"seven million objects"),
(None,None,"Ancient Egypt and Sudan"),
(None,None,"Greek and Roman Antiquities"),
(None,None,"Middle East, Asia, Africa, Oceania and the Americas"),
(None,None,"Prints and Drawings"),
(None,None,"Coins and Medals"),
(["Prehistory"],None,"Prehistory")], # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":[(None,None,"350,000 objects"),
(None,None,"anthropology, natural history and musical instruments")], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":[(None,None,"international modern and contemporary art")], # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":[(["WWII"],None,"museum ship which served during both the Second World War and Korean War")], # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":[(None,None,"4.5 million objects"),
(None,None,"145 galleries"),
(None,None,"decorative arts and design"),
(None,None,"ceramics, glass, textiles, costumes, silver, ironwork, jewelry, furniture, medieval objects, sculpture, printmaking, drawings and photographs")], # Imperial War Museum], # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":[(None,None,"archives of personal and official documents "),
(None,None,"photographs, film and video material, and oral history recordings"),
(None,None,"military vehicles and aircraft")],
"02298ab2-da45-46f9-9f79-6ad906d35868":[(["16C","17C","18C","19C","20C"],None,"British art from 1500 to the present day"),
(None,None,"David Hockney, Peter Blake and Francis Bacon")], # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":[(None,None,"11,000 portraits"),
(None,None,"portraits of historically important and famous British people"),
(None,None,"photographs and caricatures as well as paintings, drawings and sculpture")], # National Portrait Gallery
}

entities_restaurants={
"c3770c23-2986-4e4e-8406-c437e06c01e9":["4d7d58d9-8842-47b6-acaf-ca7ecdff1617"], # Geffrye Museum
"52c859bb-c59b-43c1-9371-af05df1ab638":["b5c526bf-ad11-4d36-8981-786a2b109ed2","a67afb84-29ef-4608-ba55-84d8e16b6338","cfe4c07b-a6d1-4967-9150-ed416d0dfbf7","63e0059b-c137-4e9b-b206-781427a21537"], # Churchill Museum And Cabinet War Rooms
"da6fafd6-bafe-4403-9c2f-e7702b247436":["63e0059b-c137-4e9b-b206-781427a21537","b48a0255-8301-4a6c-bd45-d4d9622c6c66","71b15adf-ceae-49f1-af90-15cadb86ce20"], # Sir John Soanes Museum
"e4798bb2-5b17-471c-9f69-38a9d7e91a68":["a67afb84-29ef-4608-ba55-84d8e16b6338","63e0059b-c137-4e9b-b206-781427a21537","b48a0255-8301-4a6c-bd45-d4d9622c6c66","e11a45c4-2902-473f-a193-c1facb82cb12"], # National Gallery
"73294388-5a07-48ca-9012-3039a455da63":["a40873b4-99bc-49e8-8d64-05405ded1d69","45ffdc95-4f7a-4df1-be98-107220aae404","64765e40-3946-4352-86e7-d2dbc86b1e12","233ce340-0727-4fdf-9be3-cec7884611ac","5886baad-b0dd-4cde-b555-a604ff57fe1a"], # Natural History Museum
"aba1c848-0c8d-4b40-a77d-63630e971557":[], # National Maritime Museum
"af70fe3b-c49f-429c-ac2d-782e44b80399":[], # V&A Museum of Childhood
"1662b8a9-2956-4a57-87e9-f797ea008b09":["4d7d58d9-8842-47b6-acaf-ca7ecdff1617",
"7b31fb46-bfc4-4017-ac3e-cb88f5e59a8e",
"b2b35ce6-c7b5-45ec-a00b-73939facc81e"], # Museum Of London
"dd5d2700-33c9-45e6-a4f7-8c59f0046c26":[], # Museum In Docklands
"a3268d2c-47a4-4572-bb62-55b822ba9cb5":["45ffdc95-4f7a-4df1-be98-107220aae404",
"a40873b4-99bc-49e8-8d64-05405ded1d69",
"5886baad-b0dd-4cde-b555-a604ff57fe1a"], # Science Museum
"874609af-cd08-43a8-9949-06e54bf0da03":["ee0d030d-6c88-4dd5-aa28-c75cede575bd",
"83f5641f-0701-4382-a410-1ba5bcdb5536",
"5c4e3210-868f-49d5-a148-cdd3aafeccb5",
"915c0ca0-debf-4d59-82da-fe667044a712",
"6fdc8567-5910-443d-be1f-98d5ced73963"], # Wallace Collection
"f156dd09-a605-4e83-9291-cb6e1e539b86":["71b15adf-ceae-49f1-af90-15cadb86ce20",
"5bb4a3dd-5d02-49ad-91d4-4b3a8549a5b8",
"b48a0255-8301-4a6c-bd45-d4d9622c6c66"], # British Museum
"7262b139-af2b-4713-b8d1-7aaf5a344e17":[], # Horniman Museum
"3e545cbe-5a9b-41dd-8d1d-953168c8472d":["7b31fb46-bfc4-4017-ac3e-cb88f5e59a8e",
"4d7d58d9-8842-47b6-acaf-ca7ecdff1617",
"b2b35ce6-c7b5-45ec-a00b-73939facc81e"], # Tate Modern
"bf4be7aa-9152-4dc3-af0f-cd0915cdd7e1":["4d7d58d9-8842-47b6-acaf-ca7ecdff1617",
"7b31fb46-bfc4-4017-ac3e-cb88f5e59a8e"], # HMS Belfast
"1ebf1c9b-9c32-4a80-999a-6f577a29ae50":["45ffdc95-4f7a-4df1-be98-107220aae404",
"a40873b4-99bc-49e8-8d64-05405ded1d69",
"5886baad-b0dd-4cde-b555-a604ff57fe1a"], # Victoria & Albert Museum
"4db953be-e9a5-4bec-8099-684013a6a420":["b5c526bf-ad11-4d36-8981-786a2b109ed2"], # Imperial War Museum
"02298ab2-da45-46f9-9f79-6ad906d35868":["0bb8c1f0-04ae-48e3-92d8-5ef75193fd44",
"b5c526bf-ad11-4d36-8981-786a2b109ed2"], # Tate Britain
"e241c444-5603-458f-8040-73b1b87c7c3a":["a67afb84-29ef-4608-ba55-84d8e16b6338",
"63e0059b-c137-4e9b-b206-781427a21537",
"b48a0255-8301-4a6c-bd45-d4d9622c6c66",
"e11a45c4-2902-473f-a193-c1facb82cb12"], # National Portrait Gallery
}

museum_slugs=datautils.create_slug_index(entities)
museums_tube_stations={}
		
def getMuseumUUID(slug):
	return museum_slugs[slug]

# 'entities_tube_stations',


import tubes
def get_tubes(uuid):
	lat,lon,ghash=entities_geo[uuid]
	r=tubes.get_data_as_dicts(entities_tube_stations[uuid],(lat,lon))
	return r

import restaurants
def get_entity_restaurants(uuid):
	lat,lon,ghash=entities_geo[uuid]
	r=restaurants.get_data_as_dicts(entities_restaurants[uuid],(lat,lon))
	return {"restaurant_list": r}

def get_data_as_dict(uuid):
	mylist = [
	datautils.get_entity_as_dict(entities.get(uuid),"full"),
	datautils.get_entity_geo_as_dict(entities_geo.get(uuid)),
	datautils.get_entity_geo_address_as_dict(entities_geo_address.get(uuid)),
	datautils.get_clouds_as_dict(entities_clouds.get(uuid)),
	datautils.get_breadcrumbs_as_dict([("/london","London")]),
	datautils.get_quotes_as_dict(entities_quotes.get(uuid)),
	datautils.get_emails_as_dict(entities_email.get(uuid)),
	datautils.get_phones_as_dict(entities_phones_openingtimes.get(uuid)),
	datautils.get_events_as_dict(entities_events.get(uuid)),
	datautils.get_sections_as_dict(entities_sections.get(uuid)),
	datautils.get_highlights_as_dict(entities_highlights.get(uuid)),
	]
	r = {}
	for item in mylist:
		if item:
			r.update(item)			
	a = {
	"website":entities_website.get(uuid),
	"wikipedia":entities_wikipedia.get(uuid),
	"openingtimes":entities_openingtimes.get(uuid),
	"bus_list":entities_bus_lines.get(uuid),
	"tube_list":get_tubes(uuid),
	}
	r.update(a)
	return {"museum": r}


	


