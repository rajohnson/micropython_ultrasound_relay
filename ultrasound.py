import machine
import utime


class Ultrasound:
    ''' reads a HC-SR04 ultrasound distance sensor and returns the distance in cm '''

    def __init__(self, trigger_pin, echo_pin):
        self.trigger = machine.Pin(trigger_pin, machine.Pin.OUT)
        self.echo = machine.Pin(echo_pin, machine.Pin.IN)

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
