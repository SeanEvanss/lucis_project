import pygame,sys
from pygame.locals import*
import time
import os

pygame.init()



#This function is universally neccesary to properly manipulate an image within a program
def load_image(path,name):
    image = pygame.image.load(os.path.join(path,name))
    return image


class Animation():
    def __init__(self, maxFrame):
        self.maxFrame=maxFrame
        self.currentSprite=0
        self.filmFrame=[]
        
        
    def addFrame(self,path,img):
        self.img=img
        self.path=path
#take note that "load_image" is a custom function we created
#'path' in this case is used to define the subfolder that the file would be
#stored in, it is a function of the os module we imported

        
        self.filmFrame.append(load_image(self.path,self.img))

    def snipper(self, image, sub):
        self.image = image
        self.sub = sub

        sub= image.pygame.transform.chop(DISPLAY,(2,2,50,50))

        
    def update(self):
        
        if(len(self.filmFrame)>1):
            i=0
            for i in range (500):
                i +=1

            if(self.currentSprite >= (len(self.filmFrame)-1)):
            
                self.currentSprite=0
            elif(self.currentSprite < len(self.filmFrame)):
           
                self.currentSprite += 1

                
                    
                
                
    def getImage(self):
        if(len(self.filmFrame)!=0):
            return self.filmFrame[self.currentSprite]
            
