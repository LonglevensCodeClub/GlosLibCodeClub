## https://www.raspberrypi.org/magpi/pygame-zero-invaders/
import pgzrun

player = Actor("player", (400,550))

def draw():
    screen.blit('background',(0, 0))
    player.draw()
    
def update():
    checkKeys()
    
def checkKeys():
    global player
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 760: player.x += 5
        
        
def updateAliens():
    global moveSequence, movedelay
    movex = movey = 0
    if movesequence < 10 or movesequence > 30: movex = -15
    if movesequence == 10 or movesequence == 30:
        movey = 50
    if movesequence >10 and movesequence < 30: movex =15
    for a in range(len(aliens)): 
        animate(aliens[a],
                pos=(aliens[a].x + movex,
                     aliens[a].y + movey),
                duration=0.5, tween='linear')
        if randint(0, 1) == 0:
            aliens[a].image = "alien1"
    
        else:
            aliens[a].image = "alien1b"
    moveseqence +=1
    if moveseqence == 40: moveseqence = 0
    
    def updateAliens():
        global moveseaqence , moveDelay
        movex = movey = 0
        if movesequence < 10 or movesequnce >30: movex = -15
        if movesequnce == 10 or movesequnce == 30:
            movey = 50
        if movesequnce >10 and movesequnce < 30: movex = 15
        for a in range(len(aliens)):
            animate(aliens[a], pos=(alien.x + movex, aliens[a].y + movey), duration=0.5,
                    tween='linear')
            if randint(0, 1) == 0:                                                                

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        

pgzrun.go()            


