#!/usr/bin/python3

""" Module to control the STS-PI rover using Bluetooth using the Raspberry Pi
with MAC address:B8:27:EB:2B:AB:C0 using RFCOMM port 3.

To disconnect the rover from the client, press button 1.

To stop the rover without using the client, press Button 3 (by the red LED).

Always shutdown the rover before disconnecting power by pressing Button 8.


COMMANDS
========
The following commands can be used to communicate with the rover:

Forwards
Backwards
SpinClockwise
SpinAntiClockwise
Stop
Photo
Video

QUESTIONS
=========
For motion commands except Stop, the rover will respond with:
Speed?
Duration?
Stop will interrupt the current motion in progress and stop the rover asap.

For camera commands, the rover will respond with:
Duration?

Once the responses are complete, the rover will respond with:
Acknowledged
This means the rover is ready to accept another command.

If the rover cannot carry out the command, it will respond with:
Request refused: <reason>
The reason could be "Camera in use"

STATUS
======
While the rover is waiting for a Bluetooth connection, the blue LED will flash.
Once a connection is made, the LED will be continuous blue.

When the camera is in use, the green LED will be lit.

When responses are being made to the client the yellow LED will be lit.

When the rover is moving the red LED will be flashing.

To inform the client when the camera is in use or not, the following status
messages are used:
Camera in use
Camera available

To inform the client when the rover is moving, the following status messages
are used:
Moving
Stopped

If either the rover or the client are about to break the Bluetooth connection
they shall send the command:
Bye
The rover shall respond to Bye with:
Bye

"""

import sys
import explorerhat
from time import sleep
import threading
from picamera import PiCamera
import time
import os
from subprocess import check_call
import bluetooth
import socket

#Global speed and duration variables
speed = 0
duration = 0

#Pi Camera declaration
camera = PiCamera()
camera.rotation = 180

#Time at which motion shall end.
endTime = time.time()

#Flag to indicate that the application is closing down
exiting = False

#Flag to indicate a client is connected
connected = False

#Flag to indicate the client connection is to be maintained.
stayConnected = True

#Flag to indicate the camera is being used.
cameraInUse = False

def sendMessage(message):
    """Sends a message to the client if the client is connected.
    Keyword arguments:
    message - The text to be sent to the client.
    """
    if connected:
        try:
            clientSocket.send(message)
            sleep(0.15)
        except Exception as e:
            print("ERROR: Unable to send ", message, " to client:", str(e))
    else:
        print("Client is not connected. Unable to send ", message)

def clientAck():
    """Inform the client that the command has been accepted and that the rover
    is ready to receive another command.
    """
    sendMessage("Acknowledged")
    explorerhat.light.yellow.off()
    print("Client acknowledgement sent.")

def clientRefuse(reason):
    """Inform the client that the command has been accepted and that the rover
    is ready to receive another command.
    """
    sendMessage("Request refused:" + reason)
    explorerhat.light.yellow.off()
    print("Client refusal sent with the reason:", reason)
    
def stop():
    """Function to stop the STS-PI moving and re-enable the movement buttons.
    """
    print("Stopping STS-PI")
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.light.red.off()
    if connected:
        sendMessage("Stopped")
    if not exiting:
        print("STS-PI Stopped")

def setStopTime(duration):
    """Sets the time at which the STS-PI will be stopped.
    Keyword arguments:
    duration -- The amount of time in seconds from the current time when the
                rover will be stopped.
    """
    now = time.time()
    global endTime
    endTime = now + duration

def waitForStop(duration):
    """Waits for the time to reach the stop time before stopping the STS-PI.
    Keyword arguments:
    duration -- The amount of time in seconds from the current time when the
                rover will be stopped.
    """
    print("Setting stop time in", duration, "seconds")
    explorerhat.light.red.blink(1)
    setStopTime(duration)
    try:
        while (time.time() < endTime and not exiting):
            sleep(0.05)
        stop()
    except (KeyboardInterrupt, SystemExit):
        print("SystemExit Called")
        stop()

