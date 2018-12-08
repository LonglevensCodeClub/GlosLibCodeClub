
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

ann=Turtle()
ann.color('turquoise')
ann.shape('turtle')

ann.penup()
ann.goto(-160, 10)
ann.pendown()

kay=Turtle()
kay.color('pink')
kay.shape('turtle')

kay.penup()
kay.goto(-160, -20)
kay.pendown()

aisha=Turtle()
aisha.color('purple')
aisha.shape('turtle')

aisha.penup()
aisha.goto(-160, 40)
aisha.pendown()

bob=Turtle()
bob.color('blue')

bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()







for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    aisha.forward(randint(1,5))
    ann.forward(randint(1,5))
    kay.forward(randint(1,5))
w=0
winner = "bonus"
[x,y] = ada.position()
if x>w:
    w = x
    winner="ada"
[x,y] = bob.position()
if x>w:
    w = x
    winner="bob"
[x,y] = aisha.position()
if x>w:
    w = x
    winner="aisha"
[x,y] = kay.position()
if x>w:
    w = x
    winner="kay"
[x,y] = ann.position()
if x>w:
    w = x
    winner="ann"

print("the winner is",winner)
