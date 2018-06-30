#!/usr/bin/python3.5

""" Module to control the STS-Pi Rover via the eight buttons on the Explorer Hat.

Button   Action
======   ======
 1.      Move forward.
 2.      Increment the speed at which the rover shall next move by 10%.
 3.      Increment the duration of the next move by one second. (Max 10 sec)
         When the red LED is lit, works as an emergency stop.
 4.      Move backwards
 5.      Spin right
 6.      Spin left
 7.      Reset speed and duration to zero.
 8.      Shutdown the rover.

LEDs
====
 Amber   Flashes once per 10% of maximum speed each time button 2 is pressed.

 Red     Flashes once per second duration set after button 3 is pressed except
         when button 3 is used to stop motion.
         Stays on while the rover is moving.

 Green   On indicates the rover is ready for use.

 Blue    Not used.

"""

import sys
import explorerhat
from time import sleep
import threading
from picamera import PiCamera
import time
import os
from subprocess import check_call

#peed and duration variables
speed = 0
duration = 0

#Pi Camera declaration
camera = PiCamera()
camera.rotation = 180

#Time at which motion shall end.
endTime = time.time()

# Flag to indicate that the application is closing down
exiting = False

# Flag to indicate that the rover is currently moving.
moving = False

def stop():
    """ Stop the STS-PI moving. Do not call directly. Use setStopTime(0) so
    that the rover and the waitForStop thread are both stopped.
    """
    print("Stopping STS-PI")
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.light.red.off()
    global moving
    moving = False
    if not exiting:
        print("STS-PI Stopped")

def setStopTime(duration):
    """ Sets the time at which the STS-PI will be stopped.
    """
    now = time.time()
    global endTime
    endTime = now + duration

def waitForStop(duration):
    """ Waits for the time to reach the stop time before stopping the STS-PI.
    """
    explorerhat.light.red.on()
    global moving
    moving = True
    setStopTime(duration)
    try:
        while (time.time() < endTime and not exiting):
            sleep(0.2)
        stop()

    except (KeyboardInterrupt, SystemExit):
        print("SystemExit Called")
        stop()

def threadForStopping(duration):
    """ Sets up a new thread for stopping the STS-PI after motion has started.
    """
    t = threading.Thread(target=waitForStop, args=[duration], daemon=True)
    t.start()

def forwards():
    """ Moves the STS-PI forwards at the speed set and for the number of seconds
    selected.
    """
    print("Forwards at ",speed,"% for ",duration, "seconds")
    explorerhat.motor.one.forwards(speed)
    explorerhat.motor.two.forwards(speed)
    threadForStopping(duration)

def backwards():
    """ Moves the STS-PI backwards at the speed set and for the number of seconds
    selected.
    """
    print("Backwards at ",speed,"% for ",duration, "seconds")
    explorerhat.motor.one.backwards(speed)
    explorerhat.motor.two.backwards(speed)
    threadForStopping(duration)
    
def spinAntiClockwise():
    """ Spins the STS-PI anti-clockwise at the speed set and for the number of
    seconds selected.
    """
    print("Spin anti-clockwise at", speed,"% for ", duration, "seconds")
    explorerhat.motor.one.speed(speed)
    explorerhat.motor.two.speed(speed * -1)
    threadForStopping(duration)

def spinClockwise():
    """ Spins the STS-PI clockwise at the speed set and for the number of
    seconds selected.
    """
    print("Spin clockwise at", speed, "% for ", duration, "seconds")
    explorerhat.motor.one.speed(speed * -1)
    explorerhat.motor.two.speed(speed)
    threadForStopping(duration)
    
def changeSpeed(increment):
    """ Updates the global speed variable when the speed slider is adjusted.
    """
    global speed
    speed += int(increment)
    if (speed > 100):
        speed = 100
    flashes = int(speed / 10)
    print("Speed now {}%".format(speed))
    for n in range(0, flashes):
        explorerhat.light.yellow.on()
        sleep(0.25)
        explorerhat.light.yellow.off()
        sleep(0.25)
    
def changeDuration(increment):
    """ Updates the global duration variable when the duration slider is
    adjusted.
    """
    global duration
    duration += int(increment)
    if (duration > 10):
        duration = 10
    print("Duration now {}secs".format(duration))
    for n in range(0, duration):
        explorerhat.light.red.on()
        sleep(0.25)
        explorerhat.light.red.off()
        sleep(0.25)

def closeDown():
    """ Closes down the application, stopping the STS-PI if it is moving.
    """
    explorerhat.light.green.off()
    print("Exiting STS-PI application")
    global exiting
    exiting = True
    setStopTime(0)
    explorerhat.light.off()
    check_call(['sudo', 'poweroff'])
    raise SystemExit
    os._exit

def buttonPressed(channel, event):
    """ Action to be taken upon each button press
    """
    print("Button =", channel, "Pressed Event =", event)
    if (channel == 1):
        forwards()
    elif (channel == 2):
        changeSpeed(10)
    elif (channel == 3):
        if moving:
            setStopTime(0)
            print("Stopped - Button 3 pressed while moving.")
        else:
            changeDuration(1)
    elif (channel == 4):
        backwards()
    elif (channel == 5):
        spinClockwise()
    elif (channel == 6):
        spinAntiClockwise()
    elif (channel == 7):
        global speed
        global duration
        speed = 0
        duration = 0
        print("Speed and duration set to zero.")
    elif (channel == 8):
        closeDown()
    sleep(0.1)

print("Initialising STS-PI")

#Show steady green light to show the STS-PI is ready for use.
explorerhat.light.green.on()

#Function to call if a button is pressed.
explorerhat.touch.pressed(buttonPressed)

#Keep alive (until the shutdown button is pressed.)
while(True):
    sleep(0.05)
