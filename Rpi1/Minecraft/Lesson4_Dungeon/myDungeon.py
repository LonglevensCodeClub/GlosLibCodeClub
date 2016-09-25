#!/usr/bin/env python3
from Dungeon import Dungeon

dungeon = Dungeon()
entrance = dungeon.create()
room1 = dungeon.newRoom(entrance, "N")
room2 = dungeon.newRoom(room1, "N")
room3 = dungeon.newRoom(room2, "D")
room4 = dungeon.newRoom(room3, "S")
room5 = dungeon.newRoom(room4, "W")
room6 = dungeon.newRoom(room5, "E")
room7 = dungeon.newRoom(room6, "U")
room8 = dungeon.newRoom(room7, "U")
room9 = dungeon.newRoom(room8, "S")
room10 = dungeon.newRoom(room9, "D")
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
