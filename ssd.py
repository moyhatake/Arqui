import RPi.GPIO as GPIO
import time, sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Setup pins
GPIO.setup(29, GPIO.IN)  # GPIO5
GPIO.setup(33, GPIO.OUT) # GPIO13
GPIO.setup(31, GPIO.OUT) # GPIO06
GPIO.setup(36, GPIO.OUT) # GPIO16
GPIO.setup(38, GPIO.OUT) # GPIO20
GPIO.setup(40, GPIO.OUT) # GPIO21
GPIO.setup(35, GPIO.OUT) # GPIO19
GPIO.setup(37, GPIO.OUT) # GPIO26

# 7 segment digits for catode
digit0  = [1, 1, 1, 1, 1, 1, 0]
digit1  = [0, 1, 1, 0, 0, 0, 0]
digit2  = [1, 1, 0, 1, 1, 0, 1]
digit3  = [1, 1, 1, 1, 0, 0, 1]
digit4  = [0, 1, 1, 0, 0, 1, 1]
digit5  = [1, 0, 1, 1, 0, 1, 1]
digit6  = [1, 0, 1, 1, 1, 1, 1]
digit7  = [1, 1, 1, 0, 0, 0, 0]
digit8  = [1, 1, 1, 1, 1, 1, 1]
digit9  = [1, 1, 1, 1, 0, 1, 1]
digit10 = [1, 1, 1, 0, 1, 1, 1]
digit11 = [0, 0, 1, 1, 1, 1, 1]
digit12 = [1, 0, 0, 1, 1, 1, 0]
digit13 = [0, 1, 1, 1, 1, 0, 1]
digit14 = [1, 0, 0, 1, 1, 1, 1]
digit15 = [1, 0, 0, 0, 1, 1, 1]

# Pinout
gpin    = [33, 31, 36, 38, 40, 35, 37]

counter = 0
digits  = [digit0, digit1, digit2, digit3, 
           digit4, digit5, digit6, digit7, 
           digit8, digit9, digit10, digit11,
           digit12, digit13, digit14, digit15]

def show(count):
    for x in range (0, 7):
        number = digits[count]
        GPIO.output(gpin[x], number[x])
    time.sleep(1)

while True:
    # Toggle value of the button
    current_state = GPIO.input(29)
    if current_state == GPIO.HIGH: toggle = GPIO.LOW
    else: toggle = GPIO.HIGH

    # Display counter value
    if toggle == GPIO.LOW:
        show(counter)
        if counter < 15: counter += 1
        else: counter = 0
    else:
        show(counter)
        if counter > 0: counter -= 1
        else: counter = 15

GPIO.cleanup()
sys.exit()
