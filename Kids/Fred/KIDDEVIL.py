# kid devil.
from tkinter import *

def playgame(death, biome):
	if death:
		print("Survival Mode")
	else:
		print("Creative Mode")
		
		
	if biome:
		print("grass")
	else:
		print("sea")
		






print('kid devil')
gamego = input("Enter a number between 1 and 5:")
#gamegoNum = int(gamego)
if gamego == "1":
	print("you chose gamemode 1!")
	playgame(death=True, biome=True)
elif gamego == "2":
	print("you chose gamemode 2!")
	playgame(death=False, biome=True)
elif gamego == "3":
	print("you chose gamemode 3!")
	playgame(death=True, biome=False)
elif gamego == "4":
	print("you chose gamemode 4!")
elif gamego == "5":
	print("you chose gamemode 5!")
else:
	print("INVALID SYNTAX")
	
	
	
