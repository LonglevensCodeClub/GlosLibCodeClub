from microbit import *

happy = Image("28282:"
             "82828:"
             "28282:"
             "82828:"
             "28282")

happy1 = Image("82828:"
             "28282:"
             "82828:"
             "28282:"
             "82828")

while True:
    display.show([happy, happy1], delay=50)