#!/usr/bin/env python3
from Dungeon import Dungeon

dungeon = Dungeon()
entrance = dungeon.create()
room1 = dungeon.newRoom(entrance, "N")

# Create more rooms by adding more "dungeon.newRoom(room, direction)"
# like the line below. "room" must be a room that you've already created.
# "direction" must be one of:
#    "N" - North
#    "S" - South
#    "E" - East
#    "W" - West
#    "U" - Up (above)
#    "D" - Down (below)
# Create one or two more rooms, then explore you dungeon to make sure
# that it is as you expect, then create more rooms.
