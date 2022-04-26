import utime
import machine

led = machine.Pin(25, machine.Pin.OUT)


class Ultrasound:
    ''' reads a HC-SR04 ultrasound distance sensor and returns the distance in cm '''

    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.trigger = machine.Pin(self.trigger_pin, machine.Pin.OUT)
        self.echo = machine.Pin(self.echo_pin, machine.Pin.IN)

    def read_cm(self):
        pulse_start_us = 0
        pulse_end_us = 0
        
        # pulse trigger high for 10us
        self.trigger.value(1)
        utime.sleep_us(10)
        self.trigger.value(0)
        
        # record last time that echo was low
        while self.echo.value() == 0:
            pulse_start_us = utime.ticks_us()
        
        # record last time that echo was high
        while self.echo.value() == 1:
            pulse_end_us = utime.ticks_us()
        
        pulse_time_us = pulse_end_us - pulse_start_us
        distance_cm = pulse_time_us / 58
        return distance_cm


distance_sensor = Ultrasound(trigger_pin=0, echo_pin=1)

while True:
    print('start loop')
    led.value(1)
    utime.sleep_us(1_000_000)  # 1s
    led.value(0)
    print('beginning reading')
    distance = distance_sensor.read_cm()
    print(f'distance is {distance} cm')
    utime.sleep_us(1_000_000)  # 1s
