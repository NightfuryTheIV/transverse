import pygame
from screen import Menu
from technoblade import player
pygame.init()
running = True
Menu(True)#Show the menu

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            Menu(False)
