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
from time import sleep
import threading
import os
from subprocess import check_call
import socket
import turtle
import logging

# Set up logging
FORMAT = '%(asctime)s %(levelname)s %(clientId)s %(message)s'
formatter = logging.Formatter(FORMAT)
consoleHandler = logging.StreamHandler(stream=sys.stdout)
consoleHandler.setFormatter(formatter)
logger = logging.getLogger("sts-pi_bluethooth_rover")
logger.addHandler(consoleHandler)
logger.setLevel(logging.DEBUG)

#Flag to indicate that the application is closing down
exiting = False

#Flag to indicate a client is connected
connected = True

#Flag to indicate the client connection is to be maintained.
stayConnected = True

#Flag to indicate the camera is being used.
cameraInUse = False


def closeDown():
    """Closes down the application, stopping the STS-PI if it is moving.
    """
    global exiting
    exiting = True
    logger.info("Exiting application", extra={"clientId":clientInfo})
    check_call(['sudo', 'poweroff'])
    raise SystemExit
    os._exit

button_delay = 0.1

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

screenX = turtle.Screen()
screenX.setworldcoordinates(-100,-120, 100, 120)
turtleX = turtle.Turtle()
turtleY = turtle.Turtle()
turtleZ = turtle.Turtle()

turtleX.color("red")
turtleY.color("green")
turtleZ.color("blue")

oldX = 0
oldY = 0
oldZ = 0

#screenZ = turtle.Screen()
#screenZ.setworldcoordinates(90, 90, 180, 180)

# X,Y,Z : Min = 100, Max = 165

while True:

  buttons = wii.state['buttons']

  # Detects whether + and - are held down and if they are it quits the program
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print('\nClosing connection ...')
    # NOTE: This is how you RUMBLE the Wiimote
    #wii.rumble = 1
    #time.sleep(1)
    #wii.rumble = 0
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
      dat = wii.state['acc']
      datX = dat[0] - oldX
      datY = dat[1] - oldY
      datZ = dat[2] - oldZ

      oldX = dat[0]
      oldY = dat[1]
      oldZ = dat[2]

      res = "Moving "
      moving = False

      if (datX < 100):

          if (datX > 1):
              res += " left"
              moving = True
          elif (datX < -1):
              res += "right"
              moving = True
          else:
              res = "static X"

          if (datY > 1):
              res += ", moving down"
              moving = True
          elif (datY < -1):
              res += ", moving up"
              moving = True
          else:
              res += ", static Y"

          if (datZ > 1):
              res += ", moving back"
              moving = True
          elif (datZ < -1):
              res += ", moving forward"
              moving = True
          else:
              res += ", static Z"

          if (moving):
              print(dat, datX, datY, datZ, res)

          turtleX.penup()
          turtleX.setheading(90)
          turtleX.forward(datX)
          turtleX.setheading(0)
          turtleX.forward(datY)
          #turtleY.goto(50, datY)
          #turtleZ.goto(90, datZ)

      time.sleep(0.01)
      check = (buttons & cwiid.BTN_HOME)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print('Minus Button pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print('Plus Button pressed')
    time.sleep(button_delay)
