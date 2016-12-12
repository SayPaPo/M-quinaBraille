import RPi.GPIO as GPIO
import time
import os
import glob
from gtts import gTTS
import subprocess

tts = gTTS(text='Bienvenido, si desea crear nuevas estadísticas sobre los archivos guardados en la memoria presiene el botón llamado cargar estadísticas', lang='es')
tts.save('/home/pi/AudiosBraille/sis_audio/Bienvenido2.mp3')
