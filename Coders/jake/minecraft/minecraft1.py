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




init()
