from time import sleep
from sense_emu import SenseHat

sense = SenseHat()
sense.set_rotation(90)
b=0,0,255
bk=0,0,0
#sense.show_message("Astro Pi. Hi from Natasha and Orla!", text_colour=b, back_colour=bk, scroll_speed=0.1)
w=255,255,255
p=255,102,155
bl=102,153,255
pr=102,0,204
p2=255,26,140
picture = [w,w,pr,p,p,pr,w,w,
  w,p2,w,p,p,w,p2,w, 
  pr,w,w,p,p,w,w,pr,
  pr,w,bl,w,w,bl,w,pr, 
  pr,w,bl,w,w,bl,w,pr,
  pr,w,w,w,w,w,w,pr,
  pr,w,p2,w,w,p2,w,pr, 
  pr,pr,w,p2,p2,w,pr,pr]
sense.set_pixels(picture)
sleep(2)
temp = round( sense.temperature, 1 )
#sense.show_message( "It is " + str(temp) + " degrees" )
b = min(255-(temp),255)
g = 0
r = min(0+(temp)+100,0)
m = int(r),int(g),int(b)
       

print(m)
grid=[0]*64
for i in range (64):
    grid[i]=m
sense.set_pixels(grid)
