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

reuben = Turtle()
reuben.color('turquoise')
reuben.shape('turtle')

reuben.penup()
reuben.goto(-220, 10)
reuben.pendown()
reuben.write("Reuben")
reuben.right(360)

sam = Turtle()
sam.color('gold')
sam.shape('turtle')

sam.penup()
sam.goto(-220,-20 )
sam.pendown()
sam.write("Sam")
sam.right(360)

for turn in range(80):
    ada.forward(randint(1,8))
    bob.forward(randint(1,8))
    jeff.forward(randint(1,8))
    reuben.forward(randint(1,8))
    sam.forward(randint(1,8))
    adaPosition = ada.position()[0]
    bobPosition = bob.position()[0]
    jeffPosition = jeff.position()[0]
    reubenPosition = reuben.position()[0]
    samPosition = sam.position()[0]
    if (adaPosition > 210 or bobPosition > 210 or jeffPosition > 210 or reubenPosition > 210 or samPosition > 210):
        break 

print("Ada", adaPosition)
print("Bob", bobPosition)
print("Jeff", jeffPosition)
print("Reuben", reubenPosition)
print("Sam", samPosition)

if (adaPosition > bobPosition and adaPosition > jeffPosition and adaPosition > reubenPosition and adaPosition > samPosition):
    ada.write("  I WIN!!!")
    ada.penup()
    ada.forward(55)
    for i in range(10):
        ada.right(360)
        ada.left(360)
if (bobPosition > adaPosition and bobPosition > jeffPosition and bobPosition > reubenPosition  and bobPosition > samPosition):
    bob.write("  I WIN!!!")
    bob.penup()
    bob.forward(55)
    for i in range(10):
        bob.right(360)
        bob.left(360)
if (jeffPosition > bobPosition and jeffPosition > adaPosition and jeffPosition > reubenPosition  and jeffPosition > samPosition):
    jeff.write("  I WIN!!!")
    jeff.penup()
    jeff.forward(55)
    for i in range(10):
        jeff.right(360)
        jeff.left(360)
if (reubenPosition > bobPosition and reubenPosition > jeffPosition and reubenPosition > adaPosition  and reubenPosition > samPosition):
    reuben.write("  I WIN!!!")
    reuben.penup()
    reuben.forward(55)
    for i in range(10):
        reuben.right(360)
        reuben.left(360)
if (samPosition > bobPosition and samPosition > jeffPosition and samPosition > adaPosition  and samPosition > reubenPosition):
    sam.write("  I WIN!!!")
    sam.penup()
    sam.forward(55)
    for i in range(10):
        sam.right(360)
        sam.left(360)

input()    
