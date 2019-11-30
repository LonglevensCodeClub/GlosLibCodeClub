from turtle import Turtle, Screen

window = Screen()

t=Turtle()
window.bgcolor("black")
t.color("orange")

def circle(x,y):
  t.goto(x,y)
  t.circle(60)

window.onclick(circle)

window.mainloop()
