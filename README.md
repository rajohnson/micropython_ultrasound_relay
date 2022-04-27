# micropython_ultrasound_relay
I have an outlet in my garage that I want to control based on whether the garage door is open.
This controls the state of a relay based on the distance from a range sensor.

The processor reads the range sensor once per second and updates the relay state based on the reading.
Threshold is set to 50 cm. 
If the reading is above 50 cm the relay is active.
Otherwise the relay is inactive.

![Block diagram](https://github.com/rajohnson/micropython_ultrasound_relay/blob/main/block_diagram.jpg)

[Demo video](https://youtu.be/Ks6QMVZVaHA)

Microcontroller - https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html

Range sensor (HC-SR04) datasheet - https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf
