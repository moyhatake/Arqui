import sys, os
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QColumnView, QAbstractItemView
from interface import *
import serial
from datetime import datetime

import RPi.GPIO as GPIO
import time, sys
import pyrebase
import dht11

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Pins
trigger =      11 #23
echo =         8  #24
dht =          4  #07
fotoresistor = 26 #37
flam =         6  #31
ser = serial.Serial('/dev/ttyACM0', 9600)

# Globals
model = QStandardItemModel()
model.setColumnCount(1)
sensor, dis, temp, hum = 0, 0, 0, 0
lig, fla = "OFF", "OFF"
ps = False

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

i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.show()
image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(echo, GPIO.IN)     	 
GPIO.setup(trigger, GPIO.OUT) 	  
GPIO.setup(fotoresistor, GPIO.IN) 
GPIO.setup(flam, GPIO.IN) 		  
instance = dht11.DHT11(pin = dht) 

class Ui_Project(QtWidgets.QMainWindow, Ui_Project):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.dataVals.setModel(model)
        self.distance.clicked.connect(self.rbDistance)
        self.temperature.clicked.connect(self.rbTemperature)
        self.humidity.clicked.connect(self.rbHumidity)
        self.light.clicked.connect(self.rbLight)
        self.flame.clicked.connect(self.rbFlame)
        self.sensorSelector.valueChanged.connect(self.mySelector)
        self.pauseResume.clicked.connect(self.pauseReading)
        
        self.listener()
    
    def listener(self):
        now_date = datetime.now()
        formatt = now_date.strftime("%m/%d, %H:%M")
        
        global model, dis, temp, hum, lig, fla
        tmp_dis = distance()
        if tmp_dis <= 400: dis = tmp_dis
        resultDHT = tempHum()
        l = light()
        f = flame()
        
        try:
            tmp_temp, tmp_hum = resultDHT
            if tmp_temp is not None: temp = tmp_temp
            if tmp_hum is not None: hum = tmp_hum
        except: print("")
            
        if ps == False:
            if sensor == 0: 
                model.appendRow([QStandardItem("{:0>4}".format(str(dis)) + " cm     |   " + formatt)])
                self.dataVals.setModel(model)
                self.lcdVal.display(dis)
                my_range = self.sliderVal.maximum() - self.sliderVal.minimum()
                my_val = self.sliderVal.minimum() + (my_range * dis / 100)
                self.sliderVal.setValue(int(my_val))
                ser.write(("0," + str(dis) + "cm").encode("ascii"))
            elif sensor == 1: 
                model.appendRow([QStandardItem("{:0>4}".format(str(temp)) + " °C        |   " + formatt)])
                self.lcdVal.display(temp)
                my_range = self.sliderVal.maximum() - self.sliderVal.minimum()
                my_val = self.sliderVal.minimum() + (my_range * temp / 100)
                self.sliderVal.setValue(int(my_val))
                ser.write(("0," + str(temp) + ":C").encode("utf-8"))
            elif sensor == 2: 
                model.appendRow([QStandardItem("{:0>4}".format(str(hum)) + " %      |   " + formatt)])
                self.lcdVal.display(hum)
                my_range = self.sliderVal.maximum() - self.sliderVal.minimum()
                my_val = self.sliderVal.minimum() + (my_range * hum / 100)
                self.sliderVal.setValue(int(my_val))
                ser.write(("0," + str(hum) + "%").encode())
            elif sensor == 3: 
                if l == 1: 
                    lig = "ON"
                    model.appendRow([QStandardItem(" ON     |   " + formatt)])
                    self.lcdVal.display(l)
                    self.sliderVal.setValue(1)
                    ser.write(b'0,ON')
                else: 
                    lig = "OFF"
                    model.appendRow([QStandardItem("OFF     |   " + formatt)])
                    self.lcdVal.display(l)
                    self.sliderVal.setValue(0)
                    ser.write(b'0,OFF')
            elif sensor == 4: 
                if f == 1: 
                    fla = "ON"
                    model.appendRow([QStandardItem(" ON     |   " + formatt)])
                    self.lcdVal.display(f)
                    self.sliderVal.setValue(1)
                    ser.write(b'0,ON')
                else: 
                    fla = "OFF"
                    model.appendRow([QStandardItem("OFF     |   " + formatt)])
                    self.lcdVal.display(f)
                    self.sliderVal.setValue(0)
                    ser.write(b'0,OFF')
            
            #self.scrollToLast()
            #self.dataVals.scrollToBottom()
            showOnOled(dis, temp, hum, lig, fla)
            sendToFB(dis, temp, hum, l, f)
        else: ser.write(b'1')
        QtCore.QTimer.singleShot(5000, self.listener)
        
    def mySelector(self, value):
        global model, sensor
        sensor = value
        if value == 0: 
            self.distance.setChecked(True)
            self.sliderVal.setMinimum(2)
            self.sliderVal.setMaximum(400)
            self.min.setText("2cm")
            self.max.setText("4m")
        elif value == 1: 
            self.temperature.setChecked(True)
            self.sliderVal.setMinimum(-40)
            self.sliderVal.setMaximum(80)
            self.min.setText("-40°C")
            self.max.setText("80°C")
        elif value == 2: 
            self.humidity.setChecked(True)
            self.sliderVal.setMinimum(0)
            self.sliderVal.setMaximum(100)
            self.min.setText("0%")
            self.max.setText("100%")
        elif value == 3: 
            self.light.setChecked(True)
            self.sliderVal.setMinimum(0)
            self.sliderVal.setMaximum(1)
            self.min.setText("OFF")
            self.max.setText("ON")
        elif value == 4: 
            self.flame.setChecked(True)
            self.sliderVal.setMinimum(0)
            self.sliderVal.setMaximum(1)
            self.min.setText("OFF")
            self.max.setText("ON")
            
        model = self.dataVals.model()
        model.clear()
            
    def pauseReading(self):
        global ps
        if ps == True: 
            ps = False
            self.pauseResume.setText("Pause")
        else: 
            ps = True
            self.pauseResume.setText("Resume")
        
    def rbDistance(self): self.sensorSelector.setValue(0)
    
    def rbTemperature(self): self.sensorSelector.setValue(1)
    
    def rbHumidity(self): self.sensorSelector.setValue(2)
    
    def rbLight(self): self.sensorSelector.setValue(3)
    
    def rbFlame(self): self.sensorSelector.setValue(4)
    
    """
    def scrollToLast(self):
        global model
        model = self.dataVals.model()
        l_i = model.index(model.rowCount() - 1, 0)
        self.dataVals.scrollTo(l_i, QAbstractItemView.PositionAtBottom)
    """
    
