#!/usr/bin/python3

""" Simple GUI to test the operation of the STS-PI Rover.

    The rover's yellow LED will light to indicate the program is running.

    The green LED will flash when a photo is being taken, solid green when
    a video is being recorded.

    The red LED will light when the rover is moving.
"""

import sys
import explorerhat
from time import sleep
from guizero import App, PushButton, Slider, Text, Waffle
import threading
from picamera import PiCamera
import time
import os

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

def stop():
    """ Stop the STS-PI moving. Do not call directly. Use setStopTime(0) so that
    the rover and the waitForStop thread are both stopped.
    """
    print("Stopping STS-PI")
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.light.red.off()
    if not exiting:
        print("Re-enabling motion buttons")
        forwardButton.enable()
        backwardButton.enable()
        spinLeftButton.enable()
        spinRightButton.enable()
        stopButton.disable()        
        print("STS-PI Stopped")

def setStopTime(duration):
    """ Sets the time at which the STS-PI will be stopped. Use this method
    instead with a duration of zero instead of calling stop directly to stop
    the rover from moving. Otherwise the waitForStop thread will execute on
    schedule after the stop has been executed and may interfere with later
    movement commands.
    """
    now = time.time()
    global endTime
    endTime = now + duration

def waitForStop(duration):
    """ Waits for the time to reach the stop time before stopping the STS-PI.
    """    
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

def threadForStopping(duration):
    """ Sets up a new thread for stopping the STS-PI after motion has started.
    """
    t = threading.Thread(target=waitForStop, args=[duration], daemon=True)
    t.start()

def forwards():
    """ Moves the STS-PI forwards at the speed set and for the number of seconds
    selected.
    """
    print("Forwards at {}% for {} seconds".format(speed, duration))
    explorerhat.motor.one.forwards(speed)
    explorerhat.motor.two.forwards(speed)
    threadForStopping(duration)

def backwards():
    """ Moves the STS-PI backwards at the speed set and for the number of seconds
    selected.
    """    
    print("Backwards at {}% for {} seconds".format(speed, duration))
    explorerhat.motor.one.backwards(speed)
    explorerhat.motor.two.backwards(speed)
    threadForStopping(duration)
    
def spinAntiClockwise():
    """ Spins the STS-PI anti-clockwise at the speed set and for the number of
    seconds selected.
    """
    print("Spin anti-clockwise at {}% for {} seconds".format(speed, duration))
    explorerhat.motor.one.speed(speed)
    explorerhat.motor.two.speed(speed * -1)
    threadForStopping(duration)

def spinClockwise():
    """ Spins the STS-PI clockwise at the speed set and for the number of
    seconds selected.
    """    
    print("Spin clockwise at {}% for {} seconds".format(speed, duration))
    explorerhat.motor.one.speed(speed * -1)
    explorerhat.motor.two.speed(speed)
    threadForStopping(duration)
    
def changeSpeed(slider_value):
    """ Updates the global speed variable when the speed slider is adjusted.
    """    
    global speed
    speed = int(slider_value)
    print("New speed =", speed)

def changeDuration(slider_value):
    """ Updates the global duration variable when the duration slider is
    adjusted.
    """    
    global duration
    duration = int(slider_value)
    print("New duration =", duration)

def disableMotionButtons():
    """ Disables all the motion buttons and enables the stop button.
    """
    stopButton.enable()
    forwardButton.disable()
    backwardButton.disable()
    spinLeftButton.disable()
    spinRightButton.disable()

def getTimeStamp():
    """ Returns a timestamp for photos and videos in the format: YYYY_MMDD_hhmmss
    """
    return time.strftime("%Y_%m%d_%H%M%S")

def takePhoto():
    """ Takes a photo using the camera on the front of the STS-PI.
    """
    filename = '/home/pi/Desktop/Rover/' + getTimeStamp() + '_photo.jpg'
    print("Taking photo, image will be saved as:", filename)
    try:
        camera.start_preview()
        explorerhat.light.green.blink()
        sleep(3)
        camera.capture(filename)
    finally:
        camera.stop_preview()
        explorerhat.light.green.off()
    
