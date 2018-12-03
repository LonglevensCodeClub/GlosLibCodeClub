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
    mc.setBlocks(x-20, -1, z-2, x+20, 50, z+58, block.WOOL.id)
        
# The house is 6 blocks deep and 7 blocks wide.
#
###########################################################


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
