import pygame
import sys
from technoblade import technoblade
from technoblade import Player
from technoblade import Button
pygame.init()

#All necessaries
technoblade = technoblade()
character = Player()
Title = pygame.image.load('../image/TITLE.png')
menu = pygame.image.load('../image/menu.png')
background = pygame.image.load('../image/Fond.png')
pygame.display.set_caption("Technoblade Trinity")
screen = pygame.display.set_mode((1280, 720))
running = True
scale=1.7
scale2=1
scale3=0.7

clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 10  # Set your desired frame rate here

def zoomimg(scale):
    zommimg = pygame.transform.scale(background, (int(background.get_width()*scale),int(background.get_height()*scale)))
    screen.blit(zommimg, (0, 0))
    pygame.display.flip()

def zoomimg2(scale):
    Menu_im = pygame.transform.scale(menu, (int(menu.get_width()*scale2),int(menu.get_height()*scale2)))
    screen.blit(Menu_im, (525, 250))
    pygame.display.flip()
    clock.tick(frame_rate)
def zoomimg3(scale):
    Title_im = pygame.transform.scale(Title, (int(Title.get_width()*scale3),int(Title.get_height()*scale3)))
    screen.blit(Title_im, (360, 0))
    pygame.display.flip()
    clock.tick(frame_rate)


easy = Button(525, 250, 210, 70, "Easy", 0, 0, 0)
medium = Button(525, 350, 210, 70, "Medium", 0, 0, 0)
hard = Button(525, 450, 210, 70, "Hard", 0, 0, 0)
insane = Button(525, 550, 210, 70, "Insane", 0, 0, 0)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            technoblade.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            technoblade.pressed[event.key]=False

        print(f"x : {pygame.mouse.get_pos()[0]}, y : {pygame.mouse.get_pos()[1]}")

    easy.pressed_check()
    medium.pressed_check()
    hard.pressed_check()
    insane.pressed_check()


    screen.blit(technoblade.player.image, technoblade.player.rect)
    zoomimg(scale)
    zoomimg2(scale2)
    zoomimg3(scale3)


    if technoblade.pressed.get(pygame.K_d):
        technoblade.player.move_right()
    elif technoblade.pressed.get(pygame.K_q):
        technoblade.player.move_left()
    elif technoblade.pressed.get(pygame.K_z):
        technoblade.player.move_up()

    print(technoblade.pressed)
