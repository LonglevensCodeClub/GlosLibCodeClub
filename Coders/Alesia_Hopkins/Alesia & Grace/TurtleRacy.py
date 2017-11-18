from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)

for step in range(14):
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
ada.color('tomato')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()
ada.write("Ada")
ada.right(360)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()
bob.write("Bob")
bob.right(360)

jeff = Turtle()
jeff.color('magenta')
jeff.shape('turtle')

jeff.penup()
jeff.goto(-160, 40)
jeff.pendown()
jeff.write("Jeff")
jeff.right(360)

greg = Turtle()
greg.color('turquoise')
greg.shape('turtle')

greg.penup()
greg.goto(-160, 10)
greg.pendown()
greg.write("Greg")
greg.right(360)

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    jeff.forward(randint(1,5))
    greg.forward(randint(1,5))
