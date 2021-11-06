import pygame,sys
import pytmx
from pytmx import load_pygame
from pygame.locals import*

pygame.init()

pygame.mixer.music.load("BWOAH.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)


pygame.key.set_repeat(10,50)



FPS=60
fpsClock= pygame.time.Clock()

DISPLAY= pygame.display.set_mode((768,384),
                                 pygame.DOUBLEBUF|pygame.HWSURFACE)
pygame.display.set_caption('Third alpha')
WHITE=(255,255,255)
BLACK=(0,0,0)

gameMap01=load_pygame("Dungeon01.tmx")
gameMap02=load_pygame("Dungeon02.tmx")
gameMap03=load_pygame("Dungeon03.tmx")

collisionGroup = gameMap03.get_layer_by_name("Collision")


for obj in collisionGroup:
    bbox = obj.x, obj.y, obj.width, obj.height
    



def load_image(name):
    image = pygame.image.load(name)
    return image
    #This function is universally neccesary to properly manipulate an image within a program



class Character():
    def _init_(self):
        self.hp=100
        

    

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

cat=load_image("cat.png")

catX= 85
catY= 100

speedX=8
speedY=8

leftLimit=80
rightLimit=550
upLimit=40
downLimit=260



CurrentImg= LucisRight.getImage()

#values used mainly for map scrolling
trueX=catX
trueY=catY

scrollX=0
scrollY=0

#main loop foir the game

while True:
    DISPLAY.fill(BLACK)

#to utilise the tmx file we must first turn the pixels into a form we can manipulate

    images=[]
    images02=[]
    for y in range(11):
        for x in range(11):
            currentTileImage = gameMap03.get_tile_image(x,y,0)
            
            images.append(currentTileImage)
            
            

#after storing the pixels into an array we can then mamnipulate the array by drawing the map        
    i = 0

    for y in range(11):
            for x in range(11):
                DISPLAY.blit(images[i],((x*64)+scrollX,(y*64)+scrollY))
                
                i += 1
    
    if(trueX>=rightLimit and pygame.key.get_pressed()[pygame.K_RIGHT]==1):
        scrollX -= 2
        
    if(trueX<=leftLimit and pygame.key.get_pressed()[pygame.K_LEFT]==1):
        scrollX += 2

    if(trueY>=downLimit and pygame.key.get_pressed()[pygame.K_DOWN]==1):
        scrollY -= 2
        
    if(trueY<=upLimit and pygame.key.get_pressed()[pygame.K_UP]==1):
        scrollY += 2

    if (catX>leftLimit and catX<rightLimit):
        trueX=catX
       

    if (catY>upLimit and catY<downLimit):
        trueY=catY

       
    
#blits the character and it's coordinates
    
    DISPLAY.blit(CurrentImg,(catX,catY))

    
     
    for event in pygame.event.get():
        if event.type== QUIT:
            
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            
            if event.key in(K_UP,K_w):
                
                if (catY>upLimit ):            
                    catY -= speedY                                            
                
                CurrentImg= LucisBack.getImage()    



                trueY -=speedY
                
            elif event.key in(K_DOWN,K_s):
                
                if (catY<downLimit ):
                    
                    catY +=speedY                    
                
                
                CurrentImg= LucisFront.getImage()


                trueY +=speedY
                
            elif event.key in(K_LEFT,K_a):
                
                if( trueX > leftLimit ):
                    
                    catX -= speedX

                    
                CurrentImg= LucisLeft.getImage()
                trueX-=speedX
                
            elif event.key in(K_RIGHT,K_d):
                
                if(catX<rightLimit):
                    catX +=speedX
                    
                
                CurrentImg= LucisRight.getImage()


                trueX +=speedX

            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                

                

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
