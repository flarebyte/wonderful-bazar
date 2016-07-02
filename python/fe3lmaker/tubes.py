#!/usr/bin/env python
# encoding: utf-8
"""
transports.py

Created by Olivier Huin on 2010-02-04
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys
import os
import datautils

STATUS_GREEN,STATUS_ORANGE,STATUS_RED,STATUS_DEBUG,STATUS_CRAWLED=range(5)

entities={
"d801bd7d-2875-45ac-a003-189e78831f5a":('8017', 'd801bd7d-2875-45ac-a003-189e78831f5a', 'EarlsCourt', "Earl's Court", ["Earl's Court"]),
"8e9e65b9-127f-4442-ac1f-7d822a4462d9":('8965', '8e9e65b9-127f-4442-ac1f-7d822a4462d9', 'SouthKenton', 'South Kenton', ['South Kenton']),
"3edaef16-d991-46dd-a8ec-ae1bde54cf79":('3169', '3edaef16-d991-46dd-a8ec-ae1bde54cf79', 'NorthHarrow', 'North Harrow', ['North Harrow']),
"9ab2674f-0593-4b86-8347-38109b2b23c5":('9267', '9ab2674f-0593-4b86-8347-38109b2b23c5', 'Croxley', 'Croxley', ['Croxley']),
"320689c7-450e-44d5-a799-0022492c1944":('3206', '320689c7-450e-44d5-a799-0022492c1944', 'Blackwall', 'Blackwall', ['Blackwall']),
"c1736808-6ac4-4c5c-8026-eafa83f98266":('1736', 'c1736808-6ac4-4c5c-8026-eafa83f98266', 'Northolt', 'Northolt', ['Northolt']),
"feb73b3b-5801-43f4-af25-1cbd0a8e9d0e":('7335', 'feb73b3b-5801-43f4-af25-1cbd0a8e9d0e', 'Ickenham', 'Ickenham', ['Ickenham']),
"6eb88e01-0501-4962-965e-0c53d6514d15":('6880', '6eb88e01-0501-4962-965e-0c53d6514d15', 'Northfields', 'Northfields', ['Northfields']),
"cdea03f1-f838-4016-af3d-2c9251a3b143":('0318', 'cdea03f1-f838-4016-af3d-2c9251a3b143', 'Brixton', 'Brixton', ['Brixton']),
"2c4f747a-1182-42d3-9455-a16923b20f75":('2474', '2c4f747a-1182-42d3-9455-a16923b20f75', 'Marylebone', 'Marylebone', ['Marylebone']),
"ffcae605-fbf5-4928-9efd-2a9b18caa418":('6055', 'ffcae605-fbf5-4928-9efd-2a9b18caa418', 'BowChurch', 'Bow Church', ['Bow Church']),
"3378c47b-ad46-4f7f-8670-0f5394af7cb2":('3378', '3378c47b-ad46-4f7f-8670-0f5394af7cb2', 'SouthHarrow', 'South Harrow', ['South Harrow']),
"f806f577-3afb-4101-8dec-e8e3435a9cc5":('8065', 'f806f577-3afb-4101-8dec-e8e3435a9cc5', 'HeronQuays', 'Heron Quays', ['Heron Quays']),
"25a32e3a-f966-4a8f-be8e-8c44573676fe":('2532', '25a32e3a-f966-4a8f-be8e-8c44573676fe', 'GreatPortlandStreet', 'Great Portland Street', ['Great Portland Street']),
"516edae9-110a-4f51-a6d2-383c99210de2":('5169', '516edae9-110a-4f51-a6d2-383c99210de2', 'DeptfordBridge', 'Deptford Bridge', ['Deptford Bridge']),
"d6252a91-cd1c-4076-a6c8-463e8cc8b401":('6252', 'd6252a91-cd1c-4076-a6c8-463e8cc8b401', 'ClaphamNorth', 'Clapham North', ['Clapham North']),
"8d6deaea-002d-4bf5-beed-0c4a3f381eae":('8600', '8d6deaea-002d-4bf5-beed-0c4a3f381eae', 'Colindale', 'Colindale', ['Colindale']),
"f7a34731-3bda-46e5-a10f-a9a2c0c4162a":('7347', 'f7a34731-3bda-46e5-a10f-a9a2c0c4162a', 'WestbournePark', 'Westbourne Park', ['Westbourne Park']),
"f97c9231-f8c8-4a52-be83-6a411f628f36":('9792', 'f97c9231-f8c8-4a52-be83-6a411f628f36', 'BowRoad', 'Bow Road', ['Bow Road']),
"73b1cff3-b7ec-49c3-94da-a20d4c406f3b":('7313', '73b1cff3-b7ec-49c3-94da-a20d4c406f3b', 'KensingtonOlympia', 'Kensington (Olympia)', ['Kensington (Olympia)']),
"e1d3e10a-16cd-4e75-8d6e-d9d299fba0bd":('1310', 'e1d3e10a-16cd-4e75-8d6e-d9d299fba0bd', 'SouthEaling', 'South Ealing', ['South Ealing']),
"0421e847-920c-442f-bd16-cb36c83f9418":('0421', '0421e847-920c-442f-bd16-cb36c83f9418', 'KingGeorgeV', 'King George V', ['King George V']),
"3f6eb6d1-feab-47b9-9504-dffe13e25c15":('3661', '3f6eb6d1-feab-47b9-9504-dffe13e25c15', 'MaidaVale', 'Maida Vale', ['Maida Vale']),
"52c525df-4eb6-4c1b-a4e4-55285e979dfa":('5252', '52c525df-4eb6-4c1b-a4e4-55285e979dfa', 'WarwickAvenue', 'Warwick Avenue', ['Warwick Avenue']),
"3347e7d7-69a0-405a-86e7-e8f3e620e5a7":('3347', '3347e7d7-69a0-405a-86e7-e8f3e620e5a7', 'Westferry', 'Westferry', ['Westferry']),
"4e82f7b0-8d8c-455d-96c9-d13ebe0360c5":('4827', '4e82f7b0-8d8c-455d-96c9-d13ebe0360c5', 'HounslowCentral', 'Hounslow Central', ['Hounslow Central']),
"e789e9e2-2587-480f-b1d3-e0cf154564ca":('7899', 'e789e9e2-2587-480f-b1d3-e0cf154564ca', 'Northwood', 'Northwood', ['Northwood']),
"b90ea9e7-280b-479c-9610-2bdba2ce40d5":('9097', 'b90ea9e7-280b-479c-9610-2bdba2ce40d5', 'TottenhamHale', 'Tottenham Hale', ['Tottenham Hale']),
"643f9889-844f-44d4-980a-2f553a72784f":('6439', '643f9889-844f-44d4-980a-2f553a72784f', 'LadbrokeGrove', 'Ladbroke Grove', ['Ladbroke Grove']),
"0457feec-f14f-4871-a3a5-97b69ddd89ea":('0457', '0457feec-f14f-4871-a3a5-97b69ddd89ea', 'Becontree', 'Becontree', ['Becontree']),
"f77ebe4b-3779-4571-8f46-d6b9e451cd51":('7743', 'f77ebe4b-3779-4571-8f46-d6b9e451cd51', 'EastActon', 'East Acton', ['East Acton']),
"889f0300-d383-42ce-aa8c-f79d72aed49d":('8890', '889f0300-d383-42ce-aa8c-f79d72aed49d', 'WoodsidePark', 'Woodside Park', ['Woodside Park']),
"103fcba9-b810-4929-b013-5a50daa094ea":('1039', '103fcba9-b810-4929-b013-5a50daa094ea', 'Snaresbrook', 'Snaresbrook', ['Snaresbrook']),
"27545394-959e-4f16-84b1-da5a70cbea74":('2754', '27545394-959e-4f16-84b1-da5a70cbea74', 'LondonCityAirport', 'London City Airport', ['London City Airport']),
"535a3a8e-f2a4-41b2-b01e-a951947725dc":('5353', '535a3a8e-f2a4-41b2-b01e-a951947725dc', 'GallionsReach', 'Gallions Reach', ['Gallions Reach']),
"37675294-b85e-4068-a8af-ebfa88c3f58f":('3767', '37675294-b85e-4068-a8af-ebfa88c3f58f', 'Barkingside', 'Barkingside', ['Barkingside']),
"82e21415-4000-41d4-b515-c6a64d610964":('8221', '82e21415-4000-41d4-b515-c6a64d610964', 'HeathrowTerminals123', 'Heathrow Terminals 1 & 2 & 3', ['Heathrow Terminals 1 & 2 & 3',"Heathrow Terminals 1-3"]),
"8503b2ae-5d51-44f0-9d23-2943532cf421":('8503', '8503b2ae-5d51-44f0-9d23-2943532cf421', 'Stockwell', 'Stockwell', ['Stockwell']),
"a5d9ae6f-e2a1-48a0-b671-05fc0c0376d7":('5962', 'a5d9ae6f-e2a1-48a0-b671-05fc0c0376d7', 'TowerGateway', 'Tower Gateway', ['Tower Gateway']),
"ddb614a5-4443-4ce0-bfcd-fb13269cb902":('6145', 'ddb614a5-4443-4ce0-bfcd-fb13269cb902', 'Oakwood', 'Oakwood', ['Oakwood']),
"ea1f0f57-6953-428a-82ae-e2ee619ab313":('1057', 'ea1f0f57-6953-428a-82ae-e2ee619ab313', 'Archway', 'Archway', ['Archway']),
"d6a59b2a-da2d-4860-9df7-ae60ffabec1d":('6592', 'd6a59b2a-da2d-4860-9df7-ae60ffabec1d', 'GoodgeStreet', 'Goodge Street', ['Goodge Street']),
"d22c6041-ea25-4dd9-9546-24afcb13f472":('2260', 'd22c6041-ea25-4dd9-9546-24afcb13f472', 'FinchleyRoad', 'Finchley Road', ['Finchley Road']),
"8eccd70b-662c-474d-b91d-5c88c03286d9":('8706', '8eccd70b-662c-474d-b91d-5c88c03286d9', 'UpminsterBridge', 'Upminster Bridge', ['Upminster Bridge']),
"9a4ec1fc-88c4-46f1-9eaf-8319d640049e":('9418', '9a4ec1fc-88c4-46f1-9eaf-8319d640049e', 'HattonCross', 'Hatton Cross', ['Hatton Cross']),
"42a97bba-8dab-4932-8925-3cbfedd59265":('4297', '42a97bba-8dab-4932-8925-3cbfedd59265', 'Osterley', 'Osterley', ['Osterley']),
"d25453cf-7eb9-44b7-af27-250820ef3ecd":('2545', 'd25453cf-7eb9-44b7-af27-250820ef3ecd', 'Ruislip', 'Ruislip', ['Ruislip']),
"42fdbaea-b1c5-4ded-b3f3-c36b67145035":('4215', '42fdbaea-b1c5-4ded-b3f3-c36b67145035', 'Bayswater', 'Bayswater', ['Bayswater']),
"f3c7ce45-e337-4d6a-8396-6f4a243b3bbe":('3745', 'f3c7ce45-e337-4d6a-8396-6f4a243b3bbe', 'HangerLane', 'Hanger Lane', ['Hanger Lane']),
"9f80e0d8-84bb-4474-91b9-c02d59390ddc":('9800', '9f80e0d8-84bb-4474-91b9-c02d59390ddc', 'Poplar', 'Poplar', ['Poplar']),
"ccf87110-0f7d-4f00-b6f7-e6c1440b20db":('8711', 'ccf87110-0f7d-4f00-b6f7-e6c1440b20db', 'KentishTown', 'Kentish Town', ['Kentish Town']),
"50303a28-12d5-4954-a2b3-d7f62bf80e10":('5030', '50303a28-12d5-4954-a2b3-d7f62bf80e10', 'WarrenStreet', 'Warren Street', ['Warren Street']),
"0534ef61-db2a-416f-8f70-6d12bf356d95":('0534', '0534ef61-db2a-416f-8f70-6d12bf356d95', 'Shoreditch', 'Shoreditch', ['Shoreditch']),
"a2cf78d3-ee61-411e-b76d-aa7ec1c3c772":('2783', 'a2cf78d3-ee61-411e-b76d-aa7ec1c3c772', 'StonebridgePark', 'Stonebridge Park', ['Stonebridge Park']),
"ce94a872-77e5-44b1-adab-6f4b70e5190c":('9487', 'ce94a872-77e5-44b1-adab-6f4b70e5190c', 'Rickmansworth', 'Rickmansworth', ['Rickmansworth']),
"f15dee6f-5cd2-4ea1-8089-04955c76ff73":('1565', 'f15dee6f-5cd2-4ea1-8089-04955c76ff73', 'GloucesterRoad', 'Gloucester Road', ['Gloucester Road']),
"deed830e-f5d2-454a-b9d2-20685f742186":('8305', 'deed830e-f5d2-454a-b9d2-20685f742186', 'Richmond', 'Richmond', ['Richmond']),
"0563b078-a7da-4c64-b1b6-a56816f2e979":('0563', '0563b078-a7da-4c64-b1b6-a56816f2e979', 'Perivale', 'Perivale', ['Perivale']),
"99c7d4d2-9ed6-489f-a71c-ea012316652a":('9974', '99c7d4d2-9ed6-489f-a71c-ea012316652a', 'RoyalVictoria', 'Royal Victoria', ['Royal Victoria']),
"24866134-afce-40c1-9341-e9284019249d":('2486', '24866134-afce-40c1-9341-e9284019249d', 'SouthWimbledon', 'South Wimbledon', ['South Wimbledon']),
"2ad77ab0-d4d5-414d-8d2c-fb7606669c08":('2770', '2ad77ab0-d4d5-414d-8d2c-fb7606669c08', 'WestActon', 'West Acton', ['West Acton']),
"6ad20349-f3f2-4290-8fb1-a0d4718c0d32":('6203', '6ad20349-f3f2-4290-8fb1-a0d4718c0d32', 'PrinceRegent', 'Prince Regent', ['Prince Regent']),
"5feb6509-d2bc-4746-9f7e-d29225e96867":('5650', '5feb6509-d2bc-4746-9f7e-d29225e96867', 'DagenhamEast', 'Dagenham East', ['Dagenham East']),
"43b5a37c-7e3b-4b49-ac58-2f33191cdf4e":('4353', '43b5a37c-7e3b-4b49-ac58-2f33191cdf4e', 'Kilburn', 'Kilburn', ['Kilburn']),
"24fa220d-ca13-443d-9e73-8be49afd7db0":('2422', '24fa220d-ca13-443d-9e73-8be49afd7db0', 'SudburyHill', 'Sudbury Hill', ['Sudbury Hill']),
"cebe7422-4f0d-435d-9219-0292d950967f":('7422', 'cebe7422-4f0d-435d-9219-0292d950967f', 'PiccadillyCircus', 'Piccadilly Circus', ['Piccadilly Circus','Picadilly Circus']),
"efb5766a-16a9-434f-8574-1b254726866d":('5766', 'efb5766a-16a9-434f-8574-1b254726866d', 'BakerStreet', 'Baker Street', ['Baker Street']),
"7ca7ca09-f3e4-4212-8bca-ad03d410212c":('7709', '7ca7ca09-f3e4-4212-8bca-ad03d410212c', 'EdgwareRoadC', 'Edgware Road', ['Edgware Road']),
"010c886c-7201-4d49-81fc-f78cecdfa1b3":('0108', '010c886c-7201-4d49-81fc-f78cecdfa1b3', 'Cyprus', 'Cyprus', ['Cyprus']),
"2a1c5044-4b2a-48b8-bc59-830c88cd7dca":('2150', '2a1c5044-4b2a-48b8-bc59-830c88cd7dca', 'SevenSisters', 'Seven Sisters', ['Seven Sisters']),
"5d50982e-bd14-46bb-8de9-3761a2498794":('5509', '5d50982e-bd14-46bb-8de9-3761a2498794', 'DollisHill', 'Dollis Hill', ['Dollis Hill']),
"c5638fe6-7996-41f9-b291-3f0fcc1caeec":('5638', 'c5638fe6-7996-41f9-b291-3f0fcc1caeec', 'BlackhorseRoad', 'Blackhorse Road', ['Blackhorse Road']),
"e8f8bb83-a6b8-4b37-90dd-ca34489bf9a3":('8883', 'e8f8bb83-a6b8-4b37-90dd-ca34489bf9a3', 'Balham', 'Balham', ['Balham']),
"c7dec458-047a-4c3b-b9af-46e3d491821d":('7458', 'c7dec458-047a-4c3b-b9af-46e3d491821d', 'Hammersmith', 'Hammersmith', ['Hammersmith']),
"c570c2e2-1ce5-4542-8269-4dd40c07e8f3":('5702', 'c570c2e2-1ce5-4542-8269-4dd40c07e8f3', 'Hampstead', 'Hampstead', ['Hampstead']),
"016338cd-a632-4ef4-af89-42e6ce3d05a5":('0163', '016338cd-a632-4ef4-af89-42e6ce3d05a5', 'ChiswickPark', 'Chiswick Park', ['Chiswick Park']),
"23724ad1-b79e-4eb1-bc07-1c19dd5dfae9":('2372', '23724ad1-b79e-4eb1-bc07-1c19dd5dfae9', 'ParsonsGreen', 'Parsons Green', ['Parsons Green']),
"ae7c6e42-5090-4910-ad23-4ec083564183":('7642', 'ae7c6e42-5090-4910-ad23-4ec083564183', 'Debden', 'Debden', ['Debden']),
"e65e7008-2695-4440-ab38-d7f81b7c6976":('6570', 'e65e7008-2695-4440-ab38-d7f81b7c6976', 'BrentCross', 'Brent Cross', ['Brent Cross']),
"8c78516a-b7e2-47eb-b9b5-117100c51bc2":('8785', '8c78516a-b7e2-47eb-b9b5-117100c51bc2', 'Paddington', 'Paddington', ['Paddington']),
"249dc44e-c5e8-4803-818a-ea54725c2a9d":('2494', '249dc44e-c5e8-4803-818a-ea54725c2a9d', 'StepneyGreen', 'Stepney Green', ['Stepney Green']),
"303e944e-a63e-4fd4-8dbe-8971d332b187":('3039', '303e944e-a63e-4fd4-8dbe-8971d332b187', 'Neasden', 'Neasden', ['Neasden']),
"6b549b5b-db83-4ffa-8ad3-baba502a92c6":('6549', '6b549b5b-db83-4ffa-8ad3-baba502a92c6', 'StJohnsWood', "St. John's Wood", ["St. John's Wood"]),
"03af5d7e-72c4-413f-a260-52c1fe5d022c":('0357', '03af5d7e-72c4-413f-a260-52c1fe5d022c', 'TheydonBois', 'Theydon Bois', ['Theydon Bois']),
"611cdae4-916d-43c3-aa1c-bcba08d75098":('6114', '611cdae4-916d-43c3-aa1c-bcba08d75098', 'SurreyQuays', 'Surrey Quays', ['Surrey Quays']),
"984d0bdd-193e-4a3b-b0b3-523edea3351e":('9840', '984d0bdd-193e-4a3b-b0b3-523edea3351e', 'Southgate', 'Southgate', ['Southgate']),
"0baa84a4-8275-4f53-bc45-1476fdd5934f":('0844', '0baa84a4-8275-4f53-bc45-1476fdd5934f', 'GoldhawkRoad', 'Goldhawk Road', ['Goldhawk Road']),
"2f61ae2d-9ffc-4f3c-afa0-87e712df3cff":('2612', '2f61ae2d-9ffc-4f3c-afa0-87e712df3cff', 'HydeParkCorner', 'Hyde Park Corner', ['Hyde Park Corner']),
"87b81f55-4ebd-41fc-a8e1-0e701cb6bda1":('8781', '87b81f55-4ebd-41fc-a8e1-0e701cb6bda1', 'Fairlop', 'Fairlop', ['Fairlop']),
"44438768-26b6-4414-bdbd-a30055d17ced":('4443', '44438768-26b6-4414-bdbd-a30055d17ced', 'ClaphamSouth', 'Clapham South', ['Clapham South']),
"ef56ae4c-6447-4907-bf07-49a13385b951":('5646', 'ef56ae4c-6447-4907-bf07-49a13385b951', 'WestFinchley', 'West Finchley', ['West Finchley']),
"0a9a00c8-2f22-4c01-bc55-8402eb72e5b3":('0900', '0a9a00c8-2f22-4c01-bc55-8402eb72e5b3', 'WestKensington', 'West Kensington', ['West Kensington']),
"662cbbc1-1d6b-48be-b85c-140fb3c2d832":('6621', '662cbbc1-1d6b-48be-b85c-140fb3c2d832', 'Bermondsey', 'Bermondsey', ['Bermondsey']),
"74125284-3256-4527-a79d-0fddd3099af9":('7412', '74125284-3256-4527-a79d-0fddd3099af9', 'ColliersWood', 'Colliers Wood', ['Colliers Wood']),
"5c389d95-edf6-4554-adec-654d9a1a16f8":('5389', '5c389d95-edf6-4554-adec-654d9a1a16f8', 'Stratford', 'Stratford', ['Stratford']),
"ed5d6e00-71b2-4df5-b7b2-05dfd3a9646c":('5600', 'ed5d6e00-71b2-4df5-b7b2-05dfd3a9646c', 'ArnosGrove', 'Arnos Grove', ['Arnos Grove']),
"25c555f4-f529-4149-823e-a04c4463d524":('2555', '25c555f4-f529-4149-823e-a04c4463d524', 'PrestonRoad', 'Preston Road', ['Preston Road']),
"0d2de214-c96e-4842-a10f-5fe058a90d5b":('0221', '0d2de214-c96e-4842-a10f-5fe058a90d5b', 'ElmPark', 'Elm Park', ['Elm Park']),
"e6fba115-a15d-4b53-8106-c0cd5f3c007f":('6115', 'e6fba115-a15d-4b53-8106-c0cd5f3c007f', 'MillHillEast', 'Mill Hill East', ['Mill Hill East']),
"364a49a3-65ad-4649-b9a0-af01a6b98920":('3644', '364a49a3-65ad-4649-b9a0-af01a6b98920', 'Leyton', 'Leyton', ['Leyton']),
"d08e5786-189f-4451-916f-3c78d21e7f12":('0857', 'd08e5786-189f-4451-916f-3c78d21e7f12', 'TotteridgeWhetstone', 'Totteridge & Whetstone', ['Totteridge & Whetstone']),
"93bcf13e-165d-4294-8c8a-434ffbdf7374":('9313', '93bcf13e-165d-4294-8c8a-434ffbdf7374', 'CanonsPark', 'Canons Park', ['Canons Park']),
"bfb41f10-53d9-44b4-8233-e5389ab3d583":('4110', 'bfb41f10-53d9-44b4-8233-e5389ab3d583', 'ShepherdsBushC', "Shepherd's Bush", ["Shepherd's Bush"]),
"a9f90eac-8bda-4b0d-a62c-0abace2ecacf":('9908', 'a9f90eac-8bda-4b0d-a62c-0abace2ecacf', 'BecktonPark', 'Beckton Park', ['Beckton Park']),
"7889cae9-8416-4153-aad3-66ce2e110e2b":('7889', '7889cae9-8416-4153-aad3-66ce2e110e2b', 'DagenhamHeathway', 'Dagenham Heathway', ['Dagenham Heathway']),
"bbed2b3a-a6d0-41f0-93af-82c7bb0c9d8b":('2360', 'bbed2b3a-a6d0-41f0-93af-82c7bb0c9d8b', 'EastHam', 'East Ham', ['East Ham']),
"6a4220d7-975d-4710-b069-2cf4dafc50e1":('6422', '6a4220d7-975d-4710-b069-2cf4dafc50e1', 'Kingsbury', 'Kingsbury', ['Kingsbury']),
"9ea06909-e76d-407f-bbf1-06a4e63f454c":('9069', '9ea06909-e76d-407f-bbf1-06a4e63f454c', 'Waterloo', 'Waterloo', ['Waterloo']),
"ac632aec-da92-4b75-a0ea-3ec9f7b60aa1":('6329', 'ac632aec-da92-4b75-a0ea-3ec9f7b60aa1', 'BuckhurstHill', 'Buckhurst Hill', ['Buckhurst Hill']),
"b39c2218-4bd9-4c5a-ac76-9483a64e58ec":('3922', 'b39c2218-4bd9-4c5a-ac76-9483a64e58ec', 'CannonStreet', 'Cannon Street', ['Cannon Street']),
"c94e833d-198e-4108-809b-ba38e1b5aba7":('9483', 'c94e833d-198e-4108-809b-ba38e1b5aba7', 'GreenPark', 'Green Park', ['Green Park']),
"4ac60516-0e6a-47b4-898c-4a4d127a8baa":('4605', '4ac60516-0e6a-47b4-898c-4a4d127a8baa', 'ParkRoyal', 'Park Royal', ['Park Royal']),
"5e7c3e79-ec13-4840-a499-5c1cef1a6b2f":('5737', '5e7c3e79-ec13-4840-a499-5c1cef1a6b2f', 'CharingCross', 'Charing Cross', ['Charing Cross']),
"4ae3072a-10a8-4400-9ed2-127b6b5b976a":('4307', '4ae3072a-10a8-4400-9ed2-127b6b5b976a', 'Amersham', 'Amersham', ['Amersham']),
"925a7fd8-5dc1-4620-a272-c4697d56172c":('9257', '925a7fd8-5dc1-4620-a272-c4697d56172c', 'DevonsRoad', 'Devons Road', ['Devons Road']),
"465b5b31-1237-4007-929b-5ffc63e19f79":('4655', '465b5b31-1237-4007-929b-5ffc63e19f79', 'NewburyPark', 'Newbury Park', ['Newbury Park']),
"0767b416-a3da-4c1c-85bf-a3e59a2657d6":('0767', '0767b416-a3da-4c1c-85bf-a3e59a2657d6', 'Chorleywood', 'Chorleywood', ['Chorleywood']),
"25ef1cc7-866a-474e-acc7-44a0d7e6bca5":('2517', '25ef1cc7-866a-474e-acc7-44a0d7e6bca5', 'Stanmore', 'Stanmore', ['Stanmore']),
"2f0faf9b-7406-4a32-8d18-927b7af16497":('2097', '2f0faf9b-7406-4a32-8d18-927b7af16497', 'RaynersLane', 'Rayners Lane', ['Rayners Lane']),
"410e92c7-e6ac-4739-90dd-0834bb8b6e83":('4109', '410e92c7-e6ac-4739-90dd-0834bb8b6e83', 'Queensbury', 'Queensbury', ['Queensbury']),
"c2ee297b-72ee-4842-9660-fd2ed00d93a2":('2297', 'c2ee297b-72ee-4842-9660-fd2ed00d93a2', 'Moorgate', 'Moorgate', ['Moorgate']),
"28b2ee7c-7a48-44d2-b4a9-499effac5775":('2827', '28b2ee7c-7a48-44d2-b4a9-499effac5775', 'RuislipGardens', 'Ruislip Gardens', ['Ruislip Gardens']),
"dd74b4e2-6e32-48f9-91cf-aa23e5551688":('7442', 'dd74b4e2-6e32-48f9-91cf-aa23e5551688', 'RuislipManor', 'Ruislip Manor', ['Ruislip Manor']),
"174ca94d-74d1-4606-9836-69aa275eb76e":('1749', '174ca94d-74d1-4606-9836-69aa275eb76e', 'Pinner', 'Pinner', ['Pinner']),
"57d3a7a7-5e23-447e-bb6a-cbbd12a9d635":('5737', '57d3a7a7-5e23-447e-bb6a-cbbd12a9d635', 'EastFinchley', 'East Finchley', ['East Finchley']),
"9aefa543-e3ff-4606-822b-b18794f4835d":('9543', '9aefa543-e3ff-4606-822b-b18794f4835d', 'BostonManor', 'Boston Manor', ['Boston Manor']),
"21ca86c8-b3a9-4040-b088-a2bba3e17c7d":('2186', '21ca86c8-b3a9-4040-b088-a2bba3e17c7d', 'TowerHill', 'Tower Hill', ['Tower Hill']),
"7e39a3bf-1054-422f-8909-c304cdd9efe9":('7393', '7e39a3bf-1054-422f-8909-c304cdd9efe9', 'Wimbledon', 'Wimbledon', ['Wimbledon']),
"7f63805a-0964-46ad-a282-e7dc199b8685":('7638', '7f63805a-0964-46ad-a282-e7dc199b8685', 'EustonSquare', 'Euston Square', ['Euston Square']),
"e427de05-8e0e-4bb6-99f7-81835be4bee7":('4270', 'e427de05-8e0e-4bb6-99f7-81835be4bee7', 'StPauls', "St. Paul's", ["St. Paul's"]),
"97c4c33d-b5af-421b-aeef-b6ff98e3f1ca":('9743', '97c4c33d-b5af-421b-aeef-b6ff98e3f1ca', 'Hainault', 'Hainault', ['Hainault']),
"afdf2e47-c231-43be-bc77-5486ee74b1e5":('2472', 'afdf2e47-c231-43be-bc77-5486ee74b1e5', 'WestHampstead', 'West Hampstead', ['West Hampstead']),
"a4840c38-6656-41f9-92ff-2e0192e89cbe":('4840', 'a4840c38-6656-41f9-92ff-2e0192e89cbe', 'OxfordCircus', 'Oxford Circus', ['Oxford Circus']),
"873fa51e-dbc3-4407-9249-ea14e11f6f3e":('8735', '873fa51e-dbc3-4407-9249-ea14e11f6f3e', 'FinsburyPark', 'Finsbury Park', ['Finsbury Park']),
"ccffd31a-972c-40ba-903a-0e4ce0d971c6":('3197', 'ccffd31a-972c-40ba-903a-0e4ce0d971c6', 'CaledonianRoad', 'Caledonian Road', ['Caledonian Road']),
"b6f356a7-c2a4-4974-8c96-9519cbb7b839":('6356', 'b6f356a7-c2a4-4974-8c96-9519cbb7b839', 'HounslowWest', 'Hounslow West', ['Hounslow West']),
"0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4":('0456', '0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4', 'Knightsbridge', 'Knightsbridge', ['Knightsbridge']),
"68f6f208-ef36-4859-9a85-6440e04d4c63":('6862', '68f6f208-ef36-4859-9a85-6440e04d4c63', 'CuttySark', 'Cutty Sark', ['Cutty Sark']),
"52433503-c65c-4089-82ff-4fd1d2780f84":('5243', '52433503-c65c-4089-82ff-4fd1d2780f84', 'Oval', 'Oval', ['Oval']),
"8ca4bf88-8884-42eb-82b9-93c921dd3fc7":('8488', '8ca4bf88-8884-42eb-82b9-93c921dd3fc7', 'WembleyCentral', 'Wembley Central', ['Wembley Central']),
"bef7f260-c351-412c-bec0-b05d82367f88":('7260', 'bef7f260-c351-412c-bec0-b05d82367f88', 'Lewisham', 'Lewisham', ['Lewisham']),
"d168eb7a-13eb-477b-b482-c69c3b4f5dbf":('1687', 'd168eb7a-13eb-477b-b482-c69c3b4f5dbf', 'HeathrowTerminal4', 'Heathrow Terminal 4', ['Heathrow Terminal 4']),
"78e36286-e750-49ee-927a-4e2bc3134788":('7836', '78e36286-e750-49ee-927a-4e2bc3134788', 'LiverpoolStreet', 'Liverpool Street', ['Liverpool Street']),
"a14eddb7-704e-4d4f-a0d6-5105d028f128":('1477', 'a14eddb7-704e-4d4f-a0d6-5105d028f128', 'Rotherhithe', 'Rotherhithe', ['Rotherhithe']),
"1f3ac254-b5cd-4317-b777-64f2432e4c7a":('1325', '1f3ac254-b5cd-4317-b777-64f2432e4c7a', 'MorningtonCrescent', 'Mornington Crescent', ['Mornington Crescent']),
"e93bad5c-e2e2-45f2-940f-35583fc357dd":('9352', 'e93bad5c-e2e2-45f2-940f-35583fc357dd', 'Hillingdon', 'Hillingdon', ['Hillingdon']),
"e5c04fad-1dfc-46c3-8e27-74a8a6b1c63e":('5041', 'e5c04fad-1dfc-46c3-8e27-74a8a6b1c63e', 'NorthwickPark', 'Northwick Park', ['Northwick Park']),
"72d3d976-272d-40ab-858f-7004cf92e4e4":('7239', '72d3d976-272d-40ab-858f-7004cf92e4e4', 'MileEnd', 'Mile End', ['Mile End']),
"8b275b50-6675-44dc-b9f8-154730faac04":('8275', '8b275b50-6675-44dc-b9f8-154730faac04', 'Mudchute', 'Mudchute', ['Mudchute']),
"e4f72828-a29a-4fdd-9bea-66fecdcfa250":('4728', 'e4f72828-a29a-4fdd-9bea-66fecdcfa250', 'FulhamBroadway', 'Fulham Broadway', ['Fulham Broadway']),
"15351ff7-4b56-4882-a4d0-c4fd315ac9ef":('1535', '15351ff7-4b56-4882-a4d0-c4fd315ac9ef', 'NewCross', 'New Cross', ['New Cross']),
"2d04e04c-9ce2-4384-80e3-06243cb8d90b":('2040', '2d04e04c-9ce2-4384-80e3-06243cb8d90b', 'Hornchurch', 'Hornchurch', ['Hornchurch']),
"29105288-d523-40cf-99a1-1ef83751460f":('2910', '29105288-d523-40cf-99a1-1ef83751460f', 'WestIndiaQuay', 'West India Quay', ['West India Quay']),
"3e8ccac4-231c-4715-90fc-2025b412d64f":('3842', '3e8ccac4-231c-4715-90fc-2025b412d64f', 'Kenton', 'Kenton', ['Kenton']),
"767e63fc-be79-449a-a461-670f3888eb56":('7676', '767e63fc-be79-449a-a461-670f3888eb56', 'NorthWembley', 'North Wembley', ['North Wembley']),
"e0b9f30a-2875-4559-a814-8d2297a2266d":('0930', 'e0b9f30a-2875-4559-a814-8d2297a2266d', 'ElversonRoad', 'Elverson Road', ['Elverson Road']),
"5177aa0d-3b92-4a1d-8356-3acfd80189be":('5177', '5177aa0d-3b92-4a1d-8356-3acfd80189be', 'Highgate', 'Highgate', ['Highgate']),
"1629ea4a-7ee7-4f0c-bb70-231721b53632":('1629', '1629ea4a-7ee7-4f0c-bb70-231721b53632', 'Holborn', 'Holborn', ['Holborn']),
"2e6585ea-25a5-4255-b312-fb33a99de249":('2658', '2e6585ea-25a5-4255-b312-fb33a99de249', 'HarrowWealdston', 'Harrow & Wealdston', ['Harrow & Wealdston']),
"09bbbf1c-4b44-4300-9b7e-7da31c621afc":('0914', '09bbbf1c-4b44-4300-9b7e-7da31c621afc', 'RoyalOak', 'Royal Oak', ['Royal Oak']),
"9ac4ad96-5502-4948-a754-8558c1a59201":('9496', '9ac4ad96-5502-4948-a754-8558c1a59201', 'HendonCentral', 'Hendon Central', ['Hendon Central']),
"9bd73108-ad7c-4b42-93c5-8a9d8cdd0acc":('9731', '9bd73108-ad7c-4b42-93c5-8a9d8cdd0acc', 'UptonPark', 'Upton Park', ['Upton Park']),
"30d86bee-6a66-4f65-9b47-dd2a21e5a4f8":('3086', '30d86bee-6a66-4f65-9b47-dd2a21e5a4f8', 'Blackfriars', 'Blackfriars', ['Blackfriars']),
"367c4cde-ffab-44df-a220-2b5c8ad298f4":('3674', '367c4cde-ffab-44df-a220-2b5c8ad298f4', 'RoyalAlbert', 'Royal Albert', ['Royal Albert']),
"fa25d9e4-e9c9-44da-ae24-ea2d2235d9f6":('2594', 'fa25d9e4-e9c9-44da-ae24-ea2d2235d9f6', 'SouthRuislip', 'South Ruislip', ['South Ruislip']),
"05da5b28-c40d-4860-92fb-6edf97f64650":('0552', '05da5b28-c40d-4860-92fb-6edf97f64650', 'Greenwich', 'Greenwich', ['Greenwich']),
"6e66b0ff-cfc1-42b3-8029-3ecad13b44ae":('6660', '6e66b0ff-cfc1-42b3-8029-3ecad13b44ae', 'StamfordBrook', 'Stamford Brook', ['Stamford Brook']),
"815fd4eb-ead4-4ef9-b778-c4dea749ce82":('8154', '815fd4eb-ead4-4ef9-b778-c4dea749ce82', 'WestBrompton', 'West Brompton', ['West Brompton']),
"2b655c4f-fbfb-4005-be97-38962e01a3ed":('2655', '2b655c4f-fbfb-4005-be97-38962e01a3ed', 'KensalGreen', 'Kensal Green', ['Kensal Green']),
"2fca6749-5045-4d77-a665-72d70249a5ac":('2674', '2fca6749-5045-4d77-a665-72d70249a5ac', 'WimbledonPark', 'Wimbledon Park', ['Wimbledon Park']),
"fa04941a-9c43-4392-b0a4-43e75b3a7e82":('0494', 'fa04941a-9c43-4392-b0a4-43e75b3a7e82', 'ClaphamCommon', 'Clapham Common', ['Clapham Common']),
"c4806aae-06ae-4c0e-bbe6-f57c358976da":('4806', 'c4806aae-06ae-4c0e-bbe6-f57c358976da', 'Alperton', 'Alperton', ['Alperton']),
"2945184c-9a8d-4707-88a3-ec1bd35999b0":('2945', '2945184c-9a8d-4707-88a3-ec1bd35999b0', 'CanningTown', 'Canning Town', ['Canning Town']),
"480e2906-9176-4d6a-b14b-3a966a5a4f3f":('4802', '480e2906-9176-4d6a-b14b-3a966a5a4f3f', 'BethnalGreen', 'Bethnal Green', ['Bethnal Green']),
"e6c6ede6-efc2-4040-9876-932552ce8646":('6662', 'e6c6ede6-efc2-4040-9876-932552ce8646', 'LambethNorth', 'Lambeth North', ['Lambeth North']),
"8450af6a-dbf3-4749-811b-6676552bed4b":('8450', '8450af6a-dbf3-4749-811b-6676552bed4b', 'HighburyIslington', 'Highbury & Islington', ['Highbury & Islington']),
"5f45b71a-7b9a-449f-bdee-cd6262795f51":('5457', '5f45b71a-7b9a-449f-bdee-cd6262795f51', 'GoldersGreen', 'Golders Green', ['Golders Green']),
"cd0ae317-6fa5-4640-8971-50661b49c32f":('0317', 'cd0ae317-6fa5-4640-8971-50661b49c32f', 'TootingBec', 'Tooting Bec', ['Tooting Bec']),
"38d6323c-663a-4f54-a58b-71cff0611d3d":('3863', '38d6323c-663a-4f54-a58b-71cff0611d3d', 'WillesdenJunction', 'Willesden Junction', ['Willesden Junction']),
"7cb122f8-02b7-4ec6-8021-85a4ae14639e":('7122', '7cb122f8-02b7-4ec6-8021-85a4ae14639e', 'SouthWoodford', 'South Woodford', ['South Woodford']),
"32b3c7d2-f9a2-4d46-ba4f-1c5efb4ddeb3":('3237', '32b3c7d2-f9a2-4d46-ba4f-1c5efb4ddeb3', 'Gunnersbury', 'Gunnersbury', ['Gunnersbury']),
"f0a2bae9-93f2-4acc-af91-602c879cd8fd":('0299', 'f0a2bae9-93f2-4acc-af91-602c879cd8fd', 'ActonTown', 'Acton Town', ['Acton Town']),
"95b2c24a-fdf9-4cb0-b04e-4989909ffb72":('9522', '95b2c24a-fdf9-4cb0-b04e-4989909ffb72', 'Barking', 'Barking', ['Barking']),
"aaf9fad0-0d23-4c27-927d-79a20d43d505":('9002', 'aaf9fad0-0d23-4c27-927d-79a20d43d505', 'Victoria', 'Victoria', ['Victoria']),
"36aa3d82-e972-4f11-81cc-b94415bf849f":('3638', '36aa3d82-e972-4f11-81cc-b94415bf849f', 'HounslowEast', 'Hounslow East', ['Hounslow East']),
"a67bcb93-f537-428c-813e-8a257ef98d98":('6793', 'a67bcb93-f537-428c-813e-8a257ef98d98', 'Queensway', 'Queensway', ['Queensway']),
"13a9b335-fdb9-44d3-bd3d-09fc64504063":('1393', '13a9b335-fdb9-44d3-bd3d-09fc64504063', 'Watford', 'Watford', ['Watford']),
"79c291cf-6caa-469a-9b65-a6f2c8e3075c":('7929', '79c291cf-6caa-469a-9b65-a6f2c8e3075c', 'WillesdenGreen', 'Willesden Green', ['Willesden Green']),
"0b7a7fd5-81c8-4f40-b072-ed5bd74eed46":('0775', '0b7a7fd5-81c8-4f40-b072-ed5bd74eed46', 'ChanceryLane', 'Chancery Lane', ['Chancery Lane']),
"d0c57e5c-e1b4-4cee-82bc-35751a8b4625":('0575', 'd0c57e5c-e1b4-4cee-82bc-35751a8b4625', 'RodingValley', 'Roding Valley', ['Roding Valley']),
"a7c40a0b-bb1a-46d9-8442-e7f45b8f7743":('7400', 'a7c40a0b-bb1a-46d9-8442-e7f45b8f7743', 'Harlesden', 'Harlesden', ['Harlesden']),
"9a89a50c-34ad-498a-bc81-598d58cd0d1f":('9895', '9a89a50c-34ad-498a-bc81-598d58cd0d1f', 'WestSilvertown', 'West Silvertown', ['West Silvertown']),
"4f6eda25-7e30-45ad-80f2-9db2453d262c":('4625', '4f6eda25-7e30-45ad-80f2-9db2453d262c', 'StJamessPark', "St. James's Park", ["St. James's Park"]),
"d60522bc-d2a5-4d89-8b52-0d236844c6ec":('6052', 'd60522bc-d2a5-4d89-8b52-0d236844c6ec', 'LatimerRoad', 'Latimer Road', ['Latimer Road']),
"2b13ebcf-2181-451d-b4b0-e53c03ae77f1":('2132', '2b13ebcf-2181-451d-b4b0-e53c03ae77f1', 'Farringdon', 'Farringdon', ['Farringdon']),
"48a452d3-6699-42fc-aa0a-d827185ecdc2":('4845', '48a452d3-6699-42fc-aa0a-d827185ecdc2', 'Shadwell', 'Shadwell', ['Shadwell']),
"3dfe2051-c378-4afa-9826-bc94298eb01a":('3205', '3dfe2051-c378-4afa-9826-bc94298eb01a', 'RegentsPark', "Regent's Park", ["Regent's Park"]),
"5c366dc4-6f3a-4ca2-8175-db52f2e5ad23":('5366', '5c366dc4-6f3a-4ca2-8175-db52f2e5ad23', 'LancasterGate', 'Lancaster Gate', ['Lancaster Gate']),
"37b045b7-e731-4056-87e8-ac5bf4e12c4a":('3704', '37b045b7-e731-4056-87e8-ac5bf4e12c4a', 'Leytonstone', 'Leytonstone', ['Leytonstone']),
"4a018a17-22e8-4539-b41d-910e4caf4b50":('4018', '4a018a17-22e8-4539-b41d-910e4caf4b50', 'LeicesterSquare', 'Leicester Square', ['Leicester Square']),
"2047f7d0-4ead-491d-93c9-c747a639d888":('2047', '2047f7d0-4ead-491d-93c9-c747a639d888', 'WestRuislip', 'West Ruislip', ['West Ruislip']),
"8046cf9c-5d92-47ee-b034-32205ba494c6":('8046', '8046cf9c-5d92-47ee-b034-32205ba494c6', 'Vauxhall', 'Vauxhall', ['Vauxhall']),
"07b7cfc5-10dd-4ff3-b46b-87a42a1d06b7":('0775', '07b7cfc5-10dd-4ff3-b46b-87a42a1d06b7', 'Chigwell', 'Chigwell', ['Chigwell']),
"0f98d1ce-4217-4f49-9e03-8402c32d2ff1":('0981', '0f98d1ce-4217-4f49-9e03-8402c32d2ff1', 'AldgateEast', 'Aldgate East', ['Aldgate East']),
"251c1166-6118-4fa3-9426-3d7b32f800d8":('2511', '251c1166-6118-4fa3-9426-3d7b32f800d8', 'Upminster', 'Upminster', ['Upminster']),
"8ec708cb-60c6-4dfa-a66c-2d7220dc7d83":('8708', '8ec708cb-60c6-4dfa-a66c-2d7220dc7d83', 'Embankment', 'Embankment', ['Embankment']),
"a8e021f5-0edf-408e-8e48-18fbeed57019":('8021', 'a8e021f5-0edf-408e-8e48-18fbeed57019', 'Chesham', 'Chesham', ['Chesham']),
"9df5a834-3827-4a46-9fb7-c26cce6837db":('9583', '9df5a834-3827-4a46-9fb7-c26cce6837db', 'WembleyPark', 'Wembley Park', ['Wembley Park']),
"093bea1f-2abe-41bb-b0ca-1716079e6104":('0931', '093bea1f-2abe-41bb-b0ca-1716079e6104', 'PontoonDock', 'Pontoon Dock', ['Pontoon Dock']),
"72af4cfa-953e-4afb-bc6c-a4f61abebee0":('7249', '72af4cfa-953e-4afb-bc6c-a4f61abebee0', 'Redbridge', 'Redbridge', ['Redbridge']),
"ea843760-eb68-4308-9c84-7d5546516ce6":('8437', 'ea843760-eb68-4308-9c84-7d5546516ce6', 'NorthGreenwich', 'North Greenwich', ['North Greenwich']),
"130b0d90-588d-4aad-b3a2-9d98efaf99cd":('1300', '130b0d90-588d-4aad-b3a2-9d98efaf99cd', 'HarrowontheHill', 'Harrow- on-the-Hill', ['Harrow- on-the-Hill']),
"34d5c090-9d83-4f39-bc46-5e4538ae2218":('3450', '34d5c090-9d83-4f39-bc46-5e4538ae2218', 'Euston', 'Euston', ['Euston']),
"ef5e3a08-aee0-4b26-9686-c699bc8d91e6":('5308', 'ef5e3a08-aee0-4b26-9686-c699bc8d91e6', 'CoventGarden', 'Covent Garden', ['Covent Garden']),
"af6b94cd-7efb-40a1-853e-e5c90607452d":('6947', 'af6b94cd-7efb-40a1-853e-e5c90607452d', 'Uxbridge', 'Uxbridge', ['Uxbridge']),
"3c1ecf94-d8e2-4e5f-8f54-645e836b3294":('3194', '3c1ecf94-d8e2-4e5f-8f54-645e836b3294', 'Barbican', 'Barbican', ['Barbican']),
"315f9ade-a54c-458c-a85f-f9962a5c6dc7":('3159', '315f9ade-a54c-458c-a85f-f9962a5c6dc7', 'EalingBroadway', 'Ealing Broadway', ['Ealing Broadway']),
"61596bb4-4814-44a5-8607-a66b4cc14bd1":('6159', '61596bb4-4814-44a5-8607-a66b4cc14bd1', 'Beckton', 'Beckton', ['Beckton']),
"78b8c3de-a903-484f-bf2c-6ce07bbdd28e":('7883', '78b8c3de-a903-484f-bf2c-6ce07bbdd28e', 'EdgwareRoad', 'Edgware Road', ['Edgware Road']),
"59f2c6ed-8120-4586-ab91-58d51304d468":('5926', '59f2c6ed-8120-4586-ab91-58d51304d468', 'HollowayRoad', 'Holloway Road', ['Holloway Road']),
"64981d6a-1322-49b2-aa95-a05d6b43423e":('6498', '64981d6a-1322-49b2-aa95-a05d6b43423e', 'Bank', 'Bank', ['Bank']),
"1e3d8c1e-1207-4030-9052-54ef0351dc62":('1381', '1e3d8c1e-1207-4030-9052-54ef0351dc62', 'NorthActon', 'North Acton', ['North Acton']),
"2599c24c-28ac-460b-9c99-ccfcd68bff37":('2599', '2599c24c-28ac-460b-9c99-ccfcd68bff37', 'CrossharbourLondonArena', 'Crossharbour & London Arena', ['Crossharbour & London Arena']),
"887a0d89-9d8b-4023-a901-86792db421ff":('8870', '887a0d89-9d8b-4023-a901-86792db421ff', 'FinchleyCentral', 'Finchley Central', ['Finchley Central']),
"742e97bc-26b6-4294-b111-b1301e8760d8":('7429', '742e97bc-26b6-4294-b111-b1301e8760d8', 'Whitechapel', 'Whitechapel', ['Whitechapel']),
"b5ef4219-5d51-49d4-8bd5-2fa1fb9e867c":('5421', 'b5ef4219-5d51-49d4-8bd5-2fa1fb9e867c', 'Pimlico', 'Pimlico', ['Pimlico']),
"a6d5538c-8cbf-44b1-b182-021be3c5c240":('6553', 'a6d5538c-8cbf-44b1-b182-021be3c5c240', 'Greenford', 'Greenford', ['Greenford']),
"b8f9c445-c7c7-4541-a396-a3d66ea350c4":('8944', 'b8f9c445-c7c7-4541-a396-a3d66ea350c4', 'QueensPark', 'Queens Park', ['Queens Park']),
"36fac8a5-abd7-4f1f-9cd6-e6e9a5843b8a":('3685', '36fac8a5-abd7-4f1f-9cd6-e6e9a5843b8a', 'EastPutney', 'East Putney', ['East Putney']),
"c4968339-846a-4814-b66f-6168c7f2398d":('4968', 'c4968339-846a-4814-b66f-6168c7f2398d', 'NottingHillGate', 'Notting Hill Gate', ['Notting Hill Gate']),
"46d479d0-c2c8-4893-bf40-41721a7be205":('4647', '46d479d0-c2c8-4893-bf40-41721a7be205', 'IslandGardens', 'Island Gardens', ['Island Gardens']),
"5af0f8f0-6783-4c15-a292-45f151ede2d2":('5080', '5af0f8f0-6783-4c15-a292-45f151ede2d2', 'Woodford', 'Woodford', ['Woodford']),
"77ebcb72-e4e5-4459-94e6-e2364e29f8b9":('7772', '77ebcb72-e4e5-4459-94e6-e2364e29f8b9', 'PuddingMillLane', 'Pudding Mill Lane', ['Pudding Mill Lane']),
"654971d2-8531-49f5-9e0c-8ad88beee31b":('6549', '654971d2-8531-49f5-9e0c-8ad88beee31b', 'ChalfontLatimer', 'Chalfont & Latimer', ['Chalfont & Latimer']),
"2fd3ee8f-d2df-4e94-86da-6d1cd67f1d4c":('2382', '2fd3ee8f-d2df-4e94-86da-6d1cd67f1d4c', 'ManorHouse', 'Manor House', ['Manor House']),
"80031d6b-6327-411f-b98a-0f8124c25d86":('8003', '80031d6b-6327-411f-b98a-0f8124c25d86', 'KewGardens', 'Kew Gardens', ['Kew Gardens']),
"ff596b51-d851-4cdb-b6ff-3f143a90c862":('5965', 'ff596b51-d851-4cdb-b6ff-3f143a90c862', 'Kennington', 'Kennington', ['Kennington']),
"0d3810fe-24fb-40d0-92c5-804a15144341":('0381', '0d3810fe-24fb-40d0-92c5-804a15144341', 'GantsHill', 'Gants Hill', ['Gants Hill']),
"01f067eb-fe23-44fb-b697-cb45fb258e71":('0106', '01f067eb-fe23-44fb-b697-cb45fb258e71', 'Wapping', 'Wapping', ['Wapping']),
"ec56b880-1907-449f-b9d9-3cb93a2d0b70":('5688', 'ec56b880-1907-449f-b9d9-3cb93a2d0b70', 'Aldgate', 'Aldgate', ['Aldgate']),
"c0eed10a-cfc3-417d-b06d-435f53af2d41":('0103', 'c0eed10a-cfc3-417d-b06d-435f53af2d41', 'ShepherdsBushH', "Shepherd's Bush", ["Shepherd's Bush"]),
"ed39a802-cf23-42a2-8006-cf2ab8a54048":('3980', 'ed39a802-cf23-42a2-8006-cf2ab8a54048', 'HighStreetKensington', 'High Street Kensington', ['High Street Kensington']),
"c8e337d3-3b61-4a7f-b973-686df3f7502d":('8337', 'c8e337d3-3b61-4a7f-b973-686df3f7502d', 'BurntOak', 'Burnt Oak', ['Burnt Oak']),
"b26ff8de-7cfe-4143-8413-1d9459ef877f":('2687', 'b26ff8de-7cfe-4143-8413-1d9459ef877f', 'EastIndia', 'East India', ['East India']),
"c95d8299-8911-4a67-af90-f945b8d990bb":('9582', 'c95d8299-8911-4a67-af90-f945b8d990bb', 'Temple', 'Temple', ['Temple']),
"497d910f-1ed1-4e9d-9e45-6a71f126fccc":('4979', '497d910f-1ed1-4e9d-9e45-6a71f126fccc', 'Arsenal', 'Arsenal', ['Arsenal']),
"422f8cfc-311d-4325-b891-278bb9f52621":('4228', '422f8cfc-311d-4325-b891-278bb9f52621', 'CanadaWater', 'Canada Water', ['Canada Water']),
"b194c301-5369-4cd9-ae07-8e454d4ebe69":('1943', 'b194c301-5369-4cd9-ae07-8e454d4ebe69', 'Southwark', 'Southwark', ['Southwark']),
"7e9b3da7-2e31-4fdf-90a0-f98cd7b0c8ed":('7937', '7e9b3da7-2e31-4fdf-90a0-f98cd7b0c8ed', 'HighBarnet', 'High Barnet', ['High Barnet']),
"f0395015-50a0-4933-bb40-6bb4d56ddffb":('0395', 'f0395015-50a0-4933-bb40-6bb4d56ddffb', 'Plaistow', 'Plaistow', ['Plaistow']),
"b1033dcd-c1e0-4a6b-97d9-b4b9fe6bcf6e":('1033', 'b1033dcd-c1e0-4a6b-97d9-b4b9fe6bcf6e', 'RavenscourtPark', 'Ravenscourt Park', ['Ravenscourt Park']),
"8823ac5f-5680-435b-a049-5ee40e86817e":('8823', '8823ac5f-5680-435b-a049-5ee40e86817e', 'AllSaints', 'All Saints', ['All Saints']),
"ad4d2a18-aca2-4020-a663-80927dd2f803":('4218', 'ad4d2a18-aca2-4020-a663-80927dd2f803', 'MoorPark', 'Moor Park', ['Moor Park']),
"5c249c9c-696d-4cbd-a8a3-c87f7029566e":('5249', '5c249c9c-696d-4cbd-a8a3-c87f7029566e', 'LondonBridge', 'London Bridge', ['London Bridge']),
"391b032a-4c3c-48b7-8be2-0ccbea92b7c1":('3910', '391b032a-4c3c-48b7-8be2-0ccbea92b7c1', 'Epping', 'Epping', ['Epping']),
"6ac25ebb-40be-4de4-bb86-c7db73ae823d":('6254', '6ac25ebb-40be-4de4-bb86-c7db73ae823d', 'MarbleArch', 'Marble Arch', ['Marble Arch']),
"0ae6e482-e472-4028-b0e4-461c6ad1f28f":('0648', '0ae6e482-e472-4028-b0e4-461c6ad1f28f', 'Southfields', 'Southfields', ['Southfields']),
"2669ea4a-b267-4a8b-b2fe-25276b670c53":('2669', '2669ea4a-b267-4a8b-b2fe-25276b670c53', 'WestHarrow', 'West Harrow', ['West Harrow']),
"4225000a-a83c-4db4-a906-fc32e828624b":('4225', '4225000a-a83c-4db4-a906-fc32e828624b', 'Limehouse', 'Limehouse', ['Limehouse']),
"a67bc448-b939-4d1a-9d9a-840c17b6a496":('6744', 'a67bc448-b939-4d1a-9d9a-840c17b6a496', 'CanaryWharf', 'Canary Wharf', ['Canary Wharf']),
"94660c36-6039-4805-a6cb-9221905ce759":('9466', '94660c36-6039-4805-a6cb-9221905ce759', 'Edgware', 'Edgware', ['Edgware']),
"ec42cf0b-0a85-4fb6-84fe-10a41a55ef9d":('4200', 'ec42cf0b-0a85-4fb6-84fe-10a41a55ef9d', 'Cockfosters', 'Cockfosters', ['Cockfosters']),
"e5ba2584-8519-4759-931d-056d31844a44":('5258', 'e5ba2584-8519-4759-931d-056d31844a44', 'WhiteCity', 'White City', ['White City']),
"b09cb073-2656-4079-b8e6-757300b367bd":('0907', 'b09cb073-2656-4079-b8e6-757300b367bd', 'OldStreet', 'Old Street', ['Old Street']),
"a59bf99e-0fd1-4823-bc06-89a1bb21101a":('5999', 'a59bf99e-0fd1-4823-bc06-89a1bb21101a', 'Loughton', 'Loughton', ['Loughton']),
"ee36d2e5-cdb0-4667-b960-d5d395d1c86a":('3625', 'ee36d2e5-cdb0-4667-b960-d5d395d1c86a', 'SwissCottage', 'Swiss Cottage', ['Swiss Cottage']),
"9021de2d-4cfd-48b5-98c1-30e002cc8f3a":('9021', '9021de2d-4cfd-48b5-98c1-30e002cc8f3a', 'SouthQuay', 'South Quay', ['South Quay']),
"f30b89ed-552a-40c9-afb5-ce64fa41ff2d":('3089', 'f30b89ed-552a-40c9-afb5-ce64fa41ff2d', 'Borough', 'Borough', ['Borough']),
"a0665b47-6400-476e-b569-ec68a6a7fd76":('0665', 'a0665b47-6400-476e-b569-ec68a6a7fd76', 'TurnpikeLane', 'Turnpike Lane', ['Turnpike Lane']),
"88392a34-b5cb-4c76-9e9d-7cfaf4fb944e":('8839', '88392a34-b5cb-4c76-9e9d-7cfaf4fb944e', 'SouthKensington', 'South Kensington', ['South Kensington']),
"7f6a1eba-5fd4-43fb-9d86-b60ef44f03d4":('7615', '7f6a1eba-5fd4-43fb-9d86-b60ef44f03d4', 'ElephantCastle', 'Elephant & Castle', ['Elephant & Castle']),
"f0a7d304-3e3f-46c8-978a-532bb28d3528":('0730', 'f0a7d304-3e3f-46c8-978a-532bb28d3528', 'KilburnPark', 'Kilburn Park', ['Kilburn Park']),
"815ea4ed-f5ee-4f5c-b3ab-3731a03eeed5":('8154', '815ea4ed-f5ee-4f5c-b3ab-3731a03eeed5', 'Monument', 'Monument', ['Monument']),
"ff3b1cfb-1ea1-48af-a66d-8f1787f38598":('3111', 'ff3b1cfb-1ea1-48af-a66d-8f1787f38598', 'Wanstead', 'Wanstead', ['Wanstead']),
"5064cba1-ec2e-416f-9153-c0273385d528":('5064', '5064cba1-ec2e-416f-9153-c0273385d528', 'Eastcote', 'Eastcote', ['Eastcote']),
"b95f74c7-0ccc-4a04-ad46-ae255ed14689":('9574', 'b95f74c7-0ccc-4a04-ad46-ae255ed14689', 'WestHam', 'West Ham', ['West Ham']),
"2ea2857a-1d56-4fe9-a145-d6031fd660ab":('2285', '2ea2857a-1d56-4fe9-a145-d6031fd660ab', 'RussellSquare', 'Russell Square', ['Russell Square']),
"1196b1e2-b958-4273-8c77-188a8ba4574c":('1196', '1196b1e2-b958-4273-8c77-188a8ba4574c', 'SudburyTown', 'Sudbury Town', ['Sudbury Town']),
"3ac40716-c714-4851-8204-5960863c4205":('3407', '3ac40716-c714-4851-8204-5960863c4205', 'WalthamstowCentral', 'Walthamstow Central', ['Walthamstow Central']),
"84826d24-3c8b-4fc3-9ecf-ec01c9afb2e2":('8482', '84826d24-3c8b-4fc3-9ecf-ec01c9afb2e2', 'WoodGreen', 'Wood Green', ['Wood Green']),
"018de108-a518-4d48-acb8-7bc2085dc28c":('0181', '018de108-a518-4d48-acb8-7bc2085dc28c', 'TootingBroadway', 'Tooting Broadway', ['Tooting Broadway']),
"25902e50-70bd-4fa6-964e-bf0154a396cd":('2590', '25902e50-70bd-4fa6-964e-bf0154a396cd', 'HollandPark', 'Holland Park', ['Holland Park']),
"b386afc8-3f11-4b5c-9a24-0543965ec173":('3868', 'b386afc8-3f11-4b5c-9a24-0543965ec173', 'BelsizePark', 'Belsize Park', ['Belsize Park']),
"9e0c5708-2ac3-41d5-baab-56d5602b76b1":('9057', '9e0c5708-2ac3-41d5-baab-56d5602b76b1', 'BromleyByBow', 'Bromley-By-Bow', ['Bromley-By-Bow']),
"58054f33-5750-4b25-9706-5028b2e96d0b":('5805', '58054f33-5750-4b25-9706-5028b2e96d0b', 'TurnhamGreen', 'Turnham Green', ['Turnham Green']),
"c9cd51e3-5fff-4ce7-9502-907fe8a28c1e":('9513', 'c9cd51e3-5fff-4ce7-9502-907fe8a28c1e', 'TufnellPark', 'Tufnell Park', ['Tufnell Park']),
"7bc2b747-1f8c-473f-a915-f1a476d1a1b3":('7274', '7bc2b747-1f8c-473f-a915-f1a476d1a1b3', 'GrangeHill', 'Grange Hill', ['Grange Hill']),
"559326bd-543e-4933-9241-990094b932cb":('5593', '559326bd-543e-4933-9241-990094b932cb', 'BaronsCourt', 'Barons Court', ['Barons Court']),
"7dbfb563-2a49-4ede-985d-5df9e4b91e93":('7563', '7dbfb563-2a49-4ede-985d-5df9e4b91e93', 'KingsCrossStPancras', "King's Cross St. Pancras", ["King's Cross St. Pancras"]),
"4335b1ca-4202-4c76-ba79-379bbbb9e9f4":('4335', '4335b1ca-4202-4c76-ba79-379bbbb9e9f4', 'EalingCommon', 'Ealing Common', ['Ealing Common']),
"70ab528d-f449-49ff-a03c-33bb16bf7ab7":('7052', '70ab528d-f449-49ff-a03c-33bb16bf7ab7', 'MansionHouse', 'Mansion House', ['Mansion House']),
"b8db5bac-3ac1-4bec-beda-69af98ebd222":('8531', 'b8db5bac-3ac1-4bec-beda-69af98ebd222', 'Morden', 'Morden', ['Morden']),
"9713cb92-a9d6-4eb8-9bf9-477860fd02ab":('9713', '9713cb92-a9d6-4eb8-9bf9-477860fd02ab', 'BondStreet', 'Bond Street', ['Bond Street']),
"f2afedc3-d882-413d-9483-f13605def449":('2388', 'f2afedc3-d882-413d-9483-f13605def449', 'Upney', 'Upney', ['Upney']),
"0999211f-c7f4-49ec-83ba-b249aefde30e":('0999', '0999211f-c7f4-49ec-83ba-b249aefde30e', 'NewCrossGate', 'New Cross Gate', ['New Cross Gate']),
"498adbf2-cab9-49d8-bff4-d35c8a0c9587":('4982', '498adbf2-cab9-49d8-bff4-d35c8a0c9587', 'CustomHouse', 'Custom House', ['Custom House']),
"437b3160-3e03-4694-aa4d-9349e8c419fa":('4373', '437b3160-3e03-4694-aa4d-9349e8c419fa', 'ChalkFarm', 'Chalk Farm', ['Chalk Farm']),
"89c3fead-9427-4698-830a-df06f301690f":('8939', '89c3fead-9427-4698-830a-df06f301690f', 'NorthEaling', 'North Ealing', ['North Ealing']),
"5799abba-8d65-47c8-b401-4c0976c68932":('5799', '5799abba-8d65-47c8-b401-4c0976c68932', 'PutneyBridge', 'Putney Bridge', ['Putney Bridge']),
"ccffda41-ad3f-4c1f-b19d-f3dfe244ee96":('4134', 'ccffda41-ad3f-4c1f-b19d-f3dfe244ee96', 'Westminster', 'Westminster', ['Westminster']),
"1750f083-8e55-4cb0-aaeb-70b14bed0158":('1750', '1750f083-8e55-4cb0-aaeb-70b14bed0158', 'BoundsGreen', 'Bounds Green', ['Bounds Green']),
"861ece04-d755-4e24-948c-1990014f49e2":('8610', '861ece04-d755-4e24-948c-1990014f49e2', 'TottenhamCourtRoad', 'Tottenham Court Road', ['Tottenham Court Road']),
"0d8038c4-2a18-42eb-95e9-b3eba2fbd129":('0803', '0d8038c4-2a18-42eb-95e9-b3eba2fbd129', 'SloaneSquare', 'Sloane Square', ['Sloane Square']),
"ac425ff0-4c85-4dc2-875b-980714c379b8":('4250', 'ac425ff0-4c85-4dc2-875b-980714c379b8', 'NorthwoodHills', 'Northwood Hills', ['Northwood Hills']),
"6bf824ad-8d24-4258-9e8c-398b85dfb3c8":('6824', '6bf824ad-8d24-4258-9e8c-398b85dfb3c8', 'CamdenTown', 'Camden Town', ['Camden Town']),
"39006e53-1040-4238-8886-b748bc899c23":('3900', '39006e53-1040-4238-8886-b748bc899c23', 'Angel', 'Angel', ['Angel']),
}

entities_geo={
"d801bd7d-2875-45ac-a003-189e78831f5a":(51.491999999999997, -0.1973, 'gcpugtb6dsd2'), # EarlsCourt
"8e9e65b9-127f-4442-ac1f-7d822a4462d9":(51.570099999999996, -0.30809999999999998, 'gcpv2up9serv'), # SouthKenton
"3edaef16-d991-46dd-a8ec-ae1bde54cf79":(51.584600000000002, -0.36259999999999998, 'gcptrwxynf3u'), # NorthHarrow
"9ab2674f-0593-4b86-8347-38109b2b23c5":(51.646999999999998, -0.44119999999999998, 'gcptvfn9x697'), # Croxley
"815ea4ed-f5ee-4f5c-b3ab-3731a03eeed5":(51.510800000000003, -0.086300000000000002, 'gcpvn130jj44'), # Monument
"48a452d3-6699-42fc-aa0a-d827185ecdc2":(51.511699999999998, -0.056000000000000001, 'gcpvn9rjrhg7'), # Shadwell
"ec42cf0b-0a85-4fb6-84fe-10a41a55ef9d":(51.651699999999998, -0.14960000000000001, 'gcpvudghfnf0'), # Cockfosters
"feb73b3b-5801-43f4-af25-1cbd0a8e9d0e":(51.561900000000001, -0.44209999999999999, 'gcptmfw1f6f6'), # Ickenham
"6eb88e01-0501-4962-965e-0c53d6514d15":(51.499499999999998, -0.31419999999999998, 'gcpubz5nqde7'), # Northfields
"cdea03f1-f838-4016-af3d-2c9251a3b143":(51.462699999999998, -0.1145, 'gcpuv2kxgywe'), # Brixton
"2c4f747a-1182-42d3-9455-a16923b20f75":(51.522500000000001, -0.16309999999999999, 'gcpvh73hr6pu'), # Marylebone
"ffcae605-fbf5-4928-9efd-2a9b18caa418":(51.527299999999997, -0.020799999999999999, 'gcpvps2b72fm'), # BowChurch
"72d3d976-272d-40ab-858f-7004cf92e4e4":(51.524900000000002, -0.0332, 'gcpvp5zf63s2'), # MileEnd
"f806f577-3afb-4101-8dec-e8e3435a9cc5":(51.503300000000003, -0.021499999999999998, 'gcpuzxbk7nbr'), # HeronQuays
"25a32e3a-f966-4a8f-be8e-8c44573676fe":(51.523800000000001, -0.1439, 'gcpvhex5yukq'), # GreatPortlandStreet
"516edae9-110a-4f51-a6d2-383c99210de2":(51.473999999999997, -0.021600000000000001, 'gcpuzd83b9jf'), # DeptfordBridge
"d6252a91-cd1c-4076-a6c8-463e8cc8b401":(51.4649, -0.12989999999999999, 'gcpuv0ckv0ew'), # ClaphamNorth
"8d6deaea-002d-4bf5-beed-0c4a3f381eae":(51.595500000000001, -0.25019999999999998, 'gcpvd29v9fm6'), # Colindale
"f7a34731-3bda-46e5-a10f-a9a2c0c4162a":(51.521000000000001, -0.2011, 'gcpv57jed48b'), # WestbournePark
"f97c9231-f8c8-4a52-be83-6a411f628f36":(51.526899999999998, -0.0247, 'gcpvpknjbqq7'), # BowRoad
"73b1cff3-b7ec-49c3-94da-a20d4c406f3b":(51.4983, -0.21060000000000001, 'gcpugnyxkdvm'), # KensingtonOlympia
"0421e847-920c-442f-bd16-cb36c83f9418":(51.502000000000002, 0.062700000000000006, 'u10hcrtsvh8s'), # KingGeorgeV
"3f6eb6d1-feab-47b9-9504-dffe13e25c15":(51.530000000000001, -0.18540000000000001, 'gcpv5ubbpb5x'), # MaidaVale
"52c525df-4eb6-4c1b-a4e4-55285e979dfa":(51.523499999999999, -0.1835, 'gcpv5gd6hhs3'), # WarwickAvenue
"3347e7d7-69a0-405a-86e7-e8f3e620e5a7":(51.509700000000002, -0.026499999999999999, 'gcpvp3h9y801'), # Westferry
"4e82f7b0-8d8c-455d-96c9-d13ebe0360c5":(51.471299999999999, -0.36649999999999999, 'gcpszdj45cvb'), # HounslowCentral
"e789e9e2-2587-480f-b1d3-e0cf154564ca":(51.6111, -0.42399999999999999, 'gcptw7e22n6e'), # Northwood
"b90ea9e7-280b-479c-9610-2bdba2ce40d5":(51.588200000000001, -0.059400000000000001, 'gcpvqxkepckp'), # TottenhamHale
"643f9889-844f-44d4-980a-2f553a72784f":(51.517200000000003, -0.2107, 'gcpv54qt6q4s'), # LadbrokeGrove
"0457feec-f14f-4871-a3a5-97b69ddd89ea":(51.540300000000002, 0.127, 'u10j4yskp261'), # Becontree
"94660c36-6039-4805-a6cb-9221905ce759":(51.613700000000001, -0.27500000000000002, 'gcpv9ezz8511'), # Edgware
"f77ebe4b-3779-4571-8f46-d6b9e451cd51":(51.516800000000003, -0.24740000000000001, 'gcpv467g55t4'), # EastActon
"889f0300-d383-42ce-aa8c-f79d72aed49d":(51.617899999999999, -0.18559999999999999, 'gcpveubb51yx'), # WoodsidePark
"103fcba9-b810-4929-b013-5a50daa094ea":(51.580800000000004, 0.021600000000000001, 'u10j2mzxzq41'), # Snaresbrook
"27545394-959e-4f16-84b1-da5a70cbea74":(51.503700000000002, 0.048800000000000003, 'u10hcpgwc1ec'), # LondonCityAirport
"535a3a8e-f2a4-41b2-b01e-a951947725dc":(51.509599999999999, 0.071599999999999997, 'u10j19h1hmku'), # GallionsReach
"37675294-b85e-4068-a8af-ebfa88c3f58f":(51.585599999999999, 0.088700000000000001, 'u10j6nbefugd'), # Barkingside
"82e21415-4000-41d4-b515-c6a64d610964":(51.471299999999999, -0.45240000000000002, 'gcpsvdnd43f0'), # HeathrowTerminals123
"8503b2ae-5d51-44f0-9d23-2943532cf421":(51.472299999999997, -0.123, 'gcpuv4nrvuht'), # Stockwell
"ddb614a5-4443-4ce0-bfcd-fb13269cb902":(51.647599999999997, -0.1318, 'gcpvv40j0f6y'), # Oakwood
"ea1f0f57-6953-428a-82ae-e2ee619ab313":(51.565300000000001, -0.1353, 'gcpvkgjmxk95'), # Archway
"d6a59b2a-da2d-4860-9df7-ae60ffabec1d":(51.520499999999998, -0.13469999999999999, 'gcpvhgjbtm23'), # GoodgeStreet
"d22c6041-ea25-4dd9-9546-24afcb13f472":(51.547199999999997, -0.18029999999999999, 'gcpv5zusnww9'), # FinchleyRoad
"6ac25ebb-40be-4de4-bb86-c7db73ae823d":(51.513599999999997, -0.15859999999999999, 'gcpvh3u82r53'), # MarbleArch
"07b7cfc5-10dd-4ff3-b46b-87a42a1d06b7":(51.617699999999999, 0.075499999999999998, 'u10j9swyzk8y'), # Chigwell
"8eccd70b-662c-474d-b91d-5c88c03286d9":(51.558199999999999, 0.23430000000000001, 'u10jm3fs794d'), # UpminsterBridge
"9a4ec1fc-88c4-46f1-9eaf-8319d640049e":(51.466900000000003, -0.42270000000000002, 'gcpsy3k0qms1'), # HattonCross
"42a97bba-8dab-4932-8925-3cbfedd59265":(51.481299999999997, -0.35220000000000001, 'gcpszgzs31us'), # Osterley
"d25453cf-7eb9-44b7-af27-250820ef3ecd":(51.5715, -0.42130000000000001, 'gcptqkm1ybru'), # Ruislip
"42fdbaea-b1c5-4ded-b3f3-c36b67145035":(51.512099999999997, -0.18790000000000001, 'gcpv59rptx7t'), # Bayswater
"f3c7ce45-e337-4d6a-8396-6f4a243b3bbe":(51.530200000000001, -0.29330000000000001, 'gcpv1kf3jte8'), # HangerLane
"9f80e0d8-84bb-4474-91b9-c02d59390ddc":(51.5077, -0.017299999999999999, 'gcpvp8eqhghn'), # Poplar
"ccf87110-0f7d-4f00-b6f7-e6c1440b20db":(51.550699999999999, -0.14019999999999999, 'gcpvkb9bt4gr'), # KentishTown
"50303a28-12d5-4954-a2b3-d7f62bf80e10":(51.524700000000003, -0.1384, 'gcpvhgg1ph1r'), # WarrenStreet
"0534ef61-db2a-416f-8f70-6d12bf356d95":(51.5227, -0.070800000000000002, 'gcpvn7kmqprt'), # Shoreditch
"a2cf78d3-ee61-411e-b76d-aa7ec1c3c772":(51.543900000000001, -0.27589999999999998, 'gcpv1xr0gp6h'), # StonebridgePark
"8ec708cb-60c6-4dfa-a66c-2d7220dc7d83":(51.507399999999997, -0.12230000000000001, 'gcpvj0wuq5q9'), # Embankment
"f15dee6f-5cd2-4ea1-8089-04955c76ff73":(51.494500000000002, -0.18290000000000001, 'gcpugy6c4nec'), # GloucesterRoad
"deed830e-f5d2-454a-b9d2-20685f742186":(51.463299999999997, -0.30130000000000001, 'gcpuc0se7nqq'), # Richmond
"0563b078-a7da-4c64-b1b6-a56816f2e979":(51.5366, -0.32319999999999999, 'gcpv0tuwkys9'), # Perivale
"99c7d4d2-9ed6-489f-a71c-ea012316652a":(51.509099999999997, 0.018100000000000002, 'u10j02vnmb0m'), # RoyalVictoria
"24866134-afce-40c1-9341-e9284019249d":(51.415399999999998, -0.19189999999999999, 'gcpu7xuk2mhz'), # SouthWimbledon
"2ad77ab0-d4d5-414d-8d2c-fb7606669c08":(51.518000000000001, -0.28089999999999998, 'gcpv1de6ne3b'), # WestActon
"a9f90eac-8bda-4b0d-a62c-0abace2ecacf":(51.508699999999997, 0.055, 'u10j12b5ctdg'), # BecktonPark
"5feb6509-d2bc-4746-9f7e-d29225e96867":(51.5443, 0.16550000000000001, 'u10j5z2e23vw'), # DagenhamEast
"1e3d8c1e-1207-4030-9052-54ef0351dc62":(51.523699999999998, -0.25969999999999999, 'gcpv45dgk9cd'), # NorthActon
"a4840c38-6656-41f9-92ff-2e0192e89cbe":(51.515000000000001, -0.14149999999999999, 'gcpvhf0bwu1b'), # OxfordCircus
"cebe7422-4f0d-435d-9219-0292d950967f":(51.509799999999998, -0.13420000000000001, 'gcpvhcn62ftj'), # PicadillyCircus
"efb5766a-16a9-434f-8574-1b254726866d":(51.522599999999997, -0.15709999999999999, 'gcpvh7msgkc8'), # BakerStreet
"7ca7ca09-f3e4-4212-8bca-ad03d410212c":(51.520299999999999, -0.17000000000000001, 'gcpvh4upw8nb'), # EdgwareRoadC
"7889cae9-8416-4153-aad3-66ce2e110e2b":(51.541699999999999, 0.1469, 'u10j5qfupj28'), # DagenhamHeathway
"2a1c5044-4b2a-48b8-bc59-830c88cd7dca":(51.5822, -0.074899999999999994, 'gcpvqq32nen8'), # SevenSisters
"5d50982e-bd14-46bb-8de9-3761a2498794":(51.552, -0.2387, 'gcpv68f0jvk6'), # DollisHill
"c5638fe6-7996-41f9-b291-3f0fcc1caeec":(51.5867, -0.041700000000000001, 'gcpvrp1dk3f5'), # BlackhorseRoad
"e8f8bb83-a6b8-4b37-90dd-ca34489bf9a3":(51.443100000000001, -0.1525, 'gcpussbvy2zu'), # Balham
"c7dec458-047a-4c3b-b9af-46e3d491821d":(51.493600000000001, -0.22509999999999999, 'gcpufyh5fyc2'), # Hammersmith
"c570c2e2-1ce5-4542-8269-4dd40c07e8f3":(51.556800000000003, -0.17799999999999999, 'gcpv7cwkhk1e'), # Hampstead
"016338cd-a632-4ef4-af89-42e6ce3d05a5":(51.494599999999998, -0.26779999999999998, 'gcpucykczc1y'), # ChiswickPark
"5f45b71a-7b9a-449f-bdee-cd6262795f51":(51.572400000000002, -0.19409999999999999, 'gcpv7s6xj0ht'), # GoldersGreen
"23724ad1-b79e-4eb1-bc07-1c19dd5dfae9":(51.475299999999997, -0.2011, 'gcpug6v9652v'), # ParsonsGreen
"e65e7008-2695-4440-ab38-d7f81b7c6976":(51.576599999999999, -0.21360000000000001, 'gcpv7jhrqz07'), # BrentCross
"8c78516a-b7e2-47eb-b9b5-117100c51bc2":(51.5154, -0.17549999999999999, 'gcpvh404yw9d'), # Paddington
"249dc44e-c5e8-4803-818a-ea54725c2a9d":(51.522100000000002, -0.047, 'gcpvngmcbzd3'), # StepneyGreen
"303e944e-a63e-4fd4-8dbe-8971d332b187":(51.554200000000002, -0.25030000000000002, 'gcpv631szx6v'), # Neasden
"7e39a3bf-1054-422f-8909-c304cdd9efe9":(51.421399999999998, -0.2064, 'gcpue2cxqe9p'), # Wimbledon
"6b549b5b-db83-4ffa-8ad3-baba502a92c6":(51.534700000000001, -0.17399999999999999, 'gcpvhj973s25'), # StJohnsWood
"03af5d7e-72c4-413f-a260-52c1fe5d022c":(51.671700000000001, 0.1033, 'u10jfqe1rp40'), # TheydonBois
"611cdae4-916d-43c3-aa1c-bcba08d75098":(51.493299999999998, -0.047800000000000002, 'gcpuyyj4nnve'), # SurreyQuays
"984d0bdd-193e-4a3b-b0b3-523edea3351e":(51.632199999999997, -0.128, 'gcpvtp6g37sq'), # Southgate
"0baa84a4-8275-4f53-bc45-1476fdd5934f":(51.501800000000003, -0.22670000000000001, 'gcpufzdgtx25'), # GoldhawkRoad
"2f61ae2d-9ffc-4f3c-afa0-87e712df3cff":(51.502699999999997, -0.1527, 'gcpuuxbbcz4s'), # HydeParkCorner
"ef5e3a08-aee0-4b26-9686-c699bc8d91e6":(51.512900000000002, -0.12429999999999999, 'gcpvj1tkrse1'), # CoventGarden
"44438768-26b6-4414-bdbd-a30055d17ced":(51.4527, -0.14799999999999999, 'gcpuswsjxq7n'), # ClaphamSouth
"ef56ae4c-6447-4907-bf07-49a13385b951":(51.609499999999997, -0.1883, 'gcpveenzhk17'), # WestFinchley
"0a9a00c8-2f22-4c01-bc55-8402eb72e5b3":(51.490699999999997, -0.20649999999999999, 'gcpugm9eh4nm'), # WestKensington
"74125284-3256-4527-a79d-0fddd3099af9":(51.417999999999999, -0.17780000000000001, 'gcpuebqe8cyt'), # ColliersWood
"5c389d95-edf6-4554-adec-654d9a1a16f8":(51.541600000000003, -0.0041999999999999997, 'gcpvpyugw4s7'), # Stratford
"2d04e04c-9ce2-4384-80e3-06243cb8d90b":(51.553899999999999, 0.21840000000000001, 'u10jkcp51pdb'), # Hornchurch
"ed5d6e00-71b2-4df5-b7b2-05dfd3a9646c":(51.616399999999999, -0.1331, 'gcpvsurp6d37'), # ArnosGrove
"25c555f4-f529-4149-823e-a04c4463d524":(51.572000000000003, -0.2954, 'gcpv3k2usttg'), # PrestonRoad
"367c4cde-ffab-44df-a220-2b5c8ad298f4":(51.508400000000002, 0.0465, 'u10j10cf5t8y'), # RoyalAlbert
"0d2de214-c96e-4842-a10f-5fe058a90d5b":(51.549599999999998, 0.19769999999999999, 'u10jk2rfntzv'), # ElmPark
"e6fba115-a15d-4b53-8106-c0cd5f3c007f":(51.608199999999997, -0.21029999999999999, 'gcpve4yze9ub'), # MillHillEast
"3378c47b-ad46-4f7f-8670-0f5394af7cb2":(51.564599999999999, -0.35210000000000002, 'gcptrgp9e6ph'), # SouthHarrow
"d08e5786-189f-4451-916f-3c78d21e7f12":(51.630200000000002, -0.17910000000000001, 'gcpveyvxdwv7'), # TotteridgeWhetstone
"bfb41f10-53d9-44b4-8233-e5389ab3d583":(51.504600000000003, -0.21870000000000001, 'gcpv500spcm6'), # ShepherdsBushC
"6ad20349-f3f2-4290-8fb1-a0d4718c0d32":(51.509300000000003, 0.033599999999999998, 'u10j0bbrqvmy'), # PrinceRegent
"010c886c-7201-4d49-81fc-f78cecdfa1b3":(51.508499999999998, 0.064000000000000001, 'u10j12ydg23f'), # Cyprus
"bbed2b3a-a6d0-41f0-93af-82c7bb0c9d8b":(51.539400000000001, 0.051799999999999999, 'u10j1nmwz08b'), # EastHam
"6a4220d7-975d-4710-b069-2cf4dafc50e1":(51.584600000000002, -0.27860000000000001, 'gcpv3wtnh4ku'), # Kingsbury
"9ea06909-e76d-407f-bbf1-06a4e63f454c":(51.503599999999999, -0.1143, 'gcpuvruy0wgt'), # Waterloo
"ac632aec-da92-4b75-a0ea-3ec9f7b60aa1":(51.626600000000003, 0.047100000000000003, 'u10j9n669xb2'), # BuckhurstHill
"b39c2218-4bd9-4c5a-ac76-9483a64e58ec":(51.511299999999999, -0.090399999999999994, 'gcpvjcq5jd2c'), # CannonStreet
"c94e833d-198e-4108-809b-ba38e1b5aba7":(51.506700000000002, -0.14280000000000001, 'gcpvhb8028b9'), # GreenPark
"4ac60516-0e6a-47b4-898c-4a4d127a8baa":(51.527000000000001, -0.28410000000000002, 'gcpv1s1nebzx'), # ParkRoyal
"5e7c3e79-ec13-4840-a499-5c1cef1a6b2f":(51.508000000000003, -0.12470000000000001, 'gcpvj0tpy70u'), # CharingCross
"925a7fd8-5dc1-4620-a272-c4697d56172c":(51.522300000000001, -0.017299999999999999, 'gcpvpe77huu4'), # DevonsRoad
"465b5b31-1237-4007-929b-5ffc63e19f79":(51.575600000000001, 0.089899999999999994, 'u10j6j13wudm'), # NewburyPark
"0767b416-a3da-4c1c-85bf-a3e59a2657d6":(51.654299999999999, -0.51829999999999998, 'gcptu5qs4ert'), # Chorleywood
"25ef1cc7-866a-474e-acc7-44a0d7e6bca5":(51.619399999999999, -0.30280000000000001, 'gcpv9j58b1xg'), # Stanmore
"46d479d0-c2c8-4893-bf40-41721a7be205":(51.487099999999998, -0.0101, 'gcpuzubwhehf'), # IslandGardens
"2f0faf9b-7406-4a32-8d18-927b7af16497":(51.575299999999999, -0.37140000000000001, 'gcptrscxcub0'), # RaynersLane
"410e92c7-e6ac-4739-90dd-0834bb8b6e83":(51.594200000000001, -0.28610000000000002, 'gcpv92rtvrur'), # Queensbury
"36fac8a5-abd7-4f1f-9cd6-e6e9a5843b8a":(51.458599999999997, -0.2112, 'gcpuepy0ndmc'), # EastPutney
"c2ee297b-72ee-4842-9660-fd2ed00d93a2":(51.518599999999999, -0.088599999999999998, 'gcpvjfxmx7p5'), # Moorgate
"28b2ee7c-7a48-44d2-b4a9-499effac5775":(51.560600000000001, -0.4103, 'gcptqdm4r26p'), # RuislipGardens
"dd74b4e2-6e32-48f9-91cf-aa23e5551688":(51.5732, -0.41249999999999998, 'gcptqseesj39'), # RuislipManor
"174ca94d-74d1-4606-9836-69aa275eb76e":(51.592599999999997, -0.3805, 'gcptx24uttww'), # Pinner
"9aefa543-e3ff-4606-822b-b18794f4835d":(51.495600000000003, -0.32500000000000001, 'gcpubw7rdgw7'), # BostonManor
"21ca86c8-b3a9-4040-b088-a2bba3e17c7d":(51.509799999999998, -0.076600000000000001, 'gcpvn304r4dv'), # TowerHill
"2047f7d0-4ead-491d-93c9-c747a639d888":(51.569600000000001, -0.43759999999999999, 'gcptq5cqenjy'), # WestRuislip
"7f63805a-0964-46ad-a282-e7dc199b8685":(51.526000000000003, -0.13589999999999999, 'gcpvhuj09q9d'), # EustonSquare
"e427de05-8e0e-4bb6-99f7-81835be4bee7":(51.514600000000002, -0.097299999999999998, 'gcpvjccnk9ry'), # StPauls
"97c4c33d-b5af-421b-aeef-b6ff98e3f1ca":(51.603000000000002, 0.093299999999999994, 'u10jd45cq03t'), # Hainault
"afdf2e47-c231-43be-bc77-5486ee74b1e5":(51.546900000000001, -0.19059999999999999, 'gcpv5xv4qww7'), # WestHampstead
"497d910f-1ed1-4e9d-9e45-6a71f126fccc":(51.558599999999998, -0.10589999999999999, 'gcpvm9fys7eh'), # Arsenal
"b5ef4219-5d51-49d4-8bd5-2fa1fb9e867c":(51.4893, -0.13339999999999999, 'gcpuuvqfgt1y'), # Pimlico
"ccffd31a-972c-40ba-903a-0e4ce0d971c6":(51.548099999999998, -0.1188, 'gcpvm213ry23'), # CaledonianRoad
"b6f356a7-c2a4-4974-8c96-9519cbb7b839":(51.473399999999998, -0.38550000000000001, 'gcpsz4rq31nr'), # HounslowWest
"0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4":(51.5015, -0.16070000000000001, 'gcpuurdczrmq'), # Knightsbridge
"68f6f208-ef36-4859-9a85-6440e04d4c63":(51.482700000000001, -0.0095999999999999992, 'gcpuzu1h2qce'), # CuttySark
"52433503-c65c-4089-82ff-4fd1d2780f84":(51.481900000000003, -0.113, 'gcpuv7vxyctp'), # Oval
"8ca4bf88-8884-42eb-82b9-93c921dd3fc7":(51.551900000000003, -0.29630000000000001, 'gcpv328pxdwt'), # WembleyCentral
"d168eb7a-13eb-477b-b482-c69c3b4f5dbf":(51.459800000000001, -0.4476, 'gcpstzfp41vp'), # HeathrowTerminal4
"fa04941a-9c43-4392-b0a4-43e75b3a7e82":(51.461799999999997, -0.1384, 'gcpuub74xnc6'), # ClaphamCommon
"a14eddb7-704e-4d4f-a0d6-5105d028f128":(51.500999999999998, -0.052499999999999998, 'gcpuyz3z0djp'), # Rotherhithe
"1f3ac254-b5cd-4317-b777-64f2432e4c7a":(51.534199999999998, -0.13869999999999999, 'gcpvhve02p1v'), # MorningtonCrescent
"e93bad5c-e2e2-45f2-940f-35583fc357dd":(51.553800000000003, -0.44990000000000002, 'gcptmc06ssf5'), # Hillingdon
"e5c04fad-1dfc-46c3-8e27-74a8a6b1c63e":(51.578400000000002, -0.31840000000000002, 'gcpv2v81uwxu'), # NorthwickPark
"559326bd-543e-4933-9241-990094b932cb":(51.490499999999997, -0.21390000000000001, 'gcpugjs1zubs'), # BaronsCourt
"8b275b50-6675-44dc-b9f8-154730faac04":(51.490200000000002, -0.014500000000000001, 'gcpuztt2nhup'), # Mudchute
"e4f72828-a29a-4fdd-9bea-66fecdcfa250":(51.480400000000003, -0.19500000000000001, 'gcpugedp04j7'), # FulhamBroadway
"15351ff7-4b56-4882-a4d0-c4fd315ac9ef":(51.476700000000001, -0.0327, 'gcpuz701w03h'), # NewCross
"ae7c6e42-5090-4910-ad23-4ec083564183":(51.645499999999998, 0.083799999999999999, 'u10jccv0bdvz'), # Debden
"29105288-d523-40cf-99a1-1ef83751460f":(51.506999999999998, -0.020299999999999999, 'gcpvp894nbxn'), # WestIndiaQuay
"3e8ccac4-231c-4715-90fc-2025b412d64f":(51.581600000000002, -0.31619999999999998, 'gcpv2y1u850j'), # Kenton
"a6d5538c-8cbf-44b1-b182-021be3c5c240":(51.542299999999997, -0.34560000000000002, 'gcpv0nurdvjg'), # Greenford
"e0b9f30a-2875-4559-a814-8d2297a2266d":(51.469299999999997, -0.017399999999999999, 'gcpuz9eq6sct'), # ElversonRoad
"5177aa0d-3b92-4a1d-8356-3acfd80189be":(51.5777, -0.14580000000000001, 'gcpvktmvfs5s'), # Highgate
"1629ea4a-7ee7-4f0c-bb70-231721b53632":(51.517400000000002, -0.12, 'gcpvj62weg3t'), # Holborn
"2e6585ea-25a5-4255-b312-fb33a99de249":(51.592500000000001, -0.33510000000000001, 'gcpv825upe56'), # HarrowWealdston
"09bbbf1c-4b44-4300-9b7e-7da31c621afc":(51.518999999999998, -0.188, 'gcpv5dxpgm9j'), # RoyalOak
"b09cb073-2656-4079-b8e6-757300b367bd":(51.526299999999999, -0.087300000000000003, 'gcpvnh06my2r'), # OldStreet
"9ac4ad96-5502-4948-a754-8558c1a59201":(51.582900000000002, -0.22589999999999999, 'gcpv6y7s0jsb'), # HendonCentral
"9bd73108-ad7c-4b42-93c5-8a9d8cdd0acc":(51.535200000000003, 0.034299999999999997, 'u10j0v8yr1xf'), # UptonPark
"95b2c24a-fdf9-4cb0-b04e-4989909ffb72":(51.5396, 0.081000000000000003, 'u10j1y6zzmvc'), # Barking
"30d86bee-6a66-4f65-9b47-dd2a21e5a4f8":(51.512, -0.1031, 'gcpvj9kzjsg1'), # Blackfriars
"662cbbc1-1d6b-48be-b85c-140fb3c2d832":(51.497900000000001, -0.063700000000000007, 'gcpuywct58mg'), # Bermondsey
"fa25d9e4-e9c9-44da-ae24-ea2d2235d9f6":(51.556899999999999, -0.39879999999999999, 'gcptqctseqc0'), # SouthRuislip
"05da5b28-c40d-4860-92fb-6edf97f64650":(51.478099999999998, -0.0149, 'gcpuzem1sv3g'), # Greenwich
"6e66b0ff-cfc1-42b3-8029-3ecad13b44ae":(51.494999999999997, -0.24590000000000001, 'gcpufqkun5g8'), # StamfordBrook
"815fd4eb-ead4-4ef9-b778-c4dea749ce82":(51.487200000000001, -0.1953, 'gcpugscy9jtz'), # WestBrompton
"2b655c4f-fbfb-4005-be97-38962e01a3ed":(51.5304, -0.22500000000000001, 'gcpv4uu4m4gc'), # KensalGreen
"78e36286-e750-49ee-927a-4e2bc3134788":(51.517800000000001, -0.082299999999999998, 'gcpvn4s0fmbx'), # LiverpoolStreet
"c4806aae-06ae-4c0e-bbe6-f57c358976da":(51.540700000000001, -0.29970000000000002, 'gcpv1nty26z7'), # Alperton
"2945184c-9a8d-4707-88a3-ec1bd35999b0":(51.514699999999998, 0.0082000000000000007, 'u10j01vyzh47'), # CanningTown
"480e2906-9176-4d6a-b14b-3a966a5a4f3f":(51.527000000000001, -0.054899999999999997, 'gcpvnu0n88zx'), # BethnalGreen
"e6c6ede6-efc2-4040-9876-932552ce8646":(51.499099999999999, -0.1115, 'gcpuvrnu1b59'), # LambethNorth
"8450af6a-dbf3-4749-811b-6676552bed4b":(51.545999999999999, -0.104, 'gcpvjxsm0wgf'), # HighburyIslington
"93bcf13e-165d-4294-8c8a-434ffbdf7374":(51.607799999999997, -0.29470000000000002, 'gcpv96cmhzpy'), # CanonsPark
"cd0ae317-6fa5-4640-8971-50661b49c32f":(51.436100000000003, -0.1598, 'gcpus7esurur'), # TootingBec
"38d6323c-663a-4f54-a58b-71cff0611d3d":(51.532600000000002, -0.24779999999999999, 'gcpv4m5x1ufu'), # WillesdenJunction
"7cb122f8-02b7-4ec6-8021-85a4ae14639e":(51.591700000000003, 0.0275, 'u10j2xup2vcq'), # SouthWoodford
"32b3c7d2-f9a2-4d46-ba4f-1c5efb4ddeb3":(51.491500000000002, -0.27539999999999998, 'gcpuctxrwxqc'), # Gunnersbury
"f0a2bae9-93f2-4acc-af91-602c879cd8fd":(51.502800000000001, -0.28010000000000002, 'gcpucxu191y2'), # ActonTown
"61596bb4-4814-44a5-8607-a66b4cc14bd1":(51.514800000000001, 0.0613, 'u10j13uxkqsx'), # Beckton
"aaf9fad0-0d23-4c27-927d-79a20d43d505":(51.496499999999997, -0.1447, 'gcpuuwwsu5rg'), # Victoria
"36aa3d82-e972-4f11-81cc-b94415bf849f":(51.473300000000002, -0.35639999999999999, 'gcpszfkmxq8f'), # HounslowEast
"a67bcb93-f537-428c-813e-8a257ef98d98":(51.5107, -0.18770000000000001, 'gcpv59prd62w'), # Queensway
"13a9b335-fdb9-44d3-bd3d-09fc64504063":(51.657299999999999, -0.41770000000000002, 'gcpty7zvdfsm'), # Watford
"79c291cf-6caa-469a-9b65-a6f2c8e3075c":(51.549199999999999, -0.2215, 'gcpv6bnxyeme'), # WillesdenGreen
"0b7a7fd5-81c8-4f40-b072-ed5bd74eed46":(51.518500000000003, -0.1111, 'gcpvj6xj50mz'), # ChanceryLane
"d0c57e5c-e1b4-4cee-82bc-35751a8b4625":(51.617100000000001, 0.043900000000000002, 'u10j8uxgquy5'), # RodingValley
"77ebcb72-e4e5-4459-94e6-e2364e29f8b9":(51.534300000000002, -0.013899999999999999, 'gcpvpttch1g3'), # PuddingMillLane
"9a89a50c-34ad-498a-bc81-598d58cd0d1f":(51.502699999999997, 0.022599999999999999, 'u10hbxb2yx5u'), # WestSilvertown
"4f6eda25-7e30-45ad-80f2-9db2453d262c":(51.499400000000001, -0.13350000000000001, 'gcpuuznv9pzp'), # StJamessPark
"d60522bc-d2a5-4d89-8b52-0d236844c6ec":(51.5139, -0.2172, 'gcpv51cf4ygz'), # LatimerRoad
"2b13ebcf-2181-451d-b4b0-e53c03ae77f1":(51.520299999999999, -0.1053, 'gcpvjdgrd248'), # Farringdon
"320689c7-450e-44d5-a799-0022492c1944":(51.507899999999999, -0.0066, 'gcpvpbepq0qx'), # Blackwall
"3dfe2051-c378-4afa-9826-bc94298eb01a":(51.523400000000002, -0.14660000000000001, 'gcpvhet1xczh'), # RegentsPark
"c9cd51e3-5fff-4ce7-9502-907fe8a28c1e":(51.556699999999999, -0.13739999999999999, 'gcpvkcegw37n'), # TufnellPark
"5c366dc4-6f3a-4ca2-8175-db52f2e5ad23":(51.511899999999997, -0.17560000000000001, 'gcpvh12ns4ph'), # LancasterGate
"b26ff8de-7cfe-4143-8413-1d9459ef877f":(51.509300000000003, -0.0020999999999999999, 'gcpvpbyrrj6n'), # EastIndia
"37b045b7-e731-4056-87e8-ac5bf4e12c4a":(51.568300000000001, 0.0083000000000000001, 'u10j25wp17ug'), # Leytonstone
"4a018a17-22e8-4539-b41d-910e4caf4b50":(51.511299999999999, -0.12809999999999999, 'gcpvj16ep439'), # LeicesterSquare
"8046cf9c-5d92-47ee-b034-32205ba494c6":(51.4861, -0.12529999999999999, 'gcpuvhub229t'), # Vauxhall
"c1736808-6ac4-4c5c-8026-eafa83f98266":(51.548299999999998, -0.36870000000000003, 'gcptr85d8et7'), # Northolt
"0f98d1ce-4217-4f49-9e03-8402c32d2ff1":(51.5154, -0.072599999999999998, 'gcpvn654uq9d'), # AldgateEast
"251c1166-6118-4fa3-9426-3d7b32f800d8":(51.558999999999997, 0.251, 'u10jmdnbbwpp'), # Upminster
"ce94a872-77e5-44b1-adab-6f4b70e5190c":(51.6404, -0.4733, 'gcptv0z75k3b'), # Rickmansworth
"a8e021f5-0edf-408e-8e48-18fbeed57019":(51.705199999999998, -0.61099999999999999, 'gcpw4hehdev7'), # Chesham
"9df5a834-3827-4a46-9fb7-c26cce6837db":(51.563499999999998, -0.27950000000000003, 'gcpv3du7pjjd'), # WembleyPark
"093bea1f-2abe-41bb-b0ca-1716079e6104":(51.502099999999999, 0.031899999999999998, 'u10hbxxjrr63'), # PontoonDock
"72af4cfa-953e-4afb-bc6c-a4f61abebee0":(51.576300000000003, 0.045400000000000003, 'u10j3j1j9zht'), # Redbridge
"ea843760-eb68-4308-9c84-7d5546516ce6":(51.500500000000002, 0.0038999999999999998, 'u10hbp6u4vh0'), # NorthGreenwich
"130b0d90-588d-4aad-b3a2-9d98efaf99cd":(51.579300000000003, -0.33660000000000001, 'gcpv2mdzhwkv'), # HarrowontheHill
"34d5c090-9d83-4f39-bc46-5e4538ae2218":(51.528199999999998, -0.13370000000000001, 'gcpvhuqts8dj'), # Euston
"87b81f55-4ebd-41fc-a8e1-0e701cb6bda1":(51.595999999999997, 0.091200000000000003, 'u10jd0f2mpe8'), # Fairlop
"af6b94cd-7efb-40a1-853e-e5c90607452d":(51.546300000000002, -0.47860000000000003, 'gcptjpeqzycb'), # Uxbridge
"3c1ecf94-d8e2-4e5f-8f54-645e836b3294":(51.520400000000002, -0.097900000000000001, 'gcpvjg08nf8m'), # Barbican
"315f9ade-a54c-458c-a85f-f9962a5c6dc7":(51.5152, -0.30170000000000002, 'gcpv14h3cck1'), # EalingBroadway
"e5ba2584-8519-4759-931d-056d31844a44":(51.512, -0.22389999999999999, 'gcpv4ckznub1'), # WhiteCity
"78b8c3de-a903-484f-bf2c-6ce07bbdd28e":(51.5199, -0.16789999999999999, 'gcpvh4vtptkw'), # EdgwareRoadB
"59f2c6ed-8120-4586-ab91-58d51304d468":(51.552599999999998, -0.1132, 'gcpvm2vedjpv'), # HollowayRoad
"64981d6a-1322-49b2-aa95-a05d6b43423e":(51.513300000000001, -0.088599999999999998, 'gcpvjcxqxrp5'), # Bank
"a5d9ae6f-e2a1-48a0-b671-05fc0c0376d7":(51.510599999999997, -0.074300000000000005, 'gcpvn31yuxvc'), # TowerGateway
"2599c24c-28ac-460b-9c99-ccfcd68bff37":(51.495699999999999, -0.0144, 'gcpuzwt80qnx'), # CrossharbourLondonArena
"887a0d89-9d8b-4023-a901-86792db421ff":(51.601199999999999, -0.19320000000000001, 'gcpve9eqf0ge'), # FinchleyCentral
"742e97bc-26b6-4294-b111-b1301e8760d8":(51.519399999999997, -0.061199999999999997, 'gcpvndg6mbjz'), # Whitechapel
"80031d6b-6327-411f-b98a-0f8124c25d86":(51.476999999999997, -0.28499999999999998, 'gcpuce07r029'), # KewGardens
"767e63fc-be79-449a-a461-670f3888eb56":(51.562100000000001, -0.3034, 'gcpv34e5420e'), # NorthWembley
"b8f9c445-c7c7-4541-a396-a3d66ea350c4":(51.534100000000002, -0.20469999999999999, 'gcpv5m6zyhs8'), # QueensPark
"57d3a7a7-5e23-447e-bb6a-cbbd12a9d635":(51.587400000000002, -0.16500000000000001, 'gcpvkppy7hr5'), # EastFinchley
"f30b89ed-552a-40c9-afb5-ce64fa41ff2d":(51.501100000000001, -0.094299999999999995, 'gcpuvz7rdsuu'), # Borough
"6bf824ad-8d24-4258-9e8c-398b85dfb3c8":(51.539200000000001, -0.1426, 'gcpvhy2jt5jx'), # CamdenTown
"5af0f8f0-6783-4c15-a292-45f151ede2d2":(51.606999999999999, 0.034099999999999998, 'u10j8fbbdd4f'), # Woodford
"a7c40a0b-bb1a-46d9-8442-e7f45b8f7743":(51.536200000000001, -0.25750000000000001, 'gcpv4jukpgfp'), # Harlesden
"654971d2-8531-49f5-9e0c-8ad88beee31b":(51.667900000000003, -0.56100000000000005, 'gcptgjz7rf8h'), # ChalfontLatimer
"2fd3ee8f-d2df-4e94-86da-6d1cd67f1d4c":(51.571199999999997, -0.095799999999999996, 'gcpvmu60p8qq'), # ManorHouse
"ff596b51-d851-4cdb-b6ff-3f143a90c862":(51.488399999999999, -0.1053, 'gcpuvt5mdm6t'), # Kennington
"0d3810fe-24fb-40d0-92c5-804a15144341":(51.576500000000003, 0.066299999999999998, 'u10j3t0qbuky'), # GantsHill
"01f067eb-fe23-44fb-b697-cb45fb258e71":(51.504300000000001, -0.055800000000000002, 'gcpvn8p67c2s'), # Wapping
"ec56b880-1907-449f-b9d9-3cb93a2d0b70":(51.514299999999999, -0.075499999999999998, 'gcpvn3ch89x1'), # Aldgate
"c0eed10a-cfc3-417d-b06d-435f53af2d41":(51.505800000000001, -0.22650000000000001, 'gcpv4b7541j2'), # ShepherdsBushH
"ed39a802-cf23-42a2-8006-cf2ab8a54048":(51.500900000000001, -0.1925, 'gcpugx7y6rte'), # HighStreetKensington
"c8e337d3-3b61-4a7f-b973-686df3f7502d":(51.602800000000002, -0.2641, 'gcpv9fp8n50u'), # BurntOak
"9021de2d-4cfd-48b5-98c1-30e002cc8f3a":(51.500700000000002, -0.019099999999999999, 'gcpuzx6j6fq1'), # SouthQuay
"c95d8299-8911-4a67-af90-f945b8d990bb":(51.511099999999999, -0.11409999999999999, 'gcpvj3kcvm0b'), # Temple
"bef7f260-c351-412c-bec0-b05d82367f88":(51.465699999999998, -0.014200000000000001, 'gcpuz9j9mjgd'), # Lewisham
"437b3160-3e03-4694-aa4d-9349e8c419fa":(51.5441, -0.15379999999999999, 'gcpvhx240hwm'), # ChalkFarm
"422f8cfc-311d-4325-b891-278bb9f52621":(51.498199999999997, -0.050200000000000002, 'gcpuyygqy220'), # CanadaWater
"b194c301-5369-4cd9-ae07-8e454d4ebe69":(51.503999999999998, -0.1052, 'gcpvj852s9mp'), # Southwark
"7e9b3da7-2e31-4fdf-90a0-f98cd7b0c8ed":(51.650300000000001, -0.1943, 'gcpvgddsb3z2'), # HighBarnet
"f0395015-50a0-4933-bb40-6bb4d56ddffb":(51.531300000000002, 0.0172, 'u10j0kux8f94'), # Plaistow
"b1033dcd-c1e0-4a6b-97d9-b4b9fe6bcf6e":(51.494199999999999, -0.2359, 'gcpufwhprns5'), # RavenscourtPark
"8823ac5f-5680-435b-a049-5ee40e86817e":(51.5107, -0.012999999999999999, 'gcpvp9nx946q'), # AllSaints
"ad4d2a18-aca2-4020-a663-80927dd2f803":(51.629399999999997, -0.432, 'gcptwnv7j9tr'), # MoorPark
"5c249c9c-696d-4cbd-a8a3-c87f7029566e":(51.505200000000002, -0.086400000000000005, 'gcpvn01pd9pm'), # LondonBridge
"391b032a-4c3c-48b7-8be2-0ccbea92b7c1":(51.6937, 0.1139, 'u10n4ddcwh1g'), # Epping
"43b5a37c-7e3b-4b49-ac58-2f33191cdf4e":(51.5471, -0.20469999999999999, 'gcpv5rfgw5us'), # Kilburn
"0ae6e482-e472-4028-b0e4-461c6ad1f28f":(51.445399999999999, -0.20660000000000001, 'gcpuem3e1veu'), # Southfields
"2669ea4a-b267-4a8b-b2fe-25276b670c53":(51.579500000000003, -0.3533, 'gcptrvy8re8q'), # WestHarrow
"4225000a-a83c-4db4-a906-fc32e828624b":(51.512300000000003, -0.039600000000000003, 'gcpvp1e0vk8n'), # Limehouse
"24fa220d-ca13-443d-9e73-8be49afd7db0":(51.556899999999999, -0.33660000000000001, 'gcpv23duswub'), # SudburyHill
"c4968339-846a-4814-b66f-6168c7f2398d":(51.509399999999999, -0.19670000000000001, 'gcpv590b081g'), # NottingHillGate
"873fa51e-dbc3-4407-9249-ea14e11f6f3e":(51.5642, -0.1065, 'gcpvmdfrnref'), # FinsburyPark
"364a49a3-65ad-4649-b9a0-af01a6b98920":(51.556600000000003, -0.0053, 'gcpvrcs4uwb4'), # Leyton
"a59bf99e-0fd1-4823-bc06-89a1bb21101a":(51.641199999999998, 0.055800000000000002, 'u10jc2bxu1rm'), # Loughton
"89c3fead-9427-4698-830a-df06f301690f":(51.517499999999998, -0.28870000000000001, 'gcpv16mz0y19'), # NorthEaling
"4ae3072a-10a8-4400-9ed2-127b6b5b976a":(51.6736, -0.60699999999999998, 'gcptfnvuxc5y'), # Amersham
"a67bc448-b939-4d1a-9d9a-840c17b6a496":(51.505099999999999, -0.020899999999999998, 'gcpvp80ybyxb'), # CanaryWharf
"a0665b47-6400-476e-b569-ec68a6a7fd76":(51.590400000000002, -0.1028, 'gcpvmxtpuedg'), # TurnpikeLane
"88392a34-b5cb-4c76-9e9d-7cfaf4fb944e":(51.494100000000003, -0.17380000000000001, 'gcpuun1qy5vr'), # SouthKensington
"f0a7d304-3e3f-46c8-978a-532bb28d3528":(51.5351, -0.19389999999999999, 'gcpv5tdv9yct'), # KilburnPark
"ff3b1cfb-1ea1-48af-a66d-8f1787f38598":(51.577500000000001, 0.028799999999999999, 'u10j2tkuxnfg'), # Wanstead
"5064cba1-ec2e-416f-9153-c0273385d528":(51.576500000000003, -0.39700000000000002, 'gcptqvnyvhrq'), # Eastcote
"ccffda41-ad3f-4c1f-b19d-f3dfe244ee96":(51.500999999999998, -0.12540000000000001, 'gcpuvpkxjfnz'), # Westminster
"2ea2857a-1d56-4fe9-a145-d6031fd660ab":(51.523000000000003, -0.1244, 'gcpvj5mrjr2d'), # RussellSquare
"1196b1e2-b958-4273-8c77-188a8ba4574c":(51.550699999999999, -0.31559999999999999, 'gcpv2bd0tfzx'), # SudburyTown
"3ac40716-c714-4851-8204-5960863c4205":(51.582999999999998, -0.0195, 'gcpvrw3uc85s'), # WalthamstowCentral
"84826d24-3c8b-4fc3-9ecf-ec01c9afb2e2":(51.597499999999997, -0.10970000000000001, 'gcpvt9015z1u'), # WoodGreen
"018de108-a518-4d48-acb8-7bc2085dc28c":(51.427500000000002, -0.16800000000000001, 'gcpus4jdvkf4'), # TootingBroadway
"25902e50-70bd-4fa6-964e-bf0154a396cd":(51.5075, -0.20599999999999999, 'gcpv529uzvgm'), # HollandPark
"b386afc8-3f11-4b5c-9a24-0543965ec173":(51.550400000000003, -0.16420000000000001, 'gcpvk22qvg5d'), # BelsizePark
"9e0c5708-2ac3-41d5-baab-56d5602b76b1":(51.524799999999999, -0.011900000000000001, 'gcpvpez3dwys'), # BromleyByBow
"58054f33-5750-4b25-9706-5028b2e96d0b":(51.495100000000001, -0.25469999999999998, 'gcpufnqs9n3u'), # TurnhamGreen
"2fca6749-5045-4d77-a665-72d70249a5ac":(51.4343, -0.19919999999999999, 'gcpue7qfw23w'), # WimbledonPark
"7bc2b747-1f8c-473f-a915-f1a476d1a1b3":(51.613199999999999, 0.092299999999999993, 'u10jd5ghwtzf'), # GrangeHill
"e1d3e10a-16cd-4e75-8d6e-d9d299fba0bd":(51.501100000000001, -0.30719999999999997, 'gcpucp2r9szh'), # SouthEaling
"7dbfb563-2a49-4ede-985d-5df9e4b91e93":(51.530799999999999, -0.12379999999999999, 'gcpvjhvuem25'), # KingsCrossStPancras
"4335b1ca-4202-4c76-ba79-379bbbb9e9f4":(51.510100000000001, -0.28820000000000001, 'gcpv13nhh6we'), # EalingCommon
"0d8038c4-2a18-42eb-95e9-b3eba2fbd129":(51.492400000000004, -0.1565, 'gcpuumyhcr14'), # SloaneSquare
"b8db5bac-3ac1-4bec-beda-69af98ebd222":(51.402200000000001, -0.1948, 'gcpu7t6psbdd'), # Morden
"9713cb92-a9d6-4eb8-9bf9-477860fd02ab":(51.514200000000002, -0.14940000000000001, 'gcpvh9g5ywzk'), # BondStreet
"ac425ff0-4c85-4dc2-875b-980714c379b8":(51.6004, -0.40920000000000001, 'gcptw9w40gwr'), # NorthwoodHills
"0999211f-c7f4-49ec-83ba-b249aefde30e":(51.475700000000003, -0.0402, 'gcpuz4fexmbx'), # NewCrossGate
"498adbf2-cab9-49d8-bff4-d35c8a0c9587":(51.509500000000003, 0.0276, 'u10j09h0e4u0'), # CustomHouse
"5799abba-8d65-47c8-b401-4c0976c68932":(51.468200000000003, -0.2089, 'gcpug1rzurbg'), # PutneyBridge
"ee36d2e5-cdb0-4667-b960-d5d395d1c86a":(51.543199999999999, -0.17380000000000001, 'gcpvhp1kyhvk'), # SwissCottage
"7f6a1eba-5fd4-43fb-9d86-b60ef44f03d4":(51.494300000000003, -0.10009999999999999, 'gcpuvwr05920'), # ElephantCastle
"b95f74c7-0ccc-4a04-ad46-ae255ed14689":(51.528700000000001, 0.0055999999999999999, 'u10j0hs06mzs'), # WestHam
"1750f083-8e55-4cb0-aaeb-70b14bed0158":(51.607100000000003, -0.12429999999999999, 'gcpvt4v3psen'), # BoundsGreen
"861ece04-d755-4e24-948c-1990014f49e2":(51.516500000000001, -0.13100000000000001, 'gcpvj42977xk'), # TottenhamCourtRoad
"70ab528d-f449-49ff-a03c-33bb16bf7ab7":(51.5122, -0.094, 'gcpvjce83dhd'), # MansionHouse
"f2afedc3-d882-413d-9483-f13605def449":(51.538499999999999, 0.1014, 'u10j4q3cdb9r'), # Upney
"39006e53-1040-4238-8886-b748bc899c23":(51.532200000000003, -0.10580000000000001, 'gcpvjt4uydmf'), # Angel
}

tubes_zone={
"d801bd7d-2875-45ac-a003-189e78831f5a":1.5, # Earl's Court
"8e9e65b9-127f-4442-ac1f-7d822a4462d9":4.0, # South Kenton
"3edaef16-d991-46dd-a8ec-ae1bde54cf79":5.0, # North Harrow
"9ab2674f-0593-4b86-8347-38109b2b23c5":7.0, # Croxley
"559326bd-543e-4933-9241-990094b932cb":2.0, # Barons Court
"2fca6749-5045-4d77-a665-72d70249a5ac":3.0, # Wimbledon Park
"ec42cf0b-0a85-4fb6-84fe-10a41a55ef9d":5.0, # Cockfosters
"feb73b3b-5801-43f4-af25-1cbd0a8e9d0e":6.0, # Ickenham
"6eb88e01-0501-4962-965e-0c53d6514d15":3.0, # Northfields
"cdea03f1-f838-4016-af3d-2c9251a3b143":2.0, # Brixton
"2c4f747a-1182-42d3-9455-a16923b20f75":1.0, # Marylebone
"7e9b3da7-2e31-4fdf-90a0-f98cd7b0c8ed":5.0, # High Barnet
"ffcae605-fbf5-4928-9efd-2a9b18caa418":2.0, # Bow Church
"72d3d976-272d-40ab-858f-7004cf92e4e4":2.0, # Mile End
"f806f577-3afb-4101-8dec-e8e3435a9cc5":2.0, # Heron Quays
"25a32e3a-f966-4a8f-be8e-8c44573676fe":1.0, # Great Portland Street
"516edae9-110a-4f51-a6d2-383c99210de2":2.5, # Deptford Bridge
"d6252a91-cd1c-4076-a6c8-463e8cc8b401":2.0, # Clapham North
"8d6deaea-002d-4bf5-beed-0c4a3f381eae":4.0, # Colindale
"f7a34731-3bda-46e5-a10f-a9a2c0c4162a":2.0, # Westbourne Park
"f97c9231-f8c8-4a52-be83-6a411f628f36":2.0, # Bow Road
"73b1cff3-b7ec-49c3-94da-a20d4c406f3b":2.0, # Kensington (Olympia)
"5799abba-8d65-47c8-b401-4c0976c68932":2.0, # Putney Bridge
"0421e847-920c-442f-bd16-cb36c83f9418":3.0, # King George V
"3f6eb6d1-feab-47b9-9504-dffe13e25c15":2.0, # Maida Vale
"52c525df-4eb6-4c1b-a4e4-55285e979dfa":2.0, # Warwick Avenue
"3347e7d7-69a0-405a-86e7-e8f3e620e5a7":2.0, # Westferry
"4e82f7b0-8d8c-455d-96c9-d13ebe0360c5":4.0, # Hounslow Central
"e789e9e2-2587-480f-b1d3-e0cf154564ca":6.0, # Northwood
"b90ea9e7-280b-479c-9610-2bdba2ce40d5":3.0, # Tottenham Hale
"643f9889-844f-44d4-980a-2f553a72784f":2.0, # Ladbroke Grove
"0457feec-f14f-4871-a3a5-97b69ddd89ea":5.0, # Becontree
"497d910f-1ed1-4e9d-9e45-6a71f126fccc":2.0, # Arsenal
"f77ebe4b-3779-4571-8f46-d6b9e451cd51":2.0, # East Acton
"889f0300-d383-42ce-aa8c-f79d72aed49d":4.0, # Woodside Park
"103fcba9-b810-4929-b013-5a50daa094ea":4.0, # Snaresbrook
"27545394-959e-4f16-84b1-da5a70cbea74":3.0, # London City Airport
"535a3a8e-f2a4-41b2-b01e-a951947725dc":3.0, # Gallions Reach
"37675294-b85e-4068-a8af-ebfa88c3f58f":5.0, # Barkingside
"82e21415-4000-41d4-b515-c6a64d610964":6.0, # Heathrow Terminals 1 & 2 & 3
"8503b2ae-5d51-44f0-9d23-2943532cf421":2.0, # Stockwell
"a5d9ae6f-e2a1-48a0-b671-05fc0c0376d7":1.0, # Tower Gateway
"ddb614a5-4443-4ce0-bfcd-fb13269cb902":5.0, # Oakwood
"ea1f0f57-6953-428a-82ae-e2ee619ab313":2.5, # Archway
"d6a59b2a-da2d-4860-9df7-ae60ffabec1d":1.0, # Goodge Street
"d22c6041-ea25-4dd9-9546-24afcb13f472":2.0, # Finchley Road
"07b7cfc5-10dd-4ff3-b46b-87a42a1d06b7":5.0, # Chigwell
"8eccd70b-662c-474d-b91d-5c88c03286d9":6.0, # Upminster Bridge
"9a4ec1fc-88c4-46f1-9eaf-8319d640049e":5.5, # Hatton Cross
"42a97bba-8dab-4932-8925-3cbfedd59265":4.0, # Osterley
"d25453cf-7eb9-44b7-af27-250820ef3ecd":6.0, # Ruislip
"42fdbaea-b1c5-4ded-b3f3-c36b67145035":1.0, # Bayswater
"f3c7ce45-e337-4d6a-8396-6f4a243b3bbe":3.0, # Hanger Lane
"9f80e0d8-84bb-4474-91b9-c02d59390ddc":2.0, # Poplar
"ccf87110-0f7d-4f00-b6f7-e6c1440b20db":2.0, # Kentish Town
"50303a28-12d5-4954-a2b3-d7f62bf80e10":1.0, # Warren Street
"0534ef61-db2a-416f-8f70-6d12bf356d95":2.0, # Shoreditch
"a2cf78d3-ee61-411e-b76d-aa7ec1c3c772":3.0, # Stonebridge Park
"8ec708cb-60c6-4dfa-a66c-2d7220dc7d83":1.0, # Embankment
"f15dee6f-5cd2-4ea1-8089-04955c76ff73":1.0, # Gloucester Road
"deed830e-f5d2-454a-b9d2-20685f742186":4.0, # Richmond
"0563b078-a7da-4c64-b1b6-a56816f2e979":4.0, # Perivale
"99c7d4d2-9ed6-489f-a71c-ea012316652a":3.0, # Royal Victoria
"24866134-afce-40c1-9341-e9284019249d":3.5, # South Wimbledon
"2ad77ab0-d4d5-414d-8d2c-fb7606669c08":3.0, # West Acton
"a9f90eac-8bda-4b0d-a62c-0abace2ecacf":3.0, # Beckton Park
"5feb6509-d2bc-4746-9f7e-d29225e96867":5.0, # Dagenham East
"815fd4eb-ead4-4ef9-b778-c4dea749ce82":2.0, # West Brompton
"cebe7422-4f0d-435d-9219-0292d950967f":1.0, # Picadilly Circus
"efb5766a-16a9-434f-8574-1b254726866d":1.0, # Baker Street
"7ca7ca09-f3e4-4212-8bca-ad03d410212c":1.0, # Edgware Road
"7889cae9-8416-4153-aad3-66ce2e110e2b":5.0, # Dagenham Heathway
"2a1c5044-4b2a-48b8-bc59-830c88cd7dca":3.0, # Seven Sisters
"c8e337d3-3b61-4a7f-b973-686df3f7502d":4.0, # Burnt Oak
"5d50982e-bd14-46bb-8de9-3761a2498794":3.0, # Dollis Hill
"c5638fe6-7996-41f9-b291-3f0fcc1caeec":3.0, # Blackhorse Road
"e8f8bb83-a6b8-4b37-90dd-ca34489bf9a3":3.0, # Balham
"c7dec458-047a-4c3b-b9af-46e3d491821d":2.0, # Hammersmith
"c570c2e2-1ce5-4542-8269-4dd40c07e8f3":2.5, # Hampstead
"016338cd-a632-4ef4-af89-42e6ce3d05a5":3.0, # Chiswick Park
"5f45b71a-7b9a-449f-bdee-cd6262795f51":3.0, # Golders Green
"23724ad1-b79e-4eb1-bc07-1c19dd5dfae9":2.0, # Parsons Green
"e65e7008-2695-4440-ab38-d7f81b7c6976":3.0, # Brent Cross
"8c78516a-b7e2-47eb-b9b5-117100c51bc2":1.0, # Paddington
"249dc44e-c5e8-4803-818a-ea54725c2a9d":2.0, # Stepney Green
"303e944e-a63e-4fd4-8dbe-8971d332b187":3.0, # Neasden
"6b549b5b-db83-4ffa-8ad3-baba502a92c6":2.0, # St. John's Wood
"03af5d7e-72c4-413f-a260-52c1fe5d022c":6.0, # Theydon Bois
"984d0bdd-193e-4a3b-b0b3-523edea3351e":4.0, # Southgate
"0baa84a4-8275-4f53-bc45-1476fdd5934f":2.0, # Goldhawk Road
"2f61ae2d-9ffc-4f3c-afa0-87e712df3cff":1.0, # Hyde Park Corner
"ef5e3a08-aee0-4b26-9686-c699bc8d91e6":1.0, # Covent Garden
"44438768-26b6-4414-bdbd-a30055d17ced":2.5, # Clapham South
"ef56ae4c-6447-4907-bf07-49a13385b951":4.0, # West Finchley
"c4968339-846a-4814-b66f-6168c7f2398d":1.5, # Notting Hill Gate
"74125284-3256-4527-a79d-0fddd3099af9":3.0, # Colliers Wood
"5c389d95-edf6-4554-adec-654d9a1a16f8":3.0, # Stratford
"2d04e04c-9ce2-4384-80e3-06243cb8d90b":6.0, # Hornchurch
"ed5d6e00-71b2-4df5-b7b2-05dfd3a9646c":4.0, # Arnos Grove
"25c555f4-f529-4149-823e-a04c4463d524":4.0, # Preston Road
"367c4cde-ffab-44df-a220-2b5c8ad298f4":3.0, # Royal Albert
"0d2de214-c96e-4842-a10f-5fe058a90d5b":6.0, # Elm Park
"e6fba115-a15d-4b53-8106-c0cd5f3c007f":4.0, # Mill Hill East
"d08e5786-189f-4451-916f-3c78d21e7f12":4.0, # Totteridge & Whetstone
"1e3d8c1e-1207-4030-9052-54ef0351dc62":2.5, # North Acton
"bfb41f10-53d9-44b4-8233-e5389ab3d583":2.0, # Shepherd's Bush
"6ad20349-f3f2-4290-8fb1-a0d4718c0d32":3.0, # Prince Regent
"010c886c-7201-4d49-81fc-f78cecdfa1b3":3.0, # Cyprus
"bbed2b3a-a6d0-41f0-93af-82c7bb0c9d8b":3.5, # East Ham
"6a4220d7-975d-4710-b069-2cf4dafc50e1":4.0, # Kingsbury
"9ea06909-e76d-407f-bbf1-06a4e63f454c":1.0, # Waterloo
"ac632aec-da92-4b75-a0ea-3ec9f7b60aa1":5.0, # Buckhurst Hill
"b39c2218-4bd9-4c5a-ac76-9483a64e58ec":1.0, # Cannon Street
"c94e833d-198e-4108-809b-ba38e1b5aba7":1.0, # Green Park
"4ac60516-0e6a-47b4-898c-4a4d127a8baa":3.0, # Park Royal
"5e7c3e79-ec13-4840-a499-5c1cef1a6b2f":1.0, # Charing Cross
"925a7fd8-5dc1-4620-a272-c4697d56172c":2.0, # Devons Road
"465b5b31-1237-4007-929b-5ffc63e19f79":4.0, # Newbury Park
"0767b416-a3da-4c1c-85bf-a3e59a2657d6":8.0, # Chorleywood
"25ef1cc7-866a-474e-acc7-44a0d7e6bca5":5.0, # Stanmore
"2f0faf9b-7406-4a32-8d18-927b7af16497":5.0, # Rayners Lane
"410e92c7-e6ac-4739-90dd-0834bb8b6e83":4.0, # Queensbury
"c2ee297b-72ee-4842-9660-fd2ed00d93a2":1.0, # Moorgate
"28b2ee7c-7a48-44d2-b4a9-499effac5775":5.0, # Ruislip Gardens
"dd74b4e2-6e32-48f9-91cf-aa23e5551688":6.0, # Ruislip Manor
"174ca94d-74d1-4606-9836-69aa275eb76e":5.0, # Pinner
"9aefa543-e3ff-4606-822b-b18794f4835d":4.0, # Boston Manor
"21ca86c8-b3a9-4040-b088-a2bba3e17c7d":1.0, # Tower Hill
"7e39a3bf-1054-422f-8909-c304cdd9efe9":3.0, # Wimbledon
"7f63805a-0964-46ad-a282-e7dc199b8685":1.0, # Euston Square
"e427de05-8e0e-4bb6-99f7-81835be4bee7":1.0, # St. Paul's
"97c4c33d-b5af-421b-aeef-b6ff98e3f1ca":5.0, # Hainault
"afdf2e47-c231-43be-bc77-5486ee74b1e5":2.0, # West Hampstead
"a4840c38-6656-41f9-92ff-2e0192e89cbe":1.0, # Oxford Circus
"ccffd31a-972c-40ba-903a-0e4ce0d971c6":2.0, # Caledonian Road
"b6f356a7-c2a4-4974-8c96-9519cbb7b839":5.0, # Hounslow West
"0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4":1.0, # Knightsbridge
"68f6f208-ef36-4859-9a85-6440e04d4c63":2.5, # Cutty Sark
"52433503-c65c-4089-82ff-4fd1d2780f84":2.0, # Oval
"8ca4bf88-8884-42eb-82b9-93c921dd3fc7":4.0, # Wembley Central
"d168eb7a-13eb-477b-b482-c69c3b4f5dbf":6.0, # Heathrow Terminal 4
"fa04941a-9c43-4392-b0a4-43e75b3a7e82":2.0, # Clapham Common
"a14eddb7-704e-4d4f-a0d6-5105d028f128":2.0, # Rotherhithe
"1f3ac254-b5cd-4317-b777-64f2432e4c7a":2.0, # Mornington Crescent
"e93bad5c-e2e2-45f2-940f-35583fc357dd":6.0, # Hillingdon
"e5c04fad-1dfc-46c3-8e27-74a8a6b1c63e":4.0, # Northwick Park
"3378c47b-ad46-4f7f-8670-0f5394af7cb2":5.0, # South Harrow
"8b275b50-6675-44dc-b9f8-154730faac04":2.0, # Mudchute
"e4f72828-a29a-4fdd-9bea-66fecdcfa250":2.0, # Fulham Broadway
"15351ff7-4b56-4882-a4d0-c4fd315ac9ef":2.0, # New Cross
"ae7c6e42-5090-4910-ad23-4ec083564183":6.0, # Debden
"29105288-d523-40cf-99a1-1ef83751460f":2.0, # West India Quay
"3e8ccac4-231c-4715-90fc-2025b412d64f":4.0, # Kenton
"a6d5538c-8cbf-44b1-b182-021be3c5c240":4.0, # Greenford
"e0b9f30a-2875-4559-a814-8d2297a2266d":2.5, # Elverson Road
"5177aa0d-3b92-4a1d-8356-3acfd80189be":3.0, # Highgate
"1629ea4a-7ee7-4f0c-bb70-231721b53632":1.0, # Holborn
"2e6585ea-25a5-4255-b312-fb33a99de249":5.0, # Harrow & Wealdston
"09bbbf1c-4b44-4300-9b7e-7da31c621afc":2.0, # Royal Oak
"9ac4ad96-5502-4948-a754-8558c1a59201":3.5, # Hendon Central
"9bd73108-ad7c-4b42-93c5-8a9d8cdd0acc":3.0, # Upton Park
"30d86bee-6a66-4f65-9b47-dd2a21e5a4f8":1.0, # Blackfriars
"662cbbc1-1d6b-48be-b85c-140fb3c2d832":2.0, # Bermondsey
"fa25d9e4-e9c9-44da-ae24-ea2d2235d9f6":5.0, # South Ruislip
"05da5b28-c40d-4860-92fb-6edf97f64650":2.5, # Greenwich
"6e66b0ff-cfc1-42b3-8029-3ecad13b44ae":2.0, # Stamford Brook
"43b5a37c-7e3b-4b49-ac58-2f33191cdf4e":2.0, # Kilburn
"2b655c4f-fbfb-4005-be97-38962e01a3ed":2.0, # Kensal Green
"78e36286-e750-49ee-927a-4e2bc3134788":1.0, # Liverpool Street
"c4806aae-06ae-4c0e-bbe6-f57c358976da":4.0, # Alperton
"2945184c-9a8d-4707-88a3-ec1bd35999b0":3.0, # Canning Town
"480e2906-9176-4d6a-b14b-3a966a5a4f3f":2.0, # Bethnal Green
"018de108-a518-4d48-acb8-7bc2085dc28c":3.0, # Tooting Broadway
"e6c6ede6-efc2-4040-9876-932552ce8646":1.0, # Lambeth North
"8450af6a-dbf3-4749-811b-6676552bed4b":2.0, # Highbury & Islington
"93bcf13e-165d-4294-8c8a-434ffbdf7374":5.0, # Canons Park
"9021de2d-4cfd-48b5-98c1-30e002cc8f3a":2.0, # South Quay
"cd0ae317-6fa5-4640-8971-50661b49c32f":3.0, # Tooting Bec
"38d6323c-663a-4f54-a58b-71cff0611d3d":3.0, # Willesden Junction
"7cb122f8-02b7-4ec6-8021-85a4ae14639e":4.0, # South Woodford
"32b3c7d2-f9a2-4d46-ba4f-1c5efb4ddeb3":3.0, # Gunnersbury
"6bf824ad-8d24-4258-9e8c-398b85dfb3c8":2.0, # Camden Town
"95b2c24a-fdf9-4cb0-b04e-4989909ffb72":4.0, # Barking
"aaf9fad0-0d23-4c27-927d-79a20d43d505":1.0, # Victoria
"36aa3d82-e972-4f11-81cc-b94415bf849f":4.0, # Hounslow East
"25902e50-70bd-4fa6-964e-bf0154a396cd":2.0, # Holland Park
"a67bcb93-f537-428c-813e-8a257ef98d98":1.0, # Queensway
"13a9b335-fdb9-44d3-bd3d-09fc64504063":8.0, # Watford
"79c291cf-6caa-469a-9b65-a6f2c8e3075c":2.5, # Willesden Green
"0b7a7fd5-81c8-4f40-b072-ed5bd74eed46":1.0, # Chancery Lane
"d0c57e5c-e1b4-4cee-82bc-35751a8b4625":5.0, # Roding Valley
"77ebcb72-e4e5-4459-94e6-e2364e29f8b9":2.5, # Pudding Mill Lane
"9a89a50c-34ad-498a-bc81-598d58cd0d1f":3.0, # West Silvertown
"4f6eda25-7e30-45ad-80f2-9db2453d262c":1.0, # St. James's Park
"d60522bc-d2a5-4d89-8b52-0d236844c6ec":2.0, # Latimer Road
"2b13ebcf-2181-451d-b4b0-e53c03ae77f1":1.0, # Farringdon
"320689c7-450e-44d5-a799-0022492c1944":2.0, # Blackwall
"3dfe2051-c378-4afa-9826-bc94298eb01a":1.0, # Regent's Park
"5c366dc4-6f3a-4ca2-8175-db52f2e5ad23":1.0, # Lancaster Gate
"37b045b7-e731-4056-87e8-ac5bf4e12c4a":3.5, # Leytonstone
"4a018a17-22e8-4539-b41d-910e4caf4b50":1.0, # Leicester Square
"2047f7d0-4ead-491d-93c9-c747a639d888":6.0, # West Ruislip
"8046cf9c-5d92-47ee-b034-32205ba494c6":1.5, # Vauxhall
"c1736808-6ac4-4c5c-8026-eafa83f98266":5.0, # Northolt
"0f98d1ce-4217-4f49-9e03-8402c32d2ff1":1.0, # Aldgate East
"251c1166-6118-4fa3-9426-3d7b32f800d8":6.0, # Upminster
"ce94a872-77e5-44b1-adab-6f4b70e5190c":7.0, # Rickmansworth
"a8e021f5-0edf-408e-8e48-18fbeed57019":10.0, # Chesham
"9df5a834-3827-4a46-9fb7-c26cce6837db":4.0, # Wembley Park
"72af4cfa-953e-4afb-bc6c-a4f61abebee0":4.0, # Redbridge
"ea843760-eb68-4308-9c84-7d5546516ce6":2.5, # North Greenwich
"130b0d90-588d-4aad-b3a2-9d98efaf99cd":5.0, # Harrow- on-the-Hill
"34d5c090-9d83-4f39-bc46-5e4538ae2218":1.0, # Euston
"87b81f55-4ebd-41fc-a8e1-0e701cb6bda1":5.0, # Fairlop
"af6b94cd-7efb-40a1-853e-e5c90607452d":6.0, # Uxbridge
"3c1ecf94-d8e2-4e5f-8f54-645e836b3294":1.0, # Barbican
"315f9ade-a54c-458c-a85f-f9962a5c6dc7":3.0, # Ealing Broadway
"61596bb4-4814-44a5-8607-a66b4cc14bd1":3.0, # Beckton
"78b8c3de-a903-484f-bf2c-6ce07bbdd28e":1.0, # Edgware Road
"59f2c6ed-8120-4586-ab91-58d51304d468":2.0, # Holloway Road
"64981d6a-1322-49b2-aa95-a05d6b43423e":1.0, # Bank
"611cdae4-916d-43c3-aa1c-bcba08d75098":2.0, # Surrey Quays
"2599c24c-28ac-460b-9c99-ccfcd68bff37":2.0, # Crossharbour & London Arena
"498adbf2-cab9-49d8-bff4-d35c8a0c9587":3.0, # Custom House
"887a0d89-9d8b-4023-a901-86792db421ff":4.0, # Finchley Central
"742e97bc-26b6-4294-b111-b1301e8760d8":2.0, # Whitechapel
"b5ef4219-5d51-49d4-8bd5-2fa1fb9e867c":1.0, # Pimlico
"767e63fc-be79-449a-a461-670f3888eb56":4.0, # North Wembley
"b8f9c445-c7c7-4541-a396-a3d66ea350c4":2.0, # Queens Park
"57d3a7a7-5e23-447e-bb6a-cbbd12a9d635":3.0, # East Finchley
"f30b89ed-552a-40c9-afb5-ce64fa41ff2d":1.0, # Borough
"f0a2bae9-93f2-4acc-af91-602c879cd8fd":3.0, # Acton Town
"5af0f8f0-6783-4c15-a292-45f151ede2d2":4.0, # Woodford
"48a452d3-6699-42fc-aa0a-d827185ecdc2":2.0, # Shadwell
"a7c40a0b-bb1a-46d9-8442-e7f45b8f7743":3.0, # Harlesden
"654971d2-8531-49f5-9e0c-8ad88beee31b":9.0, # Chalfont & Latimer
"2fd3ee8f-d2df-4e94-86da-6d1cd67f1d4c":2.5, # Manor House
"80031d6b-6327-411f-b98a-0f8124c25d86":3.5, # Kew Gardens
"ff596b51-d851-4cdb-b6ff-3f143a90c862":2.0, # Kennington
"0d3810fe-24fb-40d0-92c5-804a15144341":4.0, # Gants Hill
"01f067eb-fe23-44fb-b697-cb45fb258e71":2.0, # Wapping
"ec56b880-1907-449f-b9d9-3cb93a2d0b70":1.0, # Aldgate
"c0eed10a-cfc3-417d-b06d-435f53af2d41":2.0, # Shepherd's Bush
"ed39a802-cf23-42a2-8006-cf2ab8a54048":1.0, # High Street Kensington
"873fa51e-dbc3-4407-9249-ea14e11f6f3e":2.0, # Finsbury Park
"b26ff8de-7cfe-4143-8413-1d9459ef877f":2.5, # East India
"c95d8299-8911-4a67-af90-f945b8d990bb":1.0, # Temple
"bef7f260-c351-412c-bec0-b05d82367f88":2.5, # Lewisham
"437b3160-3e03-4694-aa4d-9349e8c419fa":2.0, # Chalk Farm
"422f8cfc-311d-4325-b891-278bb9f52621":2.0, # Canada Water
"b194c301-5369-4cd9-ae07-8e454d4ebe69":1.0, # Southwark
"46d479d0-c2c8-4893-bf40-41721a7be205":2.0, # Island Gardens
"f0395015-50a0-4933-bb40-6bb4d56ddffb":3.0, # Plaistow
"b1033dcd-c1e0-4a6b-97d9-b4b9fe6bcf6e":2.0, # Ravenscourt Park
"8823ac5f-5680-435b-a049-5ee40e86817e":2.0, # All Saints
"ad4d2a18-aca2-4020-a663-80927dd2f803":6.5, # Moor Park
"5c249c9c-696d-4cbd-a8a3-c87f7029566e":1.0, # London Bridge
"391b032a-4c3c-48b7-8be2-0ccbea92b7c1":6.0, # Epping
"6ac25ebb-40be-4de4-bb86-c7db73ae823d":1.0, # Marble Arch
"0ae6e482-e472-4028-b0e4-461c6ad1f28f":3.0, # Southfields
"2669ea4a-b267-4a8b-b2fe-25276b670c53":5.0, # West Harrow
"4225000a-a83c-4db4-a906-fc32e828624b":2.0, # Limehouse
"093bea1f-2abe-41bb-b0ca-1716079e6104":3.0, # Pontoon Dock
"0a9a00c8-2f22-4c01-bc55-8402eb72e5b3":2.0, # West Kensington
"e5ba2584-8519-4759-931d-056d31844a44":2.0, # White City
"364a49a3-65ad-4649-b9a0-af01a6b98920":3.0, # Leyton
"a59bf99e-0fd1-4823-bc06-89a1bb21101a":6.0, # Loughton
"89c3fead-9427-4698-830a-df06f301690f":3.0, # North Ealing
"4ae3072a-10a8-4400-9ed2-127b6b5b976a":10.0, # Amersham
"a67bc448-b939-4d1a-9d9a-840c17b6a496":2.0, # Canary Wharf
"a0665b47-6400-476e-b569-ec68a6a7fd76":3.0, # Turnpike Lane
"94660c36-6039-4805-a6cb-9221905ce759":5.0, # Edgware
"f0a7d304-3e3f-46c8-978a-532bb28d3528":2.0, # Kilburn Park
"ff3b1cfb-1ea1-48af-a66d-8f1787f38598":4.0, # Wanstead
"5064cba1-ec2e-416f-9153-c0273385d528":5.0, # Eastcote
"ccffda41-ad3f-4c1f-b19d-f3dfe244ee96":1.0, # Westminster
"2ea2857a-1d56-4fe9-a145-d6031fd660ab":1.0, # Russell Square
"1196b1e2-b958-4273-8c77-188a8ba4574c":4.0, # Sudbury Town
"3ac40716-c714-4851-8204-5960863c4205":3.0, # Walthamstow Central
"84826d24-3c8b-4fc3-9ecf-ec01c9afb2e2":3.0, # Wood Green
"88392a34-b5cb-4c76-9e9d-7cfaf4fb944e":1.0, # South Kensington
"b09cb073-2656-4079-b8e6-757300b367bd":1.0, # Old Street
"b386afc8-3f11-4b5c-9a24-0543965ec173":2.0, # Belsize Park
"9e0c5708-2ac3-41d5-baab-56d5602b76b1":2.5, # Bromley-By-Bow
"58054f33-5750-4b25-9706-5028b2e96d0b":2.5, # Turnham Green
"c9cd51e3-5fff-4ce7-9502-907fe8a28c1e":2.0, # Tufnell Park
"7bc2b747-1f8c-473f-a915-f1a476d1a1b3":5.0, # Grange Hill
"e1d3e10a-16cd-4e75-8d6e-d9d299fba0bd":3.0, # South Ealing
"7dbfb563-2a49-4ede-985d-5df9e4b91e93":1.0, # King's Cross St. Pancras
"4335b1ca-4202-4c76-ba79-379bbbb9e9f4":3.0, # Ealing Common
"70ab528d-f449-49ff-a03c-33bb16bf7ab7":1.0, # Mansion House
"b8db5bac-3ac1-4bec-beda-69af98ebd222":4.0, # Morden
"0d8038c4-2a18-42eb-95e9-b3eba2fbd129":1.0, # Sloane Square
"9713cb92-a9d6-4eb8-9bf9-477860fd02ab":1.0, # Bond Street
"ac425ff0-4c85-4dc2-875b-980714c379b8":6.0, # Northwood Hills
"0999211f-c7f4-49ec-83ba-b249aefde30e":2.0, # New Cross Gate
"36fac8a5-abd7-4f1f-9cd6-e6e9a5843b8a":2.5, # East Putney
"24fa220d-ca13-443d-9e73-8be49afd7db0":4.0, # Sudbury Hill
"ee36d2e5-cdb0-4667-b960-d5d395d1c86a":2.0, # Swiss Cottage
"7f6a1eba-5fd4-43fb-9d86-b60ef44f03d4":1.5, # Elephant & Castle
"b95f74c7-0ccc-4a04-ad46-ae255ed14689":3.0, # West Ham
"1750f083-8e55-4cb0-aaeb-70b14bed0158":3.5, # Bounds Green
"861ece04-d755-4e24-948c-1990014f49e2":1.0, # Tottenham Court Road
"815ea4ed-f5ee-4f5c-b3ab-3731a03eeed5":1.0, # Monument
"f2afedc3-d882-413d-9483-f13605def449":4.0, # Upney
"39006e53-1040-4238-8886-b748bc899c23":1.0, # Angel
}

tube_stations_slugs=datautils.create_slug_index(entities)

def get_tube_station_UUID(slug):
	return tube_stations_slugs.get(slug)

import re
RE_PARENTHESIS=re.compile("(\(.+\))")		
RE_STATION=re.compile("(station)",re.IGNORECASE)		

tube_stations_searches=datautils.create_search_index(entities)

def search_tube_station_UUID(search):
	without_specific=RE_PARENTHESIS.sub("", search)
	without_specific=RE_STATION.sub("", without_specific)
	s=datautils.searchify(without_specific)
	return tube_stations_searches.get(s)

def search_tube_station_UUID_list(search_list):
	if not search_list:
		return None
	r = list(search_tube_station_UUID(s) for s in search_list)
	r=filter(None,r)
	return r


def nearest_tube_stations(geo):
	r=datautils.search_geo_nearest_many(geo_entities,geo,4)
	return r

def get_data_as_dict(uuid):
	mylist = [
	datautils.get_entity_as_dict(entities.get(uuid)),
	datautils.get_entity_geo_as_dict(entities_geo.get(uuid)),
	]
	r = {}
	for item in mylist:
		if item:
			r.update(item)			
	a = {
	"zone":tubes_zone.get(uuid),
	}
	r.update(a)
	return {"tube": r}

import tubelines
def get_data_as_dicts(uuids,latlon):
	if not uuids:
		return None
	r =[]
	for uuid in uuids:
		mydict=get_data_as_dict(uuid)
		if latlon:
			distance=datautils.get_distance_as_dict(latlon,(entities_geo[uuid][0],entities_geo[uuid][1]))
			mydict["distance"]=distance
			
		tlines=tubelines.get_lines_for_station_as_dict(uuid)
		mydict["tubeline_list"]=tlines
		r.append(mydict)
	return r		
