
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from time import sleep 
from adafruit_servokit import ServoKit
import keyboard

# from gpiozero import AugularServo
# from adafruit_servokit import ServoKit

# M1 = AngluarServo(10 , min_pulse_width=0.0011 , max_pulse_width=0.02)

motors_init_State = [1500 ,1500 ,1500 ,1500 ,  1500 ,  1500]

n_ch_PCA = 6

# Parameters for Blue Robotics T200
MIN_IMP = [1100] * n_ch_PCA
MAX_IMP = [1900] * n_ch_PCA


pca = ServoKit(channels=16)

#init
def init():
    for i in range(n_ch_PCA):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i], MAX_IMP[i])
    time.sleep(7)

# forward
def move_forward(thruster_channel):
    print("Moving thruster {} forward".format(thruster_channel))
    pca.servo[thruster_channel].angle = 0

#  backward
def move_backward(thruster_channel):
    print("Moving thruster {} backward".format(thruster_channel))
    pca.servo[thruster_channel].angle = 180

# sthruster
def stop_thruster(thruster_channel):
    print("Stopping thruster {}".format(thruster_channel))
    pca.servo[thruster_channel].angle = None


def main():
    try:
        while True:
            if keyboard.is_pressed('1'):
                move_forward(0)
            elif keyboard.is_pressed('2'):
                move_backward(0)
            elif keyboard.is_pressed('3'):
                stop_thruster(0)

            if keyboard.is_pressed('4'):
                move_forward(1)
            elif keyboard.is_pressed('5'):
                move_backward(1)
            elif keyboard.is_pressed('6'):
                stop_thruster(1)

    except KeyboardInterrupt:
        for i in range(n_ch_PCA):
            pca.servo[i].angle = None
        print("\nProgram terminated by user. :) ")

if __name__ == '__main__':
    init()
    main()