from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.set_rotation(0)
sense.show_message("what is the temperature", scroll_speed=0.06)
red = (255,0,0)
sense.show_message("20", text_colour=red)
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
w=(255, 255, 255)
b = (0, 0, 0)
h = (25,0,255)
r = (255,0,0)
g = (0,255,0)
B = (0,0,255)

joe1 = [
    g, g, w, w, w, w, b, b,
    b, w, b, b, r, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
sense.set_pixels(joe1)
sleep(2)



picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, r, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, g, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
sense.set_pixels(picture)
sleep(2)

picture = [
    b, b, w, B, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, w, w, w, w, w, b,
    b, b, w, h, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]
sense.set_pixels(picture)
