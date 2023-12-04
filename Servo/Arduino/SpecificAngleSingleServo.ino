#include <Servo.h>

Servo myservo;  // Create servo object to control a servo

int val;    // Variable of servo required angle
void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  val = map(val, 0, 1023, 0, 180);     // Scale it to use it with the servo (value between 0 and 180)
  myservo.write(val);                  // Sets the servo position according to the scaled value
  delay(15);                           // Safety delay
}
