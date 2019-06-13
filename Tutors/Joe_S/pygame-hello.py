import pygame, sys
from pygame.locals import *
 
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('Hello World!')


pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		pygame.display.update()
