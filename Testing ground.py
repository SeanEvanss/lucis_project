import sys, pygame
from pygame.locals import *
import time

pygame.init()

n= int(input("Enter the size of the triangle (note that the num must be odd)."))

for i in range (0,n):
    i +=1

    for x in range (i):
        print("*", end="")
        x += 1

        
    for y in range (0,(n-i)):
        print(" ",end="")
        y +=1   


    print("")




