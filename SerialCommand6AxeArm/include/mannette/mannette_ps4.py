from approxeng.input.selectbinder import ControllerResource
import time
import serial
import time


cmd1 = "vide"
cmd2 =  "vide"
cmd3 =  "vide"
R0 = "R0"
R1 =  "R1"
R2 =  "R2"
R3 =  "R3"
R4 = "R4"
R5 = "R5"

R0_value = 0
R1_value = 0
R2_value = 0
R3_value = 0
R4_value = 0
R5_value = 0

R0_limit_positive = 100
R1_limit_positive = 100
R2_limit_positive = 100
R3_limit_positive = 100
R4_limit_positive = 100
R5_limit_positive = 100

R0_limit_negative = -100
R1_limit_negative = -100
R2_limit_negative = -100
R3_limit_negative = -100
R4_limit_negative = -100
R5_limit_negative = -100

# Configurer le port série
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)  # Remplacez 'COM3' par le port série de votre Arduino
time.sleep(2)  # Pause pour laisser le port série s'initialiser

def send_data(data):
    if arduino.isOpen():
        # Convertir la liste en chaîne séparée par des espaces
        data_str = ' '.join(map(str, data)) + '\r'
        arduino.write(data_str.encode())  # Envoyer les données encodées
        print(f"Données envoyées : {data_str}")
    else:
        print("Le port série est fermé !")



while True:
    try:
        # Get a joystick
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            # Loop until disconnected
            while joystick.connected:
 

                if int(joystick.rx * 100) > 90:
                    R0_value += 1
                    if R0_value >= R0_limit_positive:
                        R0_value = R0_limit_positive

                elif int(joystick.rx * 100) < -90 :
                    R0_value -= 1
                    if R0_value <= R0_limit_negative:
                        R0_value = R0_limit_negative

                if int(joystick.ry * -100) > 90:
                    R1_value += 1
                    if R1_value >= R1_limit_positive:
                        R1_value = R1_limit_positive
                elif int(joystick.ry * -100) < -90 :
                    R1_value -= 1
                    if R1_value <= R1_limit_negative:
                        R1_value = R1_limit_negative

                
                if int(joystick.lx * 100) > 90:
                    R2_value += 1
                    if R2_value >= R2_limit_positive:
                        R2_value = R2_limit_positive
                elif int(joystick.lx * 100) < -90 :
                    R2_value -= 1
                    if R2_value <= R2_limit_negative:
                        R2_value = R2_limit_negative
                    

                if int(joystick.ly * -100) > 90:
                    R3_value += 1
                    if R3_value >= R3_limit_positive:
                        R3_value = R3_limit_positive
                elif int(joystick.ly * -100) < -90 :
                    R3_value -= 1
                    if R3_value <= R3_limit_negative:
                        R3_value = R3_limit_negative



                presses = joystick.check_presses()
                #print(joystick.buttons.held('circle'))
                #joystick.presses.cross

                if joystick.buttons.held('triangle') is not None and joystick.buttons.held('triangle') >=0.5 :
                    R4_value += 1
                    if R4_value >= R4_limit_positive:
                        R4_value = R4_limit_positive
                elif joystick.buttons.held('cross') is not None and joystick.buttons.held('cross') >=0.5 :
                    R4_value -= 1
                    if R4_value <= R4_limit_negative:
                        R4_value = R4_limit_negative
                    

                if joystick.buttons.held('circle') is not None and joystick.buttons.held('circle') >=0.5:
                    R5_value += 1
                    if R5_value >= R5_limit_positive:
                        R5_value = R5_limit_positive
                elif joystick.buttons.held('square') is not None and joystick.buttons.held('square') >=0.5 :
                    R5_value -= 1
                    if R5_value <= R5_limit_negative:
                        R5_value = R5_limit_negative

                if joystick.presses.home:
                    R0_value = 0
                    R1_value = 0
                    R2_value = 0
                    R3_value = 0
                    R4_value = 0
                    R5_value = 0

                message = [cmd1, cmd2, cmd3, R0, R0_value, R1, R1_value, R2, R2_value, R3, R3_value, R4, R4_value, R5, R5_value]
                print(message)

                print(presses)

                
                send_data(message)
                
                #time.sleep(0.1)

        # Joystick disconnected...
        print('Connection to joystick lost')
    except IOError:
        # No joystick found, wait for a bit before trying again
        print('Unable to find any joysticks')
        time.sleep(1.0)
    #return message

arduino.close()