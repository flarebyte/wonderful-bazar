from datetime import date,timedelta

day = date.today()
delta = timedelta(days=1)
mon=None
tue=None
wed=None
thu=None
fri=None
sat=None
sun=None
week=None
month=None

f = open("calendar.csv", "w")
f.write("when,what\n")

for i in range(1, 130):
	week=day.strftime("%U")
	if (day.isoweekday()==1):
		mon=day.strftime("%d")
		month=day.strftime("%B")
	if (day.isoweekday()==2):
		tue=day.strftime("%d")
	if (day.isoweekday()==3):
		wed=day.strftime("%d")
	if (day.isoweekday()==4):
		thu=day.strftime("%d")
	if (day.isoweekday()==5):
		fri=day.strftime("%d")
	if (day.isoweekday()==6):
		sat=day.strftime("%d/%m")
	if (day.isoweekday()==7):
		sun=day.strftime("%d/%m")
		f.write("Week "+week+" : ["+mon+"-"+tue+"-"+wed+"-"+thu+"-"+fri+"] "+month+",\n")
		f.write("WE "+week+" : "+sat+"-"+sun+",\n")
	
	day = day +delta

f.close
