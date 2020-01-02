#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

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
    mc.setBlocks(x-20, -1, z-2, x+20, 50, z+58, block.AIR.id)
    mc.setBlocks(x-15, -1, z-2, x+15, -1, z+58, block.GRASS.id)
    mc.setBlocks(x-2, -1, z-2, x+2, -1, z+58, block.WOOD_PLANKS.id)
    mc.setBlocks(x-1, -1, z-2, x+1, -1, z+58, block.STONE.id)
    mc.player.setPos(x, 0, z)
    return mc
#make the lamp

def makeLamp(mc, x, y, z):
    mc.setBlocks(x, y, z, x, +5, z, block.FENCE.id)
    mc.setBlocks(x, y+5, z, x, +5, z, block.GLOWSTONE_BLOCK.id)

###########################################################
#
# Construct a House centered on coordinates x, y, z.
# The house is 6 blocks deep and 7 blocks wide.
#
###########################################################
def makeHouse(mc, x, y, z):
    # Build the shell
    mc.setBlocks(x-2, y, z-3, x+3, y+2, z+3, block.BRICK_BLOCK.id)
    mc.setBlocks(x-2, y, z-3, x+3, y, z+3, block.WOOD_PLANKS.id)
    mc.setBlocks(x-1, y, z-2, x+2, y+2, z+2, block.AIR.id)
    mc.setBlocks(x-2, y-1, z-3, x+3, y-1, z+3, block.STONE_SLAB_DOUBLE.id)
    mc.setBlocks(x-2, y, z-3, x-2, y+2, z-3, block.WOOD_PLANKS.id)
    mc.setBlocks(x+3, y, z+3, x+3, y+2, z+3, block.WOOD_PLANKS.id)
    mc.setBlocks(x-2, y, z+3, x-2, y+2, z+3, block.WOOD_PLANKS.id)
    mc.setBlocks(x+3, y, z-3, x+3, y+2, z-3, block.WOOD_PLANKS.id)
    
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
    
def makeTower(mc, x, y, z):
    
    floors = 10
    floor_height = 4
    
    for floor in range(floors):
        floor_base = y + floor_height * floor
        # Build the shell for one floor
        mc.setBlocks(x-1, floors * floor_height, z-2, x-1, floors * floor_height+3, z-2, block.IRON_BLOCK.id)
        mc.setBlocks(x-1, floors * floor_height+3, z-2, x-1, floors * floor_height+3, z-2, block.FURNACE_ACTIVE.id)
        mc.setBlocks(x-2, floor_base, z-3, x+3, floor_base+3, z+3, block.IRON_BLOCK.id)
        mc.setBlocks(x-2, floor_base, z-3, x+3, floor_base, z+3, block.WOOD_PLANKS.id)
        mc.setBlocks(x-1, floor_base, z-2, x+2, floor_base+2, z+2, block.AIR.id)
        mc.setBlocks(x-2, floor_base-1, z-3, x+3, floor_base-1, z+3, block.WOOD_PLANKS.id)
        mc.setBlocks(x-2, y-1, z-3, x+3, y-1, z+3, block.STONE_SLAB_DOUBLE.id)
        # Pillars
        mc.setBlocks(x-2, floor_base, z-3, x-2, floor_base+2, z-3, block.WOOD_PLANKS.id)
        mc.setBlocks(x+3, floor_base, z+3, x+3, floor_base+2, z+3, block.WOOD_PLANKS.id)
        mc.setBlocks(x-2, floor_base, z+3, x-2, floor_base+2, z+3, block.WOOD_PLANKS.id)
        mc.setBlocks(x+3, floor_base, z-3, x+3, floor_base+2, z-3, block.WOOD_PLANKS.id)
        # Floor
        mc.setBlocks(x-2, floor_base+3, z-3, x+3, floor_base+3, z+3, block.WOOD_PLANKS.id)
        mc.setBlock(x-1, floor_base, z-2, block.BED.id)
        mc.setBlock(x-1, floor_base, z-1, block.BED.id, 4)
        
        # Add Windows
        mc.setBlocks(x-2, floor_base+1, z, x-2, floor_base+1, z+1, block.GLASS.id)
        mc.setBlocks(x+3, floor_base+1, z, x+3, floor_base+1, z-1, block.GLASS.id)
        mc.setBlocks(x, floor_base+1, z-3, x+1, floor_base+1, z-3, block.GLASS.id)
        mc.setBlocks(x, floor_base+1, z+3, x+1, floor_base+1, z+3, block.GLASS.id)
        
        print ("Pos:", x, y, z)
        if floor < floors - 1:
            for step in range(floor_height-1):
                print("step", step)
                mc.setBlock(x+step, y+floor_base+step, z, block.STAIRS_WOOD.id, 0)
                mc.setBlock(x+step, y+floor_base-1, z, block.AIR.id)
            mc.setBlock(x+floor_height-2, y+floor_base-1, z+1, block.STAIRS_WOOD.id, 2)
            mc.setBlock(x+floor_height-2, y+floor_base-1, z-1, block.STAIRS_WOOD.id, 3)
        else:
            for step in range(floor_height-1):
                print("step", step)
                mc.setBlock(x+step, y+floor_base-1, z, block.AIR.id)
            
            
        # For Ati next Week
        # Make air blocks at top of stairs
            
    
    # Add doors front and rear and pathways
    mc.setBlock(x-2, y, z-1, block.DOOR_WOOD.id, 0)
    mc.setBlock(x-2, y+1, z-1, block.DOOR_WOOD.id, 8)
    mc.setBlock(x+3, y, z+1, block.DOOR_WOOD.id, 2)
    mc.setBlock(x+3, y+1, z+1, block.DOOR_WOOD.id, 10)
    mc.setBlocks(x-3, y-1, z-1, x-4, y-1, z-1, block.STONE.id)
    mc.setBlocks(x+4, y-1, z+1, x+5, y-1, z+1, block.STONE.id)


