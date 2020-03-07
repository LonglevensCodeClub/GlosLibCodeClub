#!/bin/python3

#Game variables that can be changed!

#game background colour.
BACKGROUNDCOLOUR = 'white'

#map variables.
MAXTILES  = 100
MAPWIDTH  = 20
MAPHEIGHT = 100

#variables representing the different resources.
DIRT    = 56  
GRASS   = 0
WATER   = 45
BRICK   = 0
WOOD    = 23   
#a list of all game resources.
resources = [DIRT,GRASS,WATER,BRICK,WOOD]

#the names of the resources.
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick',
  WOOD    : 'wood'
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif',
  WOOD    : 'wood.gif'
}
#the number of each resource the player has.
inventory = {
  DIRT    : 100,
  GRASS   : 100,
  WATER   : 10,
  BRICK   : 100,
  WOOD    :200
}
#the player image.
playerImg = 'player.gif'

#the player position. 
playerX = 0
playerY = 0

#rules to make new resources. 
crafting = {
  BRICK    : { WATER :0 , DIRT : 0 },
  WOOD     : { DIRT  :0}
}
#keys for placing resources.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4',                  
  WOOD  : '5'
}
#keys for crafting tiles.
craftkeys = {
  BRICK : 'r',
  WOOD  : 'h'
}
#game instructions that are displayed.
instructions =  [
  'Instructions:',
  'Use WASD to move'
]
