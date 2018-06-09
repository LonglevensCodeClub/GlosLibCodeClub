#!/usr/bin/python3

import sys
import explorerhat
from time import sleep
import threading
from picamera import PiCamera
import time
import os
import bluetooth

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

# Function to stop the STS-PI moving and re-enable the movement buttons.
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
    disableMotionButtons()
    explorerhat.light.red.blink(1)
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
def changeSpeed(slider_value):
    global speed
    speed = int(slider_value)
    print("New speed=", speed)

# Updates the global duration variable when the duration slider is adjusted
def changeDuration(slider_value):
    global duration
    duration = int(slider_value)
    print("New duration =", duration)

# Takes a photo using the camera on the front of the STS-PI
def takePhoto():
    print("Taking photo, image will be saved as /home/pi/Desktop/image.jpg") 
    camera.start_preview()
    explorerhat.light.green.blink()
    sleep(3)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    explorerhat.light.green.off()
    

# Takes a 10 second video using the camera on the front of the STS-PI
def takeVideo():
    print("Taking video, video will be saved as /home/pi/Desktop/video.h264") 
    camera.start_preview()
    explorerhat.light.green.blink(0.5)
    camera.start_recording('/home/pi/Desktop/video.h264')
    explorerhat.light.green.on()
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()
    explorerhat.light.green.off()

# Closes down the application, stopping the STS-PI if it is moving.
def closeDown():
    global exiting
    exiting = True
    print("Exiting STS-PI application")
    setStopTime(0)
    explorerhat.light.off()
    raise SystemExit
    os._exit
    
# Button pressed handler
def buttonPressed(channel, event):
    print("Channel=", channel, "Pressed Event=", event)
    client.send("Button" + channel + "pressed")
    if (buttonWaffle.get_pixel(channel - 1, 0) != "red"):
        buttonWaffle.set_pixel(channel - 1, 0, "red")
    else:
        buttonWaffle.set_pixel(channel - 1, 0, "white")
    sleep(0.1)

#Set up the server connection:
hostMACAddress = 'B8:27:EB:2B:AB:C0'
port = 3
backlog = 1
size = 1024
explorerhat.light.blue.blink()
print("Setting up Bluetooth connection")
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
explorerhat.light.blue.on()
print("Bluetooth connection ready")
try:
    print("Waiting client connection")
    client, clientInfo = s.accept()
    while True:
        print("Checking for incoming data")
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close()
