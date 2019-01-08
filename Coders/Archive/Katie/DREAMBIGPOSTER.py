#!/bin/python3
from turtle import *

screen = Screen()
screen.setup(400, 400)
colours = { 
  'lavendar': '#C4BBF0',
  'purple': '#8631F6' ,
  'yelow': '#F8FC02'
}
print(colours['lavendar'])
print(colours['purple'])
print(colours['yelow'])

screen.bgcolor(colours['lavendar'])

color(colours['purple'])
dot(400)

color(colours['yelow'])
style = ('Times', 30, 'bold')
write('DREAM BIG!', font=style, align='center')
hideturtle()
