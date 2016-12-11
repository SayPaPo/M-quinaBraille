#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os
import sys
import glob
from gtts import gTTS
import subprocess
import threading

arc = 0 #Se utiliza en Reproduccion_Titulos()
arc_0 = 0
entrada_anterior0 = 0

ArIz = 20
ArDe = 21
MeIz = 12
MeDe = 16
AbIz = 24
AbDe = 25

def Iniciar():

        global ArIz
        global ArDe
        global MeIz
        global MeDe
        global AbIz
        global AbDe

        os.chdir('/media/pi/SAYP1')
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

        GPIO.setup(4, GPIO.IN) #Reproducir cantidad de archivos.
        GPIO.setup(17, GPIO.IN) #Reproducir titulos de los archivos.
        GPIO.setup(27, GPIO.IN) #Estadisticas del archivo
        GPIO.setup(22, GPIO.IN) #Inicio de reproduccion
        GPIO.setup(5, GPIO.IN)
        GPIO.setup(6, GPIO.IN)
        GPIO.setup(13, GPIO.IN)        
        
	GPIO.setup(ArIz, GPIO.OUT)  
	GPIO.setup(ArDe, GPIO.OUT)
	GPIO.setup(MeIz, GPIO.OUT)
	GPIO.setup(MeDe, GPIO.OUT)
	GPIO.setup(AbIz, GPIO.OUT)
	GPIO.setup(AbDe, GPIO.OUT)

def Estadisticas_Archivo(archivos):

        global arc_0
        nombre = '/home/pi/AudiosBraille/Ests_archs_%s.mp3' % arc_0
        subprocess.Popen(['mpg123','-q',nombre]).wait()

def Estadisticas_Memoria():

        subprocess.Popen(['mpg123','-q','/home/pi/AudiosBraille/men1.mp3']).wait()

def Estadisticas(archivos):

        subprocess.Popen(['mpg123','-q','/home/pi/AudiosBraille/sis_audio/Bienvenido.mp3']).wait()

        nom_archivo = 0

        for libros in archivos: #Este proceso guarda cada uno de los nombres de archivo en archivos de audio.
                tts = gTTS(text=libros, lang='es')
                tts.save('/home/pi/AudiosBraille/titulo_%s.mp3' % nom_archivo)
                nom_archivo += 1
        print('Nombres de archivos listos')

        numero = len(archivos)
        men1 = 'La memoria contiene %s archivos de texto' % numero
        tts = gTTS(text= men1, lang='es')
        tts.save('/home/pi/AudiosBraille/men1.mp3')
        print('Cantidad de archivos guardada')

        nom_archivo1 = 0
        
        for libros in archivos:
                        
                l = open(libros,'r')
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

                men2 = 'El archivo llamado %s contiene %s p\xc3\xa1rrafos y %s saltos de l\xc3\xadnea' % (libros, parrafos, saltos)
                tts = gTTS(text=men2, lang='es')
                tts.save('/home/pi/AudiosBraille/Ests_archs_%s.mp3' % nom_archivo1)
                nom_archivo1 += 1
                
        print('Estadisticas de archivos lista')
        subprocess.Popen(['mpg123','-q','/home/pi/AudiosBraille/sis_audio/Listo.mp3']).wait()

def Repruccion_Titulos(archivos): 

        global arc
        global arc_0
        titulo = '/home/pi/AudiosBraille/titulo_%s.mp3' % arc 
        subprocess.Popen(['mpg123','-q',titulo]).wait() 
        print(arc)
        print(arc_0)

        if (arc == (len(archivos)-1)):
                subprocess.Popen(['mpg123','-q','/home/pi/AudiosBraille/sis_audio/FL.mp3']).wait()
                arc = 0
                arc_0 = len(archivos)-1
        else:
                arc_0 = arc        
                arc += 1

t = 1
vtexto = []
parrafo = []

def Reproduccion_B0(archivos):

        global arc_0
        global vtexto

        fname = archivos[arc_0]
        texto = open(fname,'r')
        vtexto = texto.readlines()

def Reproduccion_B1():

        global parrafo
#        r = threading.Thread(target=Reproduccion_B2)

        for parrafo in vtexto:

                parrafo = parrafo.decode('utf8')
                parrafo = parrafo.strip()
                parrafo = parrafo + ' '
                print(parrafo)
#                r.start()
                Reproduccion_B2()

def Reproduccion_B2():

        global t

        global parrafo

        global ArIz
        global ArDe
        global MeIz
        global MeDe
        global AbIz
        global AbDe
        
            
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

  
