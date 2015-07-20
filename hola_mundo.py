'''
print"hola mundo"
print"hola, como estas?"

for i in xrange(0,5):
	print i
	
conjunto1 = set([1, 2, 3, 4])
conjunto2 = set([1, 2, 3, 6, 10])

print conjunto1 | conjunto2
print conjunto1 & conjunto2

x=-12
if type(x) is int:
	if x<0:
		print "es un numero negativo"
	elif x>0:
		print "es un entero"
	else:
		print "es cero"


num = raw_input("Introduzca un numero ")
print num


import math
def exacta(x):
	y = math.sqrt(x)
	if int(y)==y:
		return True
	else:
		return False
'''
import pdb
def f(x):
	if x%2 is 0:
		pdb.set_trace()
		y = True
	else:
		y=False
	return y
print filter(lambda x:f(x), [1,2,3,4,5])
#print [x for x in xrange(1, 100) if not f(x) and exacta(x)] 


'''
#recibe solamente 2 paramentros
print reduce(lambda x, y: x+y, [1,2,3,4,5])
#recibe solamente 1 paramentro
print map(lambda x: x*2, [1,2,3,4,5])
'''
'''
for i in xrange(1, 10):
	print i%2==0 and "es par" or (i==3 and "es tres" or "es =! de 3")
'''
