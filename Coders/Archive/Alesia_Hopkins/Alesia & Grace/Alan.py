#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()

width = 25
height = 10
depth = 30

# Create a hollow shell made of bricks.
mc.setBlocks(x, y, z+3, x+width, y+height, z+3+depth, block.BRICK_BLOCK.id)
mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+depth, block.AIR.id)

# Set the floor.
mc.setBlocks(x-1, y-1, z+2, x+1+width, y-1, z+4+depth, block.WOOD_PLANKS.id)

# Add a door.
mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)

#Add windows
mc.setBlocks(x+6, y+2, z+6, x+8, y+4, z+6, block.GLASS.id)
mc.setBlocks(x+4, y+2, z+6+depth, x+6, y+4, z+6+depth, block.GLASS.id)
mc.setBlocks(x, y+2, z+10, x, y+4, z+14, block.GLASS.id)
mc.setBlocks(x+width, y+2, z+10, x+width, y+4, z+14, block.GLASS.id)

# Add a roof
for i in range(int(width/2) + 1):
    mc.setBlocks(x+i, y+height+i, z+3, x+i, y+height+i, z+3+depth, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+width-i, y+height+i, z+3, x+width-i, y+height+i, z+3+depth, block.STAIRS_WOOD.id, 1)
    #Gable Ends. Yay! No more code! Spoke to soon...
    
    if ((width/2) - i > 0):
        mc.setBlocks(x+1+i, y+height+i, z+3, x+width-i-1, y+height+i, z+3, block.BRICK_BLOCK.id, 0)
        mc.setBlocks(x+1+i, y+height+i, z+3+depth, x+width-i-1, y+height+i, z+3+depth, block.BRICK_BLOCK.id, 1)
# Yay. This is the proper end!       
