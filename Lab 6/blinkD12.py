# blinks an externally connected LED on D12 of adafruit nRF52840 feather sense board

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D12)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
