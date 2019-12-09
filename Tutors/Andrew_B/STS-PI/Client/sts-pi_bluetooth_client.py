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
speed = 15
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

    global app, statusWaffle, roverChoice, connectButton, exitButton
    global forwardButton, stopButton, backwardButton, spdSlider, durationSlider
    global spinRightButton, spinLeftButton, photoButton, videoButton
    global buttonWaffle, disconnectButton

    # Declare the GUI application
    app = App("STS Controller", layout="grid")

    # Bluetooth connection status waffle. Single cell, blue=connected, red=not.
    statusWaffle = Waffle(app, 1, 4, 10, 10, grid=[0,0])
    if connected:
        statusWaffle.set_pixel(0, 0, "blue")
        statusWaffle.set_pixel(1, 0, "white")
        statusWaffle.set_pixel(2, 0, "white")
        statusWaffle.set_pixel(3, 0, "white")

    # Choice of STS-PI Rover
    roverChoice = ButtonGroup(app,
                              options=["STS-Pi 1", "STS-Pi 2"],
                              selected="STS-Pi 1",
                              grid=[1,0])

    # Reconnect button for when the Bluetooth connection has been lost or reset
    connectButton = PushButton(app, connect, text="Connect", grid=[2,0])

    #Create forwards and backwards buttons
    forwardButton = PushButton(app, forwards, text="Forwards", grid=[1,1])

    #Create spin left and right buttons
    spinLeftButton = PushButton(app,
                                spinAntiClockwise,
                                text="Spin Left",
                                grid=[0,2])

    #Button to stop the STS-PI in an emergency
    stopButton = PushButton(app, stop, text="STOP", grid=[1,2])

    spinRightButton = PushButton(app,
                                 spinClockwise,
                                 text="Spin Right",
                                 grid=[2,2])

    backwardButton = PushButton(app, backwards, text="Backwards", grid=[1,3])

    #Create a slider to set the speed.
    speedTitle = Text(app, "Speed %", grid=[0,4])
    spdSlider = Slider(app, command=changeSpeed, grid=[1,4,3,1])
    spdSlider.value = 15

    #Create a slider to set the duration of the next movement
    durationTitle = Text(app, "Duration (secs)", grid=[0,5], )
    durationSlider = Slider(app,
                            command=changeDuration,
                            start=1,
                            end=10,
                            grid=[1,5,3,1])
    durationSlider.value = 1

    #Buttons to take videos and photos.
    photoButton = PushButton(app, takePhoto, text="Photo", grid=[0,6])
    videoButton = PushButton(app, takeVideo, text="Video", grid=[2,6])

    #Waffle to display button presses
    buttonWaffle = Waffle(app, 1, 8, grid=[0,7,3,2])

    # Ids for the buttons on the STS-PI rover
    buttonIds = Text(app, "1    2    3    4    5    6    7    8 ", grid=[0,9,3,1])

    # This spacer text increases the gap below the controls and the exit button.
    spacer = Text(app, "", grid=[0,10]) 

    # Button to quit the application
    disconnectButton = PushButton(app, disconnect, text="Disconnect", grid=[0,11])
    disconnectButton.disable()
    exitButton = PushButton(app, closeDown, text="Exit", grid=[2,11])

def connect():
    """Set up the Client BlueTooth connection.
    """
    serverMACaddress1 = 'B8:27:EB:2B:AB:C0'
    serverMACaddress2 = 'B8:27:EB:87:BC:83'
    port = 3
    global roverSocket, connected, roverChoice, commandInProgress
    if roverChoice.value == "STS-Pi 1":
        serverMACaddress = serverMACaddress1
    else:
        serverMACaddress = serverMACaddress2
    print("Connecting to STS-PI with serverMACaddress:", serverMACaddress)
    try:    
        roverSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        roverSocket.connect((serverMACaddress, port))
        print("Connected to ", roverSocket.getpeername())
        connected = True
        statusWaffle.set_pixel(0, 0, "blue")
        connectButton.disable()
        roverChoice.disable()
        disconnectButton.enable()
        enableMotionButtons()
        enableCameraButtons()
        commandInProgress = False
    except bluetooth.btcommon.BluetoothError as bte:
        print("Bluetooth Error:", bte )
        connected = False
        statusWaffle.set_pixel(0, 0, "red")
        connectButton.enable()
        roverChoice.enable()

