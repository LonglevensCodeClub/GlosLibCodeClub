
from turtle import *
speed(10)
penup()
goto(-140, 140)
for step in range(6):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward (150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada=Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()
