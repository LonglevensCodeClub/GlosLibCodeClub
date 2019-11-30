from turtle import Turtle
t=Turtle()
t.screen.bgcolor("gold")
t.hideturtle()
t.color("red")

def slanted_rectangle(length,width,angle):
    t.setheading(angle)
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)
 
for angle in range(360): 
 slanted_rectangle(length=200,angle=angle,width=210)
