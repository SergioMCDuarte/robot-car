from machine import Pin, PWM
from time import sleep

class ServoSG90():
    
    def __init__(self, pin):
        self.pin = Pin(pin)
        self.pwm = PWM(self.pin)
        self.pwm.freq(50)
    
    def center(self):
        self.pwm.duty_ns(1500000)
    
    def right(self):
        self.pwm.duty_ns(500000)
    
    def left(self):
        self.pwm.duty_ns(2500000)
        
if __name__ == '__main__':
    
    servo = ServoSG90(pin=18)
    
    servo.center()
    sleep(1)
    servo.right()
    sleep(1)
    servo.left()
    sleep(1)
    servo.center()
    
