'''
Uses both adafruit connect app and rotary encoder to vary brightness of external LED connected to nRF52840 Feather Sense on EduShields Tripler Baseboard with Interact Wing
Based on code provided by Adafruit for BLE control
Written by Beverly Wilt (beverly.wilt@sjsu.edu) 
'''

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

import board, pulseio, rotaryio

led = pulseio.PWMOut(board.D12)

enc = rotaryio.IncrementalEncoder(board.A4, board.A5)
last_position = None

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

n = 0

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
    ble.start_advertising(advertisement)
    while not ble.connected:
        position = enc.position
        if last_position == None:
            led_level(n)
        elif position < last_position:
            n = down(n)
            led_level(n)
        elif position > last_position:
            n = up(n)
            led_level(n)
        last_position = position

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.RIGHT:
                        n = up(n)
                        led_level(n)
                    elif packet.button == ButtonPacket.LEFT:
                        n = down(n)
                        led_level(n)
                    elif packet.button == ButtonPacket.UP:
                        n = 10
                        led_level(n)
                    elif packet.button == ButtonPacket.DOWN:
                        n = 0
                        led_level(n)

    # If we got here, we lost the connection. Go up to the top and start advertising again and waiting for a connection.
