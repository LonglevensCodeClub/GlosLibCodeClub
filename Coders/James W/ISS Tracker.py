#!/bin/python3

import json
import urllib.request
import turtle
import time 

url = 'http://api.open-notify.org/iss-now.json'
#url = url + '?lat=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#over = result['response'][1]['risetime']
#print(over)

style = ('Arial', 6, 'bold')
#location.write(time.ctime(over), font=style)

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude:', lat)
print ('Longitude:',lon)

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(lon,lat)

# Space Centre, Houston
lat = 29.5502
lon = 95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()


#print ('People in Space', result['number']) 

#people = result['people']
#print(people)
