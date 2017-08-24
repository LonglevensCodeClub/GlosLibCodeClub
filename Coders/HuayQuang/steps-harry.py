#!/usr/bin/env python
########################################################################
#
#build a flight of steps in Minecraft. 
#
########################################################################
from mcpi .minecraft import Minecraft
from mcpi import block

# How many stairs to be made.
size = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

# Connect to Minecraft	
mc = Minecraft.create()

# Find out where the Player is (we want to build near here)
x, y, z=mc.player.getTilePos()
print ("Making Steps at: " + str(x + 2) + ", " + str(z))
 
#Build a series of staggered bricks.
for steps in range(size):
	mc.setBlock(x+steps+2,y+steps, z, block.TNT.id, 1)
	mc.setBlock(x+steps+3,y+steps, z, block.TNT.id, 1)
