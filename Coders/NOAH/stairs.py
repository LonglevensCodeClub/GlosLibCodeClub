from mcpi.minecraft import Minecraft
from mcpi import block

# How many stairs to be made.
size = 50

# connect to Minecraft
mc = Minecraft.create()

# Find out where the player is (we want to build near here)
x, y, z = mc.player.getTilePos()
print ("Making steps at; " + str(x + 2) + ", " + str(z))

# Build a series of staggered bricks.
for step in range(size):
     mc.setBlock(x+step+2, y+step, z, block.STAIRS_WOOD.id, 0)
     mc.setBlock(x+step+3, y+step, z, block.WOOD.id)
