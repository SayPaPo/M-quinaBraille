l = open('El Conde de Montecristo Cap\xc3\xadtulo XXIX.txt','r')
v = l.readlines()

parrafos = 0
saltos = 0

for linea in v:
	

	if (linea == '\n'):
		saltos += 1
		
	elif (linea == '\r'):
		saltos += 1
		
	elif (linea == '\r\n'):
		saltos += 1
		
	else:
		parrafos += 1
		
mensaje = "El archivo tiene " + repr(parrafos) + " parrafos y " + repr(saltos) + " l\xc3\xadneas en blanco."
print(mensaje)