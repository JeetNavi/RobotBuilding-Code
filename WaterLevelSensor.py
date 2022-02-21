import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    while True:
        GPIO.output(18, 1)
        sleep(0.5)
        if GPIO.input(18):
            print "1"
        else:
            print "0"
except KeyboardInterrupt:
    GPIO.cleanup()
