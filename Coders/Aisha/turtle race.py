from turtle import *
from random import randint
import time

#Lists of names and colours of the racing turtles
names   = ['Ada','Ann',       'Kay',  'Aisha', 'Bob',  'Kev',   'Elliot', 'May',   'Andrew']
colours = ['red','turquoise', 'pink', 'purple', 'blue', 'green', 'orange', 'black', 'yellow']

# Show racing grid
speed(10)
penup()
goto(-140, 140)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(len(names) * 30 + 15)
    penup()
    backward(len(names) * 30 + 25)
    left(90)
    forward(20)

# Function to create Turtles
def createTurtle(colour, trackPosition, name):
    turtle=Turtle()
    turtle.color(colour)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-220, 100-30*trackPosition)
    turtle.write(name)
    turtle.goto(-160, 100-30*trackPosition)
    turtle.pendown()
    return turtle

# Create the collection of Turtles
turtles=[]
for i in range (len(names)):
    turtle=createTurtle(colours[i], i, names[i])
    turtles.append(turtle)

#Create and set up leader turtle
leader = createTurtle('red', len(turtles) + 1, 'leader')
leader.width(5)
[x, y] = leader.position()
leaderXpos = x
winningTurtle = 0

#Run the race
for turn in range(100):
    i = 0

    for turtle in turtles :
        turtle.forward(randint(1, 5))
#        if (i == 3):
#            turtle.form
        [x, y] = turtle.position()
        if x > leaderXpos:
            leaderXpos = x
            if (winningTurtle != i):
                winningTurtle = i
        i = i + 1
    leader.goto(leaderXpos, 100 - 30 * (len(turtles) + 1))
    leader.color(colours[winningTurtle])

#Report the winner
leader.penup()
leader.forward(30)
leader.write("Winner = " + names[winningTurtle])
leader.right(90)
leader.forward(20)
leader.left(90)
leader.forward(30)

#Winner victory loops
turtles[winningTurtle].penup()
for p in range(80):
    turtles[winningTurtle].left(90)
    turtles[winningTurtle].right(90)
    time.sleep(0.1)
    turtles[winningTurtle].forward(20)
    turtles[winningTurtle].backward(20)
