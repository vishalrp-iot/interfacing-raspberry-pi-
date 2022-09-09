import sys
import socket

host = ""
port = 13000
buf = 1024

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (host, port)

socket.bind(addr)

while True:
	data, addr = socket.recvfrom(buf)
	data = data.decode()

	print("Recieved: " + str(type(data)))

	if data == "exit":
		socket.close()
		sys.exit()
