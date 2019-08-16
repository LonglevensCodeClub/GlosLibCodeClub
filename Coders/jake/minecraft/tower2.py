from mcpi.minecraft import Minecraft
from mcpi import block

# How many stairs to be made.
size = 8
levels = 6

# Connect to Minecraft
mc = Minecraft.create()

    # Find out where the Player is (we want to build near here)
x, y, z = mc.player.getTilePos()

#mc.player.setTilePos(0,1,0)
# Clear the area
sizeofworld = 127

mc.setBlocks(-sizeofworld, 0, -sizeofworld, sizeofworld*2, y+size*levels, sizeofworld*2, block.AIR)
#mc.setBlocks(-sizeofworld, 0, -sizeofworld, sizeofworld*2, 0, sizeofworld*2, block.GOLD_BLOCK)

#PUT A ROW OF BLOCKS



for y in range(0,9):
    mc.setBlock(1, 0, y, block.TNT)
    
    
for y in range(0,9):
    mc.setBlock(10, 0, y, block.TNT)
        
    




