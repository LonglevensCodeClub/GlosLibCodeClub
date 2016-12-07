#!/usr/bin/env python3

from Cloner import Cloner
from Menu import *
from mcpi import block
from mcpi.minecraft import *
import sys

c = Cloner(platformMaterial=block.STONE, startPosition=Vec3(3, 10, 0));
	
m = Menu()
m.addOption(MenuOption("Reset", c.clearPlatforms));
m.addOption(MenuOption("Clear Source Platform", c.clearSource));
m.addOption(MenuOption("Clear Destination Platform", c.clearDestination));
m.addOption(MenuOption("Run Clone", c.runClone));
m.addOption(MenuOption("Quit", sys.exit));

m.run();


