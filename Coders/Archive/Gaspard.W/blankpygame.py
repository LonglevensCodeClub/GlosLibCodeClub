import pygame, sys
from pygame.locals import *
from time import sleep

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1440, 1040))
pygame.display.set_caption("OI, YOU!")
sleep(2)
pygame.display.set_caption("YES, YOU!")
sleep(2)
pygame.display.set_caption("I proudly present:")
sleep(2)
pygame.display.set_caption("[drum roll]")
sleep(2)
pygame.display.set_caption("The World's Most Boring Video Game!")
sleep(2)
pygame.display.set_caption("Actually no, it's not a video game.")
sleep(2)
pygame.display.set_caption("ITSA BLACK WINDOW!")
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
