#!/bin/python3

from turtle import *
from math import *

yMax = 20
xMax = 20
yMin = -20
xMin = -20
scale = 10

#Draw the x and y axes
goto(xMin * scale, 0)
pendown()
goto(xMax * scale, 0)
goto(xMax * scale - 5, 5)
goto(xMax * scale, 0)
goto(xMax * scale - 5, -5)
penup()
goto(xMax * scale - 5, -20)
write('x')
goto(0, yMin * scale)
pendown()
goto( 0, yMax * scale)
goto(-5, yMax * scale - 5)
goto( 0, yMax * scale)
goto( 5, yMax * scale - 5)
penup()
goto (-15, yMax * scale - 5)
write('y')

#Draw tick marks
for tickMark in range(xMin, xMax):
    penup()
    goto(tickMark * scale, 0)
    pendown()
    goto(tickMark * scale, -5)
    if (tickMark % 4 == 0 and tickMark != 0):
        penup()
        goto(tickMark * scale - 5, -15)
        write(tickMark)

for tickMark in range(yMin, yMax):
    penup()
    goto(0, tickMark * scale)
    pendown()
    goto(-5, tickMark * scale)
    if (tickMark % 4 == 0 and tickMark != 0):
        penup()
        goto(-20, tickMark * scale - 5)
        write(tickMark)



def drawLine(m, c):
    """ Draw a line on the graph.
        m - The gradient of the line.
        c - The y offset; value of y when x = 0
    """
    penup()
    for x in range(xMin, xMax):
        y = m * x + c
        if (y <= yMax and y >= yMin):
            goto(x * scale, y * scale)
            pendown()
    write('Line')


def getCircleY(r, h, x):
    """ Obtain the positive value of y for a circle. Y offset is not included
        in the answer and must be added to the value. Multiply the answer by
        -1 to obtain the lower value of y before adding the offset.
        r - The radius of the circle
        h - The offset of the centre of the circle on the x axis.
        x - The value of x for the calculation.
    """
    return sqrt(abs(r * r - (x - h) * (x - h)))


def drawCircle(radius, h, k):
    """ Draw a circle of the given radius.
        radius - The radius of the circle.
        h - The x offset of the centre.
        k - The y offset of the centre.
    """
    r = radius * scale
    penup()
    goto(-r + h * scale, k * scale)
    pendown()
    #Cannot iterate in floats so scale up to pixels
    for x in range(-r + h * scale, r + h * scale + 1, 4):
        y = getCircleY(r, h * scale, x) + k * scale
        goto(x, y)
        
    for x in range(r + h * scale, -r + h * scale - 1, -4):
        y = -1 * (getCircleY(r, h * scale, x)) + k * scale
        goto(x, y)
    write('Circle')


def drawEllipse(h, k, xWidth, yWidth):
    """ Draw an ellipse.
        h - The x offset of the centre.
        k - The y offset of the centre.
        xWidth - The width of the x axis
        yWidth - The width of the y axis
    """
    
    a = int(xWidth * scale / 2)
    b = int(yWidth * scale / 2)
    
    penup()
    goto(-a + h * scale, k * scale)
    pendown()
    #Cannot iterate in floats so scale up to pixels
    for x in range(-a, a + 1, 4):
        y = sqrt(abs(b * b *(1 - (x * x / a / a))))
        goto(x + h * scale, y + k * scale)

    for x in range(a, -a - 1, -4):
        y = -1 * sqrt(abs(b * b *(1 - (x * x / a / a))))
        goto(x + h * scale, y + k * scale)

    write('Ellipse')


def drawTangent(r, h, k, a, b):
    """ Draw a tangent at the point (a, b) on a circle. If this point is not a
        point on the circle a warning message will be printed on the console
        instead.
        r - The radius of the circle.
        h - The x offset of the centre of the circle.
        k - The y offset of the centre of the circle.
        a - The x position of the point where the tangent is to be drawn.
        b - The y position of the point where the tangent is to be drawn.
    """
    #Check x and y are on circle circumference
    #yCheck = sqrt(abs(r * r - (a - h) * (a - h))) + k
    yCheck = getCircleY(r, h, a)
    if (yCheck + k != b and yCheck * -1 + k != b):
        print("Invalid coordinate on circle given:", a, ",", b)
        print("Y value for x was:", yCheck)
        print("B", b)
        print("c1=", yCheck + k - b)
        print("c2=", yCheck * -1 + k - b)
    else:
        line = 'normal'
        if (a - h == 0):
            line = 'horizontal'
        elif (b - k == 0):
            line = 'vertical'        
        else:
            radiusGradient = (b - k) / (a - h)

        penup()
        if (line == 'normal'):
            tangentGradient = -1 / radiusGradient
            #when x = xMax
            y = tangentGradient * (xMax - a) + b
            goto(xMax * scale, y * scale)
            #when x = xMin
            y = tangentGradient *(xMin - a ) + b
            pendown()
            goto(xMin * scale, y * scale)
        else:
            if (line == 'vertical'):
                goto (a * scale, yMax * scale)
                pendown()
                goto (a * scale, yMin * scale)
            else:
                goto(xMin * scale, b * scale)
                pendown()
                goto(xMax * scale, b * scale)
        write('Tangent')

def drawQuadratic(a, b, c):
    """ Draw a quadratic curve on the graph.
        a - The x squared multiplier.
        b - The x mutliplier.
        c - The constant.
    """
    penup()
    for x in range(xMin * scale, xMax * scale + 1):
        xAdj = x / scale
        y = a * xAdj * xAdj + b * xAdj + c
        if (y <= yMax and y > yMin):
            goto(x, y * scale)
            if (not isdown()):
                pendown()
        else:
            if (isdown()):
                goto(x, y * scale)
            penup()
    write('Quadratic')


def drawSineWave(a, b, d):
    """ Draw a simple sine wave where the x axis in in degrees.
        a - The amplitude
    """
    penup()
    for x in range(xMin * scale, xMax * scale + 1, 5):
        y = a * sin(radians(x)) * scale
        goto(x + b, y + d)
        pendown()
    #write('Sine wave')

def draw2DSineWave(a):
    """ Draw a 2D sine wave where the x axis in in degrees.
        a - The amplitude
    """
    for x in range(xMin, xMax + 1):
        y = a * sin(radians(x * scale))
        penup()
        drawSineWave(a, (x - xMin) * scale, y * scale)



#Draw Ellipse
drawEllipse(-10, 10, 16, 10)

#Draw a line
color('red')
drawLine(-0.5, -3)

#Draw a circle
color('green')
drawCircle(7, 13, 7)

#Draw tangent at top of circle
#drawTangent(100, 90, 50, 90, 150)
#Draw tangent at right hand edge of circle
#drawTangent(100, 90, 50, 190, 50)

color('blue')
#Draw a tangent at x = 9, y - k > 0
yVal = getCircleY(7, 13, 9) + 7
drawTangent(7, 13, 7, 9, yVal)

#Draw a quadratic
color('purple')
drawQuadratic(2, -4, -8)

#Draw a sine wave
color('indigo')
drawSineWave(10, 0, 0)

#Draw 2D sine wave
color('pink')
draw2DSineWave(10)