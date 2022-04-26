import utime
import machine

led = machine.Pin(25, machine.Pin.OUT)

while True:
    print('hello')
    led.value(1)
    utime.sleep(1.0) # 1s
    led.value(0)
    utime.sleep(1.0) # 1s
    