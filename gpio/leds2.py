import RPi.GPIO as GPIO
import sys
import signal
from time import sleep

inputPin = 3
pin1 = 11
pin2 = 12
pin3 = 13
pin4 = 15
pin5 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
GPIO.setup(inputPin, GPIO.IN)
GPIO.add_event_detect(inputPin, GPIO.RISING)

toCross = True
def cross():
	global toCross
	if toCross:
		GPIO.output(pin1, GPIO.HIGH)
		GPIO.output(pin2, GPIO.HIGH)
		GPIO.output(pin3, GPIO.HIGH)
		GPIO.output(pin4, GPIO.LOW)
		GPIO.output(pin5, GPIO.LOW)
		toCross = False
	else:
		GPIO.output(pin4, GPIO.HIGH)
		GPIO.output(pin5, GPIO.HIGH)
		GPIO.output(pin1, GPIO.LOW)
		GPIO.output(pin2, GPIO.LOW)
		GPIO.output(pin3, GPIO.LOW)
		toCross = True


if GPIO.event_detected(inputPin):
	cross()

def sigintHandler(signal, frame):
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, sigintHandler)
while 1:
	if GPIO.event_detected(inputPin):
		cross()
	
