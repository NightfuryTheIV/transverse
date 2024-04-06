import pygame
import sys
from technoblade import technoblade
from technoblade import Player
from screen import Menu

technoblade = technoblade()
pygame.init()
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 120  # Set your desired frame rate here
running = True
Menu(True)#Show the menu


while running:
    for event in pygame.event.get():#(Allthe following is for quiting game by clicking on cross )
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()
            Menu(False)

        #Following is to see if key is pressed
        elif event.type == pygame.KEYDOWN:
            technoblade.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            technoblade.pressed[event.key]=False

    #See which key is pressed and makes the character move right, left, up
    if technoblade.pressed.get(pygame.K_d):
        technoblade.player.move_right()
    elif technoblade.pressed.get(pygame.K_q):
        technoblade.player.move_left()
    elif technoblade.pressed.get(pygame.K_z):
        technoblade.player.move_up()
    """screen.blit(technoblade.player.image, technoblade.player.rect)"""

    #print(technoblade.pressed)

