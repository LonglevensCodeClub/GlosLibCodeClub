from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
sense.get_temperature()
red = (255,0,0)
sense.show_message("Astro Pi", text_colour=red)
w = (255,255,255)
b = (0,0,0)

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

from time import sleep
sleep(2)
 
