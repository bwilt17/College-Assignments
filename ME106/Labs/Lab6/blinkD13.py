'''
Blinks an externally connected LED on D13 of adafruit nRF52840 feather sense board
Written by Beverly Wilt (beverly.wilt@sjsu.edu) 
'''

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
