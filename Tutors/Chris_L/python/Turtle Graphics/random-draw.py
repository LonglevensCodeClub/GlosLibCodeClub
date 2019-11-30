from turtle import Turtle, Screen
import random
 
t=Turtle()
window = Screen()
window.title("Random walk")

t.ht()
window.bgcolor("black")
window.tracer(0,0)

def random_drawing(turns,distance):
        for x in range(turns):
                right=t.right(random.randint(0,360))
                left=t.left(random.randint(0,360))

                t.color(random.choice(["blue","red","green"]))
                random.choice([right,left])
                t.fd(distance)
                window.update()
       

random_drawing(1000,10)

window.exitonclick()