# Sensores
def distance():
	GPIO.output(trigger, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(trigger, GPIO.LOW)
	
	while GPIO.input(echo) == 0: pulse_i = time.time()
	while GPIO.input(echo) == 1: pulse_f = time.time()
	
	dis = round(((pulse_f - pulse_i) * 17150), 1)
	return dis
	
def tempHum():
	result = instance.read()
	if result.is_valid():
		temp = "%-3.1f" % result.temperature
		hum = "%-3.1f" % result.humidity
		return float(temp), float(hum)
	
def light():
    if GPIO.input(fotoresistor) == GPIO.HIGH: return 0
    else: return 1
        
def flame():
    if GPIO.input(flam) == GPIO.HIGH: return 1
    else: return 0

# Features
def sendToFB(distance, temperature, humidity, light, flame):
    db.child("sensors").child("HC-SR04").update({"distance": distance})
    db.child("sensors").child("DHT-11").update({"temperature": temperature})
    db.child("sensors").child("DHT-11").update({"humidity": humidity})
    db.child("sensors").child("MH-LM393").update({"light": light})
    db.child("sensors").child("KY-026").update({"flame": flame})
    
def showOnOled(distance, temperature, humidity, light, flame):
    # Refresh display
    display.fill(0)
    display.show()
    image = Image.new("1", (128, 64))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    # Print new data for pixels
    draw.text((5, 12), "Distance: " + str(distance) + "cm", font = font, fill = 255)
    draw.text((5, 22), "Temperature: " + str(temperature) + "°C", font = font, fill = 255)
    draw.text((5, 32), "Humidity: " + str(humidity) + "%", font = font, fill = 255)
    draw.text((5, 42), "Light: " + light, font = font, fill = 255)
    draw.text((5, 52), "Flame: " + flame, font = font, fill = 255)
    display.image(image)
    display.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Project()
    window.show()
    app.exec_()
