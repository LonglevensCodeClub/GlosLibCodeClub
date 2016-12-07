from mcpi.minecraft import *
from mcpi import block
from Turtle import Turtle

class Maze:
	def dig(self, cellCoordinate = Vec3(0, 0, 0)):
		cellPosition = Vec3(cellCoordinate.x * self._cellSize,
			cellCoordinate.y * self._cellSize,
			cellCoordinate.z * self._cellSize);
		self._turtle.jumpAndDig(cellPosition);
		
		return self._turtle;
		
	def __init__(self, 
			emptyMaterial = block.AIR,
			floorMaterial = block.STONE_BRICK,
			wallMaterial = block.MOSS_STONE,
			ceilingMaterial = block.AIR,
			carvingMaterial = block.AIR,
			penMaterial = block.GOLD_BLOCK,
			delay=0.1,
			cellSize=3,
			cellCount=Vec3(5, 1, 5),
			withRoof = False):
		mc = Minecraft.create();
		self._mc = mc;
		self._cellSize = cellSize;
		self._turtle = Turtle(
			material=carvingMaterial, 
			penMaterial=penMaterial,
			ceilingMaterial=ceilingMaterial,
			floorMaterial=floorMaterial,
			size=cellSize, 
			delay=delay,
			mc=mc,
			position=Vec3(0, 0, 0)
			);
			
		# account for wall
		margin = cellSize + 1; 
		clearSize = Vec3(cellCount.x * cellSize,
			cellCount.y * cellSize,
			cellCount.z * cellSize);
			
		# Empty out a large space
		self._mc.setBlocks( 0 - margin, 
							-10, 
							0 - margin,
							clearSize.x + margin, 
							clearSize.y + margin, 
							clearSize.z + margin,
							emptyMaterial);
		# Build a floor
		self._mc.setBlocks( 0 - margin, 
							-10, 
							0 - margin,
							clearSize.x + margin, 
							-1, 
							clearSize.z + margin,
							floorMaterial);
					
		# Build the block out of which the maze will be carved					
		self._mc.setBlocks( -1, 
							0, 
							-1,
							clearSize.x, 
							clearSize.y, 
							clearSize.z,
							wallMaterial);
			
		# Build a roof				
		self._mc.setBlocks( -1, 
							clearSize.y, 
							-1,
							clearSize.x, 
							clearSize.y, 
							clearSize.z,
							ceilingMaterial);

		# Place the player some way away on a plinth
		self._mc.setBlock(- math.floor(clearSize.x / 2), 
			margin * 3,
			0,
			block.STONE);
		self._mc.player.setTilePos( - math.floor(clearSize.x / 2), 
									margin * 5, 
									0);
