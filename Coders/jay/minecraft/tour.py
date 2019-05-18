# Connect to minecraft
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
import time


#set xyz
x=10.0
y=210.0
z=12.0

#change position
mc.player.setTilePos(x,y,z)

#wait 10 seconds
time.sleep(10)
#set xyz
x=10

y=10
z=12.0

#change position
mc.player.setTilePos(x,y,z)



