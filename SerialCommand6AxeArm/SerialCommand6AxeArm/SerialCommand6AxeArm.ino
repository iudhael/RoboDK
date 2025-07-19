//pas encre tester mais devrai bien marcher
//controle de 6 moteurs pas a pas avec le A4988 driver

String cmd1 = "", cmd2 =  "", cmd3 =  "", R0 = "",  R1 =  "", R2 =  "", R3 =  "",  R4 = "", R5 = "";

float R0_value = 0, R1_value = 0, R2_value = 0, R3_value = 0, R4_value = 0, R5_value = 0, soudeuse = 0;

#include <AccelStepper.h>


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

AccelStepper stepper2(1, R2step, R2dir);

AccelStepper stepper3(1, R3step, R3dir);

AccelStepper stepper4(1, R4step, R4dir);

AccelStepper stepper5(1, R5step, R5dir);

AccelStepper stepper6(1, R6step, R6dir);



// Variable---------------------------------------------------------------
int R1value = 0;

int R2value = 0;

int R3value = 0;

int R4value = 0;

int R5value = 0;

int R6value = 0;
//int soudeuse = 0;


void setup()
{
  Serial.begin(38400); // Initialisation de la communication série

  stepper1.setMaxSpeed(1000.0);
  stepper1.setAcceleration(5000.0);

  stepper2.setMaxSpeed(1000.0);
  stepper2.setAcceleration(5000.0);

  stepper3.setMaxSpeed(1000.0);
  stepper3.setAcceleration(5000.0);

  stepper4.setMaxSpeed(1000.0);
  stepper4.setAcceleration(5000.0);

  stepper5.setMaxSpeed(1000.0);
  stepper5.setAcceleration(5000.0);

  stepper6.setMaxSpeed(1000.0);
  stepper6.setAcceleration(5000.0);



  pinMode(13, OUTPUT);
}

void loop()
{

  axeValues();


  stepper1.moveTo(R1value);

  stepper2.moveTo(R2value);

  stepper3.moveTo(R3value);

  stepper4.moveTo(R4value);

  stepper5.moveTo(R5value);

  stepper6.moveTo(R6value);


  stepper1.run();

  stepper2.run();

  stepper3.run();

  stepper4.run();

  stepper5.run();

  stepper6.run();


  if (R0_value == -90)
  {
    digitalWrite(13, HIGH);
  }
  //delay(1000);
  if (R1_value == 12)
  {
    digitalWrite(13, LOW);
  }
  //delay(1000);




}

void axeValues()
{
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\r'); // Lire les données reçues
    data.trim();                       // Nettoyer les espaces

    // Permet de chercher l'espace à partir de l'indice prciser idx1+1 Avec idx1+1 don cherche l'espace à l'indice idx1+1
    // le +11 est ajouter pur ignorer l'espace à l'indice idx1
    int idx1 = data.indexOf(' ');
    int idx2 = data.indexOf(' ', idx1 + 1);
    int idx3 = data.indexOf(' ', idx2 + 1);
    int idx4 = data.indexOf(' ', idx3 + 1);
    int idx5 = data.indexOf(' ', idx4 + 1);

    int idx6 = data.indexOf(' ', idx5 + 1);
    int idx7 = data.indexOf(' ', idx6 + 1);
    int idx8 = data.indexOf(' ', idx7 + 1);
    int idx9 = data.indexOf(' ', idx8 + 1);
    int idx10 = data.indexOf(' ', idx9 + 1);
    int idx11 = data.indexOf(' ', idx10 + 1);
    int idx12 = data.indexOf(' ', idx11 + 1);
    int idx13 = data.indexOf(' ', idx12 + 1);
    int idx14 = data.indexOf(' ', idx13 + 1);


    // Extraire les valeurs
    if (idx1 > 0 && idx2 > 0 && idx3 > 0 && idx4 > 0 && idx5 > 0 && idx6 > 0 && idx7 > 0 && idx8 > 0 && idx9 > 0 && idx10 > 0 && idx11 > 0 && idx12 > 0 && idx13 > 0 && idx14 > 0 ) {
      //ici on recupere les caracteres se trouvant entre les indice preciser
      cmd1 = data.substring(0, idx1);
      cmd2 = data.substring(idx1 + 1, idx2) ;
      cmd3 = data.substring(idx2 + 1, idx3);

      R0 = data.substring(idx3 + 1, idx4);
      R0_value = data.substring(idx4 + 1, idx5).toFloat();

      R1 = data.substring(idx5 + 1, idx6);
      R1_value = data.substring(idx6 + 1, idx7).toFloat();

      R2 = data.substring(idx7 + 1, idx8);
      R2_value = data.substring(idx8 + 1, idx9).toFloat();

      R3 = data.substring(idx9 + 1, idx10);
      R3_value = data.substring(idx10 + 1, idx11).toFloat();

      R4 = data.substring(idx11 + 1, idx12);
      R4_value = data.substring(idx12 + 1, idx13).toFloat();

      R5 = data.substring(idx13 + 1, idx14);
      R5_value = data.substring(idx14 + 1).toFloat();

      Serial.println("data : " + data);
      Serial.print("data R1 : "); Serial.println(R1_value);
      Serial.print("R0_value "); Serial.println(R0_value);
      Serial.print("R1_value "); Serial.println(R1_value);
      Serial.print("R2_value "); Serial.println(R2_value);
      Serial.print("R3_value "); Serial.println(R3_value);
      Serial.print("R4_value "); Serial.println(R4_value);
      Serial.print("R5_value "); Serial.println(R5_value);

    }
  }
}
