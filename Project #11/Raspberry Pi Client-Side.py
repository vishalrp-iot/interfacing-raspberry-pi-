import Adafruit_DHT
import socket
import sys
import time
import datetime

Sensor_NO = 1

sensor = 11
pin = 14

host = "192.168.255.254"
port = 8000

addr = (host, port)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(addr)

print("Connected")
try:
	while True:
		h, t = Adafruit_DHT.read_retry(sensor, pin)

		time1 = datetime.datetime.now()
		day = time1.day
		month = time1.month
		year = time1.year
		hour = time1.hour
		min = time1.minute
		sec = time1.second

		msg_str = "{Sensor_NO} {h} {t} {day} {month} {year} {hour} {min} {sec}".format(Sensor_NO=Sensor_NO, h=h, t=t, day=day, month=month, year=year, hour=hour, min=min, sec=sec)
		print(msg_str)

		socket.send(msg_str.encode())
		time.sleep(10)

except KeyboardInterrupt:
	socket.close()
	sys.exit()

except BrokenPipeError:
	print("\nConnection closed from Server")
	sys.exit()

