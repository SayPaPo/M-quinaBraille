import time

l = open('El Conde de Montecristo Cap\xc3\xadtulo XXIX.txt','r')
l2 = l.readline()
l3 = l2.decode('utf8')

x = 0

while (x <= 23):
	caracter = l3[x]
	if (caracter == ' '):
		break
	else:
		print(caracter)		
	x += 1
	time.sleep(1) 						
	
