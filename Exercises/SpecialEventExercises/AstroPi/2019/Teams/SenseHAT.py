from sense_hat import SenseHat, ACTION_HELD
from time import sleep
from os import system

shutdown_called = 0

def pushed_in(event):
    global shutdown_called
    if event.action == ACTION_HELD:
        shutdown_called += 1
        print("Shutdown called", shutdown_called, "times")

sense = SenseHat()
sense.stick.direction_middle = pushed_in
sense.set_rotation(180)
red = (255,0,0)
    
while shutdown_called < 4:

    sense.show_message("Whats the temperature?", scroll_speed=0.1, text_colour=red)

    b=0,0,0
    w=255,255,255
    temp = round (sense.get_temperature(), 1)
    sense.show_message("It is " + str(temp) + " degrees", scroll_speed=0.1)

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

    temp = sense.get_temperature()
    if temp >= 20:
        sense.set_pixels(hot)
    else:
        sense.set_pixels(cold)

    sleep(2)
    sense.clear()


r = red
bye = [r,r,r,b,b,b,r,r,
       r,b,r,r,b,r,r,b,
       r,b,r,b,r,b,r,b,
       r,r,b,b,r,b,r,r,
       r,b,r,b,r,b,r,b,
       r,b,r,b,r,b,r,b,
       r,b,r,b,r,b,r,b,
       r,r,b,b,r,b,r,r]

sense.set_pixels(bye)
system("shutdown now -h")
exit(0)













