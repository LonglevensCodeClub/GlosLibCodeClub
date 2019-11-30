import turtle 

#function called when mouse moved
def motion(event):
    x, y = event.x, event.y
    print('Motion function: {}, {}'.format(x, y))

#function called when turtle is dragged
def dragging(x, y):
    t.ondrag(None)
    print("turtle dragged x:", x, " y:", y)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def moveto(x,y):
    print("turtle clicked x:", x, " y:", y)
    t.onclick(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.onclick(moveto)

def get_mouse_click_coor(x, y):
    print("mouse clicked x:", x, " y:", y)
    t.setheading(t.towards(x, y))
    t.goto(x, y)

turtle.setup(400,400)

screen = turtle.Screen()

t = turtle.Turtle('turtle')
t.speed('fastest')

#attach mouse events to the turtle
t.ondrag(dragging)
t.onclick(moveto)
t.screen.onscreenclick(get_mouse_click_coor)

#code to capture mouse motion anywhere in the screen
canvas = t.screen.getcanvas()
canvas.bind('<Motion>', motion)

screen.mainloop()
