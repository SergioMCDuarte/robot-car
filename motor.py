from machine import Pin, PWM
from time import sleep

class Motor():
    
    def __init__(self, pin1, pin2):
        self.pin1 = Pin(pin1, Pin.OUT, Pin.PULL_DOWN)
        self.pin2 = Pin(pin2, Pin.OUT, Pin.PULL_DOWN)
        self.pwm1 = PWM(self.pin1)
        self.pwm2 = PWM(self.pin2)
        
    def move(self):
        self.pwm1.duty_u16(int(64000))
        self.pin2.value(0)
    
    def stop(self):
        self.pwm1.duty_u16(0)
        self.pin2.value(0)
        
class DualMotor():
    
    def __init__(self, motorA, motorB):
        
        self.motorA = motorA
        self.motorB = motorB
        
    def forward(self):
        self.motorA.move()
        self.motorB.move()
        
    def turn_right(self):
        self.motorA.stop()
        self.motorB.move()
        sleep(0.8)
        self.motorA.move()
        
    def turn_left(self):
        self.motorB.stop()
        self.motorA.move()
        sleep(0.8)
        self.motorB.move()
    
    def stop(self):
        self.motorA.stop()
        self.motorB.stop()
    
if __name__ == '__main__':
    
    motorA = Motor(pin1=15, pin2=14)
    
    motorB = Motor(pin1=12, pin2=13)
    
    motors = DualMotor(motorA, motorB)
    
    motors.turn_right()
    sleep(1)
    motors.stop()
    