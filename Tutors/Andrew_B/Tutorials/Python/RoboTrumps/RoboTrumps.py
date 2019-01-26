#!/bin/python3

from random import choice
from turtle import *

screen = Screen()
screen.bgcolor('white')
screen.exitonclick()
penup()
hideturtle()

file = open('data/cards.txt', 'r')
robots = {}

for line in file.read().splitlines():
    name, battery, intelligence, image = line.split(', ')
    robots[name] = [battery, intelligence, image]
    screen.register_shape('data/' + image)
file.close()

robot = ""

while robot != 'quit':
    robot = input('Choose a robot: ')
    if (robot == "random"):
        robot = choice(list(robots))
        print('Robot chosen for you:', robot)
    if robot in robots:
        stats = robots[robot]
        style = ('Arial', 14, 'bold')
        screen.clear()
        penup()
        goto(0, 100)
        shape('data/' + stats[2])
        setheading(90)
        stamp()
        hideturtle()
        setheading(-90)
        forward(70)
        write('Name: ' + robot, font=style, align='center')
        forward(25)
        write('Battery: ' + stats[0], font=style, align='center')
        forward(25)
        write('Intelligence: ' + stats[1], font=style, align='center')
    else:
        if (robot != "quit"):
            print('Robot doesn\'t exist!')
        else:
            screen.bye()
            print('Bye!')



