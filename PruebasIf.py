x = int(input("Ingrese un numero entero: "))
if x < 0:
	x = 0
	print('Numero negativo')
elif x==0:
	print('Cero')
elif x==1:
	print('Uno')
else:
	print('Numero diferente a 0 y 1')
