import RPi.GPIO as GPIO
import time
import os
import sys
import glob
from gtts import gTTS
import subprocess
import MaquinaBraille
import threading

MaquinaBraille.Iniciar() #Establece el directorio de trabajo y la configuracion de pines GPIO.
archivos = glob.glob('*.txt') #Crea un vector de nombres de los archivos en la llave. 
				#Se saco de Estadisticas_Memoria() para que se ejecute primero. 
subprocess.Popen(['mpg123','-q','/home/pi/AudiosBraille/sis_audio/Bienvenido2.mp3']).wait()


thread_inicial = 0

evento = threading.Event()

arc = 0 #Se utiliza en Reproduccion_Titulos()
arc_0 = 0


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

def Estadisticas_Archivo(archivos):

        global arc_0
        nombre = '/home/pi/AudiosBraille/Ests_archs_%s.mp3' % arc_0
        subprocess.Popen(['mpg123','-q',nombre]).wait()

vtexto = [] #
largo_vtexto = 0

def Rep_B0():
        
        global arc_0
        global vtexto
        global largo_vtexto
        fname = archivos[arc_0]
        texto = open(fname,'r')
        vtexto = texto.readlines()
        largo_vtexto = len(vtexto)

largo_vpalabras = 0
vpalabras = []
def Rep_B1(x):
        
        global vtexto
        global vpalabras
        global largo_vpalabras
        parrafo = vtexto[x]
        parrafo = parrafo.decode('utf8')
        vpalabras = parrafo.split()
        largo_vpalabras = len(vpalabras)

largo_vletra = 0
vletra=[]
def Rep_B2(y):
        global largo_vletra
        global vletra
        palabra = y
        palabra = palabra + ' '
        vletra = list(palabra)
        largo_vletra = len(vletra)
        

#def Control_Reproduccion():
        
        #global thread_inicial
        #Rep_B0()
        #for i1 in range(largo_vtexto):
                #Rep_B1(i1)
                #for i2 in range(largo_vpalabras):
                        #y = vpalabras[i2]
                        #Rep_B2(y)
                        #for i3 in range(largo_vletra):
                                #y2 = vletra[i3]
                                #MaquinaBraille.Reproduccion_B2(y2)

                                #print evento.wait(0)
                                #nuevo_thread(thread_inicial,y2)
                                #time.sleep(1)
                                #thread_inicial += 1
                                #print 'fin de caracter'
                        

def nuevo_thread(numero):
        t_numero = threading.Thread(target=Reproduccion_Braille, args=(evento,))
        t_numero.start()
        #t_numero.join()

def Reproduccion_Braille(evento):
        while (not evento.wait(0)):
                global thread_inicial
                Rep_B0()
                for i1 in range(largo_vtexto):
                        Rep_B1(i1)
                        for i2 in range(largo_vpalabras):
                                y = vpalabras[i2]
                                Rep_B2(y)
                                for i3 in range(largo_vletra):
                                        y2 = vletra[i3]
                                        MaquinaBraille.Reproduccion_B2(y2)
                #print evento.wait(0.01)
                #Control_Reproduccion()
                break
def menu():

        entrada_anterior0 = 0
        entrada_anterior1 = 0
        entrada_anterior2 = 0
        entrada_anterior3 = 0
        entrada_anterior4 = 0

        pausa = 0

        global thread_inicial
        
        while True:

                entrada0 = GPIO.input(4)
                if ((not entrada_anterior0) and entrada0):
                        MaquinaBraille.Estadisticas_Memoria() #Cuenta la cantidad de archivos en memoria y lo reproduce en audio.
                entrada_anterior0 = entrada0
                time.sleep(0.05)


                entrada1 = GPIO.input(17)
                if ((not entrada_anterior1) and entrada1):
                        Repruccion_Titulos(archivos) #Reproduce los titulos presentes en la memoria, uno por cada clic. 
                entrada_anterior1 = entrada1
                time.sleep(0.05)

                entrada3 = GPIO.input(22)
                if ((not entrada_anterior3) and entrada3):
                        print pausa
                        if pausa == 0:
                                evento.clear()
                                nuevo_thread(thread_inicial)
                                thread_inicial += 1
                                pausa = 1
                                
                        elif pausa == 1:
                                evento.set()
                                pausa = 0
                entrada_anterior3 = entrada3
                time.sleep(0.05)

                entrada2 = GPIO.input(27)
                if ((not entrada_anterior2) and entrada2):
                        Estadisticas_Archivo(archivos)
                        print('Estadisticas de archivo') #Reproduccion de las estadisticas del archivo selecionado.
                entrada_anterior2 = entrada2
                time.sleep(0.05)       

                entrada4 = GPIO.input(5)
                if ((not entrada_anterior4) and entrada4):
                        MaquinaBraille.Estadisticas(archivos) #Crea los titulos de los archivos en formato audio.
                entrada_anterior4 = entrada4
                time.sleep(0.05)

p = threading.Thread(target=menu)
p.start()
	
