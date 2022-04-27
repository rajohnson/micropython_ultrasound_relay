import machine
import relay as relay_module  # alias so relay can be the object name
import ultrasound

DISTANCE_THRESHOLD_CM = 50  # below this the relay should be low, above active

distance_sensor = ultrasound.Ultrasound(trigger_pin=0, echo_pin=1)
relay = relay_module.Relay(2)
watchdog = machine.WDT(timeout=2500)  # timeout is in ms

if __name__ == '__main__':
    ''' Read the range sensor once per second and update the relay based
        on whether the result is over/under DISTANCE_THRESHOLD_CM '''
    
    # hold the relay inactive long enough to drain residual capitance on wdt reset
    if machine.reset_cause() == machine.WDT_RESET:
        relay.off()
        machine.lightsleep(1000)  # ms
    
    while True:
        if distance_sensor.read_cm() > DISTANCE_THRESHOLD_CM:
            relay.on()
        else:
            relay.off()
        watchdog.feed()
        machine.lightsleep(1000)  # ms
