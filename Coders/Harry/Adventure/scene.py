#!/usr/bin/env python3
###############################################################
#
# scene.py  (C) Steve Martin, @0x90_Bug
#
# Manage the Scenery for the Adventure Game.
#
###############################################################
from mcpi.minecraft import Minecraft
from mcpi import block
from random import randint

class Scene(object):

    ###########################################################
    #
    # Construct a House centered on coordinates x, y, z.
    # The house is 6 blocks deep and 7 blocks wide.
    # It has a secret dungeon created below it.
    #
    ###########################################################
    def __makeHouse(self, x, y, z):
        # Build the shell
        self.mc.setBlocks(x-2, y, z-3, x+3, y+2, z+3, block.BRICK_BLOCK.id)
        self.mc.setBlocks(x-1, y, z-2, x+2, y+2, z+2, block.AIR.id)

        # Add the roof
        self.mc.setBlocks(x-2, y+3, z-3, x-2, y+3, z+3, block.STAIRS_WOOD.id, 0)
        self.mc.setBlocks(x+3, y+3, z-3, x+3, y+3, z+3, block.STAIRS_WOOD.id, 1)
        self.mc.setBlocks(x-1, y+4, z-3, x-1, y+4, z+3, block.STAIRS_WOOD.id, 0)
        self.mc.setBlocks(x+2, y+4, z-3, x+2, y+4, z+3, block.STAIRS_WOOD.id, 1)
        self.mc.setBlocks(x, y+5, z-3, x, y+5, z+3, block.STAIRS_WOOD.id, 0)
        self.mc.setBlocks(x+1, y+5, z-3, x+1, y+5, z+3, block.STAIRS_WOOD.id, 1)

        # Fill in each end of the roof
        self.mc.setBlocks(x-1, y+3, z-3, x+2, y+3, z-3, block.BRICK_BLOCK.id)
        self.mc.setBlocks(x, y+4, z-3, x+1, y+4, z-3, block.BRICK_BLOCK.id)
        self.mc.setBlocks(x-1, y+3, z+3, x+2, y+3, z+3, block.BRICK_BLOCK.id)
        self.mc.setBlocks(x, y+4, z+3, x+1, y+4, z+3, block.BRICK_BLOCK.id)
    
        # Add doors and note where they are.
        self.mc.setBlock(x-2, y, z-1, block.DOOR_WOOD.id, 0)
        self.mc.setBlock(x-2, y+1, z-1, block.DOOR_WOOD.id, 8)
        dk = "x:" + str(x-2) + "z:" + str(z-1)
        self.doors[dk] = y
        self.doorDirection[dk] = 0
        self.mc.setBlock(x+3, y, z+1, block.DOOR_WOOD.id, 2)
        self.mc.setBlock(x+3, y+1, z+1, block.DOOR_WOOD.id, 10)
        dk = "x:" + str(x+3) + "z:" + str(z+1)
        self.doors[dk] = y
        self.doorDirection[dk] = 2

        # Add front and rear pathways.
        self.mc.setBlocks(x-3, y-1, z-1, x-4, y-1, z-1, block.STONE.id)
        self.mc.setBlocks(x+4, y-1, z+1, x+5, y-1, z+1, block.STONE.id)

        # Add Windows
        self.mc.setBlocks(x-2, y+1, z, x-2, y+1, z+1, block.GLASS.id)
        self.mc.setBlocks(x+3, y+1, z, x+3, y+1, z-1, block.GLASS.id)
        self.mc.setBlocks(x, y+1, z-3, x+1, y+1, z-3, block.GLASS.id)
        self.mc.setBlocks(x, y+1, z+3, x+1, y+1, z+3, block.GLASS.id)

        # Add a secret room
        self.mc.setBlocks(x-2, y-1, z-3, x+3, y-6, z+3, block.STONE.id)
        self.mc.setBlocks(x-1, y-2, z-2, x+2, y-4, z+2, block.AIR.id)
        self.mc.setBlocks(x, y-5, z-1, x+1, y-5, z+1, block.GLOWSTONE_BLOCK.id)

        # Make a note of the finish location
        self.endX1 = x-1
        self.endX2 = x+2
        self.endY1 = y-6
        self.endY2 = y-3
        self.endZ1 = z-2
        self.endZ2 = z+2


    ####################################################################
    #
    # Add a special block that will reveal a secret access when hit
    #
    #####################################################################
    def __addSpecial(self, x, y, z, code):
        sk = "x:" + str(x) + "y: " + str(y) + "z:" + str(z)
        # Place a block of magic Obsidian in the house and remeber where it is
        self.mc.setBlock(x, y, z, block.OBSIDIAN.id)
        self.special[sk] = code


    ###########################################################
    #
    # Create a clearing in front of the payer.
    #
    ###########################################################
    def __makePlateau(self, x, y, z):
        self.mc.setBlocks(x-4, y, z-2, x+12, 50, z+9, block.AIR.id)
        self.mc.setBlocks(x-4, y-1, z-2, x+12, -1, z+9, block.GRASS.id)
        self.mc.setBlocks(x-4, y-2, z-2, x+12, -20, z+9, block.DIRT.id)


    ###########################################################
    #
    # Initialise and create the overall scene
    #
    ###########################################################
    def __init__(self, mc):
        self.mc = mc
        self.doors = dict()
        self.doorDirection = dict()
        self.special = dict()
        self.endX1 = 0
        self.endX2 = 0
        self.endY1 = 0
        self.endY2 = 0
        self.endZ1 = 0
        self.endZ2 = 0

        # Stop the payer from changing the world.
        mc.setting("world_immutable", True)

        x, y, z = self.mc.player.getTilePos()

        # We need room in front of and beside the player so make sure we're not too near the edge.
        if z > 100:
            z = 100
        if x > 100:
            x = 100

        self.__makePlateau(x, y, z)
        self.__makeHouse(x+7, y, z+4)
        self.__addSpecial(x+7, y, z+4, "open-sesame")
        self.mc.player.setTilePos(x, y, z)


    ###########################################################
    #
    # Check if the location is a door that we want to control.
    #
    ###########################################################
    def isDoor(self, x, y, z):
        # Check whether or not the specified location matches that of a door
        dk = "x:" + str(x) + "z:" + str(z)
        if (dk in self.doors):
            return True
        return False


    ###########################################################
    #
    # Force a door closed to prevent the Player going through.
    #
    ###########################################################
    def closeDoor(self, x, y, z):
        dk = "x:" + str(x) + "z:" + str(z)
        if (dk in self.doors):
            dy = self.doors[dk]
            dd = self.doorDirection[dk]
            self.mc.setBlock(x, dy, z, block.DOOR_WOOD.id, dd)
            self.mc.setBlock(x, dy+1, z, block.DOOR_WOOD.id, dd+8)
 

    ###########################################################
    #
    # Check if the Player has got to the final location.
    #
    ###########################################################
    def hasReachedEnd(self, x, y, z):
        # Check whether or not the specified location is the end of the game
        if x > self.endX1 and x < self.endX2 and y > self.endY1 and y < self.endY2 and z > self.endZ1 and z < self.endZ2:
            return True
        return False


    ###########################################################
    #
    # Check if the location is a special block that we want to monitor.
    #
    ###########################################################
    def checkSpecial(self, x, y, z):
        sk = "x:" + str(x) + "y: " + str(y) + "z:" + str(z)
        if sk in self.special:
            code = self.special[sk]
            
            # We need to update the scene to account for this action.
            if code == "open-sesame":
                # Remove the special block
                self.mc.setBlock(x, y, z, block.AIR.id)

                # Create a ladder down to the Dungeon.
                # We can do this relative to where we placed the "special" block.
                self.mc.setBlock(x+2, y-1, z-2, block.AIR.id)
                self.mc.setBlocks(x+2, y, z-2, x+2, y-4, z-2, block.LADDER.id, 3)

            # Add handling for other special blocks here...
