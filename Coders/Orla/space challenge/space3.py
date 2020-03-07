

from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(90)
temp = round( sense.temperature, 1 )
b=0,50,255
bk=0,0,0
r=255,0,0
sense.show_message("Hi from Natasha & Orla!", text_colour=b, back_colour=bk, scroll_speed=0.05)
w=255,255,255
p=255,102,155
bl=102,153,255
pr=102,0,204
p2=255,26,140
y=255,255,0

picture = [w,w,pr,p,p,pr,w,w,
  w,p,w,p,p,w,p,w, 
  pr,w,w,p,p,w,w,pr,
  pr,w,b,w,w,b,w,pr,
  pr,w,b,w,w,b,w,pr,
  pr,w,w,w,w,w,w,pr,
  pr,w,r,w,w,r,w,pr, 
  pr,pr,w,r,r,w,pr,pr]
sense.set_pixels(picture)
sleep(2)
temp = round( sense.temperature, 1 )
sense.show_message( "It's " + str(temp) + " C" )

if temp > 30:
  grid = [(255,0,0)]*64
elif temp<20:
  grid=[b]*64
else:
  grid=[y]*64
sense.set_pixels(grid)