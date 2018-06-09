#!/usr/bin/python3.5

import sys
import explorerhat
from time import sleep
import threading
from picamera import PiCamera
import time
import os
from subprocess import check_call

#Global speed and duration variables
speed = 0
duration = 0

#Pi Camera declaration
camera = PiCamera()
camera.rotation = 180

#Time at which motion shall end.
endTime = time.time()

# Flag to indicate that the application is closing down
exiting = False

print("Initialising STS-PI")

# Function to stop the STS-PI moving.
def stop():
    print("Stopping STS-PI")
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.light.red.off()
    if not exiting:
        print("STS-PI Stopped")

# Sets the time at which the STS-PI will be stopped
def setStopTime(duration):
    now = time.time()
    global endTime
    endTime = now + duration

# Waits for the time to reach the stop time before stopping the STS-PI
def waitForStop(duration):
    explorerhat.light.red.blink(0.5,0.5)
    setStopTime(duration)
    try:
        while (time.time() < endTime and not exiting):
            sleep(0.2)
        stop()

    except (KeyboardInterrupt, SystemExit):
        print("SystemExit Called")
        stop()

# Sets up a new thread for stopping the STS-PI after motion has started.
def threadForStopping(duration):
    t = threading.Thread(target=waitForStop, args=[duration], daemon=True).start()

# Moves the STS-PI forwards at the speed set and for the number of seconds selected
def forwards():
    print("Forwards at ",speed,"% for ",duration, "seconds")
    explorerhat.motor.one.forwards(speed)
    explorerhat.motor.two.forwards(speed)
    threadForStopping(duration)

# Moves the STS-PI backwards at the speed set and for the number of seconds selected
def backwards():
    print("Backwards at ",speed,"% for ",duration, "seconds")
    explorerhat.motor.one.backwards(speed)
    explorerhat.motor.two.backwards(speed)
    threadForStopping(duration)
    
# Spins the STS-PI anti-clockwise at the speed set and for the number of seconds selected
def spinAntiClockwise():
    print("Spin anti-clockwise at", speed,"% for ", duration, "seconds")
    explorerhat.motor.one.speed(speed)
    explorerhat.motor.two.speed(speed * -1)
    threadForStopping(duration)

# Spins the STS-PI clockwise at the speed set and for the number of seconds selected
def spinClockwise():
    print("Spin clockwise at", speed, "% for ", duration, "seconds")
    explorerhat.motor.one.speed(speed * -1)
    explorerhat.motor.two.speed(speed)
    threadForStopping(duration)
    
# Updates the global speed variable when the speed slider is adjusted
def changeSpeed(increment):
    global speed
    speed += int(increment)
    if (speed > 100):
        speed = 100
    flashes = int(speed / 10)
    print("New speed=", speed)
    for n in range(0, flashes):
        explorerhat.light.yellow.on()
        sleep(0.25)
        explorerhat.light.yellow.off()
        sleep(0.25)
    
# Updates the global duration variable when the duration slider is adjusted
def changeDuration(increment):
    global duration
    duration += int(increment)
    if (duration > 10):
        duration = 10
    print("new duration=", duration)
    for n in range(0, duration):
        explorerhat.light.red.on()
        sleep(0.25)
        explorerhat.light.red.off()
        sleep(0.25)


# Takes a photo using the camera on the front of the STS-PI
def takePhoto():
    print("Taking photo, image will be saved as /home/pi/Desktop/image.jpg") 
    camera.start_preview()
    explorerhat.light.blue.blink()
    sleep(3)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    explorerhat.light.blue.off()

# Takes a 10 second video using the camera on the front of the STS-PI
def takeVideo():
    print("Taking video, video will be saved as /home/pi/Desktop/video.h264") 
    camera.start_preview()
    explorerhat.light.blue.blink(0.5)
    camera.start_recording('/home/pi/Desktop/video.h264')
    explorerhat.light.blue.on()
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()
    explorerhat.light.blue.off()

# Closes down the application, stopping the STS-PI if it is moving.
def closeDown():
    print("Exiting STS-PI application")
    global exiting
    exiting = True
    setStopTime(0)
    explorerhat.light.off()
    check_call(['sudo', 'poweroff'])
    raise SystemExit
    os._exit

# Button pressed handler
def buttonPressed(channel, event):
    print("Channel=", channel, "Pressed Event=", event)
    if (channel == 1):
        forwards()
    elif (channel == 2):
        changeSpeed(10)
    elif (channel == 3):
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

#Show steady green light to show the STS-PI is ready for use.
explorerhat.light.green.on()

#Function to call if a button is pressed.
explorerhat.touch.pressed(buttonPressed)

#Keep alive (until the shutdown button is pressed.)
while(True):
    sleep(0.05)
