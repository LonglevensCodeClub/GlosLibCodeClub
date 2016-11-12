from turtle import*
from random import*

colormode(255) # leave at start


def randomcolour():
	red=randint(0, 225)
	green=randint(0,255)
	blue=randint(0,255)
	color(red,green,blue)

shape ("turtle")
randomcolour()

def randomplace():
  penup()
  x = randint(-100,100)
  y = randint(-100,-100)
  goto(x,y)
  pendown()
  

 
shape("turtle")
randomcolour()
randomplace()
stamp()
randomcolour()
randomplace()
stamp()
 
 <number
 
 
 
 
  
done() 
