from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
t.hideturtle()
t.color("red")

def slanted_rectangle(length,width,angle):
    t.setheading(angle)
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)
 
for angle in range(5): 
 slanted_rectangle(length=212,angle=angle,width=234)
