import pygame
import sys
from technoblade import technoblade
from technoblade import Player
from screen import Menu
from screen import Screen
technoblade = technoblade()
pygame.init()
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 120  # Set your desired frame rate here
running = True
Menu(True)#Show the menu
screen = pygame.display.set_mode((1280, 720))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            Menu(False)


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                technoblade.player.pressed["UP"] = True
            elif event.key == pygame.K_DOWN:
                technoblade.player.pressed["DOWN"] = True
            elif event.key == pygame.K_LEFT:
                technoblade.player.pressed["LEFT"] = True
            elif event.key == pygame.K_RIGHT:
                technoblade.player.pressed["RIGHT"] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                technoblade.player.pressed["UP"] = False
            elif event.key == pygame.K_DOWN:
                technoblade.player.pressed["DOWN"] = False
            elif event.key == pygame.K_LEFT:
                technoblade.player.pressed["LEFT"] = False
            elif event.key == pygame.K_RIGHT:
                technoblade.player.pressed["RIGHT"] = False




