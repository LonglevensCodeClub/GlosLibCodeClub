#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()

width = 5
height = 3
depth = 6

# Create a hollow shell made of bricks.
mc.setBlocks(x, y, z+3, x+width, y+height, z+3+depth, block.BRICK_BLOCK.id)
mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+depth, block.AIR.id)

# Set the floor.
mc.setBlocks(x-1, y-1, z+2, x+1+width, y-1, z+4+depth, block.WOOD_PLANKS.id)

# Add a door.
mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)

#Add windows
mc.setBlocks(x+3, y+1, z+3, x+4, y+2, z+3, block.GLASS.id)
mc.setBlocks(x+2, y+1, z+3+depth, x+3, y+2, z+3+depth, block.GLASS.id)
mc.setBlocks(x, y+1, z+5, x, y+2, z+7, block.GLASS.id)
mc.setBlocks(x+width, y+1, z+5, x+width, y+2, z+7, block.GLASS.id)
