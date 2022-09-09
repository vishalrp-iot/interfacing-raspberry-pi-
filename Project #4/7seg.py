import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

PA = 33
PB = 31
PC = 5
PD = 7
PE = 8
PF = 35
PG = 37
PH = 3

PA2 = 11
PB2 = 12
PC2 = 13
PD2 = 15
PE2 = 16
PF2 = 18
PG2 = 19
PH2 = 21

sensor = 11
pin = 21

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PA, GPIO.OUT)
GPIO.setup(PB, GPIO.OUT)
GPIO.setup(PC, GPIO.OUT)
GPIO.setup(PD, GPIO.OUT)
GPIO.setup(PE, GPIO.OUT)
GPIO.setup(PF, GPIO.OUT)
GPIO.setup(PG, GPIO.OUT)
GPIO.setup(PH, GPIO.OUT)

GPIO.setup(PA2, GPIO.OUT)
GPIO.setup(PB2, GPIO.OUT)
GPIO.setup(PC2, GPIO.OUT)
GPIO.setup(PD2, GPIO.OUT)
GPIO.setup(PE2, GPIO.OUT)
GPIO.setup(PF2, GPIO.OUT)
GPIO.setup(PG2, GPIO.OUT)
GPIO.setup(PH2, GPIO.OUT)

def disp(x):

	a = True
	b = True
	c = True
	d = True
	e = True
	f = True
	g = True
	h = True

	if x == 0:
		a = False
		b = False
		c = False
		d = False
		e = False
		f = False
		g = True
		h = True

	elif x == 1:
		a = True
		b = False
		c = False
		d = True
		e = True
		f = True
		g = True
		h = True

	elif x == 2:
		a = False
		b = False
		c = True
		d = False
		e = False
		f = True
		g = False
		h = True

	elif x == 3:
		a = False
		b = False
		c = False
		d = False
		e = True
		f = True
		g = False
		h = True

	elif x == 4:
		a = True
		b = False
		c = False
		d = True
		e = True
		f = False
		g = False
		h = True

	elif x == 5:
		a = False
		b = True
		c = False
		d = False
		e = True
		f = False
		g = False
		h = True

	elif x == 6:
		a = False
		b = True
		c = False
		d = False
		e = False
		f = False
		g = False
		h = True

	elif x == 7:
		a = False
		b = False
		c = False
		d = True
		e = True
		f = True
		g = True
		h = True

	elif x == 8:
		a = False
		b = False
		c = False
		d = False
		e = False
		f = False
		g = False
		h = True

	elif x == 9:
		a = False
		b = False
		c = False
		d = False
		e = True
		f = False
		g = False
		h = True
	else:
		print("Wrong Number")

	return a, b, c, d, e, f, g, h


'''s = input("Give a Number: ")
x = int(s[0])
y = int(s[1])
'''

try:
	while True:
		h, t = Adafruit_DHT.read_retry(sensor, pin)
		s = str(t)
		x = int(s[0])
		y = int(s[1])

		a, b, c, d, e, f, g, h = disp(x)
		GPIO.output(PA, a)
		GPIO.output(PB, b)
		GPIO.output(PC, c)
		GPIO.output(PD, d)
		GPIO.output(PE, e)
		GPIO.output(PF, f)
		GPIO.output(PG, g)
		GPIO.output(PH, h)

		a, b, c, d, e, f, g, h = disp(y)
		GPIO.output(PA2, a)
		GPIO.output(PB2, b)
		GPIO.output(PC2, c)
		GPIO.output(PD2, d)
		GPIO.output(PE2, e)
		GPIO.output(PF2, f)
		GPIO.output(PG2, g)
		GPIO.output(PH2, h)

		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
