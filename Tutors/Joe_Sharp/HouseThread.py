import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as vec3
import time
import threading

class HouseThread(threading.Thread):
	def __init__(self, delay, groundsOrigin, groundsSize, houseSize):
		super().__init__()
		self.mc = minecraft.Minecraft.create()
		self.delay = delay
		self.groundsOrigin = groundsOrigin
		self.groundsSize = groundsSize
		self.houseSize = houseSize
		
	def run(self):
		## Clear some space
		self.mc.setBlocks(self.groundsOrigin.x,
						  self.groundsOrigin.y,
						  self.groundsOrigin.z,
						  self.groundsOrigin.x + self.groundsSize.x - 1,
						  self.groundsOrigin.y + self.groundsSize.y - 1,
						  self.groundsOrigin.z + self.groundsSize.z - 1,
						  block.AIR)
						  
		# Create a floor
		floorOrigin = vec3.Vec3(self.groundsOrigin.x,
								self.groundsOrigin.y - 1, 
								self.groundsOrigin.z)
		self.mc.setBlocks(floorOrigin.x,
						  floorOrigin.y,
						  floorOrigin.z,
						  floorOrigin.x + self.groundsSize.x - 1,
						  floorOrigin.y,
						  floorOrigin.z + self.groundsSize.z - 1,
						  block.GRASS)
		time.sleep(self.delay)

		# Build a house
		houseOrigin = vec3.Vec3(self.groundsOrigin.x + 1, 
								self.groundsOrigin.y,
								self.groundsOrigin.z + 1)
		self.mc.setBlocks(houseOrigin.x,
						  houseOrigin.y,
						  houseOrigin.z,
						  houseOrigin.x + self.houseSize.x - 1,
						  houseOrigin.y + self.houseSize.y - 1,
						  houseOrigin.z + self.houseSize.z - 1,
						  block.WOOD_PLANKS)
		time.sleep(self.delay)
		
		# Carve out house interior
		houseInteriorOrigin = vec3.Vec3(houseOrigin.x + 1,
										houseOrigin.y,
										houseOrigin.z + 1)
		self.mc.setBlocks(houseInteriorOrigin.x,
						  houseInteriorOrigin.y,
						  houseInteriorOrigin.z,
						  houseInteriorOrigin.x + self.houseSize.x - 3,
						  houseInteriorOrigin.y + self.houseSize.y - 1,
						  houseInteriorOrigin.z + self.houseSize.z - 3,
						  block.AIR)
		time.sleep(self.delay)

		# Carve out door
		houseDoorOrigin = vec3.Vec3(houseOrigin.x + 2, 
									houseOrigin.y, 
									houseOrigin.z)
		self.mc.setBlocks(houseDoorOrigin.x,
						  houseDoorOrigin.y,
						  houseDoorOrigin.z,
						  houseDoorOrigin.x,
						  houseDoorOrigin.y + 1,
						  houseDoorOrigin.z,
						  block.AIR)
		time.sleep(self.delay)

		# Put a roof on
		roofOrigin = vec3.Vec3(houseOrigin.x,
							   houseOrigin.y + self.houseSize.y,
							   houseOrigin.z)
		self.mc.setBlocks(roofOrigin.x,
						  roofOrigin.y,
						  roofOrigin.z,
						  roofOrigin.x + self.houseSize.x - 1,
						  roofOrigin.y,
						  roofOrigin.z + self.houseSize.z - 1,
						  block.GRASS)
		time.sleep(self.delay)
		
		self.mc.setBlock(self.groundsOrigin.x,
						 self.groundsOrigin.y, 
						 self.groundsOrigin.z, 
						 block.OBSIDIAN)

