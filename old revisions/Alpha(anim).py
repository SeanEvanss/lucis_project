import pygame,sys
import pytmx
from pytmx import load_pygame

from pygame.locals import*

pygame.init()



FPS=30
fpsClock= pygame.time.Clock()

DISPLAY= pygame.display.set_mode((1000,600))
pygame.display.set_caption('First alpha')

WHITE=(255,255,255)

gameMap=load_pygame("Dungeon01.tmx")


def load_image(name):
    image = pygame.image.load(name)
    return image
    #This function is universally neccesary to properly manipulate an image within a programm




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



catX= 20
catY= 20



while True:
    DISPLAY.fill(WHITE)
    print(LucisRight.currentSprite)
    CurrentImg= LucisRight.getImage()
    DISPLAY.blit(LucisRight.getImage(),(catX,catY))

    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()

    LucisRight.update()
    pygame.display.update()
    fpsClock.tick(FPS)
