String cmd1 = "", cmd2 =  "", cmd3 =  "", R0 = "",  R1 =  "", R2 =  "", R3 =  "",  R4 = "", R5 = "";

float R0_value = 0, R1_value = 0, R2_value = 0, R3_value = 0, R4_value = 0, R5_value = 0, soudeuse = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop() {





  if (Serial.available()) {
    String data = Serial.readStringUntil('\r');
    //Serial.println("test");

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

    //if (idx1 > 0 && idx2 > 0 && idx3 > 0 && idx4 > 0 && idx5 > 0 && idx6 > 0 && idx7 > 0 && idx8 > 0 && idx9 > 0 && idx10 > 0 && idx11 > 0 && idx12 > 0 && idx13 > 0 && idx14 > 0 ) {
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
    //}


    
    
     //soudeuse
    /*if (cmd1 == ":EN42" && R0 == ":EN42")
    {

      Serial.print("data s : "); Serial.println(cmd3);
      if (cmd3 == "1")
      {
        digitalWrite(13, 1);
      }

    }*/


    /*Serial.println("data : " + data);

      Serial.print("data R1 : "); Serial.println(R1_value);

      if (R1_value != 0)
      {
      digitalWrite(13, 1);
      Serial.println("if ");
      }
      else
      {
      digitalWrite(13, 0);
      Serial.println("else ");
      }*/
    Serial.print(":N142\r");


  }
}

/*
  void setup() {
  Serial.begin(9600);
  }

  void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\r');
    Serial.print("Received: ");
    Serial.println(cmd);

    if (cmd.startsWith(":ECJNT")) {
      // Simuler les positions des joints (à remplacer par les valeurs réelles)
      String joints = "JNTS 10.0 20.0 30.0 40.0 50.0 60.0\r";
      Serial.print("Sending: ");
      Serial.print(joints);
      Serial.print(":N142\r"); // confirmation
    } else if (cmd.startsWith(":E")){
        Serial.print(":N142\r"); // Confirmation des autres commandes
    } else if (cmd.startsWith(":W")){
      Serial.print(":N142\r"); // Confirmation des commandes Write
    }
  }
  }*/
