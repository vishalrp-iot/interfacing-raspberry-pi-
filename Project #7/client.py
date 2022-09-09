import sys
import socket

host = "192.168.1.102"
port = 13000

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (host, port)
socket.connect(addr)

while True:
	data = input("Enter Message: ")
	socket.send(data.encode())
	if data == "exit":
		break

socket.close()
sys.exit()
