from mcpi.minecraft import *
from mcpi import block
import time

class Cloner:
	def __init__(self,
		startPosition=Vec3(0, 0, 0),
		platformSize=Vec3(5, 1, 5),
		translate=Vec3(7, 0, 0),
		platformMaterial=block.GRASS,
		penMaterial=block.GLASS,
		height=4,
		delay=0.1
		):
		self._mc = Minecraft.create();
		self._startPosition = startPosition;
		self._platformSize = platformSize;
		self._translate = translate;
		self._platformMaterial = platformMaterial;
		self._penMaterial = penMaterial;
		self._height = height;
		self._delay=delay;
		
	def runClone(self):
		self._mc.postToChat("Running Clone Operation")
		startX = self._startPosition.x;
		endX = self._startPosition.x + self._platformSize.x + 1;
		startY = self._startPosition.y + self._platformSize.y + 1;
		endY = self._startPosition.y + self._platformSize.y + self._height;
		startZ = self._startPosition.z;
		endZ = self._startPosition.z + self._platformSize.z + 1;
			
		for x in range(startX, endX):
			for y in range(startY, endY):
				for z in range(startZ, endZ):
					src = self._mc.getBlock(x, y, z)
					dest = self._mc.getBlock(	x + self._translate.x,
												y + self._translate.y,
												z + self._translate.z);
					# Put the pen there
					self._mc.setBlock(x, y , z, self._penMaterial);
					self._mc.setBlock(	x + self._translate.x,
											y + self._translate.y,
											z + self._translate.z,
											self._penMaterial);
					time.sleep(self._delay);
					if (src != dest):
						self._mc.setBlock(	x + self._translate.x,
											y + self._translate.y,
											z + self._translate.z,
											src);
					else:
						self._mc.setBlock(	x + self._translate.x,
											y + self._translate.y,
											z + self._translate.z,
											block.AIR);
						
					self._mc.setBlock(x, y , z, src);
		
	def clearSource(self):
		self._mc.postToChat("Clearing Source Platform")
		# Clear Source (with height)
		self._mc.setBlocks(
			self._startPosition.x,
			self._startPosition.y,
			self._startPosition.z,
			self._startPosition.x + self._platformSize.x,
			self._startPosition.y + self._platformSize.y + self._height,
			self._startPosition.z + self._platformSize.z,
			block.AIR);

		# Make Source
		self._mc.setBlocks(
			self._startPosition.x,
			self._startPosition.y,
			self._startPosition.z,
			self._startPosition.x + self._platformSize.x,
			self._startPosition.y + self._platformSize.y,
			self._startPosition.z + self._platformSize.z,
			self._platformMaterial);
		
	def clearDestination(self):
		self._mc.postToChat("Clearing Destination Platform")
		## Calculate origin for dest
		destStart = Vec3(	self._startPosition.x + self._translate.x,
							self._startPosition.y + self._translate.y,
							self._startPosition.z + self._translate.z);
		
		# Clear Destination
		self._mc.setBlocks(
			destStart.x,
			destStart.y,
			destStart.z,
			destStart.x + self._platformSize.x,
			destStart.y + self._platformSize.y + self._height,
			destStart.z + self._platformSize.z,
			block.AIR);
		
		# Make Destination
		self._mc.setBlocks(
			destStart.x,
			destStart.y,
			destStart.z,
			destStart.x + self._platformSize.x,
			destStart.y + self._platformSize.y,
			destStart.z + self._platformSize.z,
			self._platformMaterial);

		
	def clearPlatforms(self):
		self._mc.postToChat("Creating Both Platforms at " + str(self._startPosition))
	
		self.clearSource();
		self.clearDestination();
