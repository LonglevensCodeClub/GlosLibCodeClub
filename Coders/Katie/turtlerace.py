from turtle import *
from random import randint

speed(50)
penup()
goto(-140, 140)

for step in range(18):
 write(step, align = 'center')
 right(90)
 forward(10)
 pendown()
 forward(300)
 penup()
 backward(310)
 left(90)
 forward(20)
 
 
Bob = Turtle()
Bob.color('red')
Bob.shape('turtle')

Bob.penup()
Bob.goto(-160, 100)
Bob.write('Bob')
Bob.right(360)
Bob.pendown()

lucy = Turtle()
lucy.color('blue')
lucy.shape('turtle')

lucy.penup()
lucy.goto(-160, 70)
lucy.write('lucy')
lucy.left(360)
lucy.pendown()

Coco = Turtle()
Coco.color('Brown')
Coco.shape('turtle')

Coco.penup()
Coco.goto(-160, 40)
Coco.write('Coco')
Coco.right(360)
Coco.pendown()


fred = Turtle()
fred.color('goldenrod')
fred.shape('turtle')

fred.penup()
fred.goto(-160, 10)
fred.write('fred')
fred.left(360)
fred.pendown()

Fanta = Turtle()
Fanta.color('Orange')
Fanta.shape('turtle')

Fanta.penup()
Fanta.goto(-160, -20)
Fanta.write('Fanta')
Fanta.right(360)
Fanta.pendown()


Grape = Turtle()
Grape.color('purple')
Grape.shape('turtle')

Grape.penup()
Grape.goto(-160, -50)
Grape.write('Grape')
Grape.left(360)
Grape.pendown()

KitKat = Turtle()
KitKat.color('Tan')
KitKat.shape('turtle')

KitKat.penup()
KitKat.goto(-160, -80)
KitKat.write('KitKat')
KitKat.right(360)
KitKat.pendown()

bubblegum = Turtle()
bubblegum.color('magenta')
bubblegum.shape('turtle')

bubblegum.penup()
bubblegum.goto(-160, -110)
bubblegum.write('bubblegum')
bubblegum.left(360)
bubblegum.pendown()

LimeGreen = Turtle()
LimeGreen.color('Lime')
LimeGreen.shape('turtle')

LimeGreen.penup()
LimeGreen.goto(-160, -140)
LimeGreen.write('LimeGreen')
LimeGreen.right(720)
LimeGreen.pendown()

for turn in range(100):
 Bob.forward(randint(3,8))
 lucy.forward(randint(3,8))
 Coco.forward(randint(3,8))
 fred.forward(randint(3,8))
 Fanta.forward(randint(3,8))
 Grape.forward(randint(3,8))
 KitKat.forward(randint(3,8))
 bubblegum.forward(randint(3,8))
 LimeGreen.forward(randint(3,8))
 BobPosition = Bob.position()[0]
 lucyPosition = lucy.position()[0]
 CocoPosition = Coco.position()[0]
 fredPosition = fred.position()[0]
 FantaPosition = Fanta.position()[0]
 GrapePosition = Grape.position()[0]
 KitKatPosition = KitKat.position()[0]
 bubblegumPosition = bubblegum.position()[0]
 LimeGreenPosition = LimeGreen.position()[0]
 if (BobPosition > 210 or lucyPosition > 210 or CocoPosition > 210 or fredPosition > 210 or FantaPosition > 210 or GrapePosition > 210 or KitKatPosition > 210 or bubblegumPosition > 210 or LimeGreenPosition > 210):
        break 

 
 
