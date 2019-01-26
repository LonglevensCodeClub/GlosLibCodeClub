#!/usr/bin/python2

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

import cwiid, time
import sys
import explorerhat
from time import sleep
import threading
from picamera import PiCamera
import os
from subprocess import check_call
#import bluetooth
import socket
import logging

# Set up logging
FORMAT = '%(asctime)s %(levelname)s %(clientId)s %(message)s'
formatter = logging.Formatter(FORMAT)
consoleHandler = logging.StreamHandler(stream=sys.stdout)
consoleHandler.setFormatter(formatter)
logger = logging.getLogger("sts-pi_bluethooth_rover")
logger.addHandler(consoleHandler)
logger.setLevel(logging.DEBUG)

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
connected = True

#Flag to indicate the client connection is to be maintained.
stayConnected = True

#Flag to indicate the camera is being used.
cameraInUse = False

def sendMessage(message):
    """Sends a message to the client if the client is connected.
    Keyword arguments:
    message - The text to be sent to the client.
    """
    #if connected:
    #    try:
    #        clientSocket.send(message)
    #        sleep(0.15)
    #    except Exception as e:
    #        logger.exception("ERROR: Unable to send {} to client".format(message),
    #                         extra={"clientId":clientInfo})
    #else:
    #    logger.error("Client is not connected. Unable to send {}".format(message),
    #                 extra={"clientId":""})

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
    t = threading.Thread(target=waitForStop, args=[duration])
    t.setDaemon(True)
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

def turnRight():
    """Moves the STS-PI forwards. The client is asked to provide the speed and
    duration.
    """
    logger.info("turnRight command received",  extra={"clientId":clientInfo})
    enquireSpeedAndDuration()
    clientAck()
    logger.info("turnRight at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(0, speed, duration)

def turnLeft():
    """Moves the STS-PI forwards. The client is asked to provide the speed and
    duration.
    """
    logger.info("turnLeft command received",  extra={"clientId":clientInfo})
    enquireSpeedAndDuration()
    clientAck()
    logger.info("turnLeft at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(speed, 0, duration)


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
    #speed = enquireValue("Speed")
    #duration = enquireValue("Duration")
    #logger.info("Speed={} Duration={}".format(speed, duration),
    #            extra={"clientId":clientInfo})
    speed = 10
    duration = 0.3

button_delay = 0.3

print('Please press buttons 1 + 2 on your Wiimote now ...')
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print("Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!")
  quit()

wii.led = 1

print('Wiimote connection established!\n')
print('Go ahead and press some buttons\n')
print('Press PLUS and MINUS together to disconnect and quit.\n')

time.sleep(2)

wii.rpt_mode = cwiid.RPT_BTN

while True:

  buttons = wii.state['buttons']

  # Detects whether + and - are held down and if they are it quits the program
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print('\nClosing connection ...')
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
  if (buttons & cwiid.BTN_LEFT):
    print('Left pressed')
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print('Right pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    forwards()
    time.sleep(button_delay)    

  if (buttons & cwiid.BTN_DOWN):
    print('Down pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    print('Button 1 pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print('Button 2 pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    print('Button A pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    print('Button B pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    check = 0
    while check == 0:
      print(wii.state['acc'])
      time.sleep(0.01)
      check = (buttons & cwiid.BTN_HOME)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print('Minus Button pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print('Plus Button pressed')
    time.sleep(button_delay)
