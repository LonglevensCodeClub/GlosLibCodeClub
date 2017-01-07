

from mcpi.minecraft import Minecraft
from mcpi import block

size = 9999999999999999999

Width = 1

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
print ("Making Steps at: " + str(x +  2) + ", " + str(z))

for step in range(size):
	mc.setBlock(x+step+2, y+step, z+1, block.STAIRS_WOOD.id, 0)
	mc.setBlock(x+step+3, y+step, z+1, block.BEDROCK_INVISIBLE.id)
	mc.setBlock(x+step+2, y+step, z, block.STAIRS_WOOD.id, 0)
	mc.setBlock(x+step+3, y+step, z, block.BEDROCK_INVISIBLE.id)
