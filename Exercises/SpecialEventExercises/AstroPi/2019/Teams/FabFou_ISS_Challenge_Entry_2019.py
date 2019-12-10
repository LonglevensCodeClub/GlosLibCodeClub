
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

red = (255,0,0)
sense.show_message("Whats the temperature?", scroll_speed= 0.05,text_colour=red)

b=0,0,0
w=255,255,255
temp = round (sense.get_temperature(), 1)
sense.show_message("It is " +str(temp)+" degrees",scroll_speed= 0.05)

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








