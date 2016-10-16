from mcpi.minecraft import Minecraft
import mcpi.block as block
import random
import time

mc = Minecraft.create()

x, y, z = mc.player.getPos()
mc.setBlocks(x,
			 y,
			 z,
			 x+10000,
			 y+10000,
			 z+100000,
			 46, 1)
class Canvas:        
    def __init__(self):
        self.x, self.y, self.z = mc.player.getPos()
        self.data = []
        self.halfWidth = 14
        self.width = self.halfWidth * 2
        self.height = 20
        self.margin = 5
        self.backMaterial = block.STONE
        self.canvasDistance = 20
        self.canvasZ = self.z - self.canvasDistance - 1
        self.drawZ = self.canvasZ + 1
        
        # Clear a large area
        mc.setBlocks(self.x - self.halfWidth - self.margin,
                     self.y,
                     self.z,
                     self.x + self.halfWidth + self.margin,
                     self.y + self.height + self.margin,
                     self.canvasZ,
                     block.AIR)

        # Draw the canvas
        mc.setBlocks(self.x - self.halfWidth,
                     self.y,
                     self.canvasZ,
                     self.x + self.halfWidth,
                     self.y + self.height,
                     self.canvasZ,
                     self.backMaterial)
        
    def drawDot(self, x, y, material):
        mc.setBlock(self.x - self.halfWidth + x,
                    self.y + y,
                    self.drawZ,
                    material);
        
    def clearCanvas(self):
        mc.setBlocks(self.x - self.halfWidth,
                     self.y,
                     self.drawZ,
                     self.x + self.halfWidth,
                     self.y + self.height,
                     self.drawZ,
                     block.AIR)
        
    def clearDot(self, x, y):
        self.drawDot(x, y, block.AIR)

    def drawColumns(self, data, material):
        self.clearCanvas()
        x=0
        for y in data:
            mc.setBlocks(self.x - self.halfWidth + x,
                         self.y,
                         self.drawZ,
                         self.x - self.halfWidth + x,
                         self.y + y,
                         self.drawZ,
                         material, 1)
            x += 1
                    

#myCanvas = Canvas()
#myData = random.sample(range(0, myCanvas.height), 20)

#for top in reversed(range(0, len(myData))):
#    for current in range(0, top):
#        if (myData[current] > myData[current + 1]):
#            swap = myData[current]
#            myData[current] = myData[current+1]
#            myData[current+1] = swap
#        myCanvas.drawColumns(myData,46)
#        time.sleep(0.05)
