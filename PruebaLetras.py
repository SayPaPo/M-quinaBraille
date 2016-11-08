import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)  
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


  
x = ord((input("Ingrese una letra: "))
if x == 97:
	GPIO.output(17, 1)
        
elif x== 'b':
	GPIO.output(18, 1)
        
elif x== 'c':
	GPIO.output(23, 1)
      
