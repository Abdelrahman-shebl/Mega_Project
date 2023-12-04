#include <Adafruit_PWMServoDriver.h>
#include <wire.h>

Adafruit_PWMServoDriver myservo = Adafruit_PWMServoDriver();

#define SERVOMIN 150
#define SERVOMAX 600

int servonum =0;
int numofServo=6;


void setup() {
  
  myservo.begin();
  myservo.setPWMFreq(60);
  delay(10);
}

void loop() {
  for( int pulselen=SERVOMIN;pulselen<SERVOMAX;pulselen++){
    myservo.setPWM(servnum,0,pulselen);
  }
  delay(500);
  for( int pulselen=SERVOMAX;pulselen>SERVOMIN;pulselen--){
    myservo.setPWM(servnum,0,pulselen);
  }
  delay(500);
  servonum++;
  if(servonum>numofServo-1){
    servonum=0;
  }

}
