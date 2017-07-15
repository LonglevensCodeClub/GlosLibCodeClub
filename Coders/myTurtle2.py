from turtle import *


def drawStar():
	pendown()
	begin_fill()
	for side in range(5):
		left(144)
		forward(50)
	end_fill()
	penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawStar()
forward(100)
drawStar()
left(120)
forward(150)
drawStar()

hideturtle()
done()
