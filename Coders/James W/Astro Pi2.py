from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
sense.get_temperature()
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red, scroll_speed=0.08)
w = (255,255,255)
b = (0,0,0)
y = (255, 255, 0)
g = (0, 255, 0) 
r = (255, 0, 0)
B = (0, 0, 255)
G = (0, 255, 0)

picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b ]

sense.set_pixels(picture)

sleep(2)

temp = round ( sense.temperature, 1 )
sense.show_message( str(temp) )
sense.show_message( "It is " + str(temp) + "degrees" )


hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g ]



def setGrid(x,y):
	a,b,c,d=b,b,b,b
	if x==1:
		a=w
	elif x==2:
		b=w
	elif x==3:
		c=w
	else:
		d=w
	t=0.25
	
cold = [
  b, b, w, b, b, b, w, b,
  b, b, b, b, b, w, b, b,
  b, w, b, b, b, b, b, w,
  b, b, b, b, w, b, b, b,
  w, b, b, w, b, b, w, b,
  b, b, b, b, b, b, b, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w ]


  




 

temp = sense.temperature
if temp >= 20:
    sleep(1)
    sense.set_pixels(hot)
else:
  for i in range(0,5):
    sense.set_pixels(cold) 
    sleep(0.1)
    #sense.set_pixels(cold2)
    sleep(0.1)
  
    

