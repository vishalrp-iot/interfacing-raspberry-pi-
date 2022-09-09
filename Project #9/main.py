import time
import sys
import Adafruit_DHT
import mysql.connector

sensor = 11
pin = 14

try:
	conn = mysql.connector.connect(host="localhost", database="temp_data",user="root", password="qwerty")
	print("Connection Sucessful")
except:
	print("Connection Unsucessful")

cursor = conn.cursor()

while True:
	
	h, t = Adafruit_DHT.read_retry(sensor, pin)
	print(t, h)
	h = int(h)
	t= int(t)

	query = "INSERT INTO tempData VALUES({t}, {h});".format(h=h, t=t)

	try:
		cursor.execute(query)
		conn.commit()
		print("Commit Sucessful")
	except:
		db.rollback()
		print("unsucessful")
	
	time.sleep(2)

cursor.close()
conn.close()
