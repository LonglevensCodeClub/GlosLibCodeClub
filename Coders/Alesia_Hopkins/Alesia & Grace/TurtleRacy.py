from turtle import *
from random import randint

speed(10)
penup()
goto(-200, 140)

for step in range(20):
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
ada.goto(-220, 100)
ada.pendown()
ada.write("Ada")
ada.right(360)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-220, 70)
bob.pendown()
bob.write("Bob")
bob.right(360)

jeff = Turtle()
jeff.color('magenta')
jeff.shape('turtle')

jeff.penup()
jeff.goto(-220, 40)
jeff.pendown()
jeff.write("Jeff")
jeff.right(360)

greg = Turtle()
greg.color('turquoise')
greg.shape('turtle')

greg.penup()
greg.goto(-220, 10)
greg.pendown()
greg.write("Greg")
greg.right(360)

for turn in range(80):
    ada.forward(randint(1,8))
    bob.forward(randint(1,8))
    jeff.forward(randint(1,8))
    greg.forward(randint(1,8))
    adaPosition = ada.position()[0]
    bobPosition = bob.position()[0]
    jeffPosition = jeff.position()[0]
    gregPosition = greg.position()[0]
    if (adaPosition > 210 or bobPosition > 210 or jeffPosition > 210 or gregPosition > 210):
        break 

print("Ada", adaPosition)
print("Bob", bobPosition)
print("Jeff", jeffPosition)
print("Greg", gregPosition)

if (adaPosition > bobPosition and adaPosition > jeffPosition and adaPosition > gregPosition):
    ada.write("  I WIN!!!")
    ada.penup()
    ada.forward(55)
    for i in range(10):
        ada.right(360)
        ada.left(360)
if (bobPosition > adaPosition and bobPosition > jeffPosition and bobPosition > gregPosition):
    bob.write("  I WIN!!!")
    bob.penup()
    bob.forward(55)
    for i in range(10):
        bob.right(360)
        bob.left(360)
if (jeffPosition > bobPosition and jeffPosition > adaPosition and jeffPosition > gregPosition):
    jeff.write("  I WIN!!!")
    jeff.penup()
    jeff.forward(55)
    for i in range(10):
        jeff.right(360)
        jeff.left(360)
if (gregPosition > bobPosition and gregPosition > jeffPosition and gregPosition > adaPosition):
    greg.write("  I WIN!!!")
    greg.penup()
    greg.forward(55)
    for i in range(10):
        greg.right(360)
        greg.left(360)
input()    