def threadForStopping(duration):
    """Sets up a new thread for stopping the STS-PI after motion has started.
    """
    t = threading.Thread(target=waitForStop, args=[duration], daemon=True)
    t.start()


def move(leftWheelSpeed, rightWheelSpeed, duration):
    """move the rover with given wheel speeds for the amount of time stated by
    duration.
    Keyword arguments:
    leftWheelSpeed -- Left wheel power as a percentage.
    rightWheelSpeed -- Right wheel power as a percentage.
    duration -- The amount of time to apply the power.
    """
    if connected:
        sendMessage("Moving")
        explorerhat.motor.one.speed(leftWheelSpeed)
        explorerhat.motor.two.speed(rightWheelSpeed)
        threadForStopping(duration)
    else:
        print("WARNING: Client is not connected")

def forwards():
    """Moves the STS-PI forwards. The client is asked to provide the speed and
    duration.
    """
    print("Forwards command received")
    enquireSpeedAndDuration()
    clientAck()
    print("Forwards at ",speed,"% for ",duration, "seconds")
    move(speed, speed, duration)

def backwards():
    """Moves the STS-PI backwards. The client is asked to provide the speed and
    duration.
    """
    enquireSpeedAndDuration()
    clientAck()
    print("Backwards at ",speed,"% for ",duration, "seconds")
    move(speed * -1, speed* -1, duration)
    
def spinAntiClockwise():
    """Spins the STS-PI anti-clockwise. The client is asked to provide the speed
    and duration.
    """
    enquireSpeedAndDuration()
    clientAck()
    print("Spin anti-clockwise at", speed,"% for ", duration, "seconds")
    move(speed, speed * -1, duration)

# Spins the STS-PI clockwise at the speed set and for the number of seconds selected
def spinClockwise():
    """Spins the STS-PI clockwise. The client is asked to provide the speed and
    duration.
    """
    enquireSpeedAndDuration()
    clientAck()
    print("Spin clockwise at", speed, "% for ", duration, "seconds")
    move(speed * -1, speed, duration)

def getTimeStamp():
    """ Returns a timestamp in the format: YYYY_MMDD_hhmmss
    """
    return time.strftime("%Y_%m%d_%H%M%S")
    
def takePhoto():
    """Takes a photo using the camera on the front of the STS-PI. The photo
    file is saved in the Rover folder on the Desktop.
    """
    global cameraInUse
    cameraInUse = True
    clientAck()
    sendMessage("Camera in use")    
    filename = '/home/pi/Desktop/Rover/' + getTimeStamp() + '_photo.jpg'
    sendMessage("Creating photo with filename: " + filename)
    print("Taking photo, image will be saved as: ", filename)
    try:
        camera.start_preview()
        explorerhat.light.green.blink()
        sleep(2)
        camera.capture(filename)
    finally:
        camera.stop_preview()
        explorerhat.light.green.off()
        cameraInUse = False
        sendMessage("Camera available")
        print("Photo finished")

def takeVideo(length):
    """Takes a video using the camera on the front of the STS-PI. The client is
    asked to provide the duration. The video file is saved in the Rover folder
    on the Desktop.
    """
    global cameraInUse
    cameraInUse = True
    clientAck()
    sendMessage("Camera in use")
    filename = '/home/pi/Desktop/Rover/' + getTimeStamp() + '_video.h264'
    sendMessage("Creating video with filename " + filename)
    print("Taking video. Video will be saved as", filename)
    try:
        camera.start_preview()
        explorerhat.light.green.blink(0.5)
        camera.start_recording(filename)
        explorerhat.light.green.on()
        sleep(length)
        camera.stop_recording()
    finally:
        camera.stop_preview()
        explorerhat.light.green.off()
        cameraInUse = False
        sendMessage("Camera available")
        print("Video finished")

def closeDown():
    """Closes down the application, stopping the STS-PI if it is moving.
    """
    global exiting
    exiting = True
    print("Exiting STS-PI application")
    setStopTime(0)
    explorerhat.light.off()
    check_call(['sudo', 'poweroff'])
    raise SystemExit
    os._exit
    
