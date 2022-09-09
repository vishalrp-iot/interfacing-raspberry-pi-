
import socket
import sys
import time
import os
from threading import Thread

class Client(Thread):
	def __init__(self, s, addr):
		Thread.__init__(self)
		self.s = s
		self.addr = addr

	def run(self):
		while True:
			size_recv = 0
			time.sleep(0.3)
			size = (s.recv(32)).decode()
			if not size:
				print("\n\nPackages Received Sucessfully\n\n")
				break
			
			size = int(size)

			time.sleep(0.3)
			file_name = (s.recv(1024)).decode()
			file = open(file_name, "wb+")
			file.truncate()

			print("\nReceiving.....")
			while size_recv < size:
				data = (s.recv(buffer))
				file.write(data)
				size_recv = (os.stat(file_name)).st_size
				if size_recv == 0:
					print("File Received")
					file.close()
					break

			print("File Received")
			file.close()


host = ""
port = 13000
buffer = 5120000

address = (host, port)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(address)

try:
	while True:
		socket.listen(5)
		s, address = socket.accept()
		new_thread = Client(s, address)
		new_thread.start()

except KeyboardInterrupt:
	socket.close()
	sys.exit()