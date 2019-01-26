#!/usr/bin/env python
#########################################################
#
# Build a flight of steps in Minecraft.
#
#########################################################
from mcpi.minecraft import Minecraft
from mcpi import block

# How many stairs to be made.
size = 8
levels = 6

# Connect to Minecraft
mc = Minecraft.create()

# Find out where the Player is (we want to build near here)
x, y, z = mc.player.getTilePos()

# Clear the area
mc.setBlocks(x+1, y-1, z-3, x+size+10, y+size*levels, z+12, block.AIR)
mc.setBlocks(x+1, y-1, z-3, x+size+9, y-1, z+11, block.STONE)

# Build a series of levels.
for level in range(6):

    # Place the ceiling
    mc.setBlocks(x+2,        ((1+level)*size)+y-1, z-2, x+size+7, ((1+level)*size)+y-1, z+10, block.STONE)
    mc.setBlocks(x+4+size/2, ((1+level)*size)+y-1, z, x+size+4,   ((1+level)*size)+y-1, z, block.AIR)
 
    # Build a series of staggered bricks.
    for step in range(size):
        mc.setBlock(x+step+4, level*size+y+step, z, block.STAIRS_WOOD.id, 0)
        mc.setBlock(x+step+5, level*size+y+step, z, block.WOOD.id)

    # Build glass walls
    mc.setBlocks(x+2, y+level*size, z-2, x+2, y+level*size+size-1, z+10, block.GLASS_PANE)
    mc.setBlocks(x+size+8, y+level*size, z-2, x+size+8, y+level*size+size-1, z+10, block.GLASS_PANE)
    mc.setBlocks(x+2, y+level*size, z-2, x+size+8, y+level*size+size-1, z-2, block.GLASS_PANE)
    mc.setBlocks(x+2, y+level*size, z+10, x+size+8, y+level*size+size-1, z+10, block.GLASS_PANE)
