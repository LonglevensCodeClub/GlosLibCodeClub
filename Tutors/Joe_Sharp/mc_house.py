import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as vec3
import time
from HouseThread import HouseThread

# Set some constants
groundsSize = vec3.Vec3(8, 8, 10)
houseSize = vec3.Vec3(5, 3, 6)
countX = 5
countZ = 2
delay=0.3

## Clear a big space
mc = minecraft.Minecraft.create()
mc.setBlocks(-10, -10, -10,
			countX * groundsSize.x,
			groundsSize.y,
			countZ * groundsSize.z,
			block.AIR)

# Create houses
for x in range(countX):
	for z in range(countZ):
		thisHouseOrigin=vec3.Vec3((x * groundsSize.x), 0, (z * groundsSize.z))
		HouseThread(delay, thisHouseOrigin, groundsSize, houseSize).start()
		time.sleep(delay)
