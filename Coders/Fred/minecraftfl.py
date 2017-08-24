#!/usr/bin/env python
########################################################################
#
# Build a flight of steps in Minecraft
#
########################################################################
from mcpi.minecraft import Minecraft
from mcpi import block

# How many stairs to be made.
size = 10

# Connect to Minecraft
mc = Minecraft.create()
# Find out were the player is.
x, y, z = mc.player.getTilePos()
print ("Making steps at: " + str(x + 2) + ", " + str(z))

# dddddddddddddduuuuuuuuuuuuuuuuuuuuuuhhhhhhhhhhhhhhhhhhhhh
for step in range(size):
	mc.setBlock(x+step+2, y+step, z, block.STAIRS_WOOD.id, 0)
	mc.setBlock(x+step+3, y+step, z, block.NETHER_REACTOR_CORE.id)




    
    
    
    
    
# dhfiugbrghruefhreukuyfgyr88kjifguryjoryitg['urieghuir

