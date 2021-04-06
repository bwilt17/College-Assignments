# uses the accelerometer of nRF52480 Sense for motor speed control input
# video of program running found here: https://www.youtube.com/watch?v=oNNodXaHofY

import board, time, pulseio, rotaryio
import adafruit_lsm6ds.lsm6ds33

i2c = board.I2C()
lsm6ds33 = adafruit_lsm6ds.lsm6ds33.LSM6DS33(i2c)

motor = pulseio.PWMOut(board.D13)

enc = rotaryio.IncrementalEncoder(board.D12, board.D11)

G_MAX = 10
G_MIN = 1

def motor_speed(val):                        #controls motor speed
    if val >= G_MAX:
        motor.duty_cycle = (2**16)-1
    elif val < G_MIN:
        motor.duty_cycle = 0
    else:
        motor.duty_cycle = int((0.1*val)*((2**16)-1))

while True:
    AXIS = lsm6ds33.acceleration[0]
    acc = 10 - ((AXIS+10)/2)                #converts accelerometer value to number between 0-10
    motor_speed(acc)
    #print(acc)                             #for troubleshooting
    time.sleep(0.01)
