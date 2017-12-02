from turtle import *
from random import randint

speed(50)
penup()
goto(-140, 140)

for step in range(14):
 write(step, align = 'center')
 right(90)
 forward(10)
 pendown()
 forward(200)
 penup()
 backward(210)
 left(90)
 forward(20)
 
 
Bob = Turtle()
Bob.color('red')
Bob.shape('turtle')

Bob.penup()
Bob.goto(-160, 100)
Bob.pendown()

lucy = Turtle()
lucy.color('blue')
lucy.shape('turtle')

lucy.penup()
lucy.goto(-160, 70)
lucy.pendown()

Coco = Turtle()
Coco.color('Brown')
Coco.shape('turtle')

Coco.penup()
Coco.goto(-160, 40)
Coco.pendown()


fred = Turtle()
fred.color('yellow')
fred.shape('turtle')

fred.penup()
fred.goto(-160, 10)
fred.pendown()

Fanta = Turtle()
Fanta.color('Orange')
Fanta.shape('turtle')

Fanta.penup()
Fanta.goto(-160, -20)
Fanta.pendown()

for turn in range(100):
 Bob.forward(randint(1,5))
 lucy.forward(randint(1,5))
 Coco.forward(randint(1,5))
 fred.forward(randint(1,5))
 Fanta.forward(randint(1,5))
