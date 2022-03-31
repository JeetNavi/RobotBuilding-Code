import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
#CHANGE 24 TO WHICHEVER GPIO PIN YOU'RE USING
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        GPIO.output(24, 1)
        sleep(0.5)
        if GPIO.input(24):
            print "1"
        else:
            print "0"
except KeyboardInterrupt:
    GPIO.cleanup()
