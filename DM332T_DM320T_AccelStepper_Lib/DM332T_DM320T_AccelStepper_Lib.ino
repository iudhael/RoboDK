//controle des moteurs pas apas avec le driver DM332T ET DM320T

#include <AccelStepper.h>

#include <Encoder.h>

// Stepper----------------------------------------------------------------
int R1step = 2;
int R1dir = 3;

int R2step = 4;
int R2dir = 5;

int R3step = 6;
int R3dir = 7;

int R4step = 8;
int R4dir = 9;

int R5step = 10;
int R5dir = 11;

int R6step = 12;
int R6dir = 13;


AccelStepper stepper1(1, R1step, R1dir); // 1 pour A4988

/*
 
AccelStepper stepper2(1, R2step, R2dir);

AccelStepper stepper3(1, R3step, R3dir);

AccelStepper stepper4(1, R4step, R4dir);

AccelStepper stepper5(1, R5step, R5dir);

AccelStepper stepper6(1, R6step, R6dir);

*/



//set encoder pins
/*


 
//set encoder multiplier
float J1encMult = 10;
float J2encMult = 10;
float J3encMult = 10;
float J4encMult = 10;
float J5encMult = 5;
float J6encMult = 10;




Encoder J1encPos(14, 15);
Encoder J2encPos(17, 16);
Encoder J3encPos(19, 18);
Encoder J4encPos(20, 21);
Encoder J5encPos(23, 22);
Encoder J6encPos(24, 25);


float J1EncSteps = 0;
float J2EncSteps = 0;
float J3EncSteps = 0;
float J4EncSteps = 0;
float J5EncSteps = 0;
float J6EncSteps = 0;

float J1Steps = 0;
float J2Steps = 0;
float J3Steps = 0;
float J4Steps = 0;
float J5Steps = 0;
float J6Steps = 0;

J1stepPin

*/



void setup() {
  stepper1.setMaxSpeed(1000.0);
  stepper1.setAcceleration(5000.0);

}

void loop() {
  stepper1.moveTo(500);

  stepper1.run();
  

}
