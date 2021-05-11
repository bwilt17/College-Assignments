'''
Prints time_monotonic() value as time elapsed since start and the current encoder count every 3s for 30s.
Written by Beverly Wilt (beverly.wilt@sjsu.edu)
'''

import board, digitalio, rotaryio, time

motor = digitalio.DigitalInOut(board.D13)
motor.direction = digitalio.Direction.OUTPUT

enc = rotaryio.IncrementalEncoder(board.D12, board.D11)

last_time = time.monotonic()

while True:
    motor.value = True
    time.sleep(3)
    if time.monotonic() >=3:
        time_elapsed = (time.monotonic()-last_time)-3
        print("Encoder:", enc.position)
        print("Time elapsed:", time_elapsed, "sec")
        if time_elapsed >= 30:
            break

# only runs for the 30s necessary for problem requirements
# if want to run forever, remove the end "if time_elapsed >=30: break" statement
