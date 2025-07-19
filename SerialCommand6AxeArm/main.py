#ne marche pas encore bien
import serial
import time
import tkinter
from tkinter import messagebox
import subprocess
from approxeng.input.selectbinder import ControllerResource
import threading







AXE1value = 0
AXE2value = 0
AXE3value = 0
AXE4value = 0
AXE5value = 0
AXE6value = 0


# Configurer le port série
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=38400, timeout=1)  # Remplacez 'COM3' par le port série de votre Arduino
time.sleep(2)  # Pause pour laisser le port série s'initialiser



def infoMsg(msg):
    info_window = tkinter.Toplevel(root)
    messagebox.showinfo(title="Information", message=msg)

def warningMsg(msg):
    messagebox.showwarning(title="Attention", message=msg)

def erreurMsg(msg):
    messagebox.showwarning(title="Erreur", message=msg)

def show_about():
    # fenetre supplementaire
    about_window = tkinter.Toplevel(root)
    about_window.title("A propos")
    about_window.geometry("600x400")
    lb = tkinter.Label(about_window, text="Bonjour !")
    lb.pack()

def openRobotDK():
    pass
    """root.quit()
    time.sleep(1)
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", "openRoboDK.sh; exec bash"])"""

"""
is_on = False
def switch():
    global is_on

    # Determin is on or off
    if is_on == False:
        on_button.config(image=on)
        controller_label.config(text="Controller Mode :", fg="green")
        is_on = True
    else:
        on_button.config(image=off)
        controller_label.config(text="Controller Mode :", fg="black")
        is_on = False


print(is_on)
"""

def active_controller_mode():

    if is_active.get():  # Si le Checkbutton est coché
        controller_ckeck_text.set("Enable")  
        controller_label.config(text="Controller Mode :", fg="green")
    else:  # Si le Checkbutton est décoché
        controller_label.config(text="Controller Mode :", fg="black")
        controller_ckeck_text.set("Desable")






def send_data(data):
    if arduino.isOpen():
        # Convertir la liste en chaîne séparée par des virgules
        data_str = ','.join(map(str, data)) + '\n'
        arduino.write(data_str.encode())  # Envoyer les données encodées
        print(f"Données envoyées : {data_str}")
    else:
        print("Le port série est fermé !")



#################################################################################
#Scale Interface
#################################################################################

def update_value(value, axe):
    # Récupérer la valeur actuelle de l'échelle
    global AXE1value, AXE2value, AXE3value, AXE4value, AXE5value, AXE6value
    #print(type(value))
    if axe == 1:
        AXE1value = int(value)
    elif axe == 2 :
        AXE2value = int(value)
    elif axe == 3 :
        AXE3value = int(value)
    elif axe == 4 :
        AXE4value = int(value)
    elif axe == 5 :
        AXE5value = int(value)
    elif axe == 6 :
        AXE6value = int(value)


    print(f"Valeur actuelle 1: {AXE1value}")  # Affiche la valeur dans la console
    print(f"Valeur actuelle 2: {AXE2value}")  
    print(f"Valeur actuelle 3: {AXE3value}")  
    print(f"Valeur actuelle 4: {AXE4value}")  
    print(f"Valeur actuelle 5: {AXE5value}")  
    print(f"Valeur actuelle 6: {AXE6value}") 
    send_data([AXE1value, AXE2value, AXE3value, AXE4value, AXE5value, AXE6value]) 




def show_scale_interface():
    pass


#################################################################################
#End Scale Interface
#################################################################################


#################################################################################
#Controller Interface
#################################################################################

