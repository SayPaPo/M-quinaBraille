import win32com.client
import pyttsx

engine = pyttsx.init()

engine.setProperty('voice', "spanish-latin-american")

engine.say('Esta es una prueba de reproduccion de texto')
engine.say('fin')

engine.runAndWait()
