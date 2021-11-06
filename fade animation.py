import sys, pygame
from pygame.locals import *
import time

pygame.init()

DISPLAY = pygame.display.set_mode((900,600))
heart=pygame.image.load("heart.jpg").convert()




i=100

while True:

    for i in range(255):

        DISPLAY.fill((255,255,255))
        print(i)
        
        heart.set_alpha(i)
        DISPLAY.blit(heart,(200,100))
        time.sleep(0.01)
        pygame.display.flip()

    for i in range(255):

        DISPLAY.fill((255,255,255))
        print(i)
        
        heart.set_alpha(255-i)
        DISPLAY.blit(heart,(200,100))
        time.sleep(0.01)
        pygame.display.flip()
        

        



