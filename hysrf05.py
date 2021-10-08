from machine import Pin
from time import sleep_us, ticks_diff, ticks_us, sleep

class HYSRF05():

    def __init__(self, trigger, echo, echo_timeout_us=30000):

        self.trigger = Pin(trigger, Pin.OUT, Pin.PULL_DOWN)
        self.echo = Pin(echo, Pin.IN, Pin.PULL_DOWN)
        self.echo_timeout_us = echo_timeout_us
        self.pulse_duration = None
        self.__pulse_start__ = 0
        self.__pulse_end__ = 0
        self.__read_start__ = 0

    def _send_pulse_and_wait(self):
        self.__pulse_start__ = 0
        self.__pulse_end__ = 0
        self.__read_start__ = ticks_us()
        
        # send trigger pulse
        self.trigger.value(1)
        sleep_us(10)
        self.trigger.value(0)
        
        # wait for echo
        while ticks_diff(ticks_us(), self.__read_start__) <= self.echo_timeout_us:
            # check for start of echo signal
            if not self.__pulse_start__ and self.echo.value() == 1:
                self.__pulse_start__ = ticks_us()
            # check for end of echo signal
            if self.__pulse_start__ and self.echo.value() == 0:
                self.__pulse_end__ = ticks_us()
                break

    def distance_cm(self):
        sleep(0.5)
        self._send_pulse_and_wait()
        
        if self.__pulse_end__ == 0:
            return 
        else:
            self.pulse_duration = ticks_diff(self.__pulse_end__, self.__pulse_start__)
            return self.pulse_duration / 58


if __name__ == '__main__':

  sensor = HYSRF05(trigger = 15, echo = 14)

  while True:
    print(sensor.distance_cm())