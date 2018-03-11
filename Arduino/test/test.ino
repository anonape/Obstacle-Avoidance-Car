/******************************************************************************
Resources: TB6612 SparkFun Library
Development environment specifics:
  Developed on Arduino 1.6.4
  Developed with ROB-9457
******************************************************************************/

// This is the library for the TB6612 that contains the class Motor and all the
// functions
#include <SparkFun_TB6612.h>
#include <stdio.h>
#include <stdlib.h>

// Pins for all inputs, keep in mind the PWM defines must be on PWM pins
// the default pins listed are the ones used on the Redbot (ROB-12097) with
// the exception of STBY which the Redbot controls with a physical switch
#define AIN1 2
#define BIN1 7
#define AIN2 4
#define BIN2 8
#define PWMA 5
#define PWMB 6
#define STBY 9

// these constants are used to allow you to make your motor configuration 
// line up with function names like forward.  Value can be 1 or -1
const int offsetA = 1;
const int offsetB = -1;

//const int trigPin = 12;
//const int echoPin = 11;
const int out=12;
const int in=11;
int i = 0;
// Initializing motors.  The library will allow you to initialize as many
// motors as you have memory for.  If you are using functions like forward
// that take 2 motors as arguements you can either write new functions or
// call the function more than once.
Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);

void setup()
{
   Serial.begin(9600);
   boolean driving = false;
   pinMode(in, INPUT); //remember: the Echo pin is the microphone pin
   pinMode(out, OUTPUT); //remember: the Trig pin is the speaker pin
}


void loop()
{
  
 // establish variables for duration of the ping, 
  // and the distance result in inches and centimeters:
  long dur;
  long dis;
  long cm;

  digitalWrite(out,LOW);
  delayMicroseconds(2);

  digitalWrite(out,HIGH);
  delayMicroseconds(10);
  digitalWrite(out,LOW);

  dur=pulseIn(in,HIGH);


  cm = microsecondsToCentimeters(dur);
  if (cm < 5) {
    left(motor1, motor2, 255);
    delay(300);          
  } else {
    forward(motor1, motor2, 255);
  }
  Serial.println(String(cm));
  delay(1000);

//

//  
//  
//  Serial.write(cm);
//  delay(1000);

//  if (Serial.available()) {
//    
//    String str = Serial.readStringUntil('\n');
//    char compass = str[0];
//    Serial.println(compass);
//    
//    if (compass == 'L') {
//      left(motor1, motor2, 100);          
//    } else if (compass == 'R') {
//     right(motor1, motor2, 100);
//    } else if (compass == 'F') {
//      forward(motor1, motor2, 100);
//    } else if (compass == 'B') {
//      forward(motor1, motor2, -100);    
//    } else if (compass = 'S') {
//      brake(motor1, motor2);
//    }
//  }
//}
}
long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}

