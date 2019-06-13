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
print("Number of astronauts in space: ", peopleData['number'])
people = peopleData['people']
for p in people:
  print(p)

#Longlevens Latitude and Longitude
lat = 51.876828
lon = -2.207779

url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'
url = url.format(lat, lon, 40)
overData = decodeUrl(url)
responses = overData['response']
print("The next 40 passes of the ISS over Gloucester will be:")
for response in responses:
    print("On {}".format(time.ctime(response['risetime'])),
        "Duration = {} seconds".format(response['duration']))

screen = turtle.Screen()
screen.title('ISS Tracker by Reuben')

#Map for small screen
screen.setup(720, 360)
screen.bgpic('iss/map.gif')

#Map for large screen
#screen.setup(1440, 720)
#screen.bgpic('iss/map1440x720.gif')

screen.setworldcoordinates(-180, -87, 180, 87)
screen.register_shape('iss/iss.gif')

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()
over = overData['response'][1]['risetime']
style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

iss = turtle.Turtle()
iss.shape('iss/iss.gif')
iss.setheading(90)
iss.pencolor('white')

url = 'http://api.open-notify.org/iss-now.json'
oldLon = 1000

while True:
    posData = decodeUrl(url)
    #print(posData)
    location = posData['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    
    if (abs(lon - oldLon) > 20 ):
        iss.penup()
    else:
        iss.pendown()    
    oldLon = lon
    iss.goto(lon, lat)
    time.sleep(30)

