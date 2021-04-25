#plays a tone on Interact Wing speaker when nRF52840 Feather Sense board LED blinks on

import board
import digitalio
import time
import pulseio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

delay=int(input("Type frequency of blinks in seconds: "))
lastTime = time.monotonic()

spkr_pwm = pulseio.PWMOut(board.A3, variable_frequency=True)
frequency=659

def play(freq):                                                                 #plays tone on speaker
    spkr_pwm.frequency  = freq
    spkr_pwm.duty_cycle = 2**15

def stop():                                                                        #stops speaker tone
    spkr_pwm.duty_cycle = 0

while True:
    if(lastTime <= time.monotonic() - delay):
        led.value=not led.value
        if(led.value):
            play(frequency)
        else:
            stop()
        lastTime=time.monotonic()
    else:
        pass
