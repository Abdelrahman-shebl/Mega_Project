// Including Wire Library for I2C Communications
#include <Wire.h>

// Including Adafruit PWM Library
#include <Adafruit_PWMServoDriver.h>

// Defining Pulses and Frequencies
#define MIN_PULSE_WIDTH       650
#define MAX_PULSE_WIDTH       2350
#define FREQUENCY             50

// Creating Adafruit_PWMServoDriver Object
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Defining value variables for the 4 servos
int valA = 0;
int valB = 45;
int valC = 90;
int valD = 180;

// Defining Motor Outputs on PCA9685 board
int motorA = 0;
int motorB = 4;
int motorC = 8;
int motorD = 12;
void setup() 
{
  pwm.begin();
  pwm.setPWMFreq(FREQUENCY);
}

void moveMotor(int angleValue, int motorOut)
{
  int pulse_wide, pulse_width;

  // Convert to pulse width
  pulse_wide = map(angleValue, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  pulse_width = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
  
  //Moving Motor
  pwm.setPWM(motorOut, 0, pulse_width);
}

void loop() {
  //Moving Motor A
  moveMotor(valA, motorA);
  
  //Moving Motor B
  moveMotor(valB, motorB);
    
  //Moving Motor C
  moveMotor(valC, motorC);
  
  //Moving Motor D
  moveMotor(valD, motorD);
}