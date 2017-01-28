import turtle
import random

class Dice():
	def __init__(self):
		self.turtles = set()
		self.diceFunctions = dict()

		self.diceFunctions[1] = self.rollOne
		self.diceFunctions[2] = self.rollTwo
		self.diceFunctions[3] = self.rollThree
		self.diceFunctions[4] = self.rollFour
		self.diceFunctions[5] = self.rollFive
		self.diceFunctions[6] = self.rollSix

	def fillIn(self, x, y):
		self.spots[x][y] = True

	def draw(self, scale):
		for x in range(len(self.spots)):
			for y in range(len(self.spots[x])):
				if self.spots[x][y]:
					t = turtle.Turtle()
					t.shape("turtle")
					t.penup()
					t.goto(x=x*scale, y=y*scale)
					t.stamp()
					self.turtles.add(t)

	def roll(self):
		self.spots = [[False for x in range(3)] for y in range(3)]
		for t in self.turtles:
			t.clear()
			t.hideturtle()
			del t
		self.turtles.clear()
		w = random.randint(1, 6)
		self.diceFunctions[w]()

	def rollOne(self):
		self.fillIn(1, 1)
		
	def rollTwo(self):
		self.fillIn(0, 0)
		self.fillIn(2, 2)
		
	def rollThree(self):
		self.fillIn(0, 0)
		self.fillIn(1, 1)
		self.fillIn(2, 2)
		
	def rollFour(self):
		self.fillIn(0, 0)
		self.fillIn(0, 2)
		self.fillIn(2, 2)
		self.fillIn(2, 0)
		
	def rollFive(self):
		self.fillIn(0, 0)
		self.fillIn(0, 2)
		self.fillIn(1, 1)
		self.fillIn(2, 2)
		self.fillIn(2, 0)
		
	def rollSix(self):
		self.fillIn(0, 0)
		self.fillIn(0, 1)
		self.fillIn(0, 2)
		self.fillIn(2, 0)
		self.fillIn(2, 1)
		self.fillIn(2, 2)
	


w = turtle.Screen()

myDice = Dice()

def rollDice():
	myDice.roll()
	myDice.draw(scale=40)
	
w.onkey(rollDice, "space")

### KEEP THIS AT END OF CODE
# Start listening for key events
w.listen()

# Enter a game loop
while True:
	w.getcanvas().update_idletasks()
	w.getcanvas().update()
