import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # Setting GPIO numbering mode

GPIO.setup(11,GPIO.OUT)   # Setting pin 11 as an output

servo =GPIO.PWM(11,50)    # Setting servo as pin 11 with PWM


duty = 2
while duty <= 17:
  servo.ChangeDutyCycle(duty)   #Rotating the Servo shaft
  time.sleep(1)
  duty = duty + 1                          



servo.stop()          #Cleaning up the environment
GPIO.cleanup()
print ("Everything's cleaned up")