from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)


colour = (0,0,255)
back_colour = (0,255,0)
sense.show_message("Astro Pi", text_colour=colour, back_colour=back_colour, scroll_speed=0.1)
w = (255,255,255)
b = (0,0,0)
picture = [
  b, b, b, b, b, b, b, b,
  b, b, w, b, b, w, b, b, 
  b, b, w, b, b, w, b, b,
  b, b, b, b, b, b, b, b, 
  b, w, b, b, b, b, w, b,
  b, b, w, b, b, w, b, b,
  b, b, b, w, w, b, b, b, 
  b, b, b, b, b, b, b, b 
  ]

sense.set_pixels(picture)


