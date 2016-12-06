import RPi.GPIO as GPIO
import time
import os
import glob
from gtts import gTTS
import subprocess

tts = gTTS(text='Final de la lista', lang='es')
tts.save('/home/pi/AudiosBraille/sis_audio/FL.mp3')
