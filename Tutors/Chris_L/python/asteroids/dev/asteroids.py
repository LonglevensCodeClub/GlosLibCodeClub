from turtle import *
t=Turtle()
screen = Screen()

screenMinX = -screen.window_width() / 2
screenMinY = -screen.window_height() / 2
screenMaxX = screen.window_width() / 2
screenMaxY = screen.window_height() / 2
screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)

screen.bgcolor("black")
t.color('red')

def doLeft():
    t.left(10)

def doRight():
    t.right(10)

screen.onkey(doLeft, 'Left')
screen.onkey(doRight, 'Right')

screen.listen()


screen.exitonclick()
