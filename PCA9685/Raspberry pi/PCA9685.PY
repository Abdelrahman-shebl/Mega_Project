from adafruit_servokit import ServoKit
from time import sleep
kit=ServoKit(channels=16)   #No. of channels
servo=14                    #No. of channels to be controlled

while True:
    a=input("Enter your angle (angle from 0 to 180 )")
    kit.servo[2].angle=int(a) 
    for i in range (servo):
        kit.servo[i].angle=int(a)