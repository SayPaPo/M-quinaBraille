import RPi.GPIO as GPIO
import time
import os
import sys
import glob
from gtts import gTTS
import subprocess
import MaquinaBraille

MaquinaBraille.Iniciar() #Establece el directorio de trabajo y la configuracion de pines GPIO.
archivos = glob.glob('*.txt') #Crea un vector de nombres de los archivos en la llave. Se saco de Estadisticas_Memoria() para que se ejecute primero. 
MaquinaBraille.Estadisticas(archivos) #Crea los titulos de los archivos en formato audio.

entrada_anterior0 = 0
entrada_anterior1 = 0
entrada_anterior2 = 0
entrada_anterior3 = 0

while True:
        entrada0 = GPIO.input(27)
        if ((not entrada_anterior0) and entrada0):
                MaquinaBraille.Estadisticas_Memoria() #Cuenta la cantidad de archivos en memoria y lo reproduce en audio.
        entrada_anterior0 = entrada0
        time.sleep(0.05)


        entrada1 = GPIO.input(17)
        if ((not entrada_anterior1) and entrada1):
                MaquinaBraille.Repruccion_Titulos(archivos) #Reproduce los titulos presentes en la memoria, uno por cada clic. 
        entrada_anterior1 = entrada1
        time.sleep(0.05)

        entrada2 = GPIO.input(5)
        if ((not entrada_anterior2) and entrada2):
                MaquinaBraille.Estadisticas_Archivo(archivos)
                print('Estadisticas de archivo') #Reproduccion de las estadisticas del archivo selecionado.
        entrada_anterior2 = entrada2
        time.sleep(0.05)       

        pausa = 0

        entrada3 = GPIO.input(12)
        if ((not entrada_anterior3) and entrada3):
                MaquinaBraille.Reproduccion_B(archivos)
                print('Inicio de reproduccion')
                pausa += 1
                print(pausa)
        entrada_anterior3 = entrada3
        time.sleep(0.05) 	
	
