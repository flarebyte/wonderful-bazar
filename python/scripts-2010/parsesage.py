from urlparse import urlparse,parse_qs
import string
import smtplib
from email.mime.text import MIMEText
import hashlib



sage_direct="http://su.sageanalyst.net/NS?ci=775&di=d002&pg=&ai=aMNO:,hn:www.bbc.co.uk,uri:%2Fmobile%2Fsearch%2Fsearchpagev2%2F,qs:q%3Dpirate%26x%3D30%26y%3D4,sx:pirate,rf:http://www.test.bbc.co.uk/mobile/search/v2/index,eid:0,ct:,db:,dm:,rs:x,um:,uu:346a9f9da38e270a736d5b26a1845ee551591c5e5070215414bfd99ff5c8f14e"
sage_proxy="http://212.62.17.219/NS?ci=775&di=d002&pg=&qs=q=sarkozy&x=0&y=0&ai=uri:/mobile/search/searchpagev2,rf:http://www.test.bbc.co.uk/mobile/search/searchpagev2,eid:0,hn:www.test.bbc.co.uk,ip:132.185.240.124,ct:-1,aMNO:BBC,db:,dm:,rs:,uu:346a9f9da38e270a736d5b26a1845ee551591c5e5070215414bfd99ff5c8f14e,um:11_8_4___G10__CD9_11__CK12_14_15_3_,ump:1,ext:mobile-xhtml,test:proxy,sx:sarkozy"


def sage_to_map(sage_query):
	o = urlparse(sage_query)
	query=parse_qs(o.query)
	#print query
	ai=query["ai"][0]
	ci=query["ci"][0]
	di=query["di"][0]

	r = {}
	r['ci']=ci
	r['di']=di

	ai_params = ai.split(",")

	for param in ai_params:
		sep_pos = param.find(':')
		if sep_pos != 1:
			k = param[:sep_pos]
			v = param[sep_pos+1:]
			r[k]=v
	return r
	
KEYNOTFOUNDIN1 = '<KEYNOTFOUNDIN1>'       # KeyNotFound for dictDiff
KEYNOTFOUNDIN2 = '<KEYNOTFOUNDIN2>'       # KeyNotFound for dictDiff

def dict_diff(first, second):
    """ Return a dict of keys that differ with another config object.  If a value is
        not found in one fo the configs, it will be represented by KEYNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dicationary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    diff = {}
    sd1 = set(first)
    sd2 = set(second)
    #Keys missing in the second dict
    for key in sd1.difference(sd2):
        diff[key] = KEYNOTFOUNDIN2
    #Keys missing in the first dict
    for key in sd2.difference(sd1):
        diff[key] = KEYNOTFOUNDIN1
    #Check for differences
    for key in sd1.intersection(sd2):
        if first[key] != second[key]:
            diff[key] = (first[key], second[key])    
    return diff


m1=sage_to_map(sage_direct)	
m2=sage_to_map(sage_proxy)

print m1['rf']
diff = dict_diff(m1,m2)

print diff
	
mylog = open ( 'D:/data/temp/parsesage.log', 'w' ) 
mylog.write(str(m1))
m1_sum = hashlib.md5(str(m1)).hexdigest()
mylog.write("\n---\n")
mylog.write(str(m2))
m2_sum = hashlib.md5(str(m2)).hexdigest()
mylog.write("\n---Differences:\n")
mylog.write("\n"+m1_sum+"/"+m2_sum+"\n")
mylog.write(str(diff))
mylog.write("\n---\n")
mylog.close()
