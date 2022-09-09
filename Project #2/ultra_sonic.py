import RPi.GPIO as GPIO
import time
import sys

TRIGGER = 4
ECHO = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIGGER, GPIO.LOW)
time.sleep(2)

start_time = 0
end_time = 0

try:
	while True:
		GPIO.output(TRIGGER, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(TRIGGER, GPIO.LOW)

		while GPIO.input(ECHO) == 0:
			start_time = time.time()
		while GPIO.input(ECHO) == 1:
			end_time = time.time()

		duration = end_time - start_time
		distance = round(duration*17150, 2)

		print("Distance :{x}cm\n".format(x=distance))
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
