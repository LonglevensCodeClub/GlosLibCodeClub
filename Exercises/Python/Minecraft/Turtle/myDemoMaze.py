#!/usr/bin/env python3
from Maze import Maze
from mcpi import block
from mcpi.minecraft import *

myMaze = Maze(cellCount=Vec3(5, 1, 5), cellSize=3);

d = myMaze.dig(Vec3(1, 0, 0));
d.doorLeft();
d.right(4);
d.doorRight();
d.backward();
d.doorBackward();

