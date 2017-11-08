import pygame
import sys
import random
import time

# check initialized errors (6.0) will be ok
check_errors=pygame.init()
if check_errors[1]>0:
    print ("(!) Had {0} init errors,exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print ("(+) Successfully initialized!")
# surface
playSurface=pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")
# about the color
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
brown =pygame.Color(162,42,42)
# ftp
ftpControler=pygame.time.Clock()
# snake
snakePos=[100,50]
snakeBody=[[100,50][90,50][80,50]]