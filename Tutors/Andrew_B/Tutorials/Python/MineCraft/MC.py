from mcpi.minecraft import Minecraft
from mcpi import block

size = 10

mc = Minecraft.create()

x,y,z=mc.player.getTilePos()
print("Making Steps at : " + str(x + 2) + ", " + str(z))
mc.getBlock(x,y,z)
for step in range(size):
    mc.setBlock(x+step+2, y+step, z, block.STAIRS_WOOD, 0)
    mc.setBlock(x+step+3, y+step, z, block.WOOD.id)


