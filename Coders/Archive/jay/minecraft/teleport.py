# Connect to minecraft
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
import time


#set xyz
x=10.0
y=210.0
z=12.0

#change position
mc.player.setPos(x,y,z)


