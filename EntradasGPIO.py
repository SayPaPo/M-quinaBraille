import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.IN)

entrada_anterior =  0

while True:
    entrada = GPIO.input(27)
    if ((not entrada_anterior) and entrada):
        print('Encendido')
    entrada_anterior = entrada
    time.sleep(0.05)
