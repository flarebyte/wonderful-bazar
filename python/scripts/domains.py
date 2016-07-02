a=["b","d","p","q","f","7","e","3","z","s"]
sym=["u","i","o","x","n","m","w","8"]
m={"d":"b","b":"d","q":"p","p":"q","7":"f","f":"7","3":"e","e":"3","z":"s","s":"z"}

def cinq():
	for i in a:
		for j in a:
			for k in sym:
				print i,j,k,m[j],m[i]

def trois():
	for i in a:
			for k in sym:
				print i,k,m[i]

def quatre():
	for i in a:
		for j in a:
				print i,j,m[j],m[i]

def quatre2():
	for i in a:
			for k in sym:
				print i,k,k,m[i]


def quatre3():
	for i in a:
			for k in sym:
				print k,i,m[i],k
				
quatre3()
