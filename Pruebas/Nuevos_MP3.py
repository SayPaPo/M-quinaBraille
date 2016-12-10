import RPi.GPIO as GPIO
import time
import os
import glob
from gtts import gTTS
import subprocess

tts = gTTS(text='Todo listo para comenzar.', lang='es')
tts.save('/home/pi/AudiosBraille/sis_audio/Listo.mp3')
