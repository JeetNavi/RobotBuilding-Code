#CHANGE 24 TO WHICHEVER GPIO PIN WATER PUMP IS CONNECTED TO

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

GPIO.output(24, 1)
sleep(20)


GPIO.cleanup()
