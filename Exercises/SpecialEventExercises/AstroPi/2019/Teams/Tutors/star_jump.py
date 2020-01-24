from sense_hat import SenseHat
#from sense_emu import SenseHat
sense = SenseHat()
sense.set_rotation(270)

from time import sleep

#Col:Red, Grn, Blue
r = (255,   0,   0)
y = (255, 255,   0)
b = (  0,   0, 255)
w = (255, 255, 255)
s = (150, 100,  70) # skin
h = (150,  75,   0) # hair 
f = (  0,   0,   0) # feet

sense.show_message("Hi! Keep warm with some star jumps:", scroll_speed=0.05, text_colour=h, back_colour=b)

man_stood = [
    b, b, b, h, h, b, b, b,
    b, b, h, s, s, h, b, b,
    b, b, h, s, s, h, b, b,
    b, b, b, w, w, b, b, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, b, s, w, w, s, b, b,
    b, b, b, f, f, b, b, b
]

man_jump = [
    b, b, b, h, h, b, b, b,
    b, b, h, s, s, h, b, b,
    b, b, h, s, s, h, b, b,
    b, b, b, w, w, b, b, b,
    s, w, w, w, w, w, w, s,
    b, b, b, w, w, b, b, b,
    b, b, w, b, b, w, b, b,
    b, f, b, b, b, b, f, b
]

for t in range(6):
  sense.set_pixels(man_stood)
  sleep(0.8)
  sense.set_pixels(man_jump)
  sleep(0.8)

temp = round(sense.get_temperature(), 1)
sense.show_message('It\'s ' + str(temp) + 'C', scroll_speed=0.05, text_colour=r, back_colour=b)
