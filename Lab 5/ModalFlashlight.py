# Modal Flashlight using nRF52840 Feather Sense on Edushields Tripler Baseboard with Interact Wing
# Modes: Off, Dim, On, Fast Blink

import board, digitalio, pulseio, time

# CUSTOMIZABLES
PIN_BUTTON = board.RX   # SW0        on TriplerBaseboard-v1.0
PIN_LIGHT  = board.D5   # LED0/RGB_B on TriplerBaseboard-v1.0
#SECS_HALFBLINK = 0.5
SECS_BLINK_ON = 0.2
SECS_BLINK_OFF = 1.8

# States in the state machine (not necessarily 1:1 with flashlight modes)
STATE_OFF       = 0
STATE_FULL      = 1
STATE_DIM       = 2
STATE_FLASH_OFF = 3
STATE_FLASH_ON  = 4
s_states = ['STATE_OFF','STATE_FULL', 'STATE_DIM', 'STATE_FLASH_OFF','STATE_FLASH_ON']

# All defined input events
EVENT_NONE   = 0
EVENT_PRESS  = 1
EVENT_TIMER  = 2
s_events = ['EVENT_NONE','EVENT_PRESS','EVENT_TIMER']

# INITIALIZATIONS
button           = digitalio.DigitalInOut(PIN_BUTTON)
button.direction = digitalio.Direction.INPUT
button.pull      = digitalio.Pull.UP

light           = pulseio.PWMOut(PIN_LIGHT)
#light.direction = digitalio.Direction.OUTPUT

timer_time = None

# Set timer to expire in "delta" seconds, or None if you want to cancel the timer
def timer_set(delta):
    global timer_time

    if delta == None:
        timer_time = None
    else:
        timer_time = time.monotonic() + delta

def timer_expired():
    return (timer_time != None) and (timer_time <= time.monotonic())

# Return EVENT_PRESS (from up-position to down) or EVENT_NONE for the button
def button_event():
    global button_prev

    button_curr = button.value

    #           now down       and         was up
    if ((button_curr == False) and (button_prev == True)):
        ret = EVENT_PRESS
    else:
        ret = EVENT_NONE

    button_prev = button_curr
    return ret

# Check/prioritize receipt and reporting of events
def event_get():
    if button_event() != EVENT_NONE:
        return EVENT_PRESS
    if timer_expired() != EVENT_NONE:
        return EVENT_TIMER
    return EVENT_NONE

# Consolidate preferred method (crash, print, beep, etc.) for reporting errors here
def error(err_string):
    #print(err_string)
    raise Exception(err_string)

def event_process(s, e):
    if s == STATE_OFF:
        if e == EVENT_PRESS:
            light.duty_cycle = int(0.2*((2**16)-1))
            return STATE_DIM
        elif e == EVENT_TIMER:
            error("Timer expired in STATE_OFF")
        else:
            error("Unrecognized event in STATE_OFF")
    elif s == STATE_DIM:
        if e == EVENT_PRESS:
            light.duty_cycle = (2**16)-1
            return STATE_FULL
        elif e == EVENT_TIMER:
            error("Timer expired in STATE_DIM")
        else:
            error("Unrecognized event in STATE_DIM")
    elif s == STATE_FULL:
        if e == EVENT_PRESS:
            light.duty_cycle = 0
            timer_set(SECS_BLINK_ON)
            return STATE_FLASH_OFF
        elif e == EVENT_TIMER:
            error("Timer expired in STATE_FULL")
        else:
            error("Unrecognized event in STATE_FULL")
    elif s == STATE_FLASH_OFF:
        if e == EVENT_PRESS:
            light.duty_cycle = 0
            timer_set(None)
            return STATE_OFF
        elif e == EVENT_TIMER:
            light.duty_cycle = (2**16)-1
            timer_set(SECS_BLINK_ON)
            return STATE_FLASH_ON
        else:
            error("Unrecognized event in STATE_FLASH_OFF")
    elif s == STATE_FLASH_ON:
        if e == EVENT_PRESS:
            light.duty_cycle = 0
            timer_set(None)
            return STATE_OFF
        elif e == EVENT_TIMER:
            light.duty_cycle = 0
            timer_set(SECS_BLINK_OFF)
            return STATE_FLASH_OFF
        else:
            error("Unrecognized event in STATE_FLASH_ON")
    else:
        error("Unrecognized state: "+str(state))

# MAIN PROGRAM LOOP
state = STATE_OFF
light.duty_cycle = 0

while True:
    event = event_get()
    if event != EVENT_NONE:
        print(s_events[event], end="")
        state_new = event_process(state, event)
        if (state_new != state):
            print(" -> "+s_states[state_new])
        state = state_new