def takeVideo():
    """ Takes a video of length duration using the camera on the front of the
    STS-PI.
    """
    filename = '/home/pi/Desktop/Rover/' + getTimeStamp() + '_video.h264'
    print("Taking video, video will be saved as:", filename)
    try:
        camera.start_preview()
        explorerhat.light.green.blink(0.5)
        camera.start_recording('/home/pi/Desktop/video.h264')
        explorerhat.light.green.on()
        sleep(duration)
        camera.stop_recording()
    except Exception as e:
        print("Exception during recording:" + str(e))
    finally:
        camera.stop_preview()
        explorerhat.light.green.off()

def closeDown():
    """ Closes down the application, stopping the STS-PI if it is moving.
    """
    disableMotionButtons()
    global exiting
    exiting = True
    print("Exiting STS-PI application")
    setStopTime(0)
    explorerhat.light.off()
    app.destroy()
    sys.exit()
    os._exit
    
def buttonPressed(channel, event):
    """ Button pressed handler. Note this still runs after exit due to separate
    thread. Need to call sys.exit for the Explorer Hat thread.
    """
    if exiting:
        sys.exit()
    else:
        print("Button = {} Pressed Event = {}".format(channel, event))
        if (buttonWaffle.get_pixel(channel - 1, 0) != "red"):
            buttonWaffle.set_pixel(channel - 1, 0, "red")
        else:
            buttonWaffle.set_pixel(channel - 1, 0, "white")
        sleep(0.1)

#def buttonReleased(channel, event):
#     """Button released handler - not reliable. Note held not reporting.
#     """
#    print("Channel=", channel, "Released Event=", event)
#    buttonWaffle.set_pixel(channel - 1, 0, "white")

#Declare the GUI application
app = App("STS Controller", layout="grid")

#Indicate the rover is responsive to commands.
explorerhat.light.yellow.on()

#Create forwards and backwards buttons
forwardButton = PushButton(app, forwards, text="Forwards", grid=[1,0])
backwardButton = PushButton(app, backwards, text="Backwards", grid=[1,2])

#Create spin left and right buttons
spinLeftButton = PushButton(app, spinAntiClockwise, text="Spin Left", grid=[0,1])
spinRightButton = PushButton(app, spinClockwise, text="Spin Right", grid=[2,1])

#Create a slider to set the speed.
speedTitle = Text(app, "Speed %", grid=[0,3])
spdSlider = Slider(app, command=changeSpeed, grid=[1,3,3,1])
spdSlider.value = 10

#Create a slider to set the duration of the next movement
durationTitle = Text(app, "Duration (secs)", grid=[0,4])
durationSlider = Slider(app, command=changeDuration, grid=[1,4,3,1])
durationSlider.value = 1

#Button to stop the STS-PI in an emergency
stopButton = PushButton(app, setStopTime, [0], text="STOP", grid=[1,1])

#Buttons to take videos and photos.
photoButton = PushButton(app, takePhoto, text="Photo", grid=[0,5])
videoButton = PushButton(app, takeVideo, text="Video", grid=[2,5])

#Waffle to display button presses
buttonWaffle = Waffle(app, 1, 8, grid=[0,6,3,2])

#Function to call if a button is pressed.
explorerhat.touch.pressed(buttonPressed)
#explorerhat.touch.released(buttonReleased)
#explorerhat.touch.held(buttonHeld)

#This spacer text increases the gap below the controls and the application exit button.
buttonIds = Text(app, "1    2    3    4    5    6    7    8 ", grid=[0,8,3,1])
spacer = Text(app, "", grid=[0,9])
exitButton = PushButton(app, closeDown, text="Exit", grid=[1,10])

# Show the GUI reasonable central on the display
app.tk.geometry("300x380+600+400")
app.display()

