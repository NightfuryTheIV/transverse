import pygame, sys
from ClassesAndFunctions import Character, Bullet, Map, Button

pygame.init()

screen = pygame.display.set_mode((1000, 900))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.key == pygame.K_DOWN:
            pygame.quit()
            sys.exit()
    
    leo = Character("Leo", 3, 50, 50)
    leo.movement(0.9, 9)