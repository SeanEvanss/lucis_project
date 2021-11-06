import pygame,sys
import pytmx
from pytmx import load_pygame
from pygame.locals import*

pygame.init()

pygame.mixer.music.load("BWOAH.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)


pygame.key.set_repeat(10,50)



FPS=30
fpsClock= pygame.time.Clock()

DISPLAY= pygame.display.set_mode((800,400))
pygame.display.set_caption('First alpha')
WHITE=(255,255,255)
BLACK=(0,0,0)

gameMap=load_pygame("Dungeon01.tmx")


def load_image(name):
    image = pygame.image.load(name)
    return image
    #This function is universally neccesary to properly manipulate an image within a program



#to utilise the tmx file we must first turn the pixels into a form we can manipulate





class Animation():
    def __init__(self, maxFrame):
        self.maxFrame=maxFrame
        self.currentSprite=0
        self.maxFrame= maxFrame
        self.filmFrame=[]
        
        
    def addFrame(self,index,img):
        self.img=img
        self.index=index
        self.filmFrame.append(load_image(self.img))

        

    def update(self):
        
        if(len(self.filmFrame)>1):
        
            
            if(self.currentSprite >= (len(self.filmFrame)-1)):
            
                self.currentSprite=0
            elif(self.currentSprite < len(self.filmFrame)):
           
                self.currentSprite += 1
                
    def getImage(self):
        if(len(self.filmFrame)!=0):
            return self.filmFrame[self.currentSprite]
            
        
        
LucisRight= Animation(3)
LucisRight.addFrame(0,'Lucis Right Normal.png')
LucisRight.addFrame(1,'Lucis Right Walk 1.png')
LucisRight.addFrame(2,'Lucis Right Walk 2.png')

        
LucisFront= Animation(3)
LucisFront.addFrame(0,'Lucis Front Normal.png')
LucisFront.addFrame(1,'Lucis Front Walk 1.png')
LucisFront.addFrame(2,'Lucis Front Walk 2.png')

        
LucisLeft= Animation(3)
LucisLeft.addFrame(0,'Lucis Left Normal.png')
LucisLeft.addFrame(1,'Lucis Left Walk 1.png')
LucisLeft.addFrame(2,'Lucis Left Walk 2.png')

        
LucisBack= Animation(3)
LucisBack.addFrame(0,'Lucis Back Normal.png')
LucisBack.addFrame(1,'Lucis Back Walk 1.png')
LucisBack.addFrame(2,'Lucis Back Walk 2.png')



catX= 50
catY= 50

speedX=8
speedY=8

leftLimit=70
rightLimit=400


CurrentImg= LucisRight.getImage()

while True:
    DISPLAY.fill(BLACK)
   
    

    images=[]

    for y in range(6):
        for x in range(11):
            currentTileImage = gameMap.get_tile_image(x,y,0)
            images.append(currentTileImage)
        
    i = 0

    
        for y in range(6):
            for x in range(11):
                DISPLAY.blit(images[i],(x*64,y*64))

                i += 1

            
    

    DISPLAY.blit(CurrentImg,(catX,catY))
     
    for event in pygame.event.get():
        if event.type== QUIT:
            
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            
            if event.key in(K_UP,K_w):
                
                if catY<=0:
                    CurrentImg= LucisBack.filmFrame[0]
                    speedY=0
                    catY=0
                    
                catY -= speedY
                CurrentImg= LucisBack.getImage()    
                
            elif event.key in(K_DOWN,K_s):
                
                if catY>=320:
                    CurrentImg= LucisFront.filmFrame[0]
                    speedY=0
                    catY=320

                catY +=speedY
                CurrentImg= LucisFront.getImage()
                
            elif event.key in(K_LEFT,K_a):
                
                if catX<=0:
                    CurrentImg= LucisLeft.filmFrame[0]
                    speedX=0
                    catX=0
                    

                catX -= speedX
                CurrentImg= LucisLeft.getImage()    
                
            elif event.key in(K_RIGHT,K_d):
                
                if catX>=900:
                    CurrentImg= LucisRight.filmFrame[0]
                    speedX=0
                    catX=900

                catX +=speedX
                CurrentImg= LucisRight.getImage()

        elif event.type == KEYUP:
            if event.key in(K_UP,K_w):
                CurrentImg= LucisBack.filmFrame[0]
                speedY=8
                
            elif event.key in(K_DOWN,K_s):
                CurrentImg= LucisFront.filmFrame[0]
                speedY=8
                
            elif event.key in(K_LEFT,K_a):
                CurrentImg= LucisLeft.filmFrame[0]
                speedX=8
                
            elif event.key in(K_RIGHT,K_d):
                CurrentImg= LucisRight.filmFrame[0]
                speedX=8
                
        

    LucisRight.update()
    LucisLeft.update()
    LucisFront.update()
    LucisBack.update()
    
    pygame.display.update()
    fpsClock.tick(FPS)
