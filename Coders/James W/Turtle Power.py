import turtle 
import random

# Create a Turtle
player = turtle.Turtle()
player.shape("turtle")

# Get Hold of screen
w = turtle.Screen()

# Create a list of turtles to chase
computerColours=["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
computers = []

def myForward() :
   player.forward(30)
w.onkey(myForward, "Up")

def updateGame():
    for c in computers:
        c.left(random.randint(-30,30))
        c.forward(10)
        
def myLeft() :
    player.left(45)
w.onkey(myLeft, "Left")

def myRight() :
    player.right(45)
w.onkey(myRight, "Right")

def myBye():
    w.bye()

w.onkey(myBye, "q") 


def createTurtle():
    c = turtle.Turtle()
    c.shape("turtle")
    c.color(random.choice(computerColours))
    c.setheading(random.randint(0, 360))
    computers.append(c)

w.onkey(createTurtle, "space") 















### KEEP THIS AT END OF CODE
# Start listening for key events
w.listen() 

# Enter a game loop
while True:
    updateGame()
    w.getcanvas().update_idletasks()
    w.getcanvas().update() 
