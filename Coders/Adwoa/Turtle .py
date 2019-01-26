from turtle import*
from random import randint
speed(10)
penup()
goto(-140, 140)

for step in range(15):
    write(step,align='center')
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
for turn in range(100):
    ada.forward(randint(1,5))

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()
for turn in range(100):
    bob.forward(randint(1,5))
   
ell = Turtle()
ell.color('orange')
ell.shape('turtle')
ell.penup()
ell.goto(-160,40)
ell.pendown()
for turn in range(100):
    ell.forward(randint(1,5))

    
   
pop = Turtle()
pop.color('purple')
pop.shape('turtle')
pop.penup()
pop.goto(-160,10)
pop.pendown()
for turn in range(100):
    pop.forward(randint(1,5))



