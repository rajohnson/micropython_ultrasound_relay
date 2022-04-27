import utime
import relay as relay_module  # alias so relay can be the object name
import ultrasound

DISTANCE_THRESHOLD_CM = 50  # below this the relay should be low, above active

distance_sensor = ultrasound.Ultrasound(trigger_pin=0, echo_pin=1)
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
