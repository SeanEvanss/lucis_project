import pygame,sys
import pytmx
import time
from pytmx import load_pygame
from pygame.locals import*

pygame.init()

pygame.mixer.music.load("BWOAH.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)


pygame.key.set_repeat(10,50)



changeMap= True

FPS=60
fpsClock= pygame.time.Clock()

DISPLAY= pygame.display.set_mode((768,384),pygame.DOUBLEBUF|pygame.HWSURFACE)

pygame.display.set_caption('Fourth alpha')
WHITE=(255,255,255)
BLACK=(0,0,0)

gameMap0401=load_pygame("Dungeon04(01).tmx")
gameMap0402=load_pygame("Dungeon04(02).tmx")




  
from animationClass import *
from playerClass import *


LucisRight= Animation(3)
LucisRight.addFrame('Right Normal.png')
LucisRight.addFrame('Right Walk 1.png')
LucisRight.addFrame('Right Walk 2.png')

        
LucisFront= Animation(3)
LucisFront.addFrame('Front Normal.png')
LucisFront.addFrame('Front Walk 1.png')
LucisFront.addFrame('Front Walk 2.png')


        
LucisLeft= Animation(3)
LucisLeft.addFrame('Left Normal.png')
LucisLeft.addFrame('Left Walk 1.png')
LucisLeft.addFrame('Left Walk 2.png')

        
LucisBack= Animation(3)
LucisBack.addFrame('Back Normal.png')
LucisBack.addFrame('Back Walk 1.png')
LucisBack.addFrame('Back Walk 2.png')
       

class Player():
    def _init_(self):
        self.hp=100

    def moveLeft(self):

        
        global trueX,catX,CurrentImg

        CurrentImg= LucisLeft.getImage()
        trueX-=speedX

        if( trueX > leftLimit ):
            catX -= speedX

    def moveRight(self):

        
        global trueX,catX,CurrentImg

        CurrentImg= LucisRight.getImage()
        trueX+=speedX

        if(catX<rightLimit):
             catX +=speedX
    
                    
    def moveUp(self):

        
        global trueY,catY,CurrentImg,speedY

        CurrentImg= LucisBack.getImage()            
        trueY -=speedY

        
        if (catY>upLimit ):            
            catY -= speedY

            
            
    def moveDown(self):
       global trueY,catY,CurrentImg,speedY
       CurrentImg= LucisFront.getImage()
       trueY +=speedY

        
       if (catY<downLimit ):
           catY +=speedY
           
    def stop(self,safeX,safeY):

        global catX,catY

        catX=safeX
        catY=safeY
        


        
         


Lucis= Player()
catX= 85
catY= 100

trueX=catX
trueY=catY

speedX=12
speedY=12

leftLimit=60
rightLimit=630
upLimit=60

downLimit=260


CurrentImg= LucisRight.getImage()

#values used mainly for map scrolling


currentMap= gameMap0401
scrollX=0
scrollY=0

#main loop foir the game

while True:
    DISPLAY.fill(BLACK)
    

#to utilise the tmx file we must first turn the pixels into a form we can manipulate
#The loop is to ensure that the map tiles are only loaded if the map is changed (and not every cycle of the game loop as it slows down free memory)
    
    while (changeMap== True):
        images=[]
 
        for y in range(22):
            for x in range(24):
                currentTileImage = currentMap.get_tile_image(x,y,0)
                currentTileImage = pygame.transform.scale2x(currentTileImage)
                images.append(currentTileImage)
        changeMap= False
            
            

#after storing the pixels into an array we can then mamnipulate the array by drawing the map
#The map tiles move in corespondence to the player's position on the map (soon to be replaced by line collisions)
    i = 0
    
    
    for y in range(22):
            for x in range(24):
                DISPLAY.blit(images[i],((x*64)+scrollX,(y*64)+scrollY))
                i += 1
    
    if(trueX>=rightLimit and pygame.key.get_pressed()[pygame.K_RIGHT]==1):
        scrollX -= 5
        
    elif(trueX<=leftLimit and pygame.key.get_pressed()[pygame.K_LEFT]==1):
        scrollX += 5

    elif(trueY>=downLimit and pygame.key.get_pressed()[pygame.K_DOWN]==1):
        scrollY -= 5
        
    elif(trueY<=upLimit and pygame.key.get_pressed()[pygame.K_UP]==1):
        scrollY += 5

    if (catX>leftLimit and catX<rightLimit):
        trueX=catX
       

    if (catY>upLimit and catY<downLimit):
        trueY=catY

    
#blits the character and it's coordinates

    collisionRectList=[]
    
    #code portion for the collision rectangles.
    collisionGroup = currentMap.get_layer_by_name("Collision")
    for obj in collisionGroup:
        
        collisionRectTuple=((obj.x*2 + scrollX), (obj.y*2 + scrollY), (obj.width*2), (obj.height*2))
        collisionRect = pygame.Rect(collisionRectTuple)
        collisionRectList.append(collisionRect)
        pygame.draw.rect(DISPLAY,(0,255,0),collisionRect,1)
        



    playerRect= pygame.Rect(catX+1,catY-2,46,70)
    pygame.draw.rect(DISPLAY,(0,0,255),playerRect,1)
    pygame.draw.rect(DISPLAY,(255,0,0),(60,60,630,260),1)



    DISPLAY.blit(CurrentImg,(catX,catY))
    
    if (pygame.Rect.collidelist(playerRect,collisionRectList) != -1):
        
                

        if( (collisionRectList[pygame.Rect.collidelist(playerRect,collisionRectList)].collidepoint(playerRect.midleft))):
            
            print("right collision")
            
      
        elif( (collisionRectList[pygame.Rect.collidelist(playerRect,collisionRectList)].collidepoint(playerRect.midright))):
            print("left collision")

        elif( (collisionRectList[pygame.Rect.collidelist(playerRect,collisionRectList)].collidepoint(playerRect.midbottom))):
            print("top collision")
                
        elif( (collisionRectList[pygame.Rect.collidelist(playerRect,collisionRectList)].collidepoint(playerRect.midtop))):
            print("bottom collision")
        else:
            print("player stop")

    for event in pygame.event.get():
        if event.type== QUIT:
            
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            

           
                


                

            if event.key in(K_UP,K_w):
                Lucis.moveUp()
                
                            

            elif event.key in(K_DOWN,K_s):
                Lucis.moveDown()
                
                
            elif event.key in(K_LEFT,K_a):
                Lucis.moveLeft()
                
                
                
            elif event.key in(K_RIGHT,K_d):
                Lucis.moveRight()
                

            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            elif event.key == K_1:
                changeMap= True
                currentMap= gameMap0401

            elif event.key == K_2:
                changeMap= True
                currentMap= gameMap0402
            
                

        elif event.type == KEYUP:

            
           
            if event.key in(K_UP,K_w):
                CurrentImg= LucisBack.filmFrame[0]
           
                
            elif event.key in(K_DOWN,K_s):
                CurrentImg= LucisFront.filmFrame[0]
                
                
            elif event.key in(K_LEFT,K_a):
                CurrentImg= LucisLeft.filmFrame[0]
                
            elif event.key in(K_RIGHT,K_d):
                CurrentImg= LucisRight.filmFrame[0]
                
        
        

    LucisRight.update()
    LucisLeft.update()
    LucisFront.update()
    LucisBack.update()
    
    pygame.display.update()
    fpsClock.tick(FPS)
