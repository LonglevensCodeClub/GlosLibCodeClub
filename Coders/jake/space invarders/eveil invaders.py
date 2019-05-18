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
                aliens[a].image = "alien1"
            else:
                aliens[a].image = "alien1B"
        movesequence +=1
        if movesequnce == 40: movesequnce = 0
        
        def drawClipped(sel):
            screen.surface.blit(self._surf, (self.x-32, self.y-self.height+30),(0,0,64,self.hight))
            
        def initBases():
            global bases
            bases = []
            bc = 0
            for b in range(3):
                for p in range(3):
                    bases.append(Actor("base1". midbottom=(150+(b*200)+(p*40),520)))
                    bases[bc].drawclipped = drawclipped._get_(bases[bc])
                    bases[bc].height = 60
                    bc +=1
                    
            def drawbases():
                for b in range(len(bases)): bases[b].drawclipped()
                
            def checkKeys():
                global player, lasers
                if keyboard.space:
                    1 = len(lasers)
                    lasers.append(actor("laser2", (player.x,player.y-32)))
                    lasers[1].status = 0
                    lasers[1].type = 1
                    
            def drawlasers():
                for 1 in range(len(lasers)): lasers[1].draw()
                
            def updateLasers():
                global lasers, aliens
                for 1 in range(len(lasers)):
                    if lasers[1].type == 0:
                        lasers[1].y += (2*DIFFICULTY)
                        checklaserHit(1)
                        if lasers[1].type == 0:
                            lasers[1].y -= 5
                    checkPlayerLaserHit(1)
                    if lasers[1].y<10: lasers[1].status = 1
               lasers = listcleanup(lasers)
               aliens = listcleanup(aliens)
               
            def init():
                global lasers, score, player, moveseaqunce, movecounter, movedelay
                initAliens()
                initBases()
                movecounter = movesequnc = player.status = score = player.lasercountdown = 0
                
                    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        

pgzrun.go()            


