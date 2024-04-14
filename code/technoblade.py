import pygame
import sys
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 1  # Set your desired frame rate here


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()#All characteristic of character
        self.health = 100
        self.max_healf = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('../image/perso.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400#Character position on x
        self.rect.y = 400#Character position on y

    def move_right(self):
        self.rect.x += self.velocity#Takes actual position and add velocity
    def move_left(self):
        self.rect.x -= self.velocity#Takes actual position and reduce velocity

    def move_up(self):
        self.rect.y += self.velocity#Takes actual position and add velocity


class technoblade:
    def __init__(self):
        self.player = Player()
        self.pressed = {}

