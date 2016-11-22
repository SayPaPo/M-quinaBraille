import RPi.GPIO as GPIO
import time
import os
import glob
from gtts import gTTS
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.IN)

os.chdir('/media/pi/SAYP1/Maquina_Braille')
archivos = glob.glob('*.txt')

nom_archivo = 0
entrada_anterior =  0

while True:
    entrada = GPIO.input(27)
    if ((not entrada_anterior) and entrada):
        print('Encendido')
    entrada_anterior = entrada
    time.sleep(0.05)

#def rep_nomb_archivos(mp3):
#        subprocess.Popen(['mpg123','-q', mp3]).wait() 

def reproducir(texto): #Este proceso reproduce texto.
        tts = gTTS(text=texto, lang='es')
        tts.save('/home/pi/AudiosBraille/AudioTemporal.mp3')
        subprocess.Popen(['mpg123','-q','AudioTemporal.mp3']).wait()

for libros in archivos: #Este proceso guarda cada uno de los nombres de archivo en archivos de audio.
        tts = gTTS(text=libros, lang='es')
        tts.save('/home/pi/AudiosBraille/titulo_%s.mp3' % nom_archivo)
        nom_archivo += 1

while True:
    entrada = GPIO.input(27)
    if ((not entrada_anterior) and entrada):
        subprocess.Popen(['mpg123','-q','/home/pi/AudiosBraille/titulo_0.mp3']).wait()
#        rep_nomb_archivos('/home/pi/AudiosBraille/titulo_0.mp3')
        print('Encendido')
    entrada_anterior = entrada
    time.sleep(0.05)
    nom_archivo += 1



#l = open('El Conde de Montecristo Cap\xc3\xadtulo XXIX.txt','r')
#l2 = l.readline()
#l2 = l2.decode('utf8')

#x = 0

#while (x <= 23):
#	caracter = l2[x]
#	if (caracter == ' '):
#		break
#	else:
#		print(caracter)		
#	x += 1
#	time.sleep(1) 						
	
