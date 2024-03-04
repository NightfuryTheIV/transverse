import pygame, sys
import game
pygame.init()


pygame.display.set_caption("Technoblade Trinity")
screen = pygame.display.set_mode((1280, 720))
running = True
scale=1.7

backgroung = pygame.image.load('/Users/benjamin/Documents/GitHub/transverse/image/IMG_0250.png')
def zoomimg(scale):
    zommimg = pygame.transform.scale(backgroung, (int(backgroung.get_width()*scale),int(backgroung.get_height()*scale)))
    screen.blit(zommimg, (0, 0))
    pygame.display.flip()



while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key]=False

    zoomimg(scale)
    """    screen.blit(Player.image, Player.rect)"""
    if Game.pressed.get(pygame.K_d):
        Game.player.move_right()
    elif Game.pressed.get(pygame.K_q):
        Game.player.move_left()
    elif Game.pressed.get(pygame.K_z):
        Game.player.move_up()

    print(Game.pressed)






"""    Screen.blit(backgroung,(0, -200))"""
