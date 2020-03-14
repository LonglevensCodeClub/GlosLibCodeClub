from turtle import Turtle
import random

t=Turtle()
t.screen.bgcolor("black")

def random_drawing(turns,distance):
    for x in range (turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(["turquoise","magenta","hot pink"]))
        random.choice([right,left])
        t.fd(distance)
        print(distance)
        

 
 
 
 
random_drawing(100,50)