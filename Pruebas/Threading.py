import RPi.GPIO as GPIO
import time
import os
import sys
import glob
from gtts import gTTS
import subprocess
#import MaquinaBraille
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN) 
entrada_anterior0 = 0
pausa = 0
thread_inicial = 0

def mensaje(evento_p):
#    while True:
    while not evento_p.wait(0.5):
        print 'Hola'
    print 'Detenido'


evento = threading.Event()
#t1= threading.Thread(target=mensaje, args=(evento,))
#t1.deamon = True
#t.join()

def nuevo_thread(numero):
    t_numero = threading.Thread(target=mensaje, args=(evento,))
    t_numero.start()

while True:

    #print t.is_alive()

    entrada0 = GPIO.input(4)
    if ((not entrada_anterior0) and entrada0):
        if entrada_anterior0 == 0:
            if pausa == 0:
                evento.clear()
                nuevo_thread(thread_inicial)
                pausa = 1
                thread_inicial += 1
            elif pausa == 1:
                evento.set()
                pausa = 0
                                
    entrada_anterior0 = entrada0
    time.sleep(0.05)


