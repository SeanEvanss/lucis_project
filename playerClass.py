
from animationClass import*
import os


speedX=15
speedY=15

leftLimit=60
rightLimit=670
upLimit=60
downLimit=260



LucisRight= Animation(3)
LucisRight.addFrame('LucisSpriteRev','Lucis Right Normal.png')
LucisRight.addFrame('LucisSpriteRev','Lucis Right Walk 1.png') 
LucisRight.addFrame('LucisSpriteRev','Lucis Right Walk 2.png')

        
LucisFront= Animation(3)
LucisFront.addFrame('LucisSpriteRev','Lucis Front Normal.png')
LucisFront.addFrame('LucisSpriteRev','Lucis Front Walk 1.png')
LucisFront.addFrame('LucisSpriteRev','Lucis Front Walk 2.png')


        
LucisLeft= Animation(3)
LucisLeft.addFrame('LucisSpriteRev','Lucis Left Normal.png')
LucisLeft.addFrame('LucisSpriteRev','Lucis Left Walk 1.png')
LucisLeft.addFrame('LucisSpriteRev','Lucis Left Walk 2.png')

        
LucisBack= Animation(3)
LucisBack.addFrame('LucisSpriteRev','Lucis Back Normal.png')
LucisBack.addFrame('LucisSpriteRev','Lucis Back Walk 1.png')
LucisBack.addFrame('LucisSpriteRev','Lucis Back Walk 2.png')


                   
class Player():
    def __init__(self):
        self.hp=100
        self.catX= 200
        self.catY= 100

        self.trueX=self.catX
        self.trueY=self.catY

    def moveLeft(self):

        
        self.trueX-=speedX

        if( self.trueX > leftLimit ):
            self.catX -= speedX

    def moveRight(self):

        
        self.trueX+=speedX

        if(self.catX<rightLimit):
             self.catX +=speedX
    
                    
    def moveUp(self):
                
        self.trueY -=speedY

        
        if (self.catY>upLimit ):            
            self.catY -= speedY

            
            
    def moveDown(self):

       self.trueY +=speedY

        
       if (self.catY<downLimit ):
           self.catY +=speedY
           
    def stop(self,safeX,safeY):
        print(ok)
        
        
        
    
        
