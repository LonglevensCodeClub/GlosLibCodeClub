#!/usr/bin/env python3
from Dungeon import Dungeon

dungeon = Dungeon()
hallway = dungeon.create()
room2 = dungeon.newRoom(hallway, "D")
bedroom = dungeon.newRoom(hallway, "N")
bedroom2 = dungeon.newRoom(hallway, "W")
bedroom3 = dungeon.newRoom(bedroom, "E")
bedroom4 = dungeon.newRoom(bedroom3, "D")
room5 = dungeon.newRoom(bedroom4, "N")
room6 = dungeon.newRoom(room5, "W")
room7 = dungeon.newRoom(room6, "U")
