#varies LED blink and tone frequency with potentiometer rotation/value

import board
import digitalio
import time
import pulseio
import analogio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

#delay=int(input("Type frequency of blinks in seconds: "))
lastTime = time.monotonic()

spkr_pwm = pulseio.PWMOut(board.A3, variable_frequency=True)

pot=analogio.AnalogIn(board.A2)

def play(frequency):
    spkr_pwm.frequency  = int(frequency)
    spkr_pwm.duty_cycle = 2**15

def stop():
    spkr_pwm.duty_cycle = 0

while True:
    delay = 1-(pot.value/((2**16)-1))+.1                #converts pot value to useable delay for 				                               time.monotonic()
    if(lastTime <= time.monotonic() - delay):
        led.value=not led.value
        if(led.value):
            freq = (pot.value/10)+10                           #converts pot value to reasonable frequency for play()
            play(freq)
        else:
            stop()
        lastTime=time.monotonic()
    else:
        pass

