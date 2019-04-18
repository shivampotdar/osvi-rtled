print("Hello Python World!!")
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
print ("LED on")
GPIO.output(8,GPIO.HIGH)