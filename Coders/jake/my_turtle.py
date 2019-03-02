from turtle import *
from random import randint
speed(10)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob= Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 80)
bob.pendown()

ella = Turtle()
ella.color('green')
ella.shape('turtle')

ella.penup()
ella.goto(-160, 60)
ella.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5)) 
  ella.forward(randint(1,5))

