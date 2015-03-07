import RPi.GPIO as GPIO
from time import sleep

pin1 = 11
pin2 = 12
pin3 = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

var = pin1
for x in range(1,50):
	GPIO.output(pin1, GPIO.LOW)
	GPIO.output(pin2, GPIO.LOW)
	GPIO.output(pin3, GPIO.LOW)
	
	if var == pin1:
		GPIO.output(pin1, GPIO.HIGH)
		var = pin2
	elif var == pin2:
		GPIO.output(pin2, GPIO.HIGH)
		var = pin3
	elif var == pin3:
		GPIO.output(pin3, GPIO.HIGH)
		var = pin1
	
	sleep(0.1)


GPIO.cleanup()
