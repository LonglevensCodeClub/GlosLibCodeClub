#!/usr/bin/python3

""" Module to control the STS-PI rover using Bluetooth using the Raspberry Pi
with Bluetooth MAC address: B8:27:EB:2D:16:29 (RPi 2) or B8:27:EB:2B:AB:C0 (Rpi
3) using RFCOMM port 3. The rover and client Raspberry Pi should be BlueTooth
paired before use.

To disconnect the rover from the client, press button 1.

To stop the rover without using the client, press Button 3 (by the red LED).

Always shutdown the rover before disconnecting power by pressing Button 8.
To reboot and restart when in headless mode, press button 7.


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
This means the rover is implementing the command and is ready to accept another
command subject to no clash with the current command.

If the rover cannot carry out the command, it will respond with:
Request refused: <reason>
The reason could be "Camera in use" if a second camera action has been
requested before the first has been completed.

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
from subprocess import call
import bluetooth
import subprocess
import socket
import logging

# Set up logging
FORMAT = '%(asctime)s %(levelname)s %(clientId)s %(message)s'
formatter = logging.Formatter(FORMAT)
consoleHandler = logging.StreamHandler(stream=sys.stdout)
consoleHandler.setFormatter(formatter)
logger = logging.getLogger("sts-pi_bluethooth_rover")
logger.addHandler(consoleHandler)
logger.setLevel(logging.INFO)

#Global speed and duration variables
speed = 0
duration = 0

#Identity of the client
clientInfo = ""

#Pi Camera declaration
try:
    camera = PiCamera()
    camera.rotation = 180
except Exception as e:
    logger.exception("Camera already in use, check no other processes running " +
                     "(eg headless process on start up)",
                     extra={"clientId":clientInfo})
    raise SystemExit

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
            logger.exception("ERROR: Unable to send {} to client".format(message),
                             extra={"clientId":clientInfo})
    else:
        logger.error("Client is not connected. Unable to send {}".format(message),
                     extra={"clientId":""})

def clientAck():
    """Inform the client that the command has been accepted and that the rover
    is ready to receive another command.
    """
    sendMessage("Acknowledged")
    explorerhat.light.yellow.off()
    logger.info("Client acknowledgement sent.", extra={"clientId":clientInfo})

def clientRefuse(reason):
    """Inform the client that the command has been accepted and that the rover
    is ready to receive another command.
    """
    sendMessage("Request refused:" + reason)
    explorerhat.light.yellow.off()
    logger.warn("Client refusal sent with the reason: {}".format(reason),
                extra={"clientId":clientInfo})
    
def stop():
    """Function to stop the STS-PI moving and re-enable the movement buttons.
    """
    logger.info("Stopping STS-PI", extra={"clientId":clientInfo})
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.light.red.off()
    if connected:
        sendMessage("Stopped")
    if not exiting:
        logger.debug("STS-PI Stopped", extra={"clientId":clientInfo})

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
    logger.info("Setting stop time in {} seconds".format(duration), 
                extra={"clientId":clientInfo})
    explorerhat.light.red.blink(1)
    setStopTime(duration)
    try:
        while (time.time() < endTime and not exiting):
            sleep(0.05)
        stop()
    except (KeyboardInterrupt, SystemExit):
        logger.exception("SystemExit Called", extra={"clientId":clientInfo})
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
        logger.warn("Client is not connected",  extra={"clientId":clientInfo})

def forwards():
    """Moves the STS-PI forwards. The client is asked to provide the speed and
    duration.
    """
    logger.info("Forwards command received",  extra={"clientId":clientInfo})
    enquireSpeedAndDuration()
    clientAck()
    logger.info("Forwards at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(speed, speed, duration)

def backwards():
    """Moves the STS-PI backwards. The client is asked to provide the speed and
    duration.
    """
    enquireSpeedAndDuration()
    clientAck()
    logger.info("Backwards at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(speed * -1, speed* -1, duration)
    
def spinAntiClockwise():
    """Spins the STS-PI anti-clockwise. The client is asked to provide the speed
    and duration.
    """
    enquireSpeedAndDuration()
    clientAck()
    logger.info("Spin anti-clockwise at {}% for {} seconds".format(speed,
                                                                   duration),
                extra={"clientId":clientInfo})

    move(speed, speed * -1, duration)

def spinClockwise():
    """Spins the STS-PI clockwise. The client is asked to provide the speed and
    duration.
    """
    enquireSpeedAndDuration()
    clientAck()
    logger.info("Spin clockwise at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
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
    logger.info("Taking photo, image will be saved as: {}".format(filename),
                extra={"clientId":clientInfo})
    try:
        camera.start_preview()
        explorerhat.light.green.on()
        sleep(2)
        camera.capture(filename)
    finally:
        camera.stop_preview()
        explorerhat.light.green.off()
        cameraInUse = False
        sendMessage("Camera available")
        logger.info("Photo finished", extra={"clientId":clientInfo})

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
    logger.info("Taking video. Video will be saved as: {}".format(filename),
                extra={"clientId":clientInfo})

    try:
        camera.start_preview()
        explorerhat.light.green.on()
        camera.start_recording(filename)
        explorerhat.light.green.on()
        sleep(length)
        camera.stop_recording()
    finally:
        camera.stop_preview()
        explorerhat.light.green.off()
        cameraInUse = False
        sendMessage("Camera available")
        logger.debug("Video finished", extra={"clientId":clientInfo})

def closeDown():
    """Closes down the application, stopping the STS-PI if it is moving.
    """
    global exiting
    exiting = True
    logger.info("Exiting STS-PI application", extra={"clientId":clientInfo})
    setStopTime(0)
    explorerhat.light.off()
    check_call(['sudo', 'poweroff'])
    raise SystemExit
    os._exit

def restart():
    """Closes down the application, stopping the STS-PI if it is moving.
    """
    global exiting
    exiting = True
    logger.info("Exiting STS-PI application and rebooting", extra={"clientId":clientInfo})
    setStopTime(0)
    explorerhat.light.off()
    os.system("sudo reboot")

def buttonPressed(channel, event):
    """Informs the client that a button has been pressed or released.
    Keyword arguments:
    channel -- The button number
    event -- pressed or released.
    """
    if connected:
        sendMessage("Button" + str(channel))
        logger.info("Button Channel={} Event={}".format(channel, event),
                    extra={"clientId":clientInfo})
    else:
        logger.info("Button Channel={} Event={}".format(channel, event),
                    extra={"clientId":""})
    if channel == 1:
        setStopTime(0)
        global stayConnected
        stayConnected = False
    if channel == 3:
        setStopTime(0)
    if channel == 7:
        restart()
    if channel == 8:
        closeDown()

def enquireValue(valueRequired):
    """Asks the client for an integer value and returns it

    Keyword arguments:
    valueRequired -- Prompt for which value is required from the client.
    """
    try:
        sendMessage(valueRequired + "?")
        logger.info(valueRequired + " requested", extra={"clientId":clientInfo})
        val = clientSocket.recv(size)
        value = int.from_bytes(val, byteorder="big")
        logger.info("Value received = {}".format(value), extra={"clientId":clientInfo})
        return value
    except Exception as e:
        logger.exception("Problem requesting value=",
                         extra={"clientId":clientInfo})

def enquireSpeedAndDuration():
    """Asks the client for the speed and duration to be applied to the movement
    requested by the client.
    """
    global speed, duration
    speed = enquireValue("Speed")
    duration = enquireValue("Duration")
    logger.info("Speed={} Duration={}".format(speed, duration),
                extra={"clientId":clientInfo})

## Set up the server connection:
port = 3
backlog = 1
size = 1024
## For info:
##     STS-Pi1 : Bluetooth MAC Address = 'B8:27:EB:2B:AB:C0'
##     STS-Pi2 : Bluetooth MAC Address = 'B8:27:EB:87:BC:83'

#Allow a few seconds as boot up may override making Bluetooth discoverable.
sleep(5)

#Make Bluetooth discoverable
subprocess.call(['sudo','hciconfig','hci0', 'piscan'])

#Action to be taken if any button is pressed.
explorerhat.touch.pressed(buttonPressed)

#Main Loop
while True:
    try:
        connected = False
        explorerhat.light.blue.blink()
        logger.info("Setting up Bluetooth connection", extra={"clientId":""})
        roverSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        roverSocket.bind(("", port)) #Mac Address not required, default is local
        roverSocket.listen(backlog)
        logger.info("Bluetooth connection ready. Waiting client connection",
                    extra={"clientId":""})
        clientSocket, clientInfo = roverSocket.accept()
        logger.debug("Client info={}".format(clientInfo),
                     extra={"clientId":clientInfo})
        clientSocket.settimeout(0.5)
        connected = True
        logger.info("Client connection made to: {}".format(clientInfo),
                    extra={"clientId":clientInfo})
        explorerhat.light.blue.on()    
        
        while connected and stayConnected:
            logger.debug("Checking for incoming data",
                         extra={"clientId":clientInfo})
            sleep(0.1)
            try:
                data = clientSocket.recv(size)
                explorerhat.light.yellow.on()
                data = data.decode("utf-8")
                logger.info("received = {}".format(data),
                             extra={"clientId":clientInfo})
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
                        logger.info("Taking Photo", extra={"clientId":clientInfo})
                    else:
                        clientRefuse("Camera in use")
                        
                elif data == "Video":
                    if not cameraInUse:
                        length = enquireValue("Duration")
                        t = threading.Thread(target=takeVideo,
                                             args=[length],
                                             daemon=True)
                        t.start()
                        logger.debug("Video started", extra={"clientId":clientInfo})
                    else:
                        clientRefuse("Camera in use")
                elif data == "Stop":
                    logger.info("Emergency Stop", extra={"clientId":clientInfo})
                    setStopTime(0)
                    clientAck()
                elif data == "Bye":
                    sendMessage("Bye")
                    sleep(1)
                    connected = False
            except Exception as e:
                # Expected exception when the client is not sending messages
                logger.debug(e, extra={"clientId":clientInfo})
            
    except Exception as e1:
        logger.exception(e1, extra={"clientId":clientInfo})
        if connected:
            try:
                sendMessage("Bye")
            except Exception:
                logger.error("message", extra={"clientId":clientInfo}, exc_info=True)

    logger.info("Resetting connection", extra={"clientId":clientInfo})
    setStopTime(0)
    if connected:
        stayConnected = True
        sendMessage("Bye")
        sleep(1)
        logger.info("Closing sockets", extra={"clientId":clientInfo})
        clientSocket.shutdown(socket.SHUT_RD)
        roverSocket.shutdown(socket.SHUT_WR)
        clientSocket.close()
        roverSocket.close()
    connected = False
    explorerhat.light.blue.off()
    explorerhat.light.yellow.off()
    logger.info("Reset Bluetooth connection.", extra={"clientId":""})
