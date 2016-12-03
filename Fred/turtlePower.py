import turtle
import random

# get hold of screen
w = turtle.Screen()

# create a turtle
player = turtle.Turtle()
player.shape("turtle")

# create a list of turtles to chase
computercolours=["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
computers = []


def updateGame():
	for c in computers:
		c.left(random.randint(-30, 30))
		c.forward(10)

def createTurtle():
	c = turtle.Turtle()
	c.shape("turtle")
	c.color(random.choice(computercolours))
	c.setheading(random.randint(0, 360))
	computers.append(c)
w.onkey(createTurtle, "space")

def myforward():
	player.forward(30)
w.onkey(myforward, "Up")

def myLeft():
	player.left(45)
w.onkey(myLeft, "Left")

def myRight():
	player.right(45)
w.onkey(myRight, "Right")

def myBye():
    w.bye()

w.onkey(myBye, "q")

### KEEP THIS AT END OF CODE
# start listening for key events
w.listen()
# Enter a game loop
while True:
	updateGame()
	w.getcanvas().update_idletasks()
	w.getcanvas().update()
