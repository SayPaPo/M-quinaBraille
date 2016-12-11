import RPi.GPIO as GPIO
import time
import os
import glob
from gtts import gTTS
import subprocess

tts = gTTS(text='Ha pausado la reproducción.', lang='es')
tts.save('/home/pi/AudiosBraille/sis_audio/Pausa.mp3')
