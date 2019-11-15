from turtle import *

screen = Screen()

screenMinX = -screen.window_width() / 2
screenMinY = -screen.window_height() / 2
screenMaxX = screen.window_width() / 2
screenMaxY = screen.window_height() / 2
screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
screen.bgcolor("black")

screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))

class SpaceShip(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.color("red")
    self.shape("ship")

  def doLeft(self):
      self.left(10)
  
  def doRight(self):
      self.right(10)

ship = SpaceShip()

screen.onkey(ship.doLeft, 'Left')
screen.onkey(ship.doRight, 'Right')

screen.listen()


screen.exitonclick()
