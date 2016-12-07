from turtle import *
from threading import Thread

colormode(255)

class Shape:
	def __init__(self, color=(0, 0, 0), position=(0, 0)):
		self.turtle = Turtle()
		self.turtle.penup()
		self.turtle.goto(position)
		self.turtle.pendown()
		self.turtle.color(color)
	
class Polygon(Shape):
	def __init__(self, color=(0, 0, 0), position=(0, 0), sides=4, size = 100):
		super(Polygon, self).__init__(color=color, position=position)
		self.sides = sides
		self.size = size
	
	def draw(self):
		for i in range(self.sides):
			self.turtle.forward(self.size)
			self.turtle.right(360 / self.sides)
				
class Rectangle(Shape):
	def __init__(self, color=(0, 0, 0), position=(0, 0), height = 100, width=50):
		super(Rectangle, self).__init__(color=color, position=position)
		self.height = height
		self.width = width
	
	def draw(self):
		self.turtle.forward(self.width)
		self.turtle.right(90)	
		self.turtle.forward(self.height)
		self.turtle.right(90)	
		self.turtle.forward(self.width)
		self.turtle.right(90)	
		self.turtle.forward(self.height)
		self.turtle.right(90)	
			
shapes = []
shapes.append(Polygon(position=(-250, 50)))
shapes.append(Polygon(sides=8, size=50))
shapes.append(Polygon(sides=7, size=20))
shapes.append(Polygon(sides=5, position=(250, 50), color=(255, 0, 0), size=50))
shapes.append(Rectangle(position=(50, 50), color=(0, 255, 0)))

for s in shapes:
	s.draw()

