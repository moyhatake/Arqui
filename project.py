import RPi.GPIO as GPIO
import time, sys
import pyrebase
import dht11
#import busio
#import adafruit_ssd1306
#from board import SCL, SDA
#from PIL import Image, ImageDraw, ImageFont

# Variables
trigger = 23
echo = 24
dht = 7
fotoresistor = 37
flam = 31

config = {
	"apiKey": "AIzaSyCB3Z4kLCbI-5NPnAIXbDqtajUVoC-8fKc",
	"authDomain": "arqui-project.firebaseapp.com",
	"databaseURL": "https://arqui-project-default-rtdb.firebaseio.com",
	"projectId": "arqui-project",
	"storageBucket": "arqui-project.appspot.com",
	"messagingSenderId": "953398873506",
	"appId": "1:953398873506:web:bc6d730cc12767168836fb",
	"measurementId": "G-MLBR6R62F6"
}

# Setup
firebase = pyrebase.initialize_app(config)
db = firebase.database()

"""i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()"""

"""width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()"""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(echo, GPIO.IN)     	  # GPIO8
GPIO.setup(trigger, GPIO.OUT) 	  # GPIO11
GPIO.setup(fotoresistor, GPIO.IN) # GPIO26
GPIO.setup(flam, GPIO.IN) 		  # GPIO6
instance = dht11.DHT11(pin = dht) # GPIO4

#Sensors
def distance():
	GPIO.output(trigger, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(trigger, GPIO.LOW)
	
	while GPIO.input(echo) == 0: pulse_i = time.time()
	while GPIO.input(echo) == 1: pulse_f = time.time()
	
	dis = str(round(((pulse_f - pulse_i) * 17150), 2)) + " cm"
	return dis
	
def tempHum():
	result = instance.read()
	if result.is_valid():
		temp = "%-3.1f °C" % result.temperature
		hum = "%-3.1f %%" % result.humidity
		return temp, hum
		
def light():
	if GPIO.input(fotoresistor) == GPIO.HIGH: return 0
	else: return 1
	
def flame():
	if GPIO.input(flam) == GPIO.HIGH: return 1
	else: return 0

# Interface
def showOnInterface(distance, temperature, humidity, light, flame):
	print("")

def showOnOled(distance, temperature, humidity, light, flame):
	print("")
	#draw.text((6, 18), distance, font = font, fill = 255)
	#draw.text((6, 28), temperature, font = font, fill = 255)
	#draw.text((6, 38), humidity, font = font, fill = 255)
	#draw.text((6, 48), light, font = font, fill = 255)
	#draw.text((6, 58), flame, font = font, fill = 255)
	#disp.image(image)
	#disp.show()

def showOnMatrix(distance, temperature, humidity, light, flame):
	print("")

def sendToFB(distance, temperature, humidity, light, flame):
	db.child("sensors").child("HC-SR04").update({"distance": distance})
	db.child("sensors").child("DHT-11").update({"temperature": temperature})
	db.child("sensors").child("DHT-11").update({"humidity": humidity})
	db.child("sensors").child("MH-LM393").update({"light": light})
	db.child("sensors").child("KY-026").update({"flame": flame})
		
while True: 
	dis = distance()
	resultDHT = tempHum()
	val1, val2 = False, False
	lig = light()
	fla = flame()
	
	try:
		temp, hum = resultDHT
		if temp is not None: val1 = True
		if hum is not None: val2 = True
	except: continue
	
	if val1 and val2:
		print(dis)
		print(temp)
		print(hum)
		print(lig)
		print(fla)
		
		#showOnInterface(dis, temp, hum, lig, fla)
		#showOnOled(dis, temp, hum, lig, fla)
		#showOnMatrix(dis, temp, hum, lig, fla)
		#sendToFB(dis, temp, hum, lig, fla)

	time.sleep(1)