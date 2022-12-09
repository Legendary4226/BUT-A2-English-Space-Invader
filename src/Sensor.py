import pygame
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
sense = SenseHat()
HEIGHT = 450
WIDTH = 400

def calculateVelocity(accelerometer,shipPosition):
    if(accelerometer<0):
        #we go to the left
        if(accelerometer<-0.7):
            return -5
        elif(accelerometer<-0.5):
            return -3
        elif(accelerometer<-0.3):
            return -1
        else:
            return 0
    if(accelerometer>0):
        #we go to the right
        if(accelerometer>0.7):
            return 5
        elif(accelerometer>0.5):
            return 3
        elif(accelerometer>0.3):
            return 1
        else:
            return 0
    return shipPosition


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

shipPositionX = WIDTH/2
shipPositionY = HEIGHT-HEIGHT/8
step = 5

ship = pygame.image.load("./ship.png").convert()


pygame.display.flip()
print(shipPositionX,shipPositionY)

while True:
    for event in sense.stick.get_events():
        if(event.action == "pressed"):
            print("PIOU!!")
    ship = pygame.transform.scale(ship,(40,40))
    screen.blit(ship,(shipPositionX,shipPositionY))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    key_input = pygame.key.get_pressed()   
    shipPositionX += calculateVelocity(sense.get_accelerometer_raw()['x'],shipPositionX)
    pygame.display.update()
    pygame.time.Clock().tick(30)