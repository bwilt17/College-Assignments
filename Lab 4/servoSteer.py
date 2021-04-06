# steers servo attached to nRF52840 Feather Sense on EduShields Tripler Baseboard with Interact Wing using potentiometer 
# video here: https://www.youtube.com/watch?v=MNnB3ojfUGk

import board
import pulseio
import analogio
from   adafruit_motor import servo

pot=analogio.AnalogIn(board.A2)

PIN_SERVO = board.D2
servo_pwm = pulseio.PWMOut(PIN_SERVO, duty_cycle=(2**15), frequency=50)

servo = servo.Servo(servo_pwm, min_pulse = 500, max_pulse = 2500)

while True:
    servo.angle = 180*(1-(pot.value/(((2**16)-1))))
