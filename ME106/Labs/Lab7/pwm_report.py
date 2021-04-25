# increases duty cycle from 0% to 100% in steps of 10% every three seconds
# allows the motor to come up to speed for the first of these three seconds
# reports the change in encoder counts over the last two seconds
# prints duty cycle value (0-100) and the change in encoder counts for each speed 

import board, pulseio, rotaryio, time

motor = pulseio.PWMOut(board.D13)

enc = rotaryio.IncrementalEncoder(board.D12, board.D11)

dut_percent = 0

last_enc = enc.position

while True:
    for dut_percent in range(0,110,10):
        motor.duty_cycle = int((0.01*dut_percent)*((2**16)-1))
        time.sleep(1)
        enc_delta = enc.position-last_enc
        last_enc = enc.position
        print("Duty Cycle:", dut_percent, "%")
        print("Encoder Change:", enc_delta)
        time.sleep(2)
    break
# program/motor stops after reaches 100% duty cycle
