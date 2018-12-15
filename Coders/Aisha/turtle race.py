
from turtle import *
from random import randint

def createTurtle(colour, track, name):
    turtle=Turtle()
    turtle.color(colour)
    turtle.shape('turtle')

    turtle.penup()
    turtle.goto(-160, 100-30*track)
    turtle.write(name)
    turtle.pendown()
    return turtle
    

speed(10)
penup()
goto(-140, 140)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward (250)
    penup()
    backward(260)
    left(90)
    forward(20)

names=['ada','ann' ,'kay' ,'aisha' ,'bob','kev' , 'elliot' , 'may']
colours=['red','turquoise', 'pink', 'purple', 'blue', 'green', 'orange', 'black']
turtles=[]
for i in range (len(names)):
    turtle=createTurtle(colours[i], i, names[i])
    turtles.append(turtle)

#turtles=[ada,ann ,kay ,aisha ,bob,kev , elliot , may]
w=0
winner = 0
leader = createTurtle('red', 9, 'leader')

for turn in range(100):
    i = 0
    for turtle in turtles :
        i = i + 1
        turtle.forward(randint(1,5))
        [x,y] = turtle.position()
        if x>w:
            w = x
            winner=i
    leader.write(names[winner])
    


print("the winner is", names[winner])
