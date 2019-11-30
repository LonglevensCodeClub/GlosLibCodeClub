import turtle

t=turtle.Turtle()
window = turtle.Screen()

window.bgcolor("black")
window.title("beautiful circles")

colors=["red","yellow","purple"]
window.tracer(0,0)

for x in range(100):
  t.circle(x)
  t.color(colors[x%3])
  t.left(60)

window.mainloop()
