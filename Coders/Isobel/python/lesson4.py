from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
t.color("magenta")
t.shape("turtle")
t.shapesize(3)
t.setheading(90)

#rotate
t.left(90)
t.right(270)
t.left(90)
t.left(90)
t.left(90)

#move
t.pensize(3)
t.hideturtle()
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)



def slanted_rectangle(length,width,angle):
    t.setheading(angle)
    for steps in range (2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)

slanted_rectangle(length=200,angle=45,width=100)












def triangle(length,angle=120):
    for steps in range(3):
        t.fd(length)
        t.left(angle)
        
        
triangle(200)

t.circle(100,360)









t.screen.exitonclick()