def useController():
    while True:
        try:
            # Get a joystick
            with ControllerResource() as joystick:
                print('Found a joystick and connected')
                # Loop until disconnected
                while joystick.connected:
    

                    if int(joystick.rx * 100) > 15:
                        AXE1value += 1
                    elif int(joystick.rx * 100) < -15 :
                        AXE1value -= 1

                    if int(joystick.ry * -100) > 15:
                        AXE2value += 1
                    elif int(joystick.ry * -100) < -15 :
                        AXE2value -= 1


                    presses = joystick.check_presses()
                    if not joystick.presses.triangle:
                        if int(joystick.lx * 100) > 15:
                            AXE3value += 1
                        elif int(joystick.lx * 100) < -15 :
                            AXE3value -= 1
                        AXE5value = 0
                    else:
                        AXE3value = 0
                        if int(joystick.lx * 100) > 15:
                            AXE5value += 1
                        elif int(joystick.lx * 100) < -15 :
                            AXE5value -= 1
                    
                    if not joystick.presses.cross:
                        if int(joystick.ly * -100) > 15:
                            AXE4value += 1
                        elif int(joystick.ly * -100) < -15 :
                            AXE4value -= 1
                        AXE6value = 0
                    else:
                        AXE4value = 0
                        if int(joystick.ly * -100) > 15:
                            AXE6value += 1
                        elif int(joystick.ly * -100) < -15 :
                            AXE6value -= 1

                    if joystick.presses.circle:
                        AXE1value = 0
                        AXE2value = 0
                        AXE3value = 0
                        AXE4value = 0
                        AXE5value = 0
                        AXE6value = 0

                    message =  [AXE1value, AXE2value, AXE3value, AXE4value, AXE5value, AXE6value]
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



#################################################################################
#End Controller Interface
#################################################################################




root = tkinter.Tk()
root.title("SERIAL 6 AXE ARM COMMAND")
root.geometry("600x400")

#################################################################################
# Menu
#################################################################################
mainMenu = tkinter.Menu(root)
mode_menu = tkinter.Menu(mainMenu, tearoff=0)
mode_menu_manual = tkinter.Menu(mainMenu, tearoff=0)
about_menu = tkinter.Menu(mainMenu, tearoff=0)
help_menu = tkinter.Menu(mainMenu, tearoff=0)


mode_menu_manual.add_command(label="Scale", command=lambda: infoMsg("hello"))
mode_menu_manual.add_separator()
mode_menu_manual.add_command(label="Controller", command=lambda: useController())

mode_menu.add_cascade(label="Manual", menu=mode_menu_manual)
mode_menu_manual.add_separator()
mode_menu.add_command(label="Automatic", command=openRobotDK)


about_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Help", command=lambda: erreurMsg("hello"))



mainMenu.add_cascade(label="Mode", menu=mode_menu)
mainMenu.add_command(label="Help", command=lambda: erreurMsg("hello"))
mainMenu.add_command(label="About", command=show_about)
mainMenu.add_command(label="Quit", command=root.quit)
#################################################################################
# End Menu
#################################################################################


#################################################################################
#End Scale Interface
#################################################################################

scale_label = tkinter.Label(root, text="Scale Mode", font=("Arial", 20))
scale_label.pack(side="top", anchor="w", padx=20)

# Créer une échelle (Scale)
axe1 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal", tickinterval=300, command=lambda value: update_value(value, 1))
axe1.pack()

axe2 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 2))
axe2.pack()

axe3 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 3))
axe3.pack()

axe4 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 4))
axe4.pack()

axe5 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 5))
axe5.pack()

axe6 = tkinter.Scale(root, from_=-150, to=150, length=400, resolution=1, orient="horizontal",  tickinterval=300, command=lambda value: update_value(value, 6))
axe6.pack()

#################################################################################
#End Scale Interface
#################################################################################



#################################################################################
#End Controller Interface
#################################################################################

"""

on = tkinter.PhotoImage(file="images/on.png")
off = tkinter.PhotoImage(file="images/off.png")
# Create A Button
on_button = tkinter.Button(root, image=off, bd=0, command=switch)
on_button.pack(side="left", padx=10)
"""

controller_label = tkinter.Label(root, text="Controller Mode :", font=("Arial", 20))
controller_label.pack(side="left", padx=20)
is_active = tkinter.IntVar()
controller_ckeck_text = tkinter.StringVar(value="Desable")
controller_is_active = tkinter.Checkbutton(root, textvariable = controller_ckeck_text, variable=is_active, command=active_controller_mode, font=("Arial", 18), indicatoron=0, width=10, height=2)
controller_is_active.pack(side="left", padx=10, pady=50) 

#g = bool(is_active.trace_add("read", active_controller_mode))

if is_active.get() == True:

   useController()




#################################################################################
#End Controller Interface
#################################################################################



root.config(menu=mainMenu)
root.mainloop()

arduino.close()
