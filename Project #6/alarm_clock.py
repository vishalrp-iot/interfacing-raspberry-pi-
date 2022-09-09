import time
import datetime
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_DHT
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests
import sys
import json
import geocoder

sensor = 11
pin = 14

button1 = 10
button2 = 12
alarm_hr = 0
alarm_min = 0
cur_hr = 0
cur_min = 0
buzzer = 11
buzzer_set = False
alarm_set = False
check = False

RST = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

font = ImageFont.load_default()

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer, GPIO.OUT)

h, t = Adafruit_DHT.read_retry(sensor, pin)

URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "817ad3c8a48d83a4543a278cec2c6403"

g = geocoder.ip('me')
city = g.city

params = {"q": city, "APPID": API_KEY}

r = requests.get(URL, params=params)
result = r.json()

weather = result['weather'][0]['description']

def displayOLED():
	global alarm_hr, alarm_min, cur_hr, cur_min, h, t

	image = Image.new('1', (width, height))
	draw = ImageDraw.Draw(image)

	disp.clear()

	time = "TIME: {hr}:{min}".format(hr=cur_hr, min=cur_min)
	alarm_time = "ALARM TIME: {hr}:{min}".format(hr=alarm_hr, min=alarm_min)
	temp = "TEMP: {t}".format(t=t)+u"\u00B0"+"C" 
	humidity = "HUMIDITY: {h}%".format(h=h)
	weath = "WEATHER: " + weather.upper()
	location = "LOCATION: {city}".format(city=city)

	draw.text((0, 0), time, font=font, fill=255)
	draw.text((0, 8), alarm_time, font=font, fill=255)
	draw.text((0, 16), temp, font=font, fill=255)
	draw.text((0, 24), humidity, font=font, fill=255)
	draw.text((0, 32), weath, font=font, fill=255)
	draw.text((0, 40), location, font=font, fill=255)

	disp.image(image)
	disp.display()


def inputMinute():
	global alarm_hr, alarm_min
	displayOLED()

	while True:
		if GPIO.input(button2) == 1:
			if alarm_min >= 60:
				alarm_min = 0
			else:
				alarm_min += 1

			displayOLED()
			time.sleep(0.1)

		elif GPIO.input(button1) == 1:
			time.sleep(0.1)
			break


def inputHour():
	global alarm_hr, alarm_min
	displayOLED()

	while True:
		if GPIO.input(button2) == 1:
			if alarm_hr >= 24:
				alarm_hr = 0
			else:
				alarm_hr += 1

			displayOLED()
			time.sleep(0.1)

		elif GPIO.input(button1) == 1:
			time.sleep(0.1)
			inputMinute()
			break


def buttonPres():
	global buzzer_set, alarm_set, alarm_hr, alarm_min
	print(buzzer_set)
	if buzzer_set == True:
		time.sleep(0.1)
		GPIO.output(buzzer, GPIO.HIGH)
		buzzer_set = False
		alarm_hr, alarm_min = (0, 0)
		return

	inputHour()
	alarm_set = True


def main():
	global alarm_hr, alarm_min, alarm_set, buzzer_set, alarm_set, cur_hr, cur_min, h, t, check, weather, URL, params

	try:
		while True:
			ti = datetime.datetime.now()
			cur_hr = ti.hour
			cur_min = ti.minute

			if cur_hr%2 == 0:
				if check == False:
					h, t = Adafruit_DHT.read_retry(sensor, pin)
					r = requests.get(URL, params=params)
					result = r.json()
					weather = result['weather'][0]['description']
					check = True
			else:
				check = False

			if GPIO.input(button1) == 1:
				time.sleep(0.1)
				buttonPres()

			if alarm_hr == cur_hr and alarm_min == cur_min and alarm_set == True:
				GPIO.output(buzzer, GPIO.LOW)
				buzzer_set = True

			displayOLED()
			time.sleep(0.1)

	except KeyboardInterrupt:
		GPIO.output(buzzer, True)
		GPIO.cleanup()
		disp.clear()
		disp.display()
		sys.exit()


main()
