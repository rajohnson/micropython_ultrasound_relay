import utime
import machine
import relay as relay_module  # alias so relay can be the object name

DISTANCE_THRESHOLD_CM = 50  # below this the relay should be low, above active


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


distance_sensor = Ultrasound(trigger_pin=0, echo_pin=1)
relay = relay_module.Relay(2)

if __name__ == '__main__':
    ''' Read the range sensor once per second and update the relay based
        on whether the result is over/under DISTANCE_THRESHOLD_CM '''
    while True:
        if distance_sensor.read_cm() > DISTANCE_THRESHOLD_CM:
            relay.on()
        else:
            relay.off()
        utime.sleep_us(1_000_000)  # 1s
