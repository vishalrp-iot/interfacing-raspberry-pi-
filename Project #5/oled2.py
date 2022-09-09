import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_DHT
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

sensor = 11
pin = 14

RST = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

font = ImageFont.truetype('OpenSans-Bold.ttf', 12)

try:
	while True:
		image = Image.new('1', (width, height))
		draw = ImageDraw.Draw(image)

		disp.clear()

		h, t = Adafruit_DHT.read_retry(sensor, pin)

		t = "TEMP: {t}C".format(t=t)
		h = "HUMIDITY: {h}%".format(h=h)

		draw.text((0, 0), t, font=font, fill=255)
		draw.text((0, 12), h, font=font, fill=255)

		disp.image(image)
		disp.display()
		time.sleep(2)

except KeyboardInterrupt:
	disp.clear()
	disp.display()
