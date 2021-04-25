#uses time.monotonic instead of time.sleep to blink nRF52840 LED

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

delay=float(input("Type frequency of blinks in seconds: "))         #asks user input for blink frequency, converts to float for subtraction in loop
lastTime = time.monotonic()                                         #checks time.monotonic() value, saves as lastTime

while True:
    if(lastTime <= time.monotonic() - delay):
        led.value=not led.value                                     #toggles led.value (ie. turns led on/off)
        lastTime=time.monotonic()
    else:
        pass
