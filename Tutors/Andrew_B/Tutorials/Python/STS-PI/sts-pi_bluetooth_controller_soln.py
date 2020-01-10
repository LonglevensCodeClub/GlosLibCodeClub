#!/usr/bin/python3

""" Provides a GUI to control a STS-PI rover using Bluetooth for communication.
"""

import sys
from time import sleep
from guizero import App, ButtonGroup, PushButton, Slider, Text, Waffle
import threading
import time
import os
import bluetooth
import socket

#Global speed and duration variables
speedLeft = 0
speedRight = 0
duration = 1

#Flag to indicate that the Bluetooth connection is working.
connected = False

#Flag to indicate that an exchange between the client and rover is in progress.
commandInProgress = False

# Flag to indicate that the application is closing down
exiting = False

# Flag to indicate that the current command should be stopped asap.
abort = False

# Size of data buffer
size = 1024


def setup_gui():
    """ Create the GUI for controlling the STS-Pi Rover.
    """
    global app, rover1Button, rover2Button
    app = App("STS Pi Controller", layout="grid")
    rover1Button = PushButton(app, connect, args=[1], text="Connect to STS-Pi 1", grid=[1, 0])
    rover2Button = PushButton(app, connect, args=[2], text="Connect to STS-Pi 2", grid=[2, 0])
    disconnectButton = PushButton(app, command=disconnect, text="Disconnect", grid=[3, 0])

    leftSliderText = Text(app, "Left Wheel Speed %", grid=[1, 2])
    leftSlider = Slider(app,
                        command=changeLeftSpeed,
                        start=-100,
                        end= 100,
                        grid=[2, 2])

    rightSliderText = Text(app, "Right Wheel Speed %", grid=[1, 3])
    rightSlider = Slider(app,
                         command=changeRightSpeed,
                         start=-100,
                         end= 100,
                         grid=[2, 3])

    durationText = Text(app, "Duration secs", grid=[1, 4])
    durationSlider = Slider(app,
                         command=changeDuration,
                         start=1,
                         end= 5,
                         grid=[2, 4])

    moveButton = PushButton(app, move, text="Move", grid=[1, 5])
    stopButton = PushButton(app, stop, text="Stop", grid=[2, 5])
    app.when_closed = closeDown

    
def connect(roverChoice):
    """Set up the Client BlueTooth connection.
    """
    serverMACaddress1 = 'B8:27:EB:2B:AB:C0'
    serverMACaddress2 = 'B8:27:EB:87:BC:83'
    port = 3
    global roverSocket, connected, commandInProgress
    if roverChoice == 1:
        serverMACaddress = serverMACaddress1
    else:
        serverMACaddress = serverMACaddress2
    print("Connecting to STS-PI with serverMACaddress:", serverMACaddress)
    try:    
        roverSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        roverSocket.connect((serverMACaddress, port))
        print("Connected to ", roverSocket.getpeername())
        connected = True
        rover1Button.disable()
        rover2Button.disable()
        commandInProgress = False
    except bluetooth.btcommon.BluetoothError as bte:
        print("Bluetooth Error:", bte )
        connected = False

def disconnect():
    """Disconnect from the currently connected rover.
    """
    global roverSocket, connected
    print("Disconnecting from STS-PI")
    if connected:
        sendCommand("Bye")
        sleep(1)
        try:
            rover1Button.enable()
            rover2Button.enable()
            connected = False
            roverSocket.shutdown(socket.SHUT_RDWR)
        except Exception as e:
            print("Unable to close socket:", str(e))
        
def sendCommand(command):
    """Function to send an instruction to the rover.

    Keyword arguments:
    command -- Instruction known to the rover.
    """
    global commandInProgress, roverChoice, exiting
    attempts = 20
    while commandInProgress and not exiting:
        sleep(0.2)
        print("Waiting for previous command to be acknowledged")
        attempts -= 1
        if attempts == 0:
            exiting = True
            print("Lost communication with rover, terminating connection.")
            disconnect()
    
    if connected:
        commandInProgress = True
        try:
            roverSocket.send(command)
            print("Command sent=", command)
        except Exception as e:
            print("Error sending value:", str(e))
            commandInPrgress = False
    else:
        print("ERROR: Not connected")

