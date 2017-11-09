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
fpsController=pygame.time.Clock()
# snake
snakePos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]

foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True

direction="RIGHT"
changeTo=direction
score=0
speed=15
# game over
def gameOver():
    myFont=pygame.font.SysFont("manaco",72)
    mySurf=myFont.render("GAME OVER!!!",True,red)
    myRect=mySurf.get_rect()
    myRect.midtop=(360,15)
    playSurface.blit(mySurf,myRect)
    showScore(True)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()
def showScore(die=False):
    myFont=pygame.font.SysFont("manaco",24)
    mySurf=myFont.render("Score: {0}".format(score),True,black)
    myRect=mySurf.get_rect()
    if die:
        myRect.midtop = (360, 120)
    else:
        myRect.midtop=(80,10)
    playSurface.blit(mySurf,myRect)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key==ord("d"):
                changeTo="RIGHT"
            if event.key==pygame.K_LEFT or event.key==ord("a"):
                changeTo="LEFT"
            if event.key==pygame.K_UP or event.key==ord("w"):
                changeTo="UP"
            if event.key==pygame.K_DOWN or event.key==ord("s"):
                changeTo="DOWN"
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if changeTo=="RIGHT" and not direction=="LEFT":
        direction="RIGHT"
    if changeTo=="LEFT" and not direction=="RIGHT":
        direction="LEFT"
    if changeTo=="UP" and not direction=="DOWN":
        direction="UP"
    if changeTo=="DOWN" and not direction=="UP":
        direction="DOWN"

    if direction=="RIGHT":
        snakePos[0]+=10
    if direction=="LEFT":
        snakePos[0]-=10
    if direction=="UP":
        snakePos[1]-=10
    if direction=="DOWN":
        snakePos[1]+=10


    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        speed+=1
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))

    # Bound
    if snakePos[0] > 710 or snakePos[0] < 0 or snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    # Self hit
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    #common stuff
    showScore()
    pygame.display.flip()

    fpsController.tick(speed)