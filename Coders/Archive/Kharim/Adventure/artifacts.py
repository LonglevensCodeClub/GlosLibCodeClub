#!/usr/bin/env python3
###############################################################
#
# artifacts.py  (C) Steve Martin, @0x90_Bug
#
# Manage a register of artifacts within the Adventure Game.
#
###############################################################
from mcpi.minecraft import Minecraft
from mcpi import block
from random import randint

class Artifacts(object):

    def __init__(self, mc):
        self.mc = mc
        self.artifacts = dict()


    def addItem(self, x, z, type):
        ak = "x:" + str(x) + "z:" + str(z)
        y = self.mc.getHeight(x, z)
        base = self.mc.getBlock(x, y-1, z)

        # We don't want to put an item water is water.
        if base == block.WATER.id:
            raise Exception("Can't place item over water!")

        # We want to make sure the World is clear at the specified location
        if self.mc.getBlock(x, y+1, z) != block.AIR.id:
            raise Exception("There is another Minecraft item at that location.")

        # We don't want to put an item where there is something already.
        if ak in self.artifacts:
            raise Exception("Artifact already present at that location.")

        self.mc.setBlock(x, y, z, type)
        self.artifacts[ak] = type
 

    def scatterItems(self, minX, minZ, maxX, maxZ, quantity, type):
        done = 0
        while(done < quantity):
            x = randint(minX, maxX)
            z = randint(minZ, maxZ)
            try:
                self.addItem(x, z, type)
                done += 1
            except Exception as e:
                # For some reason that was a bad location
                print(str(e))
                pass


    def atLocation(self, x, z):
        ak = "x:" + str(x) + "z:" + str(z)
        if ak in self.artifacts:
            y = self.mc.getHeight(x, z)
            self.mc.setBlock(x, y, z, block.AIR.id)
            artifact = self.artifacts[ak]
            del self.artifacts[ak]
            return artifact
        return None