def disconnect():
    """Disconnect from the currently connected rover.
    """
    if stopButton.enabled:
        stop()
    global exiting, roverSocket
    print("Disconnecting from STS-PI")
    if connected:
        sendCommand("Bye")
        sleep(1)
        try:
            roverSocket.shutdown(socket.SHUT_RDWR)
            connectButton.enable()
            disconnectButton.disable()
            statusWaffle.set_pixel(0, 0, "white")
        except Exception as e:
            print("Unable to close socket:", str(e))
        
def sendCommand(command):
    """Function to send an instruction to the rover.

    Keyword arguments:
    command -- Instruction known to the rover.
    """
    global commandInProgress, roverChoice
    while commandInProgress and not exiting:
        sleep(0.1)
        print("Waiting for previous command to be acknowledged")
    if connected:
        commandInProgress = True
        statusWaffle.set_pixel(1, 0, "yellow")
        roverSocket.send(command)
        print("Command sent=", command)
    else:
        connectButton.enable()
        roverChoice.enable()
        statusWaffle.set_pixel(0, 0, "red")
        print("ERROR: Not connected")

def sendInteger(value):
    """Convert an integer to a byte value and send to the rover.
    """
    print("Sending integer value", value)
    roverSocket.send(value.to_bytes(2, byteorder='big'))

def receiveResponse():
    """Receive a question or update from the rover.
    """
    global connected, size, token, commandInProgress
    checkingCamera = False
    print("Started receiver", connected)
    while not exiting:
        try:
            while connected:
                global abort, commandInProgress 

                print("Listening for a response from Rover")
                data = roverSocket.recv(1024)

                if data:
                    #print("Data received=", data)
                    rover = data.decode("utf-8")
                    if (rover.endswith("?")):
                        print("Rover is asking for:", rover)
                    else:
                        print("Rover:", rover)
                    if rover.startswith("Request refused:"):
                        print("Rover has responded with:", rover)
                        commandInProgress = False
                    if rover == "Speed?":
                        if not abort:
                            sendInteger(speed)
                        else:
                            sendInteger(0)
                    elif rover == "Duration?":
                        if not abort:
                            sendInteger(duration)
                        else:
                            sendInteger(0)
                    elif rover == "Moving":
                        disableMotionButtons()
                        statusWaffle.set_pixel(2, 0, "red")
                    elif rover == "Stopped":
                        statusWaffle.set_pixel(2, 0, "white")
                        enableMotionButtons()
                        abort = False
                    elif rover == "Acknowledged":
                        commandInProgress = False
                    elif rover == "Camera in use":
                        disableCameraButtons()
                        statusWaffle.set_pixel(3, 0, "green")
                        checkingCamera = False
                    elif rover == "Camera available":
                        enableCameraButtons()
                        statusWaffle.set_pixel(3, 0, "white")
                        checkingCamera = False
                    elif rover.startswith("Button"):
                        num = rover.strip('Button')
                        buttonPressed(int(num))
                    elif rover == "Bye":
                        print("Rover has disconnected.")
                        connected = False
                        roverSocket.close()
                        if not exiting:
                            disableRoverButtons()
                            connectButton.enable()
                            roverChoice.enable()
                            statusWaffle.set_pixel(0, 0, "red")
                            commandInProgress = False
                            abort = False
                    if commandInProgress:
                        statusWaffle.set_pixel(1, 0, "yellow")
                    else:
                        statusWaffle.set_pixel(1, 0, "white")
                sleep(0.1)
        except Exception as e:
            if not exiting:
                print("Exception in receive response:", str(e))
                connected = False
                commandInProgress = False
                connectButton.enable()
                roverChoice.enable()
                disableRoverButtons()
                statusWaffle.set_pixel(0, 0, "red")

