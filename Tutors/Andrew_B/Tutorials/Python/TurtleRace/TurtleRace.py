#!/bin/python3

from turtle import *
from random import randint

# Create a Turtle giving it a name, colour and track position
def createTurtle(name, colour, position):
    turtle = Turtle()
    turtle.color(colour)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-160, 100 - 20 * position)
    turtle.write(name)
    turtle.pendown()
    return turtle

# Create the course grid
speed(10)
penup()
goto (-140, 140)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    for dashes in range(15):
        pendown()
        forward(5)
        penup()
        forward(5)
    backward(160)
    left(90)
    forward(20)

# Racing turtle names and colours
turtleNames = ['Ada', 'Bob', 'Kev', 'Kay', 'Ann']
turtleColours = ['red', 'blue', 'green', 'pink', 'turquoise']
numberOfTurtles = len(turtleNames)

#Create the collection of racing turtles.
turtles = []
for i in range(numberOfTurtles):
    turtle = createTurtle(turtleNames[i], turtleColours[i], i)
    print('Created turtle for ', turtleNames[i], 'at position', i)
    turtles.append(turtle)

# Date for monitoring which turtle is in the lead
leaderPos = -160
leaderName = ""
leaderTurtle = createTurtle('Leader', 'black', numberOfTurtles + 1)
leaderTurtle.forward(50)

# Run the race
for turn in range(100):
    for i in range(numberOfTurtles):
        turtles[i].forward(randint(1, 5))
        [x, y] = turtles[i].position()
        if x > leaderPos:
            leaderPos = x
            if (leaderName != turtleNames[i]):
                leaderName = turtleNames[i]
                print("Current Leader = ", leaderName)
                leaderTurtle.color(turtleColours[i])

winningTurtles = []
#Find the placings and find the winner(s)
for i in range(numberOfTurtles):
    [x, y] = turtles[i].position()
    
    place = numberOfTurtles + 1
    for j in range(numberOfTurtles):
        [a, b] = turtles[j].position()
        if x >= a:
            place -= 1

    print(turtleNames[i], " finished at ", x, ' in position', place)
    turtles[i].penup()
    turtles[i].forward(30)
    turtles[i].write(place, align='center')
    turtles[i].backward(30)
    if place == 1:
        winningTurtles.append(turtles[i])

#Victory Dance by the leading turtle(s)
step = 3
for angle in range(0, 720, step):
    for turtle in winningTurtles:
        turtle.right(step)
        turtle.forward(2)

        

    

