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
l = open('El Conde de Montecristo Cap\xc3\xadtulo XXIX.txt','r')
l2 = l.readline()
l3 = l2.decode('utf8')

po = 0
t = 1

ArIz = 13
ArDe = 23
MeIz = 18
MeDe = 24
AbIz = 19
AbDe = 26

#palabra0 = sys.stdin.readline()
#palabra1 = palabra0.decode('utf8')
#palabra2 = palabra1.strip()
palabra2 = l3.strip()
palabra = palabra2 + " "

    
while (po <= 23):

    if (palabra[po] == ' '):
        print("espacio")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)
        break
    


    elif (palabra[po] == 'a') or (palabra[po] == 'A'):
        print("a")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)
    
    elif (palabra[po] == "b") or (palabra[po] == "B"):
        print("b")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)
        
    elif (palabra[po] == "c") or (palabra[po] == "C"):
	print("c")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "d") or (palabra[po] == "D"):
        print("d")
	GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "e") or (palabra[po] == "E"):
	print("e")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "f") or (palabra[po] == "F"):
	print("f")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "g") or (palabra[po] == "G"):
	print("g")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "h") or (palabra[po] == "H"):
	print("h")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "i") or (palabra[po] == "I"):
	print("i")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "j") or (palabra[po] == "J"):
	print("j")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "k") or (palabra[po] == "K"):
	print("k")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "l") or (palabra[po] == "L"):
	print("l")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "m") or (palabra[po] == "M"):
	print("m")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "n") or (palabra[po] == "N"):
	print("n")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "o") or (palabra[po] == "O"):
	print("o")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "p") or (palabra[po] == "P"):
	print("p")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "q") or (palabra[po] == "Q"):
	print("q")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "r") or (palabra[po] == "R"):
	print("r")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "s") or (palabra[po] == "S"):
	print("s")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "t") or (palabra[po] == "T"):
	print("t")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "u") or (palabra[po] == "U"):
	print("u")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "v") or (palabra[po] == "V"):
	print("v")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "w") or (palabra[po] == "W"):
	print("w")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "x") or (palabra[po] == "X"):
	print("x")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "y") or (palabra[po] == "Y"):
	print("y")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "z") or (palabra[po] == "Z"):
	print("z")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == ".":
	print(".")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 1)

    elif palabra[po] == ",":
	print(",")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "?":
	print("?")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == "!":
	print("!")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "-":
	print("-")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == "#":
	print("#")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == "0":
	print("cero")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == '1':
	print("uno")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)
        
    elif palabra[po] == "2":
	print("dos")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)
        
    elif palabra[po] == "3":
	print("tres")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "4":
	print("cuatro")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "5":
	print("cinco")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "6":
	print("seis")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "7":
	print("siete")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "8":
	print("ocho")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "9":
	print("nueve")
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    else:
	print("Caracter no registrado")
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    po += 1
    time.sleep(t)


#GPIO.cleanup()

  
