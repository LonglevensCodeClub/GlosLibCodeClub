#!/usr/bin/python3
from stickers import *
import turtle
import random

def draw():
    c = turtle.Turtle()
    c.shape("square")
    c.penup
    c.speed(100)

    x = randint (-400, 400)
    y = randint (-400, 400)
    c.setposition(x,y)
    return c

stickersdraw = dict()

def observer(which_stick, count):
    print ("observed sticker {} is at {}".format(which_stick, count))

    if which_stick in stickersdraw:
         = stickersdraw[which_stick]
    else:
        

y = input("enter book size: ")
x = colstick(int(y), observer)
print ("{} stickers needed to fill a collection of {} ".format(x, y))
z = x - int(y)
print ("with " + str(z) + " swaps")

