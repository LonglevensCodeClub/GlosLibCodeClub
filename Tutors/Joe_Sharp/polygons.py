from turtle import *
import math

shape("turtle")
colormode(255)
speed(0)

def drawPolygon(startX, startY, numberSides, radius):
	lengthSide = (2 * math.pi * radius) / numberSides
	eachAngle = 360 / numberSides
	print("Drawing Polygon at x: {}, y: {}, sides: {}, radius: {}, length: {}".format( \
		startX, startY, numberSides, radius, lengthSide))
	t = Turtle()
	t.setpos(startX, startY)
	for x in range(numberSides):
		t.forward(lengthSide)
		t.right(eachAngle)
	
	
drawPolygon(startX = 0, startY = 0, numberSides = 5, radius = 50)

done()