def stop():
    """Stop the rover moving asap.
    """
    print("Emergency Stop pressed")
    global abort
    abort = True
    sendCommand("Stop")
    print("Emergency Stop requested")

def forwards():
    """Moves the STS-PI forwards at the speed set and for the number of
    seconds selected.
    """
    disableMotionButtons()
    print("Forwards at ", speed, "% for ", duration, "seconds")
    sendCommand("Forwards")

def backwards():
    """Moves the STS-PI backwards at the speed set and for the number of
    seconds selected.
    """
    disableMotionButtons()    
    print("Backwards at ", speed, "% for ", duration, "seconds")
    sendCommand("Backwards")
    
def spinAntiClockwise():
    """Spins the STS-PI anti-clockwise at the speed set and for the number of
    seconds selected.
    """
    disableMotionButtons()
    print("Spin anti-clockwise at", speed, "% for ", duration, "seconds")
    sendCommand("SpinAntiClockwise")

def spinClockwise():
    """Spins the STS-PI clockwise at the speed set and for the number of
    seconds selected.
    """
    disableMotionButtons()
    print("Spin clockwise at", speed, "% for ", duration, "seconds")
    sendCommand("SpinClockwise")
    
def changeSpeed(slider_value):
    """Updates the global speed variable when the speed slider is adjusted.
    Keyword arguments:
    slider_value - The value representing the position of the Speed slider.
    """
    global speed
    speed = int(slider_value)
    print("New speed=", speed)

def changeDuration(slider_value):
    """Updates the global duration variable when the duration slider is
    adjusted.
    Keyword arguments:
    slider_value - The value representing the position of the Duration slider.
    """
    global duration
    duration = int(slider_value)
    print("New duration =", duration)

def disableCameraButtons():
    """Disables all the camera buttons.
    """
    photoButton.disable()
    videoButton.disable()

def enableCameraButtons():
    """Enables all the camera buttons.
    """
    photoButton.enable()
    videoButton.enable()

def disableMotionButtons():
    """Disables all the motion buttons and enables the stop button.
    """
    stopButton.enable()
    forwardButton.disable()
    backwardButton.disable()
    spinLeftButton.disable()
    spinRightButton.disable()

def enableMotionButtons():
    """Enables all the motion buttons and disables the stop button.
    """
    stopButton.disable()
    forwardButton.enable()
    backwardButton.enable()
    spinLeftButton.enable()
    spinRightButton.enable()

def takePhoto():
    """Request a photo using the camera on the front of the STS-PI."""
    sendCommand("Photo")

def takeVideo():
    """Request a video using the camera on the front of the STS-PI."""
    sendCommand("Video")

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
    print("Button {} Pressed".format(number))
    if (buttonWaffle.get_pixel(number - 1, 0) != "red"):
        buttonWaffle.set_pixel(number - 1, 0, "red")
    else:
        buttonWaffle.set_pixel(number - 1, 0, "white")

def disableRoverButtons():
    """ Disable all buttons other than Connect and Exit. Also clears the Waffle
    communication status and button pressed disaplays.
    """
    disableMotionButtons()
    disableCameraButtons()
    stopButton.disable()
    statusWaffle.set_all("white")
    buttonWaffle.set_all("white")

def checkConnected():
    """Continuously checks the Bluetooth connection. Must be run in separate
    thread.
    """
    global connected, commandInProgress
    while not exiting:
        try:
            if connected:
                roverSocket.getpeername()
        except Exception as e:
            print("Rover not connected:", str(e))
            connected = False
            disableRoverButtons()

        if connected:
            print("Rover is Connected")
        else:
            print("Rover is not Connected")
        sleep(2)


setup_gui()

# Await connection
disableRoverButtons()

# Thread to receive feedback questions and status
t = threading.Thread(target=receiveResponse, daemon=True)
t.start()

# Thread to monitor connection status
t2 = threading.Thread(target=checkConnected, daemon=True)
t2.start()

# Show the GUI reasonable central on the display
screen_width = app.tk.winfo_screenwidth()
screen_height = app.tk.winfo_screenheight()
window_width = 300
window_height = 440
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
app.tk.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
app.display()
