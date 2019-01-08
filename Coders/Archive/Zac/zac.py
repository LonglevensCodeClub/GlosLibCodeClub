from turtle import *

def moveToRandomLocation():
	penup()
	setpost( randit(-400,400) , randit(-400,400) )
	pendown()

def drawstar(starSize, starColour):
	color(starColour)
	pendown()
	begin_fill()
	for side in range(5):
		left(144)
		forward(starSize)
	end_fill()
	penup()
	
bgcolor("cyan")
drawstar(500, "white")
forward(100)
drawstar(200, "pink")
left(120)
forward(150)
drawstar(1, "white")
forward(100)
drawstar(30, "black")
backward(100)
drawstar(10, "white")
drawstar(500, "purple")
forward(100)
drawstar(200, "white")
left(120)
forward(150)
drawstar(1, "white")
forward(100)
drawstar(30, "green")
right(100)
drawstar(10, "white")
drawstar(500, "white")
forward(100)
drawstar(200, "white")
left(120)
backward(150)
drawstar(1, "white")
backward(500)
drawstar(30, "white")
right(100)
drawstar(10, "white")

for star in range(30):
	moveToRandomLocation()
	drawStar( randist(5,25) , "white")


hideturtle()
done()

print("hello zac")
