from mcpi.minecraft import Minecraft
from mcpi import block
import DungeonError

class Dungeon:
    _mc = Minecraft.create()
    _rooms = {}
    _MIN_X = -10
    _MIN_Y = -30
    _MIN_Z = -80
    _MAX_X = 120
    _MAX_Y = -12
    _MAX_Z = 80
    _ROOM_WIDTH = 10
    _ROOM_LENGTH = 10
    _ROOM_HEIGHT = 4

    ###########################################################
    #
    # Construct a room with the given dimensions. Place torches
    # around the walls, optionally put a random piece of
    # treasure in the room.
    #
    ###########################################################
    def MakeRoom(self, x1, y1, z1, x2, y2, z2):
        # Plot the room itself
        self._mc.setBlocks(x1, y1, z1, x2, y2, z2, block.AIR.id)

        # Determine height of torch
        th = min([y1, y2]) + 2

        # Place torches along each wall.
        for i in range(x1+1, x2-1):
            if i % 6 == 0 and (self._mc.getBlock(i, th, z1-1) != block.AIR):
                self._mc.setBlock(i, th, z1, block.TORCH)
            if i % 6 == 0 and (self._mc.getBlock(i, th, z2+1) != block.AIR):
                self._mc.setBlock(i, th, z2, block.TORCH)
        for i in range(z1+1, z2-1):
            if i % 6 == 0 and (self._mc.getBlock(x1-1, th, i) != block.AIR):
                self._mc.setBlock(x1, th, i, block.TORCH)
            if i % 6 == 0 and (self._mc.getBlock(x2+1, th, i) != block.AIR):
                self._mc.setBlock(x2, th, i, block.TORCH)


    ###########################################################
    #
    # Construct a flight of steps going downwards. The steps
    # must go through water so must include walls and ceiling.
    #
    ############################################################
    def MakeSteps(self, x, y, z, l):
        for step in range(l+1):
            # Floor steps
            self._mc.setBlock(x+step, y-step, z-1, block.STAIRS_COBBLESTONE.id, 1)
            self._mc.setBlock(x+step, y-step, z, block.STAIRS_COBBLESTONE.id, 1)
            self._mc.setBlock(x+step, y-step, z+1, block.STAIRS_COBBLESTONE.id, 1)
            # Ceiling steps
            self._mc.setBlock(x+step, y-step+4, z-1, block.STAIRS_COBBLESTONE.id, 4)
            self._mc.setBlock(x+step, y-step+4, z, block.STAIRS_COBBLESTONE.id, 4)
            self._mc.setBlock(x+step, y-step+4, z+1, block.STAIRS_COBBLESTONE.id, 4)
            # Sidewalls
            self._mc.setBlocks(x+step, y-step, z-2, x+step, y-step+self._ROOM_HEIGHT, z-2, block.STONE)
            self._mc.setBlocks(x+step, y-step, z+2, x+step, y-step+self._ROOM_HEIGHT, z+2, block.STONE)
            # Ensure that nothing is in the void.
            self._mc.setBlocks(x+step, y-step+1, z-1, x+step, y-step+3, z+1, block.AIR)

    ###########################################################
    #
    # Construct a flight of steps going downwards to join rooms.
    #
    ############################################################
    def StepsDown(self, x, y, z):
        self._mc.setBlocks(x+3, y, z-1, x+self._ROOM_HEIGHT+4, y, z-1, block.FENCE)
        self._mc.setBlocks(x+3, y, z+1, x+self._ROOM_HEIGHT+4, y, z+1, block.FENCE)
        self._mc.setBlocks(x+self._ROOM_HEIGHT+4, y, z-1, x+self._ROOM_HEIGHT+4, y, z+1, block.FENCE)
        for step in range(1, self._ROOM_HEIGHT+3):
            # Floor steps
            self._mc.setBlock(x+step, y-step, z, block.STAIRS_COBBLESTONE.id, 1)
            # Space to walk
            self._mc.setBlocks(x+step+1, y-step, z, x+self._ROOM_HEIGHT+3, y-step, z, block.AIR)

    ############################################################
    #
    # Construct a new room.
    #
    ############################################################
    def newRoom(self, start, direction):
        handle = len(self._rooms)
        if direction.upper() not in ["N", "S", "E", "W", "U", "D"]:
            raise DungeonError.DirectionError("Direction must be: \"N\", \"S\", \"E\", \"W\", \"U\" or \"D\"")
        else:
            if start not in self._rooms:
                raise DungeonError.RoomError("Unknown room: " + str(start))
            else:
                x, y, z = self._rooms[start]
                if (direction.upper() == "N"):
                    x += self._ROOM_LENGTH+2
                elif (direction.upper() == "S"):
                    x -= self._ROOM_LENGTH+2
                elif (direction.upper() == "E"):
                    z += self._ROOM_WIDTH+2
                elif (direction.upper() == "W"):
                    z -= self._ROOM_WIDTH+2
                elif (direction.upper() == "U"):
                    y += self._ROOM_HEIGHT+2
                else:
					y -= self._ROOM_HEIGHT+2
                if (x > self._MAX_X-self._ROOM_LENGTH
                 or x < self._MIN_X
                 or z < self._MIN_Z
                 or x > self._MAX_Z-self._ROOM_WIDTH
                 or y > self._MAX_Y
                 or y < self._MIN_Y):
                    raise DungeonError.RoomError("Not enough space in direction \"" + direction + "\" from room " + str(start))
                else:
					if (self._mc.getBlock(x+1, y, z+2) == block.AIR.id):
						raise DungeonError.RoomError("There is already a room in direction \"" + direction + "\" from room " + str(start))
					else:
						self.MakeRoom(x, y, z, x+self._ROOM_LENGTH, y+self._ROOM_HEIGHT, z+self._ROOM_WIDTH)
						self._rooms[handle] = [x, y, z]
						# Create the ajoining corridore or steps
						if (direction.upper() == "N"):
							self._mc.setBlocks(x-2, y, z+self._ROOM_WIDTH/2, x, y+1, z+self._ROOM_WIDTH/2, block.AIR)
						elif (direction.upper() == "S"):
							self._mc.setBlocks(x+self._ROOM_LENGTH, y, z+self._ROOM_WIDTH/2, x+self._ROOM_LENGTH+2, y+1, z+self._ROOM_WIDTH/2, block.AIR)
						elif (direction.upper() == "E"):
							self._mc.setBlocks(x+self._ROOM_LENGTH/2, y, z-2, x+self._ROOM_LENGTH/2, y+1, z, block.AIR)
						elif (direction.upper() == "W"):
							self._mc.setBlocks(x+self._ROOM_LENGTH/2, y, z+self._ROOM_WIDTH, x+self._ROOM_LENGTH/2, y+1, z+self._ROOM_WIDTH+2, block.AIR)
						elif (direction.upper() == "U"):
							self.StepsDown(x+1, y, z+2)
						else:
							self.StepsDown(x+1, y+self._ROOM_HEIGHT+2, z+2)
        return handle


    def __init__(self):
        # Create a large underwater block of stone for the dungeon.
        self._mc.setBlocks(self._MIN_X, -4, self._MIN_Z, self._MAX_X, -30, self._MAX_Z, block.STONE)
        self._mc.setBlocks(self._MIN_X-2, 0, self._MIN_Z-2, self._MAX_X+2, -3, self._MAX_Z+2, block.WATER_STATIONARY)
        self._mc.setBlocks(self._MIN_X-4, 0, self._MIN_Z-4, self._MAX_X+4, 30, self._MAX_Z+4, block.AIR)

        # Create external plinth for player to stand on
        self._mc.setBlocks(-6, 0, -5, 0, -3, 5, block.STONE)


    def create(self):
        # Create a dungeon as the start point
        self.MakeRoom(10, -12, -5, 20, -8, 5)
        self._rooms[0] = [10, -12, -5]

        # Place some steps down into the dungeon.
        self.MakeSteps(1, 0, 0, 12)

        # Put the playr near the dungeon entrance.
        self._mc.player.setPos(-2, 1, 0)
        self._mc.setting("world_immutable", True)
        return 0
