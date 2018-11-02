#!/usr/bin/python2

""" Module to use a Wii remote control control the STS-PI rover using
the Raspberry Pi with Bluetooth MAC address: B8:27:EB:2D:16:29 (RPi 2)
 or B8:27:EB:2B:AB:C0 (Rpi 3).

To disconnect the rover from the Wii controller , press buttons + and -
at the same time.

Always shutdown the rover before disconnecting power by pressing Button
8 on the Raspberry Pi Explorer Hat on the Rover itself.

To reboot and restart when in headless mode, press button 7 on the
Explorer Hat.

CONTROLS
========
The following controls can be used to direct with the rover:

Forwards - Up Button (Wii Cross buttons)
Backwards - Down Button (Wii Cross buttons)
Spin Clockwise - Right Button (Wii Cross buttons)
Spin Anti-clockwise - Left Button (Wii Cross buttons)
Accelerate - Wii Button A
Brake - Wii Button B
Stop  - No Wii direction buttons pressed. Button 3 on the Explorer Hat
Photo - Wii Button 1
Video - Wii Button 2


STATUS
======
While the rover is waiting for a Wii controller connection, the blue Explorer
Hat LED will flash. Once a connection is made, the LED will be continuous blue.
The Wii Controller will have blue flashing LEDs until connection is made, when
one blue LED will remain lit.

When the camera is in use, the Explorer Hat green LED will be lit. Camera photo
or video requests cannot happen while the camera is already in use.

When the rover is moving the Explorer Hat red LED will flash.

"""

import cwiid
import time
import sys
import explorerhat
from time import sleep
import threading
from picamera import PiCamera
import os
from subprocess import check_call
import logging

# Set up logging
FORMAT = '%(asctime)s %(levelname)s %(clientId)s: %(message)s'
formatter = logging.Formatter(FORMAT)
consoleHandler = logging.StreamHandler(stream=sys.stdout)
consoleHandler.setFormatter(formatter)
logger = logging.getLogger("sts-pi_bluethooth_rover")
logger.addHandler(consoleHandler)
logger.setLevel(logging.DEBUG)

#Global speed and duration variables
speed = 50

#Keep this fixed. Length of time for the main loop to process button commands. Any less and motion will be interrupted.
duration = 0.4

#Identity of the client
clientInfo = "WiiRemote"

# Flag to indicate motion is happening
moving = False

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

def stop():
    """Function to stop the STS-PI moving and re-enable the movement buttons.
    """
    global moving
    logger.info("Stopping STS-PI", extra={"clientId":clientInfo})
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.light.red.off()
    if not exiting:
        logger.debug("STS-PI Stopped", extra={"clientId":clientInfo})
        moving = False

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
    global endTime
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
    global moving
    if (not moving):
        t = threading.Thread(target=waitForStop, args=[duration])
        t.setDaemon(True)
        moving = True
        t.start()
    else:
        setStopTime(duration)

