from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD
from time import sleep
from os import system

shutdown_called = 10

def pushed_in(event):
    global shutdown_called
    if event.action == ACTION_HELD:
        shutdown_called -= 1

def shut_down():
    system("shutdown now -h")
    exit(0)

def restart():
    print("Restart program")
    system("python SenseHAT.py")
            
sense = SenseHat()
sense.stick.direction_middle = pushed_in
sense.stick.direction_down = restart
sense.set_rotation(270)

red = (255,0,0)
b=0,0,0
w=255,255,255

h= (255,255,0)
hot = [b,b,h,h,b,h,h,b,
       b,b,h,h,b,h,h,b,
       b,b,h,h,b,h,h,b,
       b,b,h,h,h,h,h,b,
       b,b,h,h,h,h,h,b,
       b,b,h,h,b,h,h,b,
       b,b,h,h,b,h,h,b,
       b,b,b,b,b,b,b,b]

w=(255,255,255)
cold = [b,b,b,b,b,b,b,b,
        b,w,w,w,w,w,w,b,
        b,w,w,w,w,w,w,b,
        b,w,w,b,b,b,b,b,
        b,w,w,b,b,b,b,b,
        b,w,w,w,w,w,w,b,
        b,w,w,w,w,w,w,b,
        b,b,b,b,b,b,b,b]

blank = [b,b,b,b,b,b,b,b,
         b,b,b,b,b,b,b,b,
         b,b,b,b,b,b,b,b,
         b,b,b,b,b,b,b,b,
         b,b,b,b,b,b,b,b,
         b,b,b,b,b,b,b,b,
         b,b,b,b,b,b,b,b,
         b,b,b,b,b,b,b,b]


while (shutdown_called > 9):

    sense.show_message("Whats the temperature?", scroll_speed=0.1, text_colour=red)

    temp = round (sense.get_temperature(), 1)

    sense.show_message("It is " + str(temp) + " degrees", scroll_speed=0.1)

    if temp >= 20:
      sense.set_pixels(hot)
    else:
        sense.set_pixels(cold)

    sleep(2)
    sense.clear()

if shutdown_called < 1:
    shut_down()