def buttonPressed(channel, event):
    """Informs the client that a button has been pressed or released.
    Keyword arguments:
    channel -- The button number
    event -- pressed or released.
    """
    print("Channel=", channel, "Event=", event)
    if connected:
        sendMessage("Button" + str(channel))
    if channel == 1:
        setStopTime(0)
        global stayConnected
        stayConnected = False
    if channel == 3:
        setStopTime(0)
    if channel == 8:
        closeDown()

def enquireValue(valueRequired):
    """Asks the client for an integer value and returns it

    Keyword arguments:
    valueRequired -- Prompt for which value is required from the client.
    """
    try:
        sendMessage(valueRequired + "?")
        print(valueRequired + " requested")
        val = clientSocket.recv(size)
        value = int.from_bytes(val, byteorder="big")
        print("Value received =", value)
        return value
    except Exception as e:
        print("Exception=", str(e))

def enquireSpeedAndDuration():
    """Asks the client for the speed and duration to be applied to the movement
    requested by the client.
    """
    global speed, duration
    speed = enquireValue("Speed")
    duration = enquireValue("Duration")
    print("Speed=", speed, "Duration=", duration)

#Set up the server connection:
hostMACAddress = 'B8:27:EB:2B:AB:C0'
port = 3
backlog = 1
size = 1024

#Function to call if a button is pressed.
explorerhat.touch.pressed(buttonPressed)

while True:
    try:
        connected = False
        explorerhat.light.blue.blink()
        print("Setting up Bluetooth connection")
        roverSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        roverSocket.bind((hostMACAddress, port))
        roverSocket.listen(backlog)
        print("Bluetooth connection ready. Waiting client connection")
        clientSocket, clientInfo = roverSocket.accept()
        clientSocket.settimeout(0.5)
        connected = True
        print("Client connection made to:", clientSocket.getpeername())
        explorerhat.light.blue.on()    
        
        while connected and stayConnected:
            print("Checking for incoming data")
            try:
                data = clientSocket.recv(size)
                explorerhat.light.yellow.on()
                data = data.decode("utf-8")
                print("received = ", data)
                data_end=data.find('\n')
                if data == "Forwards":
                    forwards()
                elif data == "Backwards":
                    backwards()
                elif (data == "SpinClockwise"):
                    spinClockwise()
                elif data == "SpinAntiClockwise":
                    spinAntiClockwise()
                elif data == "Camera":
                    if cameraInUse:
                        sendMessage("Camera in use")
                        explorerhat.light.yellow.off()
                    else:
                        sendMessage("Camera available")
                        explorerhat.light.yellow.off()
                elif data == "Photo":
                    if not cameraInUse:
                        t = threading.Thread(target=takePhoto, daemon=True)
                        t.start()
                        print("Taking Photo")
                    else:
                        
                        clientRefuse("Camera in use")
                        
                elif data == "Video":
                    if not cameraInUse:
                        length = enquireValue("Duration")
                        t = threading.Thread(target=takeVideo,
                                             args=[length],
                                             daemon=True)
                        t.start()
                        print("Video started")
                    else:
                        clientRefuse("Camera in use")
                elif data == "Stop":
                    print("Emergency Stop")
                    setStopTime(0)
                    clientAck()
                elif data == "Bye":
                    sendMessage("Bye")
                    sleep(1)
                    connected = False
            except:
                print("Socket timed out")
            
    except Exception as e:
        print("Exception=", str(e))
        if connected:
            try:
                sendMessage("Bye")
            except Exception as e:
                print("Unable to say Bye:" + str(e))

    print("Resetting connection")
    stayConnected = True
    if connected:
        sendMessage("Bye")
    setStopTime(0)
    print("Closing sockets")
    clientSocket.shutdown(socket.SHUT_RD)
    roverSocket.shutdown(socket.SHUT_WR)
    clientSocket.close()
    roverSocket.close()
    connected = False
    explorerhat.light.blue.off()
    explorerhat.light.yellow.off()
    print("Resetting Bluetooth connection.")
