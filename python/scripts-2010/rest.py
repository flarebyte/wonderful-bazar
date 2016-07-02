import re
from collections import defaultdict

email = re.compile(r"(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)",re.IGNORECASE)
fullurl = re.compile("https?://[-a-z0-9\.]{4,}(?::\d+)?/[^#?]+(?:#\S+)?",re.IGNORECASE)
phone = re.compile("0[-\d\s]{10,}")
restname=re.compile("\s{2,3}(.+)\s{3}")
addr=re.compile("^(.+)(\d[A-Z]{2})$")
latlon=re.compile("(51.\d+;-0.\d+)")


fin = open("rest.txt")
lines = fin.readlines()
fin.close()

r = defaultdict(dict)
currentname = ""
for line in lines:
	m=restname.search(line)
	if m:
		currentname=m.group(1)
		continue
	m=addr.search(line)
	if m:
		zaddr=m.group(0)
		street,stuff=zaddr.split("GB -")
		stuffs=stuff.split()
		r[currentname]["street"]=street
		r[currentname]["pc"]=stuffs[-2]+" "+stuffs[-1]
		
	m=fullurl.search(line)
	if m:
		r[currentname]["url"]=m.group(0)
	m=latlon.search(line)
	if m:
		latlong =m.group(0)
		lat,lon=latlong.split(";")
		r[currentname]["latlon"]=(float(lat),float(lon))
print len(r)
fout=open("rest_out.py","w")
fout.write(str(r))
fout.close()
		 
	
