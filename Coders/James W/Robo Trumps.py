
robots = {}

file = open('cards.txt', 'r')
for line in file.read().splitlines():
  name, battery, intelligence, image = line.split(', ')
  robots[name] = [battery, intelligence, image] 

file.close()

while True:
  

 robot = input('Choose a robot ')

 if robot in robots:
  print(robots[robot])
  
 else:
  print('Robot doesn\'t exist!')
  
  from random import choice
  from turtle import *
  
  screen =  Screen()
  screen.bgcolor('white')
  penup()
  hideturtle()
  
  robots = {}
  
  
  rainbow, 10, 34, rainbow.png
space, 13, 28, space.png
bird, 6, 4, bird.png
  
 
