import socket
import sys
import os
import time

host = "192.168.0.2"
port = 13000
buffer = 5120000

address = (host, port)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(address)

file_names = []

print("Enter the Name of the File and enter send to send them:")
while True:
	x = input()
	if x == "send":
		break
	file_names.append(x)

file_location = input("Give the location of the file or give 0 if the file is in the CWD: ")

if file_location != "0":
	file_name = file_location + "/" + file_name

for file_name in file_names:
	try:
		f = open(file_name, "rb")
	except FileNotFoundError:
		print("No file called {f} present in the Directory".format(f=file_name))
		continue

	time.sleep(1)
	size = str(os.path.getsize(file_name))
	socket.send(size.encode())

	time.sleep(0.5)
	socket.send(file_name.encode())

	while True:
		data = f.read(buffer)
		socket.sendall(data)

		if not data:
			f.close()
			break

socket.close()
