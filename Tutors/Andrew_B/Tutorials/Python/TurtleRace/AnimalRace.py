#!/bin/python3

from turtle import *
from random import randint

#Turtle images, names and colours
turtleFiles = ['cat.gif', 'bear.gif', 'bull.gif', 'chicken.gif', 'fish.gif']
turtleNames = ['Tiddles', 'Barnie', 'Bully', 'Chucky', 'Goldie']
turtleColours = ['orange', 'brown', 'red', 'green', 'black']

# Create the course grid
speed(40)
penup()
gridWidth = 20 + len(turtleNames) * 40
goto(-130, gridWidth / 2)
dashes = gridWidth / 10
for step in range(16):
    write(step, align='center')
    right(90)
    for dash in range(int(dashes / 2)):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(gridWidth)
    left(90)
    forward(20)

#Finishing Line
backward(20)
pensize(2)
right(90)
forward(10)
pendown()
forward(gridWidth- 10)
hideturtle()

# Create a Turtle giving it a name, colour and track position
def createTurtle(name, colour, position, file):
    turtle = Turtle()
    turtle.color(colour)
    turtle.shape('animals/' + file)
    turtle.turtlesize(stretch_wid=3, stretch_len=5)
    turtle.resizemode('user')
    turtle.penup()
    trackPosition = gridWidth / 2 - 40 * position
    turtle.goto(-210, trackPosition)
    turtle.write(name)
    turtle.pendown()
    turtle.goto(-155, trackPosition)
    return turtle

#Create the collection of racing turtles.
screen = Screen()
turtles = []
i = 0
for file in turtleFiles:
    print(file)
    screen.addshape('animals/' + file)
    turtle = createTurtle(turtleNames[i], turtleColours[i], i + 1, file)
    print('Created turtle for', turtleNames[i], 'at position', i)
    turtles.append(turtle)
    i += 1

# Date for monitoring which turtle is in the lead
leaderPos = -160
leaderName = ""
leaderTurtle = createTurtle('Leader', 'black', len(turtles) + 2, turtleFiles[0])
leaderTurtle.forward(30)
leaderTurtle.penup()
leaderTurtle.forward(30)

# Run the race
leaderPos = 0
while leaderPos < 170:
    for i in range(len(turtles)):
        turtles[i].forward(randint(1, 5))
        [x, y] = turtles[i].position()
        if x > leaderPos:
            leaderPos = x
            if (leaderName != turtleNames[i]):
                leaderName = turtleNames[i]
                print("Current Leader =", leaderName)
                leaderTurtle.color(turtleColours[i])
                leaderTurtle.shape('animals/' + turtleFiles[i])

#Find the placings and find the winner(s)
winningTurtles = []
for i in range(len(turtles)):
    [x, y] = turtles[i].position()
    
    place = len(turtles) + 1
    for j in range(len(turtles)):
        [a, b] = turtles[j].position()
        if x >= a:
            place -= 1

    print(turtleNames[i], "finished at", x, "in position", place)
    turtles[i].penup()
    turtles[i].forward(30)
    turtles[i].write(place, align='center')
    turtles[i].backward(30)
    if place == 1:
        winningTurtles.append(turtles[i])
    turtle.speed(1)

#Announce Winner
leaderTurtle.forward(30)
winners = len(winningTurtles)
if (winners > 1):
    leaderTurtle.write("The winners are:")
    leaderTurtle.forward(90)
else:
    leaderTurtle.write("The winner is:")
    leaderTurtle.forward(70)
for turtle in winningTurtles:
    i = 0
    for turt in turtles:
        if (turt == turtle):
            leaderTurtle.color(turtleColours[i])
            leaderTurtle.write(turtleNames[i])
            leaderTurtle.right(90)
            leaderTurtle.forward(30)
            leaderTurtle.left(90)
            winners -= 1
        i += 1

if len(winningTurtles) > 1:
    leaderTurtle.hideturtle()

#Victory loops
for turtle in winningTurtles:
    turtle.circle(-50)
for turtle in winningTurtles:
    turtle.circle(50)
