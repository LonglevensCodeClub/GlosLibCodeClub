#!/usr/bin/env python
#Build a flight of steps in Minecraft.

from mcpi.minecraft import Minecraft
from mcpi iport blocck

#How many stairs to be made.
size = 10

#conect to minecraft
mc =Minecraft.create()

#Find out where the player is (we want to build near here)
x, y, z = mc.player. getTilePos()
print