from turtle import *
from random import randint

names   = ['Ada','Ann',       'Kay',  'Aisha',  'Bob',  'Kev',   'Elliot', 'May',   'Andrew']
colours = ['red','turquoise', 'pink', 'purple', 'blue', 'green', 'orange', 'black', 'yellow']


# Show grid
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

# Function to create a Turtle
def createTurtle(colour, track, name):
    turtle=Turtle()
    turtle.color(colour)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-220, 100-30*track)
    turtle.write(name)
    turtle.goto(-160, 100-30*track)
    turtle.pendown()
    return turtle

# Create the collection of Turtles
turtles=[]
for i in range (len(names)):
    turtle=createTurtle(colours[i], i, names[i])
    turtles.append(turtle)

#Create and set up leader turtle
leaderXpos = -1000
winningTurtle = -1
leader = createTurtle('red', len(turtles) + 1, 'leader')
leader.hideturtle()
leader.width(5)

#Run the race
for turn in range(100):
    i = 0
    change = False
    for turtle in turtles :
        turtle.forward(randint(1, 5))
        [x, y] = turtle.position()
        if x > leaderXpos:
            leaderXpos = x
            if (winningTurtle != i):
                change = True
                winningTurtle = i
        i = i + 1
    leader.goto(leaderXpos, 100 - 30 * (len(turtles) + 1))
    if (change):
        leader.color(colours[winningTurtle])
        #leader.write(names[winningTurtle])

#Report the winner
leader.penup()
leader.forward(30)
leader.write("Winner = " + names[winningTurtle])
leader.right(90)
leader.forward(20)
leader.left(90)
leader.forward(30)
leader.showturtle()
