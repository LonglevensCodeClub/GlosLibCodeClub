#!/usr/bin/python
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
mc.postToChat("Hello world")

x, y, z = mc.player.getPos()
mc.setBlocks(x+10,y,z+10,x+1,y+11,z+1,46,1)
