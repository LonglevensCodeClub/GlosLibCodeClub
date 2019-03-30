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
    print("z=", z)
    #if z > 70:
    # We need room along the z axis for the steet
    mc.setBlocks(x-20, -1, z-2, x+20, 50, z+58, block.IRON.id, 1)
    mc.setBlocks(x-19, -2, z-1, x+19, 49, z+57, block.AIR.id)


init()