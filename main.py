from hysrf05 import HYSRF05
from sg90 import ServoSG90
from motor import Motor, DualMotor

MINIMUM_DISTANCE = 20 #cm

if __name__ == '__main__':
    sensor = HYSRF05(trigger = 16, echo = 17)
    servo = ServoSG90(pin=18)
    servo.center()
    motorA = Motor(pin1=15, pin2=14)
    motorB = Motor(pin1=12, pin2=13)
    motors = DualMotor(motorA, motorB)

    while True:
        
        distance = sensor.distance_cm()
        print(distance)
        
        if distance is not None and distance < MINIMUM_DISTANCE:
            motors.stop()
            servo.right()
            distance = sensor.distance_cm()
            
            if distance is not None and distance > MINIMUM_DISTANCE:
                motors.turn_right()
                servo.right()
                motors.forward()
            
            else:
                servo.left()
                distance = sensor.distance_cm()
                
                if distance is not None and distance > MINIMUM_DISTANCE:
                    motors.turn_left()
                    servo.center()
                    motors.forward()
            
        else:
            servo.center()
            motors.forward()