def move(leftWheelSpeed, rightWheelSpeed, duration):
    """move the rover with given wheel speeds for the amount of time stated by
    duration.
    Keyword arguments:
    leftWheelSpeed -- Left wheel power as a percentage.
    rightWheelSpeed -- Right wheel power as a percentage.
    duration -- The amount of time to apply the power.
    """
    if connected:
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
    logger.info("Forwards at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(speed, speed, duration)

def turnRight():
    """Moves the STS-PI forwards. The client is asked to provide the speed and
    duration.
    """
    logger.info("turnRight command received",  extra={"clientId":clientInfo})
    enquireSpeedAndDuration()
    logger.info("turnRight at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(0, speed, duration)

def turnLeft():
    """Moves the STS-PI forwards. The client is asked to provide the speed and
    duration.
    """
    logger.info("turnLeft command received",  extra={"clientId":clientInfo})
    enquireSpeedAndDuration()
    logger.info("turnLeft at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(speed, 0, duration)


def backwards():
    """Moves the STS-PI backwards. The client is asked to provide the speed and
    duration.
    """
    logger.info("Backwards at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(speed * -1, speed* -1, duration)
    
def spinAntiClockwise():
    """Spins the STS-PI anti-clockwise. The client is asked to provide the speed
    and duration.
    """
    logger.info("Spin anti-clockwise at {}% for {} seconds".format(speed,
                                                                   duration),
                extra={"clientId":clientInfo})

    move(speed, speed * -1, duration)

def spinClockwise():
    """Spins the STS-PI clockwise. The client is asked to provide the speed and
    duration.
    """
    logger.info("Spin clockwise at {}% for {} seconds".format(speed, duration),
                extra={"clientId":clientInfo})
    move(speed * -1, speed, duration)

def getTimeStamp():
    """ Returns a timestamp in the format: YYYY_MMDD_hhmmss
    """
    return time.strftime("%Y_%m%d_%H%M%S")

def takePhoto():
    """Sets up a new thread for taking a photo by STS-PI Rover.
    """
    t = threading.Thread(target=recordPhoto)
    t.setDaemon(True)
    t.start()
    
def recordPhoto():
    """Takes a photo using the camera on the front of the STS-PI. The photo
    file is saved in the Rover folder on the Desktop. The camera must not
    currently be in use. This function should not be called directly, use
    TakePhoto instead to generate a thread so that the rover can keep moving.
    """
    global cameraInUse
    if (cameraInUse):
        logger.info("Camera is already in use, aborting photo request.",
                        extra={"clientId":clientInfo})
        return
    cameraInUse = True
    filename = '/home/pi/Desktop/Rover/' + getTimeStamp() + '_photo.jpg'
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
        logger.info("Photo finished", extra={"clientId":clientInfo})

def takeVideo(duration):
    """Sets up a new thread for taking a video by STS-PI Rover.
    """
    t = threading.Thread(target=recordVideo, args=[duration])
    t.setDaemon(True)
    t.start()

def recordVideo(length):
    """Takes a video using the camera on the front of the STS-PI. The client is
    asked to provide the duration. The video file is saved in the Rover folder
    on the Desktop. The camera must not currently be in use. This function
    should not be called directly, use TakeVideo instead to generate a thread so
    that the rover can keep moving.
    """
    global cameraInUse
    if (cameraInUse):
        logger.info("Camera is already in use, aborting video request.",
                    extra={"clientId":clientInfo})
        return
    cameraInUse = True
    filename = '/home/pi/Desktop/Rover/' + getTimeStamp() + '_video.h264'
    logger.info("Taking {} second video. Video will be saved as: {}".format(length, filename),
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

def wii_rumble(length):
    """ This will vibrate the Wiimote.
        length -- Amount of time to vibrate
    """
    wii.rumble = 1
    sleep(length)
    wii.rumble = 0

def buttonPressed(channel, event):
    """ Action to be taken upon each button press
    """
    logger.debug("Button = {} Pressed Event = {}".format(channel, event),
                 extra={"clientId":clientInfo})    

    if (channel == 3):
        setStopTime(0)
        logger.warn("Stopped - Button 3 pressed while moving.",
                 extra={"clientId":clientInfo})

    if channel == 7:
        restart()
        logger.warn("Reboot selected on Explorer Hat",
                    extra={"clientId":clientInfo})

    elif (channel == 8):
        logger.warn("Shutdown selected on Explorer Hat",
                    extra={"clientId":clientInfo})
        closeDown()

    sleep(0.1)

#Function to call if a button on the Explorer Hat is pressed.
explorerhat.touch.pressed(buttonPressed)

# Set up the Wii Bluetooth connection
explorerhat.light.blue.blink()

button_delay = 0.3

print('Please press buttons 1 + 2 on your Wiimote now ...')
time.sleep(1)

try:
    wii=cwiid.Wiimote()
except RuntimeError:
    logger.error("Cannot connect to your Wiimote. Run again and make sure" +
                 " you are holding buttons 1 + 2!",
                 extra={"clientId":clientInfo})
    quit()

explorerhat.light.blue.on()
wii.led = 1

logger.info('Wiimote connection established!', extra={"clientId":clientInfo})

print('Press PLUS and MINUS together to disconnect and quit.')

time.sleep(2)

wii.rpt_mode = cwiid.RPT_BTN


while not exiting:
 
    buttons = wii.state['buttons']

    # Detects whether + and - are held down and if they are it quits the program
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        logger.info('\nClosing connection ...', extra={"clientId":clientInfo})
        exiting = True
        try:
            wii.close()
            logger.info('Exiting program', extra={"clientId":clientInfo})
            quit()

        except SystemError as re:
            print('ERROR:', re)

    if (buttons & cwiid.BTN_LEFT):
        spinAntiClockwise()
    elif (buttons & cwiid.BTN_RIGHT):
        spinClockwise()
    elif (buttons & cwiid.BTN_UP):
        forwards()
    elif (buttons & cwiid.BTN_DOWN):
        backwards()
    else:
        setStopTime(0)
    
    if (buttons & cwiid.BTN_1):
            takePhoto()

    if (buttons & cwiid.BTN_2):
            takeVideo(10)

    if (buttons & cwiid.BTN_A):
        speed += 10
        if (speed > 100):
            speed = 100
            logger.debug('Max speed achieved.', extra={"clientId":clientInfo})
        else:
            logger.info('Speed increased to {}%'.format(speed),
                        extra={"clientId":clientInfo})
            
    if (buttons & cwiid.BTN_B):
        speed -= 10
        if (speed < 0):
            speed = 0
            logger.debug('Minimum speed achieved.', extra={"clientId":clientInfo})

        logger.info('Speed decreased to {}%'.format(speed),
                    extra={"clientId":clientInfo})

    # Test for wii controller motion sensing.
    if (buttons & cwiid.BTN_HOME):
        wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        check = 0
        while check == 0:
            print(wii.state['acc'])
            time.sleep(0.01)
            check = (buttons & cwiid.BTN_HOME)

    time.sleep(button_delay)

