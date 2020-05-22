import RPi.GPIO as GPIO

#setting up GPIO pins (LED's)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

forwardledpin = 14
backledpin = 23
rightledpin = 18
leftledpin = 15
GPIO.setup(forwardledpin, GPIO.OUT)
GPIO.setup(backledpin, GPIO.OUT)
GPIO.setup(rightledpin, GPIO.OUT)
GPIO.setup(leftledpin, GPIO.OUT)

def GPIOTRUE(pin):
    GPIO.output(pin, GPIO.HIGH)

def GPIOFALSE(pin):
    GPIO.output(pin, GPIO.LOW)