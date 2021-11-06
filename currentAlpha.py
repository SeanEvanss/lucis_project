import pygame,sys
import pytmx
import time
from pytmx import load_pygame
from pygame.locals import*

pygame.init()

pygame.mixer.music.load("BWOAH.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)

pygame.key.set_repeat(10,105)

changeMap= True

FPS=60
fpsClock= pygame.time.Clock()





DISPLAY= pygame.display.set_mode((768,384),pygame.DOUBLEBUF|pygame.HWSURFACE)

pygame.display.set_caption('sixth alpha')
WHITE=(255,255,255)
BLACK=(0,0,0)

heart=pygame.image.load("heart.jpg").convert()

gameMap0401=load_pygame("DG01RM01.tmx")
gameMap0402=load_pygame("DG01RM02.tmx")
#load the actual map data into the system


currentMap= gameMap0401

mapDict={}
mapDict['rm01']=gameMap0401
mapDict['rm02']=gameMap0402


  
from animationClass import *
from playerClass import *

  

Lucis= Player()
CurrentImg= LucisRight.getImage()


#inital values, used mainly for map scrolling

scrollX=0
scrollY=0

#main loop for the game




while True:
    
    
    DISPLAY.fill(BLACK)

    #to utilise the tmx file we must first turn the pixels into a form we can manipulate
    #The loop is to ensure that the map tiles are only loaded if the map is changed (and not every cycle of the game loop as it clogs up the game loop having to read from
    #an external file repeatdly)
    
    while (changeMap== True):
        images=[]
 
        for y in range(currentMap.height):
            for x in range(currentMap.width):
                currentTileImage = currentMap.get_tile_image(x,y,0)
                
                images.append(currentTileImage)
                
        changeMap= False

    
    if (Lucis.catX>leftLimit and Lucis.catX<rightLimit):
        Lucis.trueX=Lucis.catX
       
    if (Lucis.catY>upLimit and Lucis.catY<downLimit):
        Lucis.trueY=Lucis.catY


            
            

#after storing the pixels into an array we can then mamnipulate the array by drawing the map
#The map tiles move in corespondence to the player's position on the map (soon to be replaced by line collisions)
    i = 0
    
    for y in range(currentMap.height):
        for x in range(currentMap.width):
            DISPLAY.blit(images[i],((x*64)+scrollX,(y*64)+scrollY))
            i += 1



    warpRectList=[]
    warpListObj=[]
    
    #code portion for warp rectangles
    warpRectGroup= currentMap.get_layer_by_name("warp")

    for obj in warpRectGroup:
        warpRectTuple=((obj.x + scrollX), (obj.y + scrollY), (obj.width), (obj.height))
        warpRectIndex=(obj.warpIndex)
        warpRect = pygame.Rect(warpRectTuple)

        warpListObj.append(obj)
        warpRectList.append(warpRect)
        pygame.draw.rect(DISPLAY,(0,0,180),warpRect,1)
        


    
    
    collisionRectList=[]
    
    #code portion for the collision rectangles.
    collisionGroup = currentMap.get_layer_by_name("Collision")

    for obj in collisionGroup:
    
        collisionRectTuple=((obj.x + scrollX), (obj.y + scrollY), (obj.width), (obj.height))
        collisionRect = pygame.Rect(collisionRectTuple)
        collisionRectList.append(collisionRect)
        pygame.draw.rect(DISPLAY,(0,255,0),collisionRect,1)
        

    
    #blits the character and it's coordinates

    playerRect= pygame.Rect(Lucis.catX-1,Lucis.catY-2,48,72)
    
    pygame.draw.rect(DISPLAY,(0,0,255),playerRect,1)
    

    currentIndex=0

    DISPLAY.blit(CurrentImg,(Lucis.catX,Lucis.catY))

    

    
    
    
    if (pygame.Rect.collidelist(playerRect,collisionRectList) != -1):
            pass

    if (pygame.Rect.collidelist(playerRect,warpRectList) != -1):
        

        currentIndex= (warpListObj[pygame.Rect.collidelist(playerRect,warpRectList)].warpIndex)
        
        
        print (warpListObj[pygame.Rect.collidelist(playerRect,warpRectList)].x)
        print (warpListObj[pygame.Rect.collidelist(playerRect,warpRectList)].y)
        
        changeMap = True
        currentMap = mapDict[warpListObj[pygame.Rect.collidelist(playerRect,warpRectList)].nextMap]

        #we use " warpListObj[pygame.Rect.collidelist(playerRect,warpRectList)].nextMap " because the text output we get, cannot be simply converted into the name varible needed
        #to load the new map.

        warpRectGroup= currentMap.get_layer_by_name("warp")
        
        for obj in warpRectGroup:
            if (obj.warpIndex == currentIndex):
                scrollX= -(obj.x)+ 80
                scrollY= -(obj.y)+ 80

                print(obj.x)
                print(obj.y)

                Lucis.catX= int(obj.catX)
                Lucis.catY= int(obj.catY)
                     
        
        for i in range(255):

            DISPLAY.fill((255,255,255))

        
            heart.set_alpha(i)
            
            DISPLAY.blit(heart,(130,-20))
            time.sleep(0.01)
            pygame.display.flip()

        for i in range(255):

            DISPLAY.fill((255,255,255))
        
        
            heart.set_alpha(255-i)
            DISPLAY.blit(heart,(130,-20))
            time.sleep(0.01)
            pygame.display.flip()



        
            
        # Above 2 range loops meant for modifying the alpha on the heart and blitting it to the DISPLAY
        # THis is done to give it the appearence of fadding in and out, will be using it in battle/room transitons

    for event in pygame.event.get():
        if event.type== QUIT:
            
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            
      

            if event.key in(K_UP,K_w):

                CurrentImg= LucisBack.getImage()
                if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) >0 ):

                    if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) >1 ):
                        if( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midtop)) or (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[1]].collidepoint(playerRect.midtop))):
                            continue
                        
                    elif( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midtop))):
                        continue
        
            
                Lucis.moveUp()                
                if(Lucis.trueY<=upLimit and pygame.key.get_pressed()[pygame.K_UP]==1):
                    scrollY += speedY
                
                            

            if event.key in(K_DOWN,K_s):

                CurrentImg= LucisFront.getImage()

                
                if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) > 0 ):

                    if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) >1 ):
                        if( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midbottom)) or (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[1]].collidepoint(playerRect.midbottom))):
                            continue
                        
                    elif( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midbottom))):
                        continue

                
                Lucis.moveDown()
                if(Lucis.trueY>=downLimit and pygame.key.get_pressed()[pygame.K_DOWN]==1):
                    scrollY -= speedY
                
                
            if event.key in(K_LEFT,K_a):

                CurrentImg= LucisLeft.getImage()

                if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) > 0 ):

                    if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) >1 ):
                        if( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midleft)) or (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[1]].collidepoint(playerRect.midleft))):
                            continue
                        
                    elif( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midleft))):
                        continue

        
                Lucis.moveLeft()            
                if(Lucis.trueX<=leftLimit and pygame.key.get_pressed()[pygame.K_LEFT]==1):
                    scrollX += speedX
                
                
            if event.key in(K_RIGHT,K_d):

                CurrentImg= LucisRight.getImage()
                
                if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) > 0 ):

                    if(len(pygame.Rect.collidelistall(playerRect,collisionRectList)) >1 ):
                        if( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midright)) or (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[1]].collidepoint(playerRect.midright))):
                            continue
                        
                    elif( (collisionRectList[pygame.Rect.collidelistall(playerRect,collisionRectList)[0]].collidepoint(playerRect.midright))):
                        continue

                    
            
                Lucis.moveRight()
                if(Lucis.trueX>=rightLimit and pygame.key.get_pressed()[pygame.K_RIGHT]==1):
                    scrollX -= speedX

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
