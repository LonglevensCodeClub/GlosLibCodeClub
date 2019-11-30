import turtle

#set window size
turtle.setup(300,600)

window = turtle.Screen()
window.title("traffic light!")
window.bgcolor("lightgreen")

light = turtle.Turtle()
light.speed("fast")

def draw_housing():
    light.pensize(3)
    light.color("black","darkgrey")
    light.begin_fill()
    light.forward(80)
    light.left(90)
    light.forward(200)
    light.circle(40, 180)
    light.forward(200)
    light.left(90)
    light.end_fill()

def draw_light():
    light.penup()
    light.forward(40)
    light.left(90)
    light.forward(40)

    light.shape("circle")
    light.shapesize(3)
    light.fillcolor("green")
    light.speed("slowest")


def nextstate():
    global state_num
    window.onkey(None, "space")
    if state_num == 0:
            light.forward(70)
            light.fillcolor("orange")
            state_num = 1
    elif state_num == 1:
            light.forward(70)
            light.fillcolor("red")
            state_num = 2
    else:
            light.back(140)
            light.fillcolor("green")
            state_num = 0
    window.onkey(nextstate, "space")

state_num = 0

#call the functions we created
draw_housing()
draw_light()

window.onkey(nextstate, "space")
window.listen()

#keep screen visible
turtle.mainloop()
