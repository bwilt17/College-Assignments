'''
Produces following behavior from nRF52840 Feather Sense board on Edushields Tripler Baseboard with Interact Wing:
    - varies brightness of external LED so that by turning rotary encoder one direction, the brightness of LED increments from 0% to 100% brightness 
    - dims LED in the same increments when turning the encoder in the other direction back down to 0%
Written by Beverly Wilt (beverly.wilt@sjsu.edu) 
'''

import board, pulseio, rotaryio

led = pulseio.PWMOut(board.D12)

enc = rotaryio.IncrementalEncoder(board.A4, board.A5)
last_position = 0

brightness = 0

def led_level(level):
    if level in range(0,11,1):
        led.duty_cycle = int((0.1*level)*((2**16)-1))
    elif level >= 11:
        led.duty_cycle = (2**16)-1
    else:
        led.duty_cycle = 0

def up(p):
    if p < 10:
        p = p + 1
    return p

def down(p):
    if p > 0:
        p = p - 1
    return p

while True:
    position = enc.position
    if position < last_position:
        brightness = down(brightness)
        led_level(brightness)
    elif position > last_position:
        brightness = up(brightness)
        led_level(brightness)
    last_position = position
