import serial

s = serial.Serial('/dev/ttyUSB0', 9600)

# print(s.name) # Printing port name

while True: print(s.readline().decode().strip())
