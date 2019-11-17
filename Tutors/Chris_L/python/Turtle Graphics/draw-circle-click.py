from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
t.color("orange")

def circle(x,y):
  t.gotoxy(0,0)
  t.circle(60)

t.onclick(circle)
t.screen.listen()

t.screen.mainloop()
