#!/usr/bin/env python
    #########################################################
#
# Build a flight of steps in Minecraft.
#
#########################################################
def makeSpire():
    height = 2
    Blocktype = 1
    
#spier sides: should be same as height
    sideHeight = height
    mc.setblocks(x + 1, y, z + 1, x+ 3, y + sideHeight -1,z + 3, Blocktype)



from mcpi.minecraft import Minecraft
from mcpi import block

# How many stairs to be made.
size = 8
levels = 6

# Connect to Minecraft
mc = Minecraft.create()

    # Find out where the Player is (we want to build near here)
x, y, z = mc.player.getTilePos()

mc.player.setTilePos(0,1,0)
# Clear the area
sizeofworld = 127

mc.setBlocks(-sizeofworld, 0, -sizeofworld, sizeofworld*2, y+size*levels, sizeofworld*2, block.AIR)
mc.setBlocks(x+1, y-1, z-3, x+size+9, y-1, z+11, block.GOLD_BLOCK)

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




###########################################################

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




