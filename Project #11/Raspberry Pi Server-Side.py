import socket
import sys
from threading import Thread
import mysql.connector

class Client(Thread):
	def __init__(self, connect, addr):
		Thread.__init__(self)
		self.connect = connect
		self.addr = addr

	def run(self):
		try:
			while True:
				data = (self.connect).recv(1024)
				data = data.decode()
				data = data.split()

				query = f"INSERT INTO data_table VALUES('#{data[0]}', '{data[5]}-{data[4]}-{data[3]}', '{data[6]}:{data[7]}:{data[8]}', {data[2]}, {data[1]})"

				try:
					cursor.execute(query)
					conn.commit()
					print(f"Table Updated by Sensor #{data[0]}")
				except:
					conn.rollback()
					continue
		except:
			print("Client Closed Connection")


host = ""
port = 8000

addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind(addr)

try:
	conn = mysql.connector.connect(host="localhost", database="sensor_data_station", user="root", password="secret")
	print("Connected to Database")
except:
	print("Could not connect to the Database")
	sys.exit()

cursor = conn.cursor()
sock.listen(1000)

try:
	while True:
		connect, addr = sock.accept()
		new_thread = Client(connect, addr)
		new_thread.start()

except:
	socket.close()
	cursor.close()
	conn.close()
	sys.exit()
