from turtle import Turtle

t=Turtle()
t.hideturtle()
#t.screen.bgpic("turtle.gif")
t.screen.bgcolor('black')
t.color('red')
t.setheading(17)
t.shape("turtle")
t.shapesize(3)


def square(length):
    for steps in range(4):
        t.fd(length)
        t.left(90)

#from turtle import turtle#t=Turtle

#t.pensize(50)
square(100)
square(200)
t.goto(5,23)
square(200)

t.screen.exitonclick()

#t.fd(distance)

#





