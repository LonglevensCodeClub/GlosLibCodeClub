from turtle import Turtle
import random
 
t=Turtle()
t.ht()
t.screen.bgcolor("black")
t.tracer(0)

def random_drawing(turns,distance):
 	for x in range(turns):
	    right=t.right(random.randint(0,360))
 	    left=t.left(random.randint(0,360))
 	    t.color(random.choice(["blue","red","green"]))
 	    random.choice([right,left])
 	    t.fd(distance)
	    t.screen.update()


t.speed(0)

random_drawing(2000,5)

t.screen.exitonclick()
