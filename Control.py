import RPi.GPIO as GPIO
import time
import os
import sys
import glob
from gtts import gTTS
import subprocess
import MaquinaBraille

MaquinaBraille.Iniciar()
MaquinaBraille.Nombre_Archivo()

entrada_anterior0 =  0
entrada_anterior1 = 0


while True:
        entrada = GPIO.input(27)
        if ((not entrada_anterior0) and entrada):
                MaquinaBraille.Estadisticas_Memoria()
        entrada_anterior0 = entrada
        time.sleep(0.05)


        entrada = GPIO.input(17)
        if ((not entrada_anterior1) and entrada):
                MaquinaBraille.Repruccion_Titulos()
        entrada_anterior1 = entrada
        time.sleep(0.05)    
		
	
