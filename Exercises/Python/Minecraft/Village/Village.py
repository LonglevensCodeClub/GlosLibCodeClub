#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block

###########################################################
#
# Initialise the Village. A clearing is made in front of the player.
# A road is placed along the z axis with grass either side of it.
# The Minecraft connection is returned.
#
###########################################################
def init():
    mc = Minecraft.create()
    x, y, z = mc.player.getTilePos()
    if z > 70:
        # We need room along the z axis for the steet
        z = 70
    mc.setBlocks(x-15, -1, z-2, x+15, 50, z+58, block.AIR.id)
    mc.setBlocks(x-15, -1, z-2, x+15, -1, z+58, block.GRASS.id)
    mc.setBlocks(x-2, -1, z-2, x+2, -1, z+58, block.STONE.id)
    mc.player.setPos(x, 0, z)
    return mc

###########################################################
#
# Construct a House centered on coordinates x, y, z.
# The house is 6 blocks deep and 7 blocks wide.
#
###########################################################
def makeHouse(mc, x, y, z):
    # Build the shell
    mc.setBlocks(x-2, y, z-3, x+3, y+2, z+3, block.BRICK_BLOCK.id)
    mc.setBlocks(x-1, y, z-2, x+2, y+2, z+2, block.AIR.id)

    # Add the roof
    mc.setBlocks(x-2, y+3, z-3, x-2, y+3, z+3, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+3, y+3, z-3, x+3, y+3, z+3, block.STAIRS_WOOD.id, 1)
    mc.setBlocks(x-1, y+4, z-3, x-1, y+4, z+3, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+2, y+4, z-3, x+2, y+4, z+3, block.STAIRS_WOOD.id, 1)
    mc.setBlocks(x, y+5, z-3, x, y+5, z+3, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+1, y+5, z-3, x+1, y+5, z+3, block.STAIRS_WOOD.id, 1)

    # Fill in each end of the roof
    mc.setBlocks(x-1, y+3, z-3, x+2, y+3, z-3, block.BRICK_BLOCK.id)
    mc.setBlocks(x, y+4, z-3, x+1, y+4, z-3, block.BRICK_BLOCK.id)
    mc.setBlocks(x-1, y+3, z+3, x+2, y+3, z+3, block.BRICK_BLOCK.id)
    mc.setBlocks(x, y+4, z+3, x+1, y+4, z+3, block.BRICK_BLOCK.id)
    
    # Add doors front and rear and pathways
    mc.setBlock(x-2, y, z-1, block.DOOR_WOOD.id, 0)
    mc.setBlock(x-2, y+1, z-1, block.DOOR_WOOD.id, 8)
    mc.setBlock(x+3, y, z+1, block.DOOR_WOOD.id, 2)
    mc.setBlock(x+3, y+1, z+1, block.DOOR_WOOD.id, 10)
    mc.setBlocks(x-3, y-1, z-1, x-4, y-1, z-1, block.STONE.id)
    mc.setBlocks(x+4, y-1, z+1, x+5, y-1, z+1, block.STONE.id)

    # Add Windows
    mc.setBlocks(x-2, y+1, z, x-2, y+1, z+1, block.GLASS.id)
    mc.setBlocks(x+3, y+1, z, x+3, y+1, z-1, block.GLASS.id)
    mc.setBlocks(x, y+1, z-3, x+1, y+1, z-3, block.GLASS.id)
    mc.setBlocks(x, y+1, z+3, x+1, y+1, z+3, block.GLASS.id)




mc = init()
x, y, z = mc.player.getTilePos()
# This next line will be left in place for the children to see how yo build a house.
#makeHouse(mc, x+8, y, z+4)

# These lines will be deleted before being given to the children - this will be their exercise.
for i in range(6):
    makeHouse(mc, x+7, y, z+4+10*i)
    makeHouse(mc, x-8, y, z+4+10*i)
