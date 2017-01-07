#!/usr/bin/env python3
import sys
sys.path.append("../")
from Maze import Maze
from mcpi import block
from mcpi.minecraft import *


myMaze = Maze(	cellCount=Vec3(8, 1, 8), 
				cellSize=3,
				wallMaterial=block.TNT);

d = myMaze.dig(Vec3(1, 0, 0));
d.doorLeft();
d.right(4);
d.forward(2);
d.left(2);
d.forward(3);
d.backward(1);
d.right(4);
d.forward(1);
d.right(1);
d.doorRight();
d._mc.setBlocks(11,0,11,11,15,11,block.TNT.id,1)
