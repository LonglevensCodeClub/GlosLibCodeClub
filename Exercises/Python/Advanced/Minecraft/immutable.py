#!/usr/bin/env python3
from mcpi.minecraft import Minecraft

_mc = Minecraft.create()
_mc.setting("world_immutable", True)
