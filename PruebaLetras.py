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

print("Escriba un caracter")

po = 0
t = 1

ArIz = 13
ArDe = 23
MeIz = 18
MeDe = 24
AbIz = 19
AbDe = 26

palabra0 = sys.stdin.readline()
palabra1 = palabra0.strip()
palabra = palabra0 + " "

    
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
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "d") or (palabra[po] == "D"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "e") or (palabra[po] == "E"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "f") or (palabra[po] == "F"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "g") or (palabra[po] == "G"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "h") or (palabra[po] == "H"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "i") or (palabra[po] == "I"):
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "j") or (palabra[po] == "J"):
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "k") or (palabra[po] == "K"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "l") or (palabra[po] == "L"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "m") or (palabra[po] == "M"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "n") or (palabra[po] == "N"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "o") or (palabra[po] == "O"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "p") or (palabra[po] == "P"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "q") or (palabra[po] == "Q"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "r") or (palabra[po] == "R"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "s") or (palabra[po] == "S"):
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "t") or (palabra[po] == "T"):
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif (palabra[po] == "u") or (palabra[po] == "U"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "v") or (palabra[po] == "V"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "w") or (palabra[po] == "W"):
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "x") or (palabra[po] == "X"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "y") or (palabra[po] == "Y"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif (palabra[po] == "z") or (palabra[po] == "Z"):
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == ".":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 1)

    elif palabra[po] == ",":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "?":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == "!":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "-":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == "#":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 1)
        GPIO.output(AbDe, 1)

    elif palabra[po] == "0":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == '1':
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)
        
    elif palabra[po] == "2":
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)
        
    elif palabra[po] == "3":
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "4":
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "5":
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 0)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "6":
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "7":
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "8":
        GPIO.output(ArIz, 1)
        GPIO.output(ArDe, 0)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 1)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    elif palabra[po] == "9":
        GPIO.output(ArIz, 0)
        GPIO.output(ArDe, 1)
        GPIO.output(MeIz, 1)
        GPIO.output(MeDe, 0)
        GPIO.output(AbIz, 0)
        GPIO.output(AbDe, 0)

    po += 1
    time.sleep(t)


#GPIO.cleanup()

  
