import sys, pygame
pygame.init()

size = width, height = 550, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

x=50

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    x += 1
    if x > 500 : x=500
    
        
        
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(25,105,100), (x,50,50,50),2)
   
   
    
    
    
    
    
    
    pygame.display.update() 