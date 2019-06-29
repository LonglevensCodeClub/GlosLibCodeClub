from turtle import *
from random import randint
speed(5)
penup()
goto(-140,140)

for step in range(15):
    write(step, align= 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
        
    
#write(0)
#forward(100)
#write(5)
#write(0)
#forward(20)
#write(1)
#forward(20)
#write(2)
#forward(20)
#write(3)
#forward(20)
#write(4)
#forward(20)
#write(5)
#forward(20)
screen=Screen()
screen.addshape('animals/bear.gif')
ada = Turtle()
ada.color('red')
ada.shape('animals/bear.gif')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

screen.addshape('animals/cat.gif')
bob = Turtle()
bob.color('blue')
bob.shape('animals/cat.gif')
 
bob.penup()
bob.goto(-160,70)
bob.pendown()

screen.addshape('animals/bull.gif')
Tim = Turtle()
Tim.color('green')
Tim.shape('animals/bull.gif')
 
Tim.penup()
Tim.goto(-160,40)
Tim.pendown()

screen.addshape('animals/chicken.gif')
Jim= Turtle()
Jim.color('yellow')
Jim.shape('animals/chicken.gif')
 
Jim.penup()
Jim.goto(-160,10)
Jim.pendown()



for turn in range(100):
 ada.forward(randint(1,5))
 bob.forward(randint(1,5))
 Tim.forward(randint(1,5))
 Jim.forward(randint(1,5))
 
leader="ada"
[leaderposition,y]=ada.position()
[turtleposition,y]=bob.position()
if turtleposition >leaderposition:
    leaderposition=turtleposition
    leader="bob"
[turtleposition,y]=Tim.position()
if turtleposition >leaderposition:
    leaderposition=turtleposition
    leader="Tim"
[turtleposition,y]=Jim.position()
if turtleposition >leaderposition:
    leaderposition=turtleposition
    leader="Jim"
print("Winner is",leader)
