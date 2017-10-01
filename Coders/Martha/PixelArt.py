from sense_emu import SenseHat
import time
from PIL import Image
import os

# Open image file
image_file = os.path.join(
os.sep, "/home", "pi", "GlosLibCodeClub", "Coders", "Martha", "example1.png")
img = Image.open(image_file)

# generate rbg values for image pixels
rbg_img = img.convert ('RGB')
image_pixels = list(rbg_img.getdata())

# Get the 64 Pixels you need
pixel_width = 1
image_width = pixel_width*8
sense_pixels = []
start_pixel = 0
while start_pixel < (image_width*64):
    sense_pixels.extend(image_pixels[start_pixel:(start_pixel+image_width):pixel_width])
    start_pixel += (image_width*pixel_width)

# Display the image
sense = SenseHat()
sense.set_rotation(r=180)
sense.set_pixels(sense_pixels)
time.sleep (30)

sense.clear()