def sendInteger(value):
    """Convert an integer to a byte value and send to the rover.
    """
    print("Sending integer value", value)
    try:
        roverSocket.send(str(value).encode('utf8'))
    except Exception as e:
        print("Error sending value:", str(e))
    
def receiveResponse():
    """Receive a question or update from the rover.
    """
    global connected, size, token, commandInProgress
    print("Connection made =", connected)
    while not exiting:
        try:
            while connected:
                global abort, commandInProgress, speedRight, speedLeft

                print("Listening for a response from Rover")
                data = roverSocket.recv(1024)

                if data:
                    print("Data received=", data)
                    rover = data.decode("utf-8")
                    if (rover.endswith("?")):
                        print("Rover is asking for:", rover)
                    else:
                        print("Rover:", rover)
                    if rover.startswith("Request refused:"):
                        print("Rover has responded with:", rover)
                        commandInProgress = False
                    elif rover == "Wheel Speed Left?":
                        if not abort:
                            sendInteger(speedLeft)
                        else:
                            sendInteger(0)
                    elif rover == "Wheel Speed Right?":
                        if not abort:
                            sendInteger(speedRight)
                        else:
                            sendInteger(0)
                    elif rover == "Duration?":
                        if not abort:
                            sendInteger(duration)
                        else:
                            sendInteger(0)
                    elif rover == "Moving":
                        moving = True
                    elif rover == "Stopped":
                        abort = False
                    elif rover == "Acknowledged":
                        commandInProgress = False
                    elif rover == "Camera in use":
                        disableCameraButtons()
                        checkingCamera = False
                    elif rover == "Camera available":
                        enableCameraButtons()
                        checkingCamera = False
                    elif rover.startswith("Button"):
                        num = rover.strip('ButtonpPressed')
                        buttonPressed(int(num))
                    elif rover == "Bye":
                        print("Rover has disconnected.")
                        connected = False
                        roverSocket.close()
                        if not exiting:
                            disableRoverButtons()
                            commandInProgress = False
                            abort = False
                sleep(0.1)
        except Exception as e:
            if not exiting:
                print("Exception in receive response:", str(e))
                connected = False
                commandInProgress = False

def stop():
    """Stop the rover moving asap.
    """
    print("Emergency Stop pressed")
    global abort
    abort = True
    sendCommand("Stop")
    print("Emergency Stop requested")

def move():
    """Moves the STS-PI forwards at the speed set and for the number of
    seconds selected.
    """
    print("Move for ", duration, "seconds at speeds of {}% left and {}% right"
              .format(speedLeft, speedRight))
    sendCommand("Move")

def changeLeftSpeed(slider_value):
    """Updates the global speed variable when the speed slider is adjusted.
    Keyword arguments:
    slider_value - The value representing the position of the Speed slider.
    """
    global speedLeft
    speedLeft = int(slider_value)
    print("New left wheel speed=", speedLeft)

def changeRightSpeed(slider_value):
    """Updates the global speed variable when the speed slider is adjusted.
    Keyword arguments:
    slider_value - The value representing the position of the Speed slider.
    """
    global speedRight
    speedRight = int(slider_value)
    print("New right wheel speed=", speedRight)

def changeDuration(slider_value):
    """Updates the global duration variable when the duration slider is
    adjusted.
    Keyword arguments:
    slider_value - The value representing the position of the Duration slider.
    """
    global duration
    duration = int(slider_value)
    print("New duration =", duration)

def closeDown():
    """Closes down the application, stopping the STS-PI if it is moving."""
    global exiting, roverSocket
    exiting = True
    print("Exiting STS-PI application")
    if connected:
        disconnect()
        try:
            roverSocket.close()
        except Exception as e:
            print("Unable to close socket:", str(e))
    app.destroy()
    raise SystemExit
    
def buttonPressed(number):
    """Button pressed notification handler. simply toggles the requisite Waffle
    upon each press notification.

    Keyword arguments:
    number -- The number of the button pressed.
    """

def disableRoverButtons():
    """ Disable all buttons other than Connect and Exit. Also clears the Waffle
    communication status and button pressed disaplays.
    """

# Await connection
disableRoverButtons()

# Thread to receive feedback questions and status
t = threading.Thread(target=receiveResponse, daemon=True)
t.start()

#Show the GUI.
setup_gui()
