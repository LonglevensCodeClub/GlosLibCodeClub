from turtle import *
from random import randint

penup()
goto(-140, 140)

for step in range(15):
    speed(100)
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada1 = Turtle()
ada1.color('red')
ada1.shape('turtle')

ada1.penup()
ada1.goto(-160, 100)
ada1.pendown()

ada2 = Turtle()
ada2.color('blue')
ada2.shape('turtle')

ada2.penup()
ada2.goto(-160, 70)
ada2.pendown()

ada3 = Turtle()
ada3.color('green')
ada3.shape('turtle')

ada3.penup()
ada3.goto(-160, 40)
ada3.pendown()

ada4 = Turtle()
ada4.color('yellow')
ada4.shape('turtle')

ada4.penup()
ada4.goto(-160, 10)
ada4.pendown()

for turn in range(100):
    ada1.forward(randint(1,5))
    ada2.forward(randint(1,5))
    ada3.forward(randint(1,5))
    ada4.forward(randint(1,5))

for step in range(36):
    ada1.forward(10)
    ada1.right(10)
    ada2.forward(10)
    ada2.right(10)
    ada3.forward(10)
    ada3.right(10)
    ada4.forward(10)
    ada4.right(10)
