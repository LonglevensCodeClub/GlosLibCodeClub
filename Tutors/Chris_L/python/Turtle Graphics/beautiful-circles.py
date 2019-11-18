from turtle import Turtle

t=Turtle()

t.screen.bgcolor("black")
t.screen.title("beautiful circles")

colors=["red","yellow","purple"]
t.screen.tracer(0,0)

for x in range(100):
  t.circle(x)
  t.color(colors[x%3])
  t.left(60)

t.screen.exitonclick()
t.screen.mainloop()
