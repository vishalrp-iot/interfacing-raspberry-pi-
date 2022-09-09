import sys
import socket
import Adafruit_DHT
import time
import datetime
from threading import Thread

sensor = 11
pin = 14

host = ""
port = 5000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (host, port)
socket.bind(addr)

socket.listen(5)


def main():
	while True:
		sock, addr = socket.accept()
		print("accepted")
		new_thread = Client_Thread(sock, addr)
		new_thread.start()


class Client_Thread(Thread):
	def __init__(self, socket, addr):
		try:
			Thread.__init__(self)
			self.socket = socket
			self.addr = addr
			print("Thread Created")
		except KeyboardInterrupt:
			socket.close()
			sys.exit()


	def run(self):
		try:
			print("Thread Started")
			while True:
				h, t = Adafruit_DHT.read_retry(sensor, pin)

				cur_time = datetime.datetime.now()
				day = cur_time.day
				month = cur_time.month
				year = cur_time.year
				hour = cur_time.hour
				min = cur_time.minute
				sec = cur_time.second

				msg_str = "{h} {t} {d} {m} {y} {hour} {min} {sec}\n".format(h=h,t=t,d=day,m=month,y=year,hour=hour,min=min,sec=sec)
				print(msg_str)

				(self.socket).send(msg_str.encode())
				time.sleep(5)


		except KeyboardInterrupt:
			socket.close()
			sys.exit()


main()

