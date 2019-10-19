from turtle import *

screen = Screen()
screen.setup(800, 800)

colours = {
    'sweetcornyellow': '#CCCC00',
    'MASTERSWORDBLUE': '#0010EE',
    'RASSBERRY': '#A90000',
    'LIME': '#00FF00',
    'GANONDORFHAIRRED': '#FA0000'
  }

print(colours['sweetcornyellow'])
screen.bgcolor(colours['LIME'])

color(colours['LIME'])
style = ('Courier', 40, 'bold')
write('HELLO', font=style, align='center')
hideturtle()


            
