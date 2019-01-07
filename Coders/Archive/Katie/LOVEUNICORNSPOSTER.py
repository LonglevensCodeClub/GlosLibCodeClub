#!/bin/python3
from turtle import *

screen = Screen()
screen.setup(400, 400)
colours = { 
  'lavendar': '#C4BBF0',
  'purple': '#8631F6' ,
  'yelow': '#F8FC02',
  'darkpink' : '#9D4D71',
  'black': '#000000',
  
  'pink': '#FCD8F1',
  'pastelpurple': '#E3D8FC',
  'green': '#DFFCD8'
}
print(colours['lavendar'])
print(colours['purple'])
print(colours['yelow'])

screen.bgcolor(colours['pink'])

color(colours['green'])
dot(400)

color(colours['pastelpurple'])
style = ('Times', 30, 'bold')
write('LOVE UNICORNS!', font=style, align='center')
hideturtle()
