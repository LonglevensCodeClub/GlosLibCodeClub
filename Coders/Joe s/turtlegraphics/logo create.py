from turtle import Turtle

t=Turtle()
t.screen.bgcolor("black")
t.color("white")

def square(length):
    for steps in range(4):
        t.fd(length)
        t.left(90)
        
        
def draw_square(x,y,length):
    t.hideturtle()
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    square(length)
    t.end_fill()
    
    
def rectangle(length,width):
    for steps in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)
        
        
def draw_rectangle(length,width,x,y):
    t.hideturtle()
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    rectangle(length,width)
    t.end_fill()
    
t.write("Marvels Spider man",move=True,align='center',font=('Cambria',18,'normal'))
draw_square(-120,-20,20)
draw_square(-120,30,20)
draw_square(-140,0,20)


        
            