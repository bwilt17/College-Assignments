# Produces following behavior from nRF52480 Sense board on EduShields TriplerBaseboard:
#   Horizontal – both LEDs on at medium brightness
#   USB connector side vertically up (nRF processor side vertically down) – LED0 at full brightness, LED1 is off
#   nRF processor side vertically upward (USB connector side vertically downward) LED1 is at full brightness, LED0 is off
#   Tilt angles between the extremes - LED brightness of LED0 and LED1 varies proportionally


import board, time, pulseio
import adafruit_lsm6ds.lsm6ds33

i2c = board.I2C()

lsm6ds33 = adafruit_lsm6ds.lsm6ds33.LSM6DS33(i2c)

led0 = pulseio.PWMOut(board.D5)
led1 = pulseio.PWMOut(board.D6)

def led0_level(level):                        #controls led brightness
    if level >= 10:
        led0.duty_cycle = (2**16)-1
    elif level < 1:
        led0.duty_cycle = 0
    else:
        led0.duty_cycle = int((0.1*level)*((2**16)-1))
    
def led1_level(level):
    if level >= 10:
        led1.duty_cycle = (2**16)-1
    elif level < 1:
        led1.duty_cycle = 0
    else:
        led1.duty_cycle = int((0.1*level)*((2**16)-1))
    
while True:
    acc = ((lsm6ds33.acceleration[0])+10)/2   #converts accelerometer value to number between 0-10
    led0_level(acc)
    led1_level(10-acc)
    #print(acc)                               #for troubleshooting
    time.sleep(0.01)
