from turtle import Turtle

t=Turtle()
t.screen.bgcolor("black")
t.screen.title("beautiful squares")

colors=["blue","purple","red","yellow"]
t.screen.tracer(0,0)

for x in range(300):
  t.color(colors[x%4])
  t.fd(x)
  t.left(90)

t.screen.exitonclick()
t.screen.mainloop()
