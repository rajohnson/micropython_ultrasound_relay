import utime
import machine

DISTANCE_THRESHOLD_CM = 50  # below this the relay should be low, above active
led = machine.Pin(25, machine.Pin.OUT)


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


class Relay:
    def __init__(self, coil_pin):
        self.coil = machine.Pin(coil_pin, machine.Pin.OUT)

    def on(self):
        self.coil.value(1)

    def off(self):
        self.coil.value(0)


distance_sensor = Ultrasound(trigger_pin=0, echo_pin=1)
relay = Relay(2)

if __name__ == '__main__':
    ''' Read the range sensor once per second and update the relay based
        on whether the result is over/under DISTANCE_THRESHOLD_CM '''
    while True:
        print('start loop')
        led.value(1)
        print('beginning reading')
        distance = distance_sensor.read_cm()
        print(f'distance is {distance} cm')
        if distance > DISTANCE_THRESHOLD_CM:
            relay.on()
        else:
            relay.off()
        led.value(0)
        utime.sleep_us(1_000_000)  # 1s
