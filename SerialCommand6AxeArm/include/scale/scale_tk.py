import serial
import time
import tkinter

cmd1 = "v"
cmd2 =  "v"
cmd3 =  "v"
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
#soudeuse = 0

# Configurer le port série
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=38400, timeout=1)  # Remplacez 'COM3' par le port série de votre Arduino
time.sleep(2)  # Pause pour laisser le port série s'initialiser

def send_data(data):
    if arduino.isOpen():
        # Convertir la liste en chaîne séparée par des espaces
        data_str = ' '.join(map(str, data)) + '\r'
        arduino.write(data_str.encode())  # Envoyer les données encodées
        print(f"Données envoyées : {data_str}")
    else:
        print("Le port série est fermé !")



def update_value(value, axe):
    # Récupérer la valeur actuelle de l'échelle
    global R0_value, R1_value, R2_value, R3_value, R4_value, R5_value
    #print(type(value))
    if axe == 1:
        R0_value = int(value)
    elif axe == 2 :
        R1_value = int(value)
    elif axe == 3 :
        R2_value = int(value)
    elif axe == 4 :
        R3_value = int(value)
    elif axe == 5 :
        R4_value = int(value)
    elif axe == 6 :
        R5_value = int(value)


    print(f"Valeur actuelle 1: {R0_value}")  # Affiche la valeur dans la console
    print(f"Valeur actuelle 2: {R1_value}")  
    print(f"Valeur actuelle 3: {R2_value}")  
    print(f"Valeur actuelle 4: {R3_value}")  
    print(f"Valeur actuelle 5: {R4_value}")  
    print(f"Valeur actuelle 6: {R5_value}") 
    time.sleep(0.1)
    send_data([cmd1, cmd2, cmd3, R0, R0_value, R1, R1_value, R2, R2_value, R3, R3_value, R4, R4_value, R5, R5_value]) 




root = tkinter.Tk()
root.title("SERIAL 6 LED COMMAND")
root.geometry("600x400")

# Créer une échelle (Scale)
axe0 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal", tickinterval=300, command=lambda value: update_value(value, 1))
axe0.pack()

axe1 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 2))
axe1.pack()

axe2 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 3))
axe2.pack()

axe3 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 4))
axe3.pack()

axe4 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 5))
axe4.pack()

axe5 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 6))
axe5.pack()




root.mainloop()

arduino.close()