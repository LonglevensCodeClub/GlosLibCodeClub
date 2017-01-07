from mcpi.minecraft import *
from mcpi import block
import math
import time

class Turtle:
    ###########################################################
    #
    # Move forwards
    #
    ###########################################################
	def forward(self, steps=1):
		for i in range(steps):
			self._position.x += self._size
			self.dig()
		return self;
		
    ###########################################################
    #
    # Move backwards
    #
    ###########################################################
	def backward(self, steps=1):
		for i in range(steps):
			self._position.x -= self._size
			self.dig()
		return self;
		   
	###########################################################
    #
    # Move up
    #
    ###########################################################
	def up(self, steps=1):
		for i in range(steps):
			self._position.y += self._size
			self.dig(allowFloor=False)
		return self;
		   
	###########################################################
    #
    # Move down
    #
    ###########################################################
	def down(self, steps=1):
		for i in range(steps):
			self._position.y -= self._size
			self.dig(allowCeiling=False)
		return self;
		   
	###########################################################
    #
    # Turn right
    #
    ###########################################################
	def right(self, steps=1):
		for i in range(steps):
			self._position.z += self._size
			self.dig()
		return self;
		   
	###########################################################
    #
    # Turn left
    #
    ###########################################################
	def left(self, steps=1):
		for i in range(steps):
			self._position.z -= self._size
			self.dig()
		return self;
		
	###########################################################
    #
    # Set the current material
    #
    ###########################################################
	def setMaterial(self, material):
		self._material = material;
		return self;
		
	###########################################################
    #
    # Set the ceiling material
    #
    ###########################################################
	def setCeilingMaterial(self, material):
		self._ceilingMaterial = material;
		self.replaceCeiling(material);
		return self;
		
	###########################################################
    #
    # Set the floor material
    #
    ###########################################################
	def setFloorMaterial(self, material):
		self._floorMaterial = material;
		self.replaceFloor(material);
		return self;
			
	def fork(self):
		clone = Turtle();
		clone._position = self._position.clone();
		clone._penMaterial = self._penMaterial;
		clone._floorMaterial = self._floorMaterial;
		clone._size = self._size;
		clone._material = self._material;
		clone._parent = self;
		return clone
		
	def replaceFloor(self, material):
		adjust = max(0, self._size - 1);
		self._mc.setBlocks(	self._position.x,
							self._position.y-1,
							self._position.z,
							self._position.x + adjust,
							self._position.y-1,
							self._position.z + adjust,
							material);
		return self;
		
	def replaceCeiling(self, material):
		adjust = max(0, self._size - 1);
		self._mc.setBlocks(	self._position.x,
							self._position.y+self._size,
							self._position.z,
							self._position.x + adjust,
							self._position.y+self._size,
							self._position.z + adjust,
							material);
		return self;
		
	def endFork(self):
		return self._parent;
			
	def dig(self, allowFloor=True, allowCeiling=True):
		adjust = max(0, self._size - 1);
		
		if (self._delay > 0):
			self._mc.setBlocks(
				self._position.x, 
				self._position.y, 
				self._position.z,
				self._position.x + adjust, 
				self._position.y + adjust, 
				self._position.z + adjust,
				self._penMaterial)
			time.sleep(self._delay);
		self._mc.setBlocks(
			self._position.x, 
			self._position.y, 
			self._position.z,
			self._position.x + adjust, 
			self._position.y + adjust, 
			self._position.z + adjust,
			self._material)
			
		if (allowCeiling and self._ceilingMaterial):
			self.replaceCeiling(self._ceilingMaterial);
			
		if (allowFloor and self._floorMaterial):
			self.replaceFloor(self._floorMaterial);
			
	def jump(self, position = Vec3(0, 0, 0)):
		self._position = position;
		
	def jumpAndDig(self, position = Vec3(0, 0, 0)):
		self.jump(position);
		self.dig();
		
	def doorForward(self):
		self._mc.setBlocks(
			self._position.x+self._size,
			self._position.y,
			self._position.z,
			self._position.x+self._size,
			self._position.y+1,
			self._position.z,
			block.AIR);
		
	def doorBackward(self):
		self._mc.setBlocks(
			self._position.x-1,
			self._position.y,
			self._position.z,
			self._position.x-1,
			self._position.y+1,
			self._position.z,
			block.AIR);
		
	def doorLeft(self):
		self._mc.setBlocks(
			self._position.x,
			self._position.y,
			self._position.z-1,
			self._position.x,
			self._position.y+1,
			self._position.z-1,
			block.AIR);
		
	def doorRight(self):
		self._mc.setBlocks(
			self._position.x+self._size-1,
			self._position.y,
			self._position.z+self._size,
			self._position.x+self._size-1,
			self._position.y+1,
			self._position.z+self._size,
			block.AIR);
		
	def __init__(self,
			mc=None,
			size=3, 
			material = block.STONE, 
			penMaterial = block.GLASS,
			ceilingMaterial = None,
			floorMaterial = None,
			delay=0.1,
			position=Vec3(0,0,0)):
		self._mc = mc if (mc) else Minecraft.create();
		self._material = material;
		self._size = size;
		self._material = material;
		self._penMaterial = penMaterial;
		self._ceilingMaterial = ceilingMaterial;
		self._floorMaterial = floorMaterial;
		self._delay = delay;
		self._parent = None;
		self._position = position;

