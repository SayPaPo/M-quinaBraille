l = open('El Conde de Montecristo Cap\xc3\xadtulo XXIX.txt','r')

parrafos = 0
saltos = 0
l2 = l.readline()

while (parrafos <=1000):
	if (l2 == ''):
		mensaje = "El archivo tiene " + repr(parrafos) + " parrafos y " + repr(saltos) + " l\xc3\xadneas en blanco."
		print(mensaje)
		break
	elif (l2 == '\n'):
		saltos += 1
		l2 = l.readline()
	elif (l2 == '\r'):
		saltos += 1
		l2 = l.readline()
	elif (l2 == '\r\n'):
		saltos += 1
		l2 = l.readline()
	else:
		parrafos += 1
		l2 = l.readline()
	