import machine


class Relay:
    '''Relay output. Relay will be inactive when initialized.'''
    def __init__(self, coil_pin):
        self.coil = machine.Pin(coil_pin, machine.Pin.OUT)
        self.coil.value(0)

    def on(self):
        self.coil.value(1)

    def off(self):
        self.coil.value(0)
