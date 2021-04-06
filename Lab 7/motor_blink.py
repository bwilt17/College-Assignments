#basic "blink" program, modified to control a 3V DC motor on pin D13 of Adafruit nRF52840 Feather Sense board

import board
import digitalio
import time

motor = digitalio.DigitalInOut(board.D13)
motor.direction = digitalio.Direction.OUTPUT

while True:
    motor.value = True
    time.sleep(3)
    motor.value = False
    time.sleep(3)
