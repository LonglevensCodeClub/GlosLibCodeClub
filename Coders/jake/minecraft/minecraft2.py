#!/usr/bin/env python


 #Build a flight of steps in minecraft.
 
 
from mcpi.minecraft import Minecraft
from mcpi import block

#How many stairs to be made.
size = 50

 #connect to minecraft
mc = Minecraft.create()

# find out where the player is (we want to build ner here)
x, y, z = mc.player.getTilePos()
print ("making steps at: " + str(x + 2) + ", " + str(z))

 #Build a siries of staggered bricks.
for step in range(size):
    mc.setBlock(x+step+2, y+step, z, block.STAIRS_WOOD.id, 0)
    mc.setBlock(x+step+3, y+step, z, block.WOOD.id)
    

    mc.setBlock(x+step+2, y+step, z+1, block.STAIRS_WOOD.id, 0)
    mc.setBlock(x+step+3, y+step, z+1, block.WOOD.id)




#mc.setblocks(x1, y2, z1,  x2, x2, y2, z2, block)
    
    