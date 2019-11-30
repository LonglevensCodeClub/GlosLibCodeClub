from turtle import Turtle, Screen

t=Turtle()
window = Screen()

window.bgcolor("black")
window.title("Spirals")

colors=["blue","purple","red","yellow","orange","brown"]

window.tracer(0,0)

for x in range(300):
  t.color(colors[x%6])
  t.fd(x)
  t.left(59)

#keep window open until mouse clicked
window.exitonclick()

