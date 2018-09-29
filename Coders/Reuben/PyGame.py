
import random, pygame, sys
from pygame.locals import *

FPS =  30 
WINDOWWIDTH = 640
WINFOWWIDTH = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE =10 
BOARDWIDTH = 10
BOARDHEIGHT = 7 
assert(BOARDWIDTH*BOARDHEIGHT)% 2 == 0, ' Board needs to have an even number of boxesfor pairs of matches.'
