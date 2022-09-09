import socket
import sys
from threading import Thread
import mysql.connector
import time

class Client(Thread):
	def __init__(self, connect, addr):
		Thread.__init__(self)
		self.connect = connect
		self.addr = addr

	def run(self):
		try:

			#data = (self.connect).recv(1024)
			#data = data.decode()
			#data = data.split()
			conn = mysql.connector.connect(host="localhost", database="sensor_data_station", user="root", password="secret")
			cursor = conn.cursor()

			sensor_no = (self.connect).recv(1024)
			sensor_no = sensor_no.decode()

			query = f"select * from data_table where Sensor_NO = '#{sensor_no}' order by DATE desc, TIME desc limit 1;"

			try:
				cursor.execute(query)
				res = cursor.fetchall()

				date = str(res[0][1])
				cur_time = str(res[0][2])
				temp = res[0][3]
				humidity = res[0][4]

				msg_str = f"{date} {cur_time} {temp} {humidity}"
				(self.connect).send(msg_str.encode())
				print("Package Sent")
				(self.connect).close()
				conn.close()
				cursor.close()
			except:
				print("Error in Query Execution")
				(self.connect).close()
				conn.close()
				cursor.close()
		except:
			print("Client Closed Connection")
			(self.connect).close()
			conn.close()
			cursor.close()


host = ""
port = 10000

addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind(addr)

'''
try:
	conn = mysql.connector.connect(host="localhost", database="sensor_data_station", user="root", password="secret")
	print("Connected to Database")
except:
	print("Could not connect to the Database")
	sys.exit()
'''


sock.listen(1000)

try:
	while True:
		connect, addr = sock.accept()
		
		new_thread = Client(connect, addr)
		new_thread.start()

except:
	socket.close()
	sys.exit()
