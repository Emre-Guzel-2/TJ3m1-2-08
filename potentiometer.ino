// Created by Emre Guzel
// Created on April 14 2026
// This program runs a servo motor with a potentiometer

#include <Servo.h>

// setting the variables and the pins 
Servo servoNumber8;
// RATIO helps turn the pot reading into a servo angle
// dividing the pot reading by 5 gives us the angle in degrees
const int RATIO = (1023/180);
const int potPin = A0;
int potReading = 0;   
int servoAngle = 0;

// setting the pin of the servo 
void setup()
{
  servoNumber8.attach(8);
}

void loop()
{
  // setting the calculations and angles 
  potReading = analogRead(potPin);
  servoAngle = potReading / RATIO;
  servoNumber8.write(servoAngle);

  delay(15);
}