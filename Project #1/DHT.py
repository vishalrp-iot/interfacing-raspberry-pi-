import time
import sys
import Adafruit_DHT

sensor = 11
pin = 14

try:
	while True:
		h, t = Adafruit_DHT.read_retry(sensor, pin)
		print("Tempreture :{x}C, Humidity :{y}%\n".format(x = t, y = h))
		time.sleep(1)

except:
	sys.exit()
