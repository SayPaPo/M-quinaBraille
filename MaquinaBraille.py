import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT)  
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#print("Escriba un caracter")
texto = open('TextoParrafos.txt','r')
vtexto = texto.readlines()


po = 0
t = 1

ArIz = 13
ArDe = 23
MeIz = 18
MeDe = 24
AbIz = 19
AbDe = 26

for parrafo in vtexto:

    parrafo = parrafo.decode('utf8')
    parrafo = parrafo.strip()
    parrafo = parrafo + ' '
    
    for letra in parrafo:

	    if (letra== ' '):
		print("espacio")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== 'a') or (letra== 'A'):
		print("a")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== u'\xe1'):
		print(u'\xe1')
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)
	    
	    elif (letra== "b") or (letra== "B"):
		print("b")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)
		
	    elif (letra== "c") or (letra== "C"):
		print("c")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== "d") or (letra== "D"):
		print("d")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== "e") or (letra== "E"):
		print("e")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== u'\xe9'):
		print(u'\xa9')
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== "f") or (letra== "F"):
		print("f")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== "g") or (letra== "G"):
		print("g")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== "h") or (letra== "H"):
		print("h")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== "i") or (letra== "I"):
		print("i")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== u'\xed'):
		print(u'\xed')
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "j") or (letra== "J"):
		print("j")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif (letra== "k") or (letra== "K"):
		print("k")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "l") or (letra== "L"):
		print("l")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "m") or (letra== "M"):
		print("m")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "n") or (letra== "N"):
		print("n")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== u'\xf1'):
		print(u'\xf1')
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "o") or (letra== "O"):
		print("o")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== u'\xf3'):
		print(u'\xf3')
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "p") or (letra== "P"):
		print("p")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "q") or (letra== "Q"):
		print("q")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "r") or (letra== "R"):
		print("r")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "s") or (letra== "S"):
		print("s")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "t") or (letra== "T"):
		print("t")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif (letra== "u") or (letra== "U"):
		print("u")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif (letra== u'\xfa'):
		print(u'\xfa')
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif (letra== "v") or (letra== "V"):
		print("v")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif (letra== "w") or (letra== "W"):
		print("w")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 1)

	    elif (letra== "x") or (letra== "X"):
		print("x")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif (letra== "y") or (letra== "Y"):
		print("y")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif (letra== "z") or (letra== "Z"):
		print("z")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif letra== ".":
		print(".")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 1)

	    elif letra== ",":
		print(",")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== "?":
		print("?")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif letra== "!":
		print("!")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 0)

	    elif letra== "-":
		print("-")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif letra== "#":
		print("#")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    elif letra== "0":
		print("cero")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== '1':
		print("uno")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)
		
	    elif letra== "2":
		print("dos")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)
		
	    elif letra== "3":
		print("tres")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== "4":
		print("cuatro")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== "5":
		print("cinco")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 0)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== "6":
		print("seis")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== "7":
		print("siete")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== "8":
		print("ocho")
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 0)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    elif letra== "9":
		print("nueve")
		GPIO.output(ArIz, 0)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 0)
		GPIO.output(AbIz, 0)
		GPIO.output(AbDe, 0)

	    else:
		print("Caracter no registrado")
		print(letra)
		GPIO.output(ArIz, 1)
		GPIO.output(ArDe, 1)
		GPIO.output(MeIz, 1)
		GPIO.output(MeDe, 1)
		GPIO.output(AbIz, 1)
		GPIO.output(AbDe, 1)

	    time.sleep(t)


#GPIO.cleanup()

  
