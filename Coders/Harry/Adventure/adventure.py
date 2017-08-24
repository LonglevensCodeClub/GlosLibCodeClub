#!/usr/bin/env python3
###############################################################
#
# adventure.py  (C) Steve Martin, @0x90_Bug
#
# This is the main Minecraft Adventure Game
#
###############################################################

import sys
from artifacts import Artifacts
from scene import Scene
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

# The number of flowers that we have collected
mushroomsCollected = 0	

# Create our Adventure Scene
mc = Minecraft.create()
scene = Scene(mc)

# Scatter 20 flowers near the player.
artifacts = Artifacts(mc)
px, py, pz = mc.player.getTilePos()
artifacts.scatterItems(px-20, pz-20, px+20, pz+20, 20, block.MUSHROOM_RED.id)	

# Greet the Player and give them instructions.
mc.postToChat("Welcome to our Minecraft Adventure!")
mc.postToChat("Your mission is to find the secret Dungeon.")

lastPX, lastPY, lastPZ = mc.player.getTilePos()

# Now we're going to monitor the player's position as they move around.
while True:
    sleep(0.3) # We don't want to hog all the CPU
    px, py, pz = mc.player.getTilePos()

    # If the player is in the secret Dungeon, then their mission is complete.
    if scene.hasReachedEnd(px, py, pz):
        mc.postToChat("Well done! You have found the secret Dungeon You are a genius!")
        sys.exit()

    # If The player has found an item, collect it
    if artifacts.atLocation(px, pz) == block.MUSHROOM_RED.id:
        mc.postToChat("You have collected a mushroom.")
        mushroomsCollected += 1

    # Check to see if the player has hit any blocks
    blockEvents = mc.events.pollBlockHits()
    for blockEvent in blockEvents:
        # Yes, check to see if it was a "special" block.
        eventX, eventY, eventZ = blockEvent.pos
        scene.checkSpecial(eventX, eventY, eventZ)

        # Check to see if it was a door...
        if scene.isDoor(eventX, eventY, eventZ):
            # If so, check that they are allowed through...
            if(mushroomsCollected < 10):
                # If not, force the door closed!
                scene.closeDoor(eventX, eventY, eventZ)
                mc.postToChat("You must collect ten mushrooms before entering.")
                # And force the Player back to where they just were.
                mc.player.setTilePos(lastPX, lastPY, lastPZ)

    lastPX, lastPY, lastPZ = mc.player.getTilePos()
 


##################################################
#
#  Exercises:
#
# 1. Can you change the number of flowers to be collected ?
#
# 2. Can you tell the player how many flowers they have collected each time they find a new one ?
#
# 3. Can you change the item that has to be collected ?
#
# 4. Can you add an extra element to the adventure game ?
#    Here are some ideas:
#        A "poisened" flower that if collected results in something bad happening,
#            for example the player being sent to a well.
#        A second house that must be visited first to obtain a item before the
#            player can open the door to the house with the dungeon below it.
#        A "special" block that must be hit before the player is able to access
#            the next part of the game.
#
