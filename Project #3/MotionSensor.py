import RPi.GPIO as GPIO
import time
import sys

IN = 4
OUT = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN, GPIO.IN)
GPIO.setup(OUT, GPIO.OUT)

try:
	while True:
		if GPIO.input(4) == 1:
			GPIO.output(OUT, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(OUT, GPIO.LOW)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
