import pygame,sys
from technoblade import technoblade
from technoblade import Player
pygame.init()

technoblade = technoblade()
character = Player()
menu = pygame.image.load('/Users/benjamin/Documents/GitHub/transverse/image/png-transparent-game-menu-user-interface-design-game-interaction-design-a-set-of-game-buttons-text-rectangle-video-game copie 2.png')
background = pygame.image.load('/Users/benjamin/Documents/GitHub/transverse/image/IMG_0250.png')

pygame.display.set_caption("Technoblade Trinity")
screen = pygame.display.set_mode((1280, 720))
running = True
scale=1.7



char=character.image
def zoomimg(scale):
    zommimg = pygame.transform.scale(background, (int(background.get_width()*scale),int(background.get_height()*scale)))
    screen.blit(zommimg, (0, 0))
    pygame.display.flip()

def zoomimg2(scale):
    zommimg = pygame.transform.scale(char, (int(char.get_width()*scale),int(char.get_height()*scale)))
    screen.blit(zommimg, (0, 0))
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            technoblade.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            technoblade.pressed[event.key]=False
    screen.blit(technoblade.player.image, technoblade.player.rect)
    zoomimg(scale)
    zoomimg2(scale)
    if technoblade.pressed.get(pygame.K_d):
        technoblade.player.move_right()
    elif technoblade.pressed.get(pygame.K_q):
        technoblade.player.move_left()
    elif technoblade.pressed.get(pygame.K_z):
        technoblade.player.move_up()

    print(technoblade.pressed)

    "ifjeing"