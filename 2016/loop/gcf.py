
def lcm(a,b):
	m=a*b
	while a!=0 and b!=0:
		if a>b:
			a%=b
		else:
		 b%=a
	return m//(a+b)
	
while 1:
	try:
		x=int(intput('a='))
		y=int(intput('b='))
		print ('НОК:',lcm(x,y))
	except:
		break
		
