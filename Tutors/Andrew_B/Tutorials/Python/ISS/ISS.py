#!/bin/python3

import json
import turtle
import urllib.request
import time

# URLs that provide JSON data containing information about the ISS.
astronautsUrl    = 'http://api.open-notify.org/astros.json'
positionUrl      = 'http://api.open-notify.org/iss-now.json'
timesOverheadUrl = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'

def loadJsonFromUrl(url):
    """ Returns the JSON provided by the given URL. """
    #print("URL", url, "returned:")
    html = urllib.request.urlopen(url).read()
    result = json.loads(html.decode('utf-8'))
    #print(result)
    return result

def updatePositionOnMap(posData):
    """ Moves the ISS avatar to the current position on the world map. Checks
        longitude against previous value to switch with pen up when the craft
        swaps from east to west. Set oldLon to 1000 before first call to ensure
        that a plot line is not drawn to the starting position from the centre.
        posData - The JSON containing the latitude and longitude data. """
    location = posData['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    tim = posData['timestamp']
    print("On {} the ISS was at: {}, {}".format(time.ctime(tim), lat, lon))
    global oldLon
    if (abs(lon - oldLon) > 20 ):
        iss.penup()
    else:
        iss.pendown()    
    iss.goto(lon, lat) 
    oldLon = lon

def findNextPasses(latitude, longitude, passesToFind):
    """ Dispays and returns in JSON format the forthcoming times when the ISS
        will be at the given location.
        latitude - The latitude of the location to be displayed.
        longitude - The longitude of the location to be displayed.
        passesToFind - The number of passes to be looked up."""
    url = timesOverheadUrl.format(latitude, longitude, passesToFind)
    overData = loadJsonFromUrl(url)
    responses = overData['response']
    for response in responses:
        print("Time = {}".format(time.ctime(response['risetime'])),
              "Duration = {} seconds".format(response['duration']))
    return overData

def displayNextPass(overData, latitude, longitude):
    """ Displays the next time the ISS will be over the given location on the map.
        overData - The JSON from the URL providing the times overhead data.
        latitude - The latitude of the location to be displayed.
        longitude - The longitude of the location to be displayed."""
    location = turtle.Turtle()
    location.penup()
    location.color('yellow')
    location.goto(longitude, latitude)
    location.dot(5)
    location.hideturtle()
    over = overData['response'][1]['risetime']
    style = ('Arial', 6, 'bold')
    location.write(time.ctime(over), font=style)

# Display the astronauts currently in space.
peopleData = loadJsonFromUrl(astronautsUrl)
print("Number of astronauts in space: ", peopleData['number'])
people = peopleData['people']
for p in people:
    print(p['name'], "in", p['craft'])
        
#Longlevens Latitude and Longitude
lat = 51.876828
lon = -2.207779

# Plot the position of the ISS and Longlevens on a world map.
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -85, 180, 85)
screen.bgpic('iss/map.gif')
screen.register_shape('iss/iss.gif')

# Print out the date and times of the next 40 passes over Longlevens.
nextPasses = findNextPasses(lat, lon, 40)

# Display the date and time of the next pass over Longlevens on the map.
displayNextPass(nextPasses, lat, lon)

# Display the ISS on the map.
iss = turtle.Turtle()
iss.shape('iss/iss.gif')
iss.setheading(90)
iss.pencolor('white')
iss.penup()

# Initial value of the previous longitude of the ISS so that first move of the
# ISS on the map will cause the pen to be lifted and avoid a stray plot line.
oldLon = 1000

# Plot the ISS on the map for approximately 2 orbits at one minute intervals.
# IMPORTANT: Do not adjust sleep time below 5 seconds - it is against the rules
# of the server providing the data.
# NOTE: It takes the ISS approximately 92 minutes to complete each orbit.
for position in range(185):
    positionData = loadJsonFromUrl(positionUrl)
    updatePositionOnMap(positionData)
    time.sleep(60)
