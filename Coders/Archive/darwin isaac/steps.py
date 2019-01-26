from mcpi.minecraft import minecraft
from mcpiimport block


size = 10


mc = minecraft.create()


x,y,z = mc.player.getTilepos()
print ("Making Steps at: " + str (x + 2) + ", " + str (z)
sdfq	q	


for step in range(size)
	 mc.setBlock(x+step+2, y+step,  z,  block.STAIRS_WOOD.id,0)
	 mc.setBlock(x+step+3, y+step, z, block.WOOD.id)      
	 
