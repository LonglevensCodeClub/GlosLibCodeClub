from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
sense.get_temperature()
red = (255,0,0)
sense.show_message("Hi from James & Conor", text_colour=red, scroll_speed=0.04)
w = (255,255,255)
b = (0,0,0)
y = (255, 255, 0)
g = (0, 255, 0) 
r = (255, 0, 0)

picture = [
    b,b,w,w,w,w,b,b,
    b,w,b,b,b,b,w,b,
    b,w,b,w,w,b,w,b,
    b,w,b,b,b,b,w,b,
    b,b,w,w,w,w,b,b,
    b,b,w,w,w,w,b,b,
    b,w,w,w,w,w,w,b,
    b,w,w,w,w,w,w,b ]

sense.set_pixels(picture)
sleep(1)
temp = round ( sense.temperature, 1 )
sense.show_message( "It is " + str(temp) + "degrees", scroll_speed=0.04 )

hot = [
  b, b, b, b, b, y, y, b,
  b, b, b, b, y, y, y, y,
  b, b, b, b, b, y, y, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g ]
  
a = w
d = b
c = b
cold = [
  a,d,c,a,d,c,a,d,
  d,c,a,d,c,a,d,c,
  a,d,c,a,d,c,a,d,
  c,a,d,c,a,d,c,a,
  d,c,a,d,c,a,d,c,
  a,d,c,a,d,c,a,d,
  c,a,d,c,a,d,c,a,
  a,d,c,a,d,c,a,d ] 


if temp >= 20:
    sleep(1)
    sense.set_pixels(hot)
else:
  for i in range(0,5):
    for i in range(0,2):
      print("i =", i)
      cold = [
  a,c,c,a,c,d,a,c,
  d,a,a,d,a,c,d,a,
  c,d,c,c,b,a,c,d,
  a,c,d,a,c,d,a,c,
  d,a,a,d,a,c,d,a,
  c,d,c,c,d,a,c,d,
  a,c,d,a,c,d,a,c,
  d,a,c,d,a,c,d,a ] 
      sense.set_pixels(cold)
      sleep(0.2)
      if i == 0:
        a = w
        d = b
        c = b
      elif i == 1:
        a = b
        d = w
        c = b
      elif i == 2:
        a = b
        d = b
        c = w
      