def makeShop(mc, x, y, z):
    # Build the shell
    mc.setBlocks(x-2, y, z-3, x+3, y+2, z+3, block.STONE_SLAB_DOUBLE.id)
    mc.setBlocks(x-2, y-1, z-3, x+3, y-1, z+3, block.STONE_SLAB_DOUBLE.id)
    mc.setBlocks(x-1, y, z-2, x+2, y+2, z+2, block.AIR.id)

    # Add the roof
    mc.setBlocks(x-2, y+3, z-3, x-2, y+3, z+3, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+3, y+3, z-3, x+3, y+3, z+3, block.STAIRS_WOOD.id, 1)
    mc.setBlocks(x-1, y+4, z-3, x-1, y+4, z+3, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+2, y+4, z-3, x+2, y+4, z+3, block.STAIRS_WOOD.id, 1)
    mc.setBlocks(x, y+5, z-3, x, y+5, z+3, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+1, y+5, z-3, x+1, y+5, z+3, block.STAIRS_WOOD.id, 1)

    # Fill in each end of the roof
    mc.setBlocks(x-1, y+3, z-3, x+2, y+3, z-3, block.STONE_SLAB_DOUBLE.id)
    mc.setBlocks(x, y+4, z-3, x+1, y+4, z-3, block.STONE_SLAB_DOUBLE.id)
    mc.setBlocks(x-1, y+3, z+3, x+2, y+3, z+3, block.STONE_SLAB_DOUBLE.id)
    mc.setBlocks(x, y+4, z+3, x+1, y+4, z+3, block.STONE_SLAB_DOUBLE.id)
    
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
    mc.setBlocks(x-2, y+2, z, x-2, y+2, z+1, block.GLASS.id)
    mc.setBlocks(x+3, y+2, z, x+3, y+2, z-1, block.GLASS.id)
    mc.setBlocks(x, y+2, z-3, x+1, y+2, z-3, block.GLASS.id)
    mc.setBlocks(x, y+2, z+3, x+1, y+2, z+3, block.GLASS.id)





mc = init()
x, y, z = mc.player.getTilePos()
makeShop(mc, x+7, y, z+4)
makeLamp(mc, x+4, y, z+9)
makeLamp(mc, x-4, y, z+9)
makeHouse(mc, x+7, y, z+14)
makeLamp(mc, x-4, y, z+19)
makeShop(mc, x+14, y, z+4)
makeLamp(mc, x+4, y, z+19) 
makeTower(mc, x+14, y, z+14)
makeLamp(mc, x-4, y, z+29)
makeShop(mc, x-8, y, z+4)
makeLamp(mc, x+4, y, z+29) 
makeHouse(mc, x-8, y, z+14)
makeLamp(mc, x-4, y, z+39) 
makeShop(mc, x-15, y, z+4)
makeLamp(mc, x+4, y, z+39) 
makeTower(mc, x-15, y, z+14)
makeLamp(mc, x-11, y, z+9) 
makeShop(mc, x+7, y, z+24)
makeLamp(mc, x+11, y, z+9) 
makeHouse(mc, x+7, y, z+34)
makeLamp(mc, x+11, y, z+19)
makeShop(mc, x+14, y, z+24)
makeLamp(mc, x-11, y, z+19) 
makeTower(mc, x+14, y, z+34)
makeLamp(mc, x-11, y, z+29) 
makeShop(mc, x-8, y, z+24)
makeLamp(mc, x+11, y, z+29) 
makeHouse(mc, x-8, y, z+34)
makeLamp(mc, x-11, y, z+39) 
makeShop(mc, x-15, y, z+24)
makeLamp(mc, x+11, y, z+39) 
makeTower(mc, x-15, y, z+34)




##################################################
#
#  Exercises:
#
# 1. Run this code and explore the world in Minecraft, see the road
#    and the house that have been built.
#
# 2. Make a copy of the above line of code "makeHouse..." and
#    change it so that a second house is build on the other side of the road.
#    Hint: You will have to change the location of the new house.
#
# 3. Wrap both of the "makeHouse..." lines in a for loop to create 
#    a row of houses along each side of the road. You should be able to make
#    6 houses spaced 10 blocks apart. You will have to change the arguments
#    supplied to both "makeHouse..." calls so that the houses are built
#    all along the road. Refer to last week's "Steps" exercise for an
#    example of building things inside a for loop.
#
# 4. Copy and Paste the whole "makeHouse..." function and change the name
#    of it to something else (for example "makeShop"). Now change the code
#    inside the copied function so that it creates your new design (for
#    example, a shop will have large windows, a pavement all the way across
#    the front and an awning.
#
# 5. Change your for loop so that is uses both "makeHouse" and "makeShop"
#    (for example the houses on one side of the street and the shops on the
#    other).
#
