#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Olivier Huin on 2010-02-06.
Copyright (c) 2010 Flarebyte.com Limited. All rights reserved.
"""

import sys, os, uuid, string,re
import geohash


def main():
	pass


if __name__ == '__main__':
	main()

def slugify(name):
	r = re.sub("[^A-Za-z0-9]","",name)
	return r

def clean_name(name):
	r = string.replace(name,'"','')	
	return r

def clean_display_name(display_name,name):
	if (display_name=="NULL"):
		return clean_name(name)
	else:
		return clean_name(display_name)

def write_to_transport(identities,all_lines):
	fout = open ("transport_out.py","w")
	fout.write(str(identities))
	fout.write(str(all_lines))
	fout.close()
	
	
def create_tube_stations():
	identities = {}
	id_uuid = {}
	all_lines = {}
	stations = open ("stations_wikipedia.csv")
	transport_lines = open("lines_wikipedia.csv")
	lines=stations.readlines()
	tlines=transport_lines.readlines()
	for line in lines:
		if (line.startswith('"id"')):
			continue
		if (line.count(",")==7):
			(int_id,latitude,longitude,name,display_name,zone,total_lines,rail)=line.split(",")
		else:
			print line
		uuid_station=str(uuid.uuid4())
		short_uuids=uuid_station.split("-")
		identities[uuid_station] = (slugify(name),[clean_display_name(display_name,name)],short_uuids[1],float(latitude),float(longitude),geohash.encode(float(latitude),float(longitude)),float(zone))
		id_uuid[int_id]=uuid_station
	for triple in tlines:
		if (triple.count(",")==2):
			(station1,station2,zline)=triple.split(",")
		else:
			print triple
		if (not all_lines.has_key(int(zline))):
			all_lines[int(zline)]=[id_uuid[station1],id_uuid[station2]]
		else:
			if not id_uuid[station1] in all_lines[int(zline)]:
				all_lines[int(zline)].append(id_uuid[station1])
							
			if not id_uuid[station2] in all_lines[int(zline)]:
				all_lines[int(zline)].append(id_uuid[station2])
		
	write_to_transport(identities,all_lines)
	stations.close()
	transport_lines.close()

def organize_stations():
	tube_stations= {
	'd801bd7d-2875-45ac-a003-189e78831f5a': ('EarlsCourt', ["Earl's Court"], '2875', 51.491999999999997, -0.1973, 'gcpugtb6dsd2', 1.5),
	 '36fac8a5-abd7-4f1f-9cd6-e6e9a5843b8a': ('EastPutney', ['East Putney'], 'abd7', 51.458599999999997, -0.2112, 'gcpuepy0ndmc', 2.5),
	 '3edaef16-d991-46dd-a8ec-ae1bde54cf79': ('NorthHarrow', ['North Harrow'], 'd991', 51.584600000000002, -0.36259999999999998, 'gcptrwxynf3u', 5.0),
	 '9ab2674f-0593-4b86-8347-38109b2b23c5': ('Croxley', ['Croxley'], '0593', 51.646999999999998, -0.44119999999999998, 'gcptvfn9x697', 7.0),
	 '48a452d3-6699-42fc-aa0a-d827185ecdc2': ('Shadwell', ['Shadwell'], '6699', 51.511699999999998, -0.056000000000000001, 'gcpvn9rjrhg7', 2.0),
	 'c1736808-6ac4-4c5c-8026-eafa83f98266': ('Northolt', ['Northolt'], '6ac4', 51.548299999999998, -0.36870000000000003, 'gcptr85d8et7', 5.0),
	 'feb73b3b-5801-43f4-af25-1cbd0a8e9d0e': ('Ickenham', ['Ickenham'], '5801', 51.561900000000001, -0.44209999999999999, 'gcptmfw1f6f6', 6.0),
	 '6eb88e01-0501-4962-965e-0c53d6514d15': ('Northfields', ['Northfields'], '0501', 51.499499999999998, -0.31419999999999998, 'gcpubz5nqde7', 3.0),
	 'cdea03f1-f838-4016-af3d-2c9251a3b143': ('Brixton', ['Brixton'], 'f838', 51.462699999999998, -0.1145, 'gcpuv2kxgywe', 2.0),
	 '2c4f747a-1182-42d3-9455-a16923b20f75': ('Marylebone', ['Marylebone'], '1182', 51.522500000000001, -0.16309999999999999, 'gcpvh73hr6pu', 1.0),
	 'ffcae605-fbf5-4928-9efd-2a9b18caa418': ('BowChurch', ['Bow Church'], 'fbf5', 51.527299999999997, -0.020799999999999999, 'gcpvps2b72fm', 2.0),
	 'ac632aec-da92-4b75-a0ea-3ec9f7b60aa1': ('BuckhurstHill', ['Buckhurst Hill'], 'da92', 51.626600000000003, 0.047100000000000003, 'u10j9n669xb2', 5.0),
	 '72d3d976-272d-40ab-858f-7004cf92e4e4': ('MileEnd', ['Mile End'], '272d', 51.524900000000002, -0.0332, 'gcpvp5zf63s2', 2.0),
	 'f806f577-3afb-4101-8dec-e8e3435a9cc5': ('HeronQuays', ['Heron Quays'], '3afb', 51.503300000000003, -0.021499999999999998, 'gcpuzxbk7nbr', 2.0),
	 '25a32e3a-f966-4a8f-be8e-8c44573676fe': ('GreatPortlandStreet', ['Great Portland Street'], 'f966', 51.523800000000001, -0.1439, 'gcpvhex5yukq', 1.0),
	 '516edae9-110a-4f51-a6d2-383c99210de2': ('DeptfordBridge', ['Deptford Bridge'], '110a', 51.473999999999997, -0.021600000000000001, 'gcpuzd83b9jf', 2.5),
	 'd6252a91-cd1c-4076-a6c8-463e8cc8b401': ('ClaphamNorth', ['Clapham North'], 'cd1c', 51.4649, -0.12989999999999999, 'gcpuv0ckv0ew', 2.0),
	 '8d6deaea-002d-4bf5-beed-0c4a3f381eae': ('Colindale', ['Colindale'], '002d', 51.595500000000001, -0.25019999999999998, 'gcpvd29v9fm6', 4.0),
	 '889f0300-d383-42ce-aa8c-f79d72aed49d': ('WoodsidePark', ['Woodside Park'], 'd383', 51.617899999999999, -0.18559999999999999, 'gcpveubb51yx', 4.0),
	 'f7a34731-3bda-46e5-a10f-a9a2c0c4162a': ('WestbournePark', ['Westbourne Park'], '3bda', 51.521000000000001, -0.2011, 'gcpv57jed48b', 2.0),
	 'f97c9231-f8c8-4a52-be83-6a411f628f36': ('BowRoad', ['Bow Road'], 'f8c8', 51.526899999999998, -0.0247, 'gcpvpknjbqq7', 2.0),
	 '73b1cff3-b7ec-49c3-94da-a20d4c406f3b': ('KensingtonOlympia', ['Kensington (Olympia)'], 'b7ec', 51.4983, -0.21060000000000001, 'gcpugnyxkdvm', 2.0),
	 '5799abba-8d65-47c8-b401-4c0976c68932': ('PutneyBridge', ['Putney Bridge'], '8d65', 51.468200000000003, -0.2089, 'gcpug1rzurbg', 2.0),
	 '0421e847-920c-442f-bd16-cb36c83f9418': ('KingGeorgeV', ['King George V'], '920c', 51.502000000000002, 0.062700000000000006, 'u10hcrtsvh8s', 3.0),
	 '3f6eb6d1-feab-47b9-9504-dffe13e25c15': ('MaidaVale', ['Maida Vale'], 'feab', 51.530000000000001, -0.18540000000000001, 'gcpv5ubbpb5x', 2.0),
	 '27545394-959e-4f16-84b1-da5a70cbea74': ('LondonCityAirport', ['London City Airport'], '959e', 51.503700000000002, 0.048800000000000003, 'u10hcpgwc1ec', 3.0),
	 '52c525df-4eb6-4c1b-a4e4-55285e979dfa': ('WarwickAvenue', ['Warwick Avenue'], '4eb6', 51.523499999999999, -0.1835, 'gcpv5gd6hhs3', 2.0),
	 '3347e7d7-69a0-405a-86e7-e8f3e620e5a7': ('Westferry', ['Westferry'], '69a0', 51.509700000000002, -0.026499999999999999, 'gcpvp3h9y801', 2.0),
	 '4e82f7b0-8d8c-455d-96c9-d13ebe0360c5': ('HounslowCentral', ['Hounslow Central'], '8d8c', 51.471299999999999, -0.36649999999999999, 'gcpszdj45cvb', 4.0),
	 'ddb614a5-4443-4ce0-bfcd-fb13269cb902': ('Oakwood', ['Oakwood'], '4443', 51.647599999999997, -0.1318, 'gcpvv40j0f6y', 5.0),
	 'e789e9e2-2587-480f-b1d3-e0cf154564ca': ('Northwood', ['Northwood'], '2587', 51.6111, -0.42399999999999999, 'gcptw7e22n6e', 6.0),
	 'b90ea9e7-280b-479c-9610-2bdba2ce40d5': ('TottenhamHale', ['Tottenham Hale'], '280b', 51.588200000000001, -0.059400000000000001, 'gcpvqxkepckp', 3.0),
	 '643f9889-844f-44d4-980a-2f553a72784f': ('LadbrokeGrove', ['Ladbroke Grove'], '844f', 51.517200000000003, -0.2107, 'gcpv54qt6q4s', 2.0),
	 '0457feec-f14f-4871-a3a5-97b69ddd89ea': ('Becontree', ['Becontree'], 'f14f', 51.540300000000002, 0.127, 'u10j4yskp261', 5.0),
	 'afdf2e47-c231-43be-bc77-5486ee74b1e5': ('WestHampstead', ['West Hampstead'], 'c231', 51.546900000000001, -0.19059999999999999, 'gcpv5xv4qww7', 2.0),
	 'f77ebe4b-3779-4571-8f46-d6b9e451cd51': ('EastActon', ['East Acton'], '3779', 51.516800000000003, -0.24740000000000001, 'gcpv467g55t4', 2.0),
	 '50303a28-12d5-4954-a2b3-d7f62bf80e10': ('WarrenStreet', ['Warren Street'], '12d5', 51.524700000000003, -0.1384, 'gcpvhgg1ph1r', 1.0),
	 'e6fba115-a15d-4b53-8106-c0cd5f3c007f': ('MillHillEast', ['Mill Hill East'], 'a15d', 51.608199999999997, -0.21029999999999999, 'gcpve4yze9ub', 4.0),
	 '103fcba9-b810-4929-b013-5a50daa094ea': ('Snaresbrook', ['Snaresbrook'], 'b810', 51.580800000000004, 0.021600000000000001, 'u10j2mzxzq41', 4.0),
	 '422f8cfc-311d-4325-b891-278bb9f52621': ('CanadaWater', ['Canada Water'], '311d', 51.498199999999997, -0.050200000000000002, 'gcpuyygqy220', 2.0),
	 '535a3a8e-f2a4-41b2-b01e-a951947725dc': ('GallionsReach', ['Gallions Reach'], 'f2a4', 51.509599999999999, 0.071599999999999997, 'u10j19h1hmku', 3.0),
	 '37675294-b85e-4068-a8af-ebfa88c3f58f': ('Barkingside', ['Barkingside'], 'b85e', 51.585599999999999, 0.088700000000000001, 'u10j6nbefugd', 5.0),
	 '82e21415-4000-41d4-b515-c6a64d610964': ('HeathrowTerminals123', ['Heathrow Terminals 1 & 2 & 3'], '4000', 51.471299999999999, -0.45240000000000002, 'gcpsvdnd43f0', 6.0),
	 '8503b2ae-5d51-44f0-9d23-2943532cf421': ('Stockwell', ['Stockwell'], '5d51', 51.472299999999997, -0.123, 'gcpuv4nrvuht', 2.0),
	 'a5d9ae6f-e2a1-48a0-b671-05fc0c0376d7': ('TowerGateway', ['Tower Gateway'], 'e2a1', 51.510599999999997, -0.074300000000000005, 'gcpvn31yuxvc', 1.0),
	 '2fca6749-5045-4d77-a665-72d70249a5ac': ('WimbledonPark', ['Wimbledon Park'], '5045', 51.4343, -0.19919999999999999, 'gcpue7qfw23w', 3.0),
	 'ea1f0f57-6953-428a-82ae-e2ee619ab313': ('Archway', ['Archway'], '6953', 51.565300000000001, -0.1353, 'gcpvkgjmxk95', 2.5),
	 'd6a59b2a-da2d-4860-9df7-ae60ffabec1d': ('GoodgeStreet', ['Goodge Street'], 'da2d', 51.520499999999998, -0.13469999999999999, 'gcpvhgjbtm23', 1.0),
	 'd22c6041-ea25-4dd9-9546-24afcb13f472': ('FinchleyRoad', ['Finchley Road'], 'ea25', 51.547199999999997, -0.18029999999999999, 'gcpv5zusnww9', 2.0),
	 '391b032a-4c3c-48b7-8be2-0ccbea92b7c1': ('Epping', ['Epping'], '4c3c', 51.6937, 0.1139, 'u10n4ddcwh1g', 6.0),
	 '72af4cfa-953e-4afb-bc6c-a4f61abebee0': ('Redbridge', ['Redbridge'], '953e', 51.576300000000003, 0.045400000000000003, 'u10j3j1j9zht', 4.0),
	 '9a4ec1fc-88c4-46f1-9eaf-8319d640049e': ('HattonCross', ['Hatton Cross'], '88c4', 51.466900000000003, -0.42270000000000002, 'gcpsy3k0qms1', 5.5),
	 '42a97bba-8dab-4932-8925-3cbfedd59265': ('Osterley', ['Osterley'], '8dab', 51.481299999999997, -0.35220000000000001, 'gcpszgzs31us', 4.0),
	 'd25453cf-7eb9-44b7-af27-250820ef3ecd': ('Ruislip', ['Ruislip'], '7eb9', 51.5715, -0.42130000000000001, 'gcptqkm1ybru', 6.0),
	 '42fdbaea-b1c5-4ded-b3f3-c36b67145035': ('Bayswater', ['Bayswater'], 'b1c5', 51.512099999999997, -0.18790000000000001, 'gcpv59rptx7t', 1.0),
	 'f3c7ce45-e337-4d6a-8396-6f4a243b3bbe': ('HangerLane', ['Hanger Lane'], 'e337', 51.530200000000001, -0.29330000000000001, 'gcpv1kf3jte8', 3.0),
	 'b194c301-5369-4cd9-ae07-8e454d4ebe69': ('Southwark', ['Southwark'], '5369', 51.503999999999998, -0.1052, 'gcpvj852s9mp', 1.0),
	 '0ae6e482-e472-4028-b0e4-461c6ad1f28f': ('Southfields', ['Southfields'], 'e472', 51.445399999999999, -0.20660000000000001, 'gcpuem3e1veu', 3.0),
	 '9f80e0d8-84bb-4474-91b9-c02d59390ddc': ('Poplar', ['Poplar'], '84bb', 51.5077, -0.017299999999999999, 'gcpvp8eqhghn', 2.0),
	 'ccf87110-0f7d-4f00-b6f7-e6c1440b20db': ('KentishTown', ['Kentish Town'], '0f7d', 51.550699999999999, -0.14019999999999999, 'gcpvkb9bt4gr', 2.0),
	 '59f2c6ed-8120-4586-ab91-58d51304d468': ('HollowayRoad', ['Holloway Road'], '8120', 51.552599999999998, -0.1132, 'gcpvm2vedjpv', 2.0),
	 '0534ef61-db2a-416f-8f70-6d12bf356d95': ('Shoreditch', ['Shoreditch'], 'db2a', 51.5227, -0.070800000000000002, 'gcpvn7kmqprt', 2.0),
	 'a2cf78d3-ee61-411e-b76d-aa7ec1c3c772': ('StonebridgePark', ['Stonebridge Park'], 'ee61', 51.543900000000001, -0.27589999999999998, 'gcpv1xr0gp6h', 3.0),
	 'ce94a872-77e5-44b1-adab-6f4b70e5190c': ('Rickmansworth', ['Rickmansworth'], '77e5', 51.6404, -0.4733, 'gcptv0z75k3b', 7.0),
	 'f15dee6f-5cd2-4ea1-8089-04955c76ff73': ('GloucesterRoad', ['Gloucester Road'], '5cd2', 51.494500000000002, -0.18290000000000001, 'gcpugy6c4nec', 1.0),
	 'deed830e-f5d2-454a-b9d2-20685f742186': ('Richmond', ['Richmond'], 'f5d2', 51.463299999999997, -0.30130000000000001, 'gcpuc0se7nqq', 4.0),
	 '0563b078-a7da-4c64-b1b6-a56816f2e979': ('Perivale', ['Perivale'], 'a7da', 51.5366, -0.32319999999999999, 'gcpv0tuwkys9', 4.0),
	 '99c7d4d2-9ed6-489f-a71c-ea012316652a': ('RoyalVictoria', ['Royal Victoria'], '9ed6', 51.509099999999997, 0.018100000000000002, 'u10j02vnmb0m', 3.0),
	 '8c78516a-b7e2-47eb-b9b5-117100c51bc2': ('Paddington', ['Paddington'], 'b7e2', 51.5154, -0.17549999999999999, 'gcpvh404yw9d', 1.0),
	 '2ad77ab0-d4d5-414d-8d2c-fb7606669c08': ('WestActon', ['West Acton'], 'd4d5', 51.518000000000001, -0.28089999999999998, 'gcpv1de6ne3b', 3.0),
	 '6ad20349-f3f2-4290-8fb1-a0d4718c0d32': ('PrinceRegent', ['Prince Regent'], 'f3f2', 51.509300000000003, 0.033599999999999998, 'u10j0bbrqvmy', 3.0),
	 '5feb6509-d2bc-4746-9f7e-d29225e96867': ('DagenhamEast', ['Dagenham East'], 'd2bc', 51.5443, 0.16550000000000001, 'u10j5z2e23vw', 5.0),
	 '815fd4eb-ead4-4ef9-b778-c4dea749ce82': ('WestBrompton', ['West Brompton'], 'ead4', 51.487200000000001, -0.1953, 'gcpugscy9jtz', 2.0),
	 'cebe7422-4f0d-435d-9219-0292d950967f': ('PicadillyCircus', ['Picadilly Circus'], '4f0d', 51.509799999999998, -0.13420000000000001, 'gcpvhcn62ftj', 1.0),
	 'efb5766a-16a9-434f-8574-1b254726866d': ('BakerStreet', ['Baker Street'], '16a9', 51.522599999999997, -0.15709999999999999, 'gcpvh7msgkc8', 1.0),
	 '7ca7ca09-f3e4-4212-8bca-ad03d410212c': ('EdgwareRoadC', ['Edgware Road'], 'f3e4', 51.520299999999999, -0.17000000000000001, 'gcpvh4upw8nb', 1.0),
	 '010c886c-7201-4d49-81fc-f78cecdfa1b3': ('Cyprus', ['Cyprus'], '7201', 51.508499999999998, 0.064000000000000001, 'u10j12ydg23f', 3.0),
	 '2a1c5044-4b2a-48b8-bc59-830c88cd7dca': ('SevenSisters', ['Seven Sisters'], '4b2a', 51.5822, -0.074899999999999994, 'gcpvqq32nen8', 3.0),
	 '6b549b5b-db83-4ffa-8ad3-baba502a92c6': ('StJohnsWood', ["St. John's Wood"], 'db83', 51.534700000000001, -0.17399999999999999, 'gcpvhj973s25', 2.0),
	 '5d50982e-bd14-46bb-8de9-3761a2498794': ('DollisHill', ['Dollis Hill'], 'bd14', 51.552, -0.2387, 'gcpv68f0jvk6', 3.0),
	 'c5638fe6-7996-41f9-b291-3f0fcc1caeec': ('BlackhorseRoad', ['Blackhorse Road'], '7996', 51.5867, -0.041700000000000001, 'gcpvrp1dk3f5', 3.0),
	 'e8f8bb83-a6b8-4b37-90dd-ca34489bf9a3': ('Balham', ['Balham'], 'a6b8', 51.443100000000001, -0.1525, 'gcpussbvy2zu', 3.0),
	 'c7dec458-047a-4c3b-b9af-46e3d491821d': ('Hammersmith', ['Hammersmith'], '047a', 51.493600000000001, -0.22509999999999999, 'gcpufyh5fyc2', 2.0),
	 'c570c2e2-1ce5-4542-8269-4dd40c07e8f3': ('Hampstead', ['Hampstead'], '1ce5', 51.556800000000003, -0.17799999999999999, 'gcpv7cwkhk1e', 2.5),
	 '016338cd-a632-4ef4-af89-42e6ce3d05a5': ('ChiswickPark', ['Chiswick Park'], 'a632', 51.494599999999998, -0.26779999999999998, 'gcpucykczc1y', 3.0),
	 '23724ad1-b79e-4eb1-bc07-1c19dd5dfae9': ('ParsonsGreen', ['Parsons Green'], 'b79e', 51.475299999999997, -0.2011, 'gcpug6v9652v', 2.0),
	 'ae7c6e42-5090-4910-ad23-4ec083564183': ('Debden', ['Debden'], '5090', 51.645499999999998, 0.083799999999999999, 'u10jccv0bdvz', 6.0),
	 'e65e7008-2695-4440-ab38-d7f81b7c6976': ('BrentCross', ['Brent Cross'], '2695', 51.576599999999999, -0.21360000000000001, 'gcpv7jhrqz07', 3.0),
	 '24866134-afce-40c1-9341-e9284019249d': ('SouthWimbledon', ['South Wimbledon'], 'afce', 51.415399999999998, -0.19189999999999999, 'gcpu7xuk2mhz', 3.5),
	 'b09cb073-2656-4079-b8e6-757300b367bd': ('OldStreet', ['Old Street'], '2656', 51.526299999999999, -0.087300000000000003, 'gcpvnh06my2r', 1.0),
	 '303e944e-a63e-4fd4-8dbe-8971d332b187': ('Neasden', ['Neasden'], 'a63e', 51.554200000000002, -0.25030000000000002, 'gcpv631szx6v', 3.0),
	 '7e39a3bf-1054-422f-8909-c304cdd9efe9': ('Wimbledon', ['Wimbledon'], '1054', 51.421399999999998, -0.2064, 'gcpue2cxqe9p', 3.0),
	 'b1033dcd-c1e0-4a6b-97d9-b4b9fe6bcf6e': ('RavenscourtPark', ['Ravenscourt Park'], 'c1e0', 51.494199999999999, -0.2359, 'gcpufwhprns5', 2.0),
	 '861ece04-d755-4e24-948c-1990014f49e2': ('TottenhamCourtRoad', ['Tottenham Court Road'], 'd755', 51.516500000000001, -0.13100000000000001, 'gcpvj42977xk', 1.0),
	 '611cdae4-916d-43c3-aa1c-bcba08d75098': ('SurreyQuays', ['Surrey Quays'], '916d', 51.493299999999998, -0.047800000000000002, 'gcpuyyj4nnve', 2.0),
	 '984d0bdd-193e-4a3b-b0b3-523edea3351e': ('Southgate', ['Southgate'], '193e', 51.632199999999997, -0.128, 'gcpvtp6g37sq', 4.0),
	 'a67bcb93-f537-428c-813e-8a257ef98d98': ('Queensway', ['Queensway'], 'f537', 51.5107, -0.18770000000000001, 'gcpv59prd62w', 1.0),
	 '0baa84a4-8275-4f53-bc45-1476fdd5934f': ('GoldhawkRoad', ['Goldhawk Road'], '8275', 51.501800000000003, -0.22670000000000001, 'gcpufzdgtx25', 2.0),
	 '2f61ae2d-9ffc-4f3c-afa0-87e712df3cff': ('HydeParkCorner', ['Hyde Park Corner'], '9ffc', 51.502699999999997, -0.1527, 'gcpuuxbbcz4s', 1.0),
	 '87b81f55-4ebd-41fc-a8e1-0e701cb6bda1': ('Fairlop', ['Fairlop'], '4ebd', 51.595999999999997, 0.091200000000000003, 'u10jd0f2mpe8', 5.0),
	 '44438768-26b6-4414-bdbd-a30055d17ced': ('ClaphamSouth', ['Clapham South'], '26b6', 51.4527, -0.14799999999999999, 'gcpuswsjxq7n', 2.5),
	 'ef56ae4c-6447-4907-bf07-49a13385b951': ('WestFinchley', ['West Finchley'], '6447', 51.609499999999997, -0.1883, 'gcpveenzhk17', 4.0),
	 '0a9a00c8-2f22-4c01-bc55-8402eb72e5b3': ('WestKensington', ['West Kensington'], '2f22', 51.490699999999997, -0.20649999999999999, 'gcpugm9eh4nm', 2.0),
	 '662cbbc1-1d6b-48be-b85c-140fb3c2d832': ('Bermondsey', ['Bermondsey'], '1d6b', 51.497900000000001, -0.063700000000000007, 'gcpuywct58mg', 2.0),
	 '74125284-3256-4527-a79d-0fddd3099af9': ('ColliersWood', ['Colliers Wood'], '3256', 51.417999999999999, -0.17780000000000001, 'gcpuebqe8cyt', 3.0),
	 '5c389d95-edf6-4554-adec-654d9a1a16f8': ('Stratford', ['Stratford'], 'edf6', 51.541600000000003, -0.0041999999999999997, 'gcpvpyugw4s7', 3.0),
	 'ed5d6e00-71b2-4df5-b7b2-05dfd3a9646c': ('ArnosGrove', ['Arnos Grove'], '71b2', 51.616399999999999, -0.1331, 'gcpvsurp6d37', 4.0),
	 '25c555f4-f529-4149-823e-a04c4463d524': ('PrestonRoad', ['Preston Road'], 'f529', 51.572000000000003, -0.2954, 'gcpv3k2usttg', 4.0),
	 '367c4cde-ffab-44df-a220-2b5c8ad298f4': ('RoyalAlbert', ['Royal Albert'], 'ffab', 51.508400000000002, 0.0465, 'u10j10cf5t8y', 3.0),
	 '0d2de214-c96e-4842-a10f-5fe058a90d5b': ('ElmPark', ['Elm Park'], 'c96e', 51.549599999999998, 0.19769999999999999, 'u10jk2rfntzv', 6.0),
	 'b386afc8-3f11-4b5c-9a24-0543965ec173': ('BelsizePark', ['Belsize Park'], '3f11', 51.550400000000003, -0.16420000000000001, 'gcpvk22qvg5d', 2.0),
	 '3378c47b-ad46-4f7f-8670-0f5394af7cb2': ('SouthHarrow', ['South Harrow'], 'ad46', 51.564599999999999, -0.35210000000000002, 'gcptrgp9e6ph', 5.0),
	 'd08e5786-189f-4451-916f-3c78d21e7f12': ('TotteridgeWhetstone', ['Totteridge & Whetstone'], '189f', 51.630200000000002, -0.17910000000000001, 'gcpveyvxdwv7', 4.0),
	 '93bcf13e-165d-4294-8c8a-434ffbdf7374': ('CanonsPark', ['Canons Park'], '165d', 51.607799999999997, -0.29470000000000002, 'gcpv96cmhzpy', 5.0),
	 'bfb41f10-53d9-44b4-8233-e5389ab3d583': ('ShepherdsBushC', ["Shepherd's Bush"], '53d9', 51.504600000000003, -0.21870000000000001, 'gcpv500spcm6', 2.0),
	 'a9f90eac-8bda-4b0d-a62c-0abace2ecacf': ('BecktonPark', ['Beckton Park'], '8bda', 51.508699999999997, 0.055, 'u10j12b5ctdg', 3.0),
	 '7889cae9-8416-4153-aad3-66ce2e110e2b': ('DagenhamHeathway', ['Dagenham Heathway'], '8416', 51.541699999999999, 0.1469, 'u10j5qfupj28', 5.0),
	 'bbed2b3a-a6d0-41f0-93af-82c7bb0c9d8b': ('EastHam', ['East Ham'], 'a6d0', 51.539400000000001, 0.051799999999999999, 'u10j1nmwz08b', 3.5),
	 '4ac60516-0e6a-47b4-898c-4a4d127a8baa': ('ParkRoyal', ['Park Royal'], '0e6a', 51.527000000000001, -0.28410000000000002, 'gcpv1s1nebzx', 3.0),
	 '6a4220d7-975d-4710-b069-2cf4dafc50e1': ('Kingsbury', ['Kingsbury'], '975d', 51.584600000000002, -0.27860000000000001, 'gcpv3wtnh4ku', 4.0),
	 '9ea06909-e76d-407f-bbf1-06a4e63f454c': ('Waterloo', ['Waterloo'], 'e76d', 51.503599999999999, -0.1143, 'gcpuvruy0wgt', 1.0),
	 '25ef1cc7-866a-474e-acc7-44a0d7e6bca5': ('Stanmore', ['Stanmore'], '866a', 51.619399999999999, -0.30280000000000001, 'gcpv9j58b1xg', 5.0),
	 'b39c2218-4bd9-4c5a-ac76-9483a64e58ec': ('CannonStreet', ['Cannon Street'], '4bd9', 51.511299999999999, -0.090399999999999994, 'gcpvjcq5jd2c', 1.0),
	 'c94e833d-198e-4108-809b-ba38e1b5aba7': ('GreenPark', ['Green Park'], '198e', 51.506700000000002, -0.14280000000000001, 'gcpvhb8028b9', 1.0),
	 '46d479d0-c2c8-4893-bf40-41721a7be205': ('IslandGardens', ['Island Gardens'], 'c2c8', 51.487099999999998, -0.0101, 'gcpuzubwhehf', 2.0),
	 '5e7c3e79-ec13-4840-a499-5c1cef1a6b2f': ('CharingCross', ['Charing Cross'], 'ec13', 51.508000000000003, -0.12470000000000001, 'gcpvj0tpy70u', 1.0),
	 '05da5b28-c40d-4860-92fb-6edf97f64650': ('Greenwich', ['Greenwich'], 'c40d', 51.478099999999998, -0.0149, 'gcpuzem1sv3g', 2.5),
	 '925a7fd8-5dc1-4620-a272-c4697d56172c': ('DevonsRoad', ['Devons Road'], '5dc1', 51.522300000000001, -0.017299999999999999, 'gcpvpe77huu4', 2.0),
	 '465b5b31-1237-4007-929b-5ffc63e19f79': ('NewburyPark', ['Newbury Park'], '1237', 51.575600000000001, 0.089899999999999994, 'u10j6j13wudm', 4.0),
	 '0767b416-a3da-4c1c-85bf-a3e59a2657d6': ('Chorleywood', ['Chorleywood'], 'a3da', 51.654299999999999, -0.51829999999999998, 'gcptu5qs4ert', 8.0),
	 'a67bc448-b939-4d1a-9d9a-840c17b6a496': ('CanaryWharf', ['Canary Wharf'], 'b939', 51.505099999999999, -0.020899999999999998, 'gcpvp80ybyxb', 2.0),
	 'a4840c38-6656-41f9-92ff-2e0192e89cbe': ('OxfordCircus', ['Oxford Circus'], '6656', 51.515000000000001, -0.14149999999999999, 'gcpvhf0bwu1b', 1.0),
	 '410e92c7-e6ac-4739-90dd-0834bb8b6e83': ('Queensbury', ['Queensbury'], 'e6ac', 51.594200000000001, -0.28610000000000002, 'gcpv92rtvrur', 4.0),
	 'c2ee297b-72ee-4842-9660-fd2ed00d93a2': ('Moorgate', ['Moorgate'], '72ee', 51.518599999999999, -0.088599999999999998, 'gcpvjfxmx7p5', 1.0),
	 'ff3b1cfb-1ea1-48af-a66d-8f1787f38598': ('Wanstead', ['Wanstead'], '1ea1', 51.577500000000001, 0.028799999999999999, 'u10j2tkuxnfg', 4.0),
	 'dd74b4e2-6e32-48f9-91cf-aa23e5551688': ('RuislipManor', ['Ruislip Manor'], '6e32', 51.5732, -0.41249999999999998, 'gcptqseesj39', 6.0),
	 '174ca94d-74d1-4606-9836-69aa275eb76e': ('Pinner', ['Pinner'], '74d1', 51.592599999999997, -0.3805, 'gcptx24uttww', 5.0),
	 '9aefa543-e3ff-4606-822b-b18794f4835d': ('BostonManor', ['Boston Manor'], 'e3ff', 51.495600000000003, -0.32500000000000001, 'gcpubw7rdgw7', 4.0),
	 '21ca86c8-b3a9-4040-b088-a2bba3e17c7d': ('TowerHill', ['Tower Hill'], 'b3a9', 51.509799999999998, -0.076600000000000001, 'gcpvn304r4dv', 1.0),
	 '2047f7d0-4ead-491d-93c9-c747a639d888': ('WestRuislip', ['West Ruislip'], '4ead', 51.569600000000001, -0.43759999999999999, 'gcptq5cqenjy', 6.0),
	 '7f63805a-0964-46ad-a282-e7dc199b8685': ('EustonSquare', ['Euston Square'], '0964', 51.526000000000003, -0.13589999999999999, 'gcpvhuj09q9d', 1.0),
	 'e427de05-8e0e-4bb6-99f7-81835be4bee7': ('StPauls', ["St. Paul's"], '8e0e', 51.514600000000002, -0.097299999999999998, 'gcpvjccnk9ry', 1.0),
	 '97c4c33d-b5af-421b-aeef-b6ff98e3f1ca': ('Hainault', ['Hainault'], 'b5af', 51.603000000000002, 0.093299999999999994, 'u10jd45cq03t', 5.0),
	 'c8e337d3-3b61-4a7f-b973-686df3f7502d': ('BurntOak', ['Burnt Oak'], '3b61', 51.602800000000002, -0.2641, 'gcpv9fp8n50u', 4.0),
	 '497d910f-1ed1-4e9d-9e45-6a71f126fccc': ('Arsenal', ['Arsenal'], '1ed1', 51.558599999999998, -0.10589999999999999, 'gcpvm9fys7eh', 2.0),
	 'b5ef4219-5d51-49d4-8bd5-2fa1fb9e867c': ('Pimlico', ['Pimlico'], '5d51', 51.4893, -0.13339999999999999, 'gcpuuvqfgt1y', 1.0),
	 'ccffd31a-972c-40ba-903a-0e4ce0d971c6': ('CaledonianRoad', ['Caledonian Road'], '972c', 51.548099999999998, -0.1188, 'gcpvm213ry23', 2.0),
	 'b6f356a7-c2a4-4974-8c96-9519cbb7b839': ('HounslowWest', ['Hounslow West'], 'c2a4', 51.473399999999998, -0.38550000000000001, 'gcpsz4rq31nr', 5.0),
	 '0faa4a5e-67b5-4e49-bd64-bdadcc8eb4b4': ('Knightsbridge', ['Knightsbridge'], '67b5', 51.5015, -0.16070000000000001, 'gcpuurdczrmq', 1.0),
	 '24fa220d-ca13-443d-9e73-8be49afd7db0': ('SudburyHill', ['Sudbury Hill'], 'ca13', 51.556899999999999, -0.33660000000000001, 'gcpv23duswub', 4.0),
	 '52433503-c65c-4089-82ff-4fd1d2780f84': ('Oval', ['Oval'], 'c65c', 51.481900000000003, -0.113, 'gcpuv7vxyctp', 2.0),
	 '8ca4bf88-8884-42eb-82b9-93c921dd3fc7': ('WembleyCentral', ['Wembley Central'], '8884', 51.551900000000003, -0.29630000000000001, 'gcpv328pxdwt', 4.0),
	 'bef7f260-c351-412c-bec0-b05d82367f88': ('Lewisham', ['Lewisham'], 'c351', 51.465699999999998, -0.014200000000000001, 'gcpuz9j9mjgd', 2.5),
	 'd168eb7a-13eb-477b-b482-c69c3b4f5dbf': ('HeathrowTerminal4', ['Heathrow Terminal 4'], '13eb', 51.459800000000001, -0.4476, 'gcpstzfp41vp', 6.0),
	 '78e36286-e750-49ee-927a-4e2bc3134788': ('LiverpoolStreet', ['Liverpool Street'], 'e750', 51.517800000000001, -0.082299999999999998, 'gcpvn4s0fmbx', 1.0),
	 '03af5d7e-72c4-413f-a260-52c1fe5d022c': ('TheydonBois', ['Theydon Bois'], '72c4', 51.671700000000001, 0.1033, 'u10jfqe1rp40', 6.0),
	 'a14eddb7-704e-4d4f-a0d6-5105d028f128': ('Rotherhithe', ['Rotherhithe'], '704e', 51.500999999999998, -0.052499999999999998, 'gcpuyz3z0djp', 2.0),
	 '1f3ac254-b5cd-4317-b777-64f2432e4c7a': ('MorningtonCrescent', ['Mornington Crescent'], 'b5cd', 51.534199999999998, -0.13869999999999999, 'gcpvhve02p1v', 2.0),
	 '28b2ee7c-7a48-44d2-b4a9-499effac5775': ('RuislipGardens', ['Ruislip Gardens'], '7a48', 51.560600000000001, -0.4103, 'gcptqdm4r26p', 5.0),
	 'e93bad5c-e2e2-45f2-940f-35583fc357dd': ('Hillingdon', ['Hillingdon'], 'e2e2', 51.553800000000003, -0.44990000000000002, 'gcptmc06ssf5', 6.0),
	 'e5c04fad-1dfc-46c3-8e27-74a8a6b1c63e': ('NorthwickPark', ['Northwick Park'], '1dfc', 51.578400000000002, -0.31840000000000002, 'gcpv2v81uwxu', 4.0),
	 '559326bd-543e-4933-9241-990094b932cb': ('BaronsCourt', ['Barons Court'], '543e', 51.490499999999997, -0.21390000000000001, 'gcpugjs1zubs', 2.0),
	 '8b275b50-6675-44dc-b9f8-154730faac04': ('Mudchute', ['Mudchute'], '6675', 51.490200000000002, -0.014500000000000001, 'gcpuztt2nhup', 2.0),
	 'e4f72828-a29a-4fdd-9bea-66fecdcfa250': ('FulhamBroadway', ['Fulham Broadway'], 'a29a', 51.480400000000003, -0.19500000000000001, 'gcpugedp04j7', 2.0),
	 '15351ff7-4b56-4882-a4d0-c4fd315ac9ef': ('NewCross', ['New Cross'], '4b56', 51.476700000000001, -0.0327, 'gcpuz701w03h', 2.0),
	 '2d04e04c-9ce2-4384-80e3-06243cb8d90b': ('Hornchurch', ['Hornchurch'], '9ce2', 51.553899999999999, 0.21840000000000001, 'u10jkcp51pdb', 6.0),
	 '29105288-d523-40cf-99a1-1ef83751460f': ('WestIndiaQuay', ['West India Quay'], 'd523', 51.506999999999998, -0.020299999999999999, 'gcpvp894nbxn', 2.0),
	 '2f0faf9b-7406-4a32-8d18-927b7af16497': ('RaynersLane', ['Rayners Lane'], '7406', 51.575299999999999, -0.37140000000000001, 'gcptrscxcub0', 5.0),
	 '3e8ccac4-231c-4715-90fc-2025b412d64f': ('Kenton', ['Kenton'], '231c', 51.581600000000002, -0.31619999999999998, 'gcpv2y1u850j', 4.0),
	 '767e63fc-be79-449a-a461-670f3888eb56': ('NorthWembley', ['North Wembley'], 'be79', 51.562100000000001, -0.3034, 'gcpv34e5420e', 4.0),
	 'e0b9f30a-2875-4559-a814-8d2297a2266d': ('ElversonRoad', ['Elverson Road'], '2875', 51.469299999999997, -0.017399999999999999, 'gcpuz9eq6sct', 2.5),
	 '5177aa0d-3b92-4a1d-8356-3acfd80189be': ('Highgate', ['Highgate'], '3b92', 51.5777, -0.14580000000000001, 'gcpvktmvfs5s', 3.0),
	 '1629ea4a-7ee7-4f0c-bb70-231721b53632': ('Holborn', ['Holborn'], '7ee7', 51.517400000000002, -0.12, 'gcpvj62weg3t', 1.0),
	 '2e6585ea-25a5-4255-b312-fb33a99de249': ('HarrowWealdston', ['Harrow & Wealdston'], '25a5', 51.592500000000001, -0.33510000000000001, 'gcpv825upe56', 5.0),
	 '09bbbf1c-4b44-4300-9b7e-7da31c621afc': ('RoyalOak', ['Royal Oak'], '4b44', 51.518999999999998, -0.188, 'gcpv5dxpgm9j', 2.0),
	 '9ac4ad96-5502-4948-a754-8558c1a59201': ('HendonCentral', ['Hendon Central'], '5502', 51.582900000000002, -0.22589999999999999, 'gcpv6y7s0jsb', 3.5),
	 '9bd73108-ad7c-4b42-93c5-8a9d8cdd0acc': ('UptonPark', ['Upton Park'], 'ad7c', 51.535200000000003, 0.034299999999999997, 'u10j0v8yr1xf', 3.0),
	 '30d86bee-6a66-4f65-9b47-dd2a21e5a4f8': ('Blackfriars', ['Blackfriars'], '6a66', 51.512, -0.1031, 'gcpvj9kzjsg1', 1.0),
	 'b26ff8de-7cfe-4143-8413-1d9459ef877f': ('EastIndia', ['East India'], '7cfe', 51.509300000000003, -0.0020999999999999999, 'gcpvpbyrrj6n', 2.5),
	 'fa25d9e4-e9c9-44da-ae24-ea2d2235d9f6': ('SouthRuislip', ['South Ruislip'], 'e9c9', 51.556899999999999, -0.39879999999999999, 'gcptqctseqc0', 5.0),
	 '7cb122f8-02b7-4ec6-8021-85a4ae14639e': ('SouthWoodford', ['South Woodford'], '02b7', 51.591700000000003, 0.0275, 'u10j2xup2vcq', 4.0),
	 '6e66b0ff-cfc1-42b3-8029-3ecad13b44ae': ('StamfordBrook', ['Stamford Brook'], 'cfc1', 51.494999999999997, -0.24590000000000001, 'gcpufqkun5g8', 2.0),
	 '43b5a37c-7e3b-4b49-ac58-2f33191cdf4e': ('Kilburn', ['Kilburn'], '7e3b', 51.5471, -0.20469999999999999, 'gcpv5rfgw5us', 2.0),
	 '2b655c4f-fbfb-4005-be97-38962e01a3ed': ('KensalGreen', ['Kensal Green'], 'fbfb', 51.5304, -0.22500000000000001, 'gcpv4uu4m4gc', 2.0),
	 'fa04941a-9c43-4392-b0a4-43e75b3a7e82': ('ClaphamCommon', ['Clapham Common'], '9c43', 51.461799999999997, -0.1384, 'gcpuub74xnc6', 2.0),
	 'c4806aae-06ae-4c0e-bbe6-f57c358976da': ('Alperton', ['Alperton'], '06ae', 51.540700000000001, -0.29970000000000002, 'gcpv1nty26z7', 4.0),
	 '2945184c-9a8d-4707-88a3-ec1bd35999b0': ('CanningTown', ['Canning Town'], '9a8d', 51.514699999999998, 0.0082000000000000007, 'u10j01vyzh47', 3.0),
	 '480e2906-9176-4d6a-b14b-3a966a5a4f3f': ('BethnalGreen', ['Bethnal Green'], '9176', 51.527000000000001, -0.054899999999999997, 'gcpvnu0n88zx', 2.0),
	 'f0a7d304-3e3f-46c8-978a-532bb28d3528': ('KilburnPark', ['Kilburn Park'], '3e3f', 51.5351, -0.19389999999999999, 'gcpv5tdv9yct', 2.0),
	 '8450af6a-dbf3-4749-811b-6676552bed4b': ('HighburyIslington', ['Highbury & Islington'], 'dbf3', 51.545999999999999, -0.104, 'gcpvjxsm0wgf', 2.0),
	 '5f45b71a-7b9a-449f-bdee-cd6262795f51': ('GoldersGreen', ['Golders Green'], '7b9a', 51.572400000000002, -0.19409999999999999, 'gcpv7s6xj0ht', 3.0),
	 'cd0ae317-6fa5-4640-8971-50661b49c32f': ('TootingBec', ['Tooting Bec'], '6fa5', 51.436100000000003, -0.1598, 'gcpus7esurur', 3.0),
	 '38d6323c-663a-4f54-a58b-71cff0611d3d': ('WillesdenJunction', ['Willesden Junction'], '663a', 51.532600000000002, -0.24779999999999999, 'gcpv4m5x1ufu', 3.0),
	 '0f98d1ce-4217-4f49-9e03-8402c32d2ff1': ('AldgateEast', ['Aldgate East'], '4217', 51.5154, -0.072599999999999998, 'gcpvn654uq9d', 1.0),
	 '6bf824ad-8d24-4258-9e8c-398b85dfb3c8': ('CamdenTown', ['Camden Town'], '8d24', 51.539200000000001, -0.1426, 'gcpvhy2jt5jx', 2.0),
	 '61596bb4-4814-44a5-8607-a66b4cc14bd1': ('Beckton', ['Beckton'], '4814', 51.514800000000001, 0.0613, 'u10j13uxkqsx', 3.0),
	 'aaf9fad0-0d23-4c27-927d-79a20d43d505': ('Victoria', ['Victoria'], '0d23', 51.496499999999997, -0.1447, 'gcpuuwwsu5rg', 1.0),
	 '36aa3d82-e972-4f11-81cc-b94415bf849f': ('HounslowEast', ['Hounslow East'], 'e972', 51.473300000000002, -0.35639999999999999, 'gcpszfkmxq8f', 4.0),
	 '2b13ebcf-2181-451d-b4b0-e53c03ae77f1': ('Farringdon', ['Farringdon'], '2181', 51.520299999999999, -0.1053, 'gcpvjdgrd248', 1.0),
	 '13a9b335-fdb9-44d3-bd3d-09fc64504063': ('Watford', ['Watford'], 'fdb9', 51.657299999999999, -0.41770000000000002, 'gcpty7zvdfsm', 8.0),
	 '79c291cf-6caa-469a-9b65-a6f2c8e3075c': ('WillesdenGreen', ['Willesden Green'], '6caa', 51.549199999999999, -0.2215, 'gcpv6bnxyeme', 2.5),
	 '0b7a7fd5-81c8-4f40-b072-ed5bd74eed46': ('ChanceryLane', ['Chancery Lane'], '81c8', 51.518500000000003, -0.1111, 'gcpvj6xj50mz', 1.0),
	 'd0c57e5c-e1b4-4cee-82bc-35751a8b4625': ('RodingValley', ['Roding Valley'], 'e1b4', 51.617100000000001, 0.043900000000000002, 'u10j8uxgquy5', 5.0),
	 'a7c40a0b-bb1a-46d9-8442-e7f45b8f7743': ('Harlesden', ['Harlesden'], 'bb1a', 51.536200000000001, -0.25750000000000001, 'gcpv4jukpgfp', 3.0),
	 '9a89a50c-34ad-498a-bc81-598d58cd0d1f': ('WestSilvertown', ['West Silvertown'], '34ad', 51.502699999999997, 0.022599999999999999, 'u10hbxb2yx5u', 3.0),
	 '4f6eda25-7e30-45ad-80f2-9db2453d262c': ('StJamessPark', ["St. James's Park"], '7e30', 51.499400000000001, -0.13350000000000001, 'gcpuuznv9pzp', 1.0),
	 'd60522bc-d2a5-4d89-8b52-0d236844c6ec': ('LatimerRoad', ['Latimer Road'], 'd2a5', 51.5139, -0.2172, 'gcpv51cf4ygz', 2.0),
	 '320689c7-450e-44d5-a799-0022492c1944': ('Blackwall', ['Blackwall'], '450e', 51.507899999999999, -0.0066, 'gcpvpbepq0qx', 2.0),
	 '3dfe2051-c378-4afa-9826-bc94298eb01a': ('RegentsPark', ["Regent's Park"], 'c378', 51.523400000000002, -0.14660000000000001, 'gcpvhet1xczh', 1.0),
	 '5c366dc4-6f3a-4ca2-8175-db52f2e5ad23': ('LancasterGate', ['Lancaster Gate'], '6f3a', 51.511899999999997, -0.17560000000000001, 'gcpvh12ns4ph', 1.0),
	 '37b045b7-e731-4056-87e8-ac5bf4e12c4a': ('Leytonstone', ['Leytonstone'], 'e731', 51.568300000000001, 0.0083000000000000001, 'u10j25wp17ug', 3.5),
	 '4a018a17-22e8-4539-b41d-910e4caf4b50': ('LeicesterSquare', ['Leicester Square'], '22e8', 51.511299999999999, -0.12809999999999999, 'gcpvj16ep439', 1.0),
	 '8046cf9c-5d92-47ee-b034-32205ba494c6': ('Vauxhall', ['Vauxhall'], '5d92', 51.4861, -0.12529999999999999, 'gcpuvhub229t', 1.5),
	 '07b7cfc5-10dd-4ff3-b46b-87a42a1d06b7': ('Chigwell', ['Chigwell'], '10dd', 51.617699999999999, 0.075499999999999998, 'u10j9swyzk8y', 5.0),
	 '32b3c7d2-f9a2-4d46-ba4f-1c5efb4ddeb3': ('Gunnersbury', ['Gunnersbury'], 'f9a2', 51.491500000000002, -0.27539999999999998, 'gcpuctxrwxqc', 3.0),
	 '251c1166-6118-4fa3-9426-3d7b32f800d8': ('Upminster', ['Upminster'], '6118', 51.558999999999997, 0.251, 'u10jmdnbbwpp', 6.0),
	 '8ec708cb-60c6-4dfa-a66c-2d7220dc7d83': ('Embankment', ['Embankment'], '60c6', 51.507399999999997, -0.12230000000000001, 'gcpvj0wuq5q9', 1.0),
	 '249dc44e-c5e8-4803-818a-ea54725c2a9d': ('StepneyGreen', ['Stepney Green'], 'c5e8', 51.522100000000002, -0.047, 'gcpvngmcbzd3', 2.0),
	 'a8e021f5-0edf-408e-8e48-18fbeed57019': ('Chesham', ['Chesham'], '0edf', 51.705199999999998, -0.61099999999999999, 'gcpw4hehdev7', 10.0),
	 '9df5a834-3827-4a46-9fb7-c26cce6837db': ('WembleyPark', ['Wembley Park'], '3827', 51.563499999999998, -0.27950000000000003, 'gcpv3du7pjjd', 4.0),
	 '093bea1f-2abe-41bb-b0ca-1716079e6104': ('PontoonDock', ['Pontoon Dock'], '2abe', 51.502099999999999, 0.031899999999999998, 'u10hbxxjrr63', 3.0),
	 'ea843760-eb68-4308-9c84-7d5546516ce6': ('NorthGreenwich', ['North Greenwich'], 'eb68', 51.500500000000002, 0.0038999999999999998, 'u10hbp6u4vh0', 2.5),
	 '130b0d90-588d-4aad-b3a2-9d98efaf99cd': ('HarrowontheHill', ['Harrow- on-the-Hill'], '588d', 51.579300000000003, -0.33660000000000001, 'gcpv2mdzhwkv', 5.0),
	 '34d5c090-9d83-4f39-bc46-5e4538ae2218': ('Euston', ['Euston'], '9d83', 51.528199999999998, -0.13370000000000001, 'gcpvhuqts8dj', 1.0),
	 'ef5e3a08-aee0-4b26-9686-c699bc8d91e6': ('CoventGarden', ['Covent Garden'], 'aee0', 51.512900000000002, -0.12429999999999999, 'gcpvj1tkrse1', 1.0),
	 'af6b94cd-7efb-40a1-853e-e5c90607452d': ('Uxbridge', ['Uxbridge'], '7efb', 51.546300000000002, -0.47860000000000003, 'gcptjpeqzycb', 6.0),
	 '3c1ecf94-d8e2-4e5f-8f54-645e836b3294': ('Barbican', ['Barbican'], 'd8e2', 51.520400000000002, -0.097900000000000001, 'gcpvjg08nf8m', 1.0),
	 '315f9ade-a54c-458c-a85f-f9962a5c6dc7': ('EalingBroadway', ['Ealing Broadway'], 'a54c', 51.5152, -0.30170000000000002, 'gcpv14h3cck1', 3.0),
	 '95b2c24a-fdf9-4cb0-b04e-4989909ffb72': ('Barking', ['Barking'], 'fdf9', 51.5396, 0.081000000000000003, 'u10j1y6zzmvc', 4.0),
	 '78b8c3de-a903-484f-bf2c-6ce07bbdd28e': ('EdgwareRoadB', ['Edgware Road'], 'a903', 51.5199, -0.16789999999999999, 'gcpvh4vtptkw', 1.0),
	 '58054f33-5750-4b25-9706-5028b2e96d0b': ('TurnhamGreen', ['Turnham Green'], '5750', 51.495100000000001, -0.25469999999999998, 'gcpufnqs9n3u', 2.5),
	 '64981d6a-1322-49b2-aa95-a05d6b43423e': ('Bank', ['Bank'], '1322', 51.513300000000001, -0.088599999999999998, 'gcpvjcxqxrp5', 1.0),
	 '1e3d8c1e-1207-4030-9052-54ef0351dc62': ('NorthActon', ['North Acton'], '1207', 51.523699999999998, -0.25969999999999999, 'gcpv45dgk9cd', 2.5),
	 '2599c24c-28ac-460b-9c99-ccfcd68bff37': ('CrossharbourLondonArena', ['Crossharbour & London Arena'], '28ac', 51.495699999999999, -0.0144, 'gcpuzwt80qnx', 2.0),
	 '887a0d89-9d8b-4023-a901-86792db421ff': ('FinchleyCentral', ['Finchley Central'], '9d8b', 51.601199999999999, -0.19320000000000001, 'gcpve9eqf0ge', 4.0),
	 '742e97bc-26b6-4294-b111-b1301e8760d8': ('Whitechapel', ['Whitechapel'], '26b6', 51.519399999999997, -0.061199999999999997, 'gcpvndg6mbjz', 2.0),
	 '80031d6b-6327-411f-b98a-0f8124c25d86': ('KewGardens', ['Kew Gardens'], '6327', 51.476999999999997, -0.28499999999999998, 'gcpuce07r029', 3.5),
	 'a6d5538c-8cbf-44b1-b182-021be3c5c240': ('Greenford', ['Greenford'], '8cbf', 51.542299999999997, -0.34560000000000002, 'gcpv0nurdvjg', 4.0),
	 'b8f9c445-c7c7-4541-a396-a3d66ea350c4': ('QueensPark', ['Queens Park'], 'c7c7', 51.534100000000002, -0.20469999999999999, 'gcpv5m6zyhs8', 2.0),
	 '57d3a7a7-5e23-447e-bb6a-cbbd12a9d635': ('EastFinchley', ['East Finchley'], '5e23', 51.587400000000002, -0.16500000000000001, 'gcpvkppy7hr5', 3.0),
	 'f0a2bae9-93f2-4acc-af91-602c879cd8fd': ('ActonTown', ['Acton Town'], '93f2', 51.502800000000001, -0.28010000000000002, 'gcpucxu191y2', 3.0),
	 '5af0f8f0-6783-4c15-a292-45f151ede2d2': ('Woodford', ['Woodford'], '6783', 51.606999999999999, 0.034099999999999998, 'u10j8fbbdd4f', 4.0),
	 '4335b1ca-4202-4c76-ba79-379bbbb9e9f4': ('EalingCommon', ['Ealing Common'], '4202', 51.510100000000001, -0.28820000000000001, 'gcpv13nhh6we', 3.0),
	 '654971d2-8531-49f5-9e0c-8ad88beee31b': ('ChalfontLatimer', ['Chalfont & Latimer'], '8531', 51.667900000000003, -0.56100000000000005, 'gcptgjz7rf8h', 9.0),
	 '2fd3ee8f-d2df-4e94-86da-6d1cd67f1d4c': ('ManorHouse', ['Manor House'], 'd2df', 51.571199999999997, -0.095799999999999996, 'gcpvmu60p8qq', 2.5),
	 'ff596b51-d851-4cdb-b6ff-3f143a90c862': ('Kennington', ['Kennington'], 'd851', 51.488399999999999, -0.1053, 'gcpuvt5mdm6t', 2.0),
	 '0d3810fe-24fb-40d0-92c5-804a15144341': ('GantsHill', ['Gants Hill'], '24fb', 51.576500000000003, 0.066299999999999998, 'u10j3t0qbuky', 4.0),
	 '01f067eb-fe23-44fb-b697-cb45fb258e71': ('Wapping', ['Wapping'], 'fe23', 51.504300000000001, -0.055800000000000002, 'gcpvn8p67c2s', 2.0),
	 'ec56b880-1907-449f-b9d9-3cb93a2d0b70': ('Aldgate', ['Aldgate'], '1907', 51.514299999999999, -0.075499999999999998, 'gcpvn3ch89x1', 1.0),
	 'c0eed10a-cfc3-417d-b06d-435f53af2d41': ('ShepherdsBushH', ["Shepherd's Bush"], 'cfc3', 51.505800000000001, -0.22650000000000001, 'gcpv4b7541j2', 2.0),
	 'ed39a802-cf23-42a2-8006-cf2ab8a54048': ('HighStreetKensington', ['High Street Kensington'], 'cf23', 51.500900000000001, -0.1925, 'gcpugx7y6rte', 1.0),
	 '873fa51e-dbc3-4407-9249-ea14e11f6f3e': ('FinsburyPark', ['Finsbury Park'], 'dbc3', 51.5642, -0.1065, 'gcpvmdfrnref', 2.0),
	 '9021de2d-4cfd-48b5-98c1-30e002cc8f3a': ('SouthQuay', ['South Quay'], '4cfd', 51.500700000000002, -0.019099999999999999, 'gcpuzx6j6fq1', 2.0),
	 'c95d8299-8911-4a67-af90-f945b8d990bb': ('Temple', ['Temple'], '8911', 51.511099999999999, -0.11409999999999999, 'gcpvj3kcvm0b', 1.0),
	 'b8db5bac-3ac1-4bec-beda-69af98ebd222': ('Morden', ['Morden'], '3ac1', 51.402200000000001, -0.1948, 'gcpu7t6psbdd', 4.0),
	 '8e9e65b9-127f-4442-ac1f-7d822a4462d9': ('SouthKenton', ['South Kenton'], '127f', 51.570099999999996, -0.30809999999999998, 'gcpv2up9serv', 4.0),
	 '7e9b3da7-2e31-4fdf-90a0-f98cd7b0c8ed': ('HighBarnet', ['High Barnet'], '2e31', 51.650300000000001, -0.1943, 'gcpvgddsb3z2', 5.0),
	 'f0395015-50a0-4933-bb40-6bb4d56ddffb': ('Plaistow', ['Plaistow'], '50a0', 51.531300000000002, 0.0172, 'u10j0kux8f94', 3.0),
	 '8823ac5f-5680-435b-a049-5ee40e86817e': ('AllSaints', ['All Saints'], '5680', 51.5107, -0.012999999999999999, 'gcpvp9nx946q', 2.0),
	 'ad4d2a18-aca2-4020-a663-80927dd2f803': ('MoorPark', ['Moor Park'], 'aca2', 51.629399999999997, -0.432, 'gcptwnv7j9tr', 6.5),
	 '5c249c9c-696d-4cbd-a8a3-c87f7029566e': ('LondonBridge', ['London Bridge'], '696d', 51.505200000000002, -0.086400000000000005, 'gcpvn01pd9pm', 1.0),
	 'ec42cf0b-0a85-4fb6-84fe-10a41a55ef9d': ('Cockfosters', ['Cockfosters'], '0a85', 51.651699999999998, -0.14960000000000001, 'gcpvudghfnf0', 5.0),
	 '6ac25ebb-40be-4de4-bb86-c7db73ae823d': ('MarbleArch', ['Marble Arch'], '40be', 51.513599999999997, -0.15859999999999999, 'gcpvh3u82r53', 1.0),
	 'e6c6ede6-efc2-4040-9876-932552ce8646': ('LambethNorth', ['Lambeth North'], 'efc2', 51.499099999999999, -0.1115, 'gcpuvrnu1b59', 1.0),
	 '2669ea4a-b267-4a8b-b2fe-25276b670c53': ('WestHarrow', ['West Harrow'], 'b267', 51.579500000000003, -0.3533, 'gcptrvy8re8q', 5.0),
	 '4225000a-a83c-4db4-a906-fc32e828624b': ('Limehouse', ['Limehouse'], 'a83c', 51.512300000000003, -0.039600000000000003, 'gcpvp1e0vk8n', 2.0),
	 '94660c36-6039-4805-a6cb-9221905ce759': ('Edgware', ['Edgware'], '6039', 51.613700000000001, -0.27500000000000002, 'gcpv9ezz8511', 5.0),
	 'c4968339-846a-4814-b66f-6168c7f2398d': ('NottingHillGate', ['Notting Hill Gate'], '846a', 51.509399999999999, -0.19670000000000001, 'gcpv590b081g', 1.5),
	 'e5ba2584-8519-4759-931d-056d31844a44': ('WhiteCity', ['White City'], '8519', 51.512, -0.22389999999999999, 'gcpv4ckznub1', 2.0),
	 '364a49a3-65ad-4649-b9a0-af01a6b98920': ('Leyton', ['Leyton'], '65ad', 51.556600000000003, -0.0053, 'gcpvrcs4uwb4', 3.0),
	 'a59bf99e-0fd1-4823-bc06-89a1bb21101a': ('Loughton', ['Loughton'], '0fd1', 51.641199999999998, 0.055800000000000002, 'u10jc2bxu1rm', 6.0),
	 'ee36d2e5-cdb0-4667-b960-d5d395d1c86a': ('SwissCottage', ['Swiss Cottage'], 'cdb0', 51.543199999999999, -0.17380000000000001, 'gcpvhp1kyhvk', 2.0),
	 '4ae3072a-10a8-4400-9ed2-127b6b5b976a': ('Amersham', ['Amersham'], '10a8', 51.6736, -0.60699999999999998, 'gcptfnvuxc5y', 10.0),
	 'f30b89ed-552a-40c9-afb5-ce64fa41ff2d': ('Borough', ['Borough'], '552a', 51.501100000000001, -0.094299999999999995, 'gcpuvz7rdsuu', 1.0),
	 'a0665b47-6400-476e-b569-ec68a6a7fd76': ('TurnpikeLane', ['Turnpike Lane'], '6400', 51.590400000000002, -0.1028, 'gcpvmxtpuedg', 3.0),
	 '88392a34-b5cb-4c76-9e9d-7cfaf4fb944e': ('SouthKensington', ['South Kensington'], 'b5cb', 51.494100000000003, -0.17380000000000001, 'gcpuun1qy5vr', 1.0),
	 '68f6f208-ef36-4859-9a85-6440e04d4c63': ('CuttySark', ['Cutty Sark'], 'ef36', 51.482700000000001, -0.0095999999999999992, 'gcpuzu1h2qce', 2.5),
	 '815ea4ed-f5ee-4f5c-b3ab-3731a03eeed5': ('Monument', ['Monument'], 'f5ee', 51.510800000000003, -0.086300000000000002, 'gcpvn130jj44', 1.0),
	 '5064cba1-ec2e-416f-9153-c0273385d528': ('Eastcote', ['Eastcote'], 'ec2e', 51.576500000000003, -0.39700000000000002, 'gcptqvnyvhrq', 5.0),
	 'b95f74c7-0ccc-4a04-ad46-ae255ed14689': ('WestHam', ['West Ham'], '0ccc', 51.528700000000001, 0.0055999999999999999, 'u10j0hs06mzs', 3.0),
	 '2ea2857a-1d56-4fe9-a145-d6031fd660ab': ('RussellSquare', ['Russell Square'], '1d56', 51.523000000000003, -0.1244, 'gcpvj5mrjr2d', 1.0),
	 '1196b1e2-b958-4273-8c77-188a8ba4574c': ('SudburyTown', ['Sudbury Town'], 'b958', 51.550699999999999, -0.31559999999999999, 'gcpv2bd0tfzx', 4.0),
	 '3ac40716-c714-4851-8204-5960863c4205': ('WalthamstowCentral', ['Walthamstow Central'], 'c714', 51.582999999999998, -0.0195, 'gcpvrw3uc85s', 3.0),
	 '84826d24-3c8b-4fc3-9ecf-ec01c9afb2e2': ('WoodGreen', ['Wood Green'], '3c8b', 51.597499999999997, -0.10970000000000001, 'gcpvt9015z1u', 3.0),
	 '018de108-a518-4d48-acb8-7bc2085dc28c': ('TootingBroadway', ['Tooting Broadway'], 'a518', 51.427500000000002, -0.16800000000000001, 'gcpus4jdvkf4', 3.0),
	 '25902e50-70bd-4fa6-964e-bf0154a396cd': ('HollandPark', ['Holland Park'], '70bd', 51.5075, -0.20599999999999999, 'gcpv529uzvgm', 2.0),
	 '9e0c5708-2ac3-41d5-baab-56d5602b76b1': ('BromleyByBow', ['Bromley-By-Bow'], '2ac3', 51.524799999999999, -0.011900000000000001, 'gcpvpez3dwys', 2.5),
	 'c9cd51e3-5fff-4ce7-9502-907fe8a28c1e': ('TufnellPark', ['Tufnell Park'], '5fff', 51.556699999999999, -0.13739999999999999, 'gcpvkcegw37n', 2.0),
	 '7bc2b747-1f8c-473f-a915-f1a476d1a1b3': ('GrangeHill', ['Grange Hill'], '1f8c', 51.613199999999999, 0.092299999999999993, 'u10jd5ghwtzf', 5.0),
	 'e1d3e10a-16cd-4e75-8d6e-d9d299fba0bd': ('SouthEaling', ['South Ealing'], '16cd', 51.501100000000001, -0.30719999999999997, 'gcpucp2r9szh', 3.0),
	 '7dbfb563-2a49-4ede-985d-5df9e4b91e93': ('KingsCrossStPancras', ["King's Cross St. Pancras"], '2a49', 51.530799999999999, -0.12379999999999999, 'gcpvjhvuem25', 1.0),
	 '77ebcb72-e4e5-4459-94e6-e2364e29f8b9': ('PuddingMillLane', ['Pudding Mill Lane'], 'e4e5', 51.534300000000002, -0.013899999999999999, 'gcpvpttch1g3', 2.5),
	 '0d8038c4-2a18-42eb-95e9-b3eba2fbd129': ('SloaneSquare', ['Sloane Square'], '2a18', 51.492400000000004, -0.1565, 'gcpuumyhcr14', 1.0),
	 '9713cb92-a9d6-4eb8-9bf9-477860fd02ab': ('BondStreet', ['Bond Street'], 'a9d6', 51.514200000000002, -0.14940000000000001, 'gcpvh9g5ywzk', 1.0),
	 'f2afedc3-d882-413d-9483-f13605def449': ('Upney', ['Upney'], 'd882', 51.538499999999999, 0.1014, 'u10j4q3cdb9r', 4.0),
	 '0999211f-c7f4-49ec-83ba-b249aefde30e': ('NewCrossGate', ['New Cross Gate'], 'c7f4', 51.475700000000003, -0.0402, 'gcpuz4fexmbx', 2.0),
	 '8eccd70b-662c-474d-b91d-5c88c03286d9': ('UpminsterBridge', ['Upminster Bridge'], '662c', 51.558199999999999, 0.23430000000000001, 'u10jm3fs794d', 6.0),
	 '498adbf2-cab9-49d8-bff4-d35c8a0c9587': ('CustomHouse', ['Custom House'], 'cab9', 51.509500000000003, 0.0276, 'u10j09h0e4u0', 3.0),
	 '437b3160-3e03-4694-aa4d-9349e8c419fa': ('ChalkFarm', ['Chalk Farm'], '3e03', 51.5441, -0.15379999999999999, 'gcpvhx240hwm', 2.0),
	 '89c3fead-9427-4698-830a-df06f301690f': ('NorthEaling', ['North Ealing'], '9427', 51.517499999999998, -0.28870000000000001, 'gcpv16mz0y19', 3.0),
	 '7f6a1eba-5fd4-43fb-9d86-b60ef44f03d4': ('ElephantCastle', ['Elephant & Castle'], '5fd4', 51.494300000000003, -0.10009999999999999, 'gcpuvwr05920', 1.5),
	 'ccffda41-ad3f-4c1f-b19d-f3dfe244ee96': ('Westminster', ['Westminster'], 'ad3f', 51.500999999999998, -0.12540000000000001, 'gcpuvpkxjfnz', 1.0),
	 '1750f083-8e55-4cb0-aaeb-70b14bed0158': ('BoundsGreen', ['Bounds Green'], '8e55', 51.607100000000003, -0.12429999999999999, 'gcpvt4v3psen', 3.5),
	 '70ab528d-f449-49ff-a03c-33bb16bf7ab7': ('MansionHouse', ['Mansion House'], 'f449', 51.5122, -0.094, 'gcpvjce83dhd', 1.0),
	 'ac425ff0-4c85-4dc2-875b-980714c379b8': ('NorthwoodHills', ['Northwood Hills'], '4c85', 51.6004, -0.40920000000000001, 'gcptw9w40gwr', 6.0),
	 '39006e53-1040-4238-8886-b748bc899c23': ('Angel', ['Angel'], '1040', 51.532200000000003, -0.10580000000000001, 'gcpvjt4uydmf', 1.0)}
	new_tube_stations={}
	for k in tube_stations:
		new_tube_stations[k]=(tube_stations[k][2],tube_stations[k][5],tube_stations[k][0],tube_stations[k][1],(tube_stations[k][3],tube_stations[k][4]),tube_stations[k][6])
	
	write_to_transport(new_tube_stations,{})
	
organize_stations()
print "OK"
