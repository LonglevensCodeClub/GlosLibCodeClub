from turtle import Turtle
t=Turtle()
t.screen.bgcolor("blue")




def drawcircle(angle,radius):
   for steps in range(15):
    t.circle(radius,180)
    t.left(angle)


t.color("red")

drawcircle(angle=78,radius=20)
