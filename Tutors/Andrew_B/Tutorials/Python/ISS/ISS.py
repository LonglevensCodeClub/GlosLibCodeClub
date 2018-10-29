#!/bin/python3

import json
import turtle
import urllib.request
import time

def decodeUrl(url):
    html = urllib.request.urlopen(url).read()
    result = json.loads(html.decode('utf-8'))
    return result

url = 'http://api.open-notify.org/astros.json'
peopleData = decodeUrl(url)
print("People in Space: ", peopleData['number'])

people = peopleData['people']
print("People =", people)
for p in people:
    print(p['name'], "in", p['craft'])

url = 'http://api.open-notify.org/iss-now.json'
posData = decodeUrl(url)
print(posData)

location = posData['iss_position']
lat = location['latitude']
lon = location['longitude']
print("Position =", lat, lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('iss/map.gif')

screen.register_shape('iss/iss.gif')
iss = turtle.Turtle()
iss.shape('iss/iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))

#Longlevens Latitude and Longitude
lat = 51.876828
lon = -2.207779

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
overData = decodeUrl(url)
over = overData['response'][1]['risetime']
#print("Time overhead =", over)
style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)
