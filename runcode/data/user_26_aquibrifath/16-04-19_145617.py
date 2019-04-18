print("Hello Python World!!")
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
print "ON"
GPIO.output(8,GPIO.HIGH)
time.sleep(1)
print "Off"
GPIO.output(8,GPIO.LOW)
time.sleep(1)
print "ON"
GPIO.output(8,GPIO.HIGH)
time.sleep(1)
print "Off"
GPIO.output(8,GPIO.LOW)
time.sleep(1)
print "ON"
GPIO.output(8,GPIO.HIGH)
time.sleep(1)
print "Off"
GPIO.output(8,GPIO.LOW)
time.sleep(1)