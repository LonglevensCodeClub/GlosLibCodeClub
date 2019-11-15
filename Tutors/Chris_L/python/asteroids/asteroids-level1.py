from turtle import *
import random
import math

screen = Screen()


screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
screen.bgcolor("black")

penup()
ht()
speed(0)
goto(0, screenMaxY - 20)
color('red')
write("Asteroids!!", align="center", font=("Arial",20))
goto(0, screenMaxY - 33)
write("Use the arrow keys to move and 'space bar' to fire", align="center")
goto(0, 0)
color("lightblue")


screen.exitonclick()