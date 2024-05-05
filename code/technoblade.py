import pygame
import sys
from math import sin, cos, pi
Gravity = 9.81


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()#All characteristic of character
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.xvelocity = 5
        self.yvelocity = 0
        self.image = pygame.image.load('../image/perso.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.pressed = {"UP": False, "LEFT": False, "RIGHT": False, "DOWN": False, "JUMP": False}
        self.air_time = 0

    def jump(self):
        self.rect.y += -1



    def update(self):
        if self.pressed["RIGHT"]:
            self.rect.x += self.xvelocity
        if self.pressed["LEFT"]:
            self.rect.x -= self.xvelocity
        if self.pressed["JUMP"]:
            self.yvelocity = 0
            for i in range(50):
                self.jump()


player = Player()


class Projectile:
    def __init__(self, name, type, velocity, speed):
        self.player = player
        self.name = name
        self.type = type  # We might use different types of arrows for diffreent levels in the future
        self.velocity = velocity  # the actual at which the arrow is flying
        self.speed = speed  # the speed at which the flight trajectory is refreshed (between 0.1 and 1)
        self.clock = 0  # This will be used inside the trajectory equations
        self.basex = player.rect.x
        self.x = 0
        self.basey = player.rect.y
        self.y = 0
        self.angle = 0

    def firing_angle(self):
        if player.pressed["UP"]:
            self.angle += pi/180
        if player.pressed["DOWN"]:
            self.angle -= pi/180

    def flight(self, angle):
        self.x = self.velocity * cos(angle) * self.clock + self.basex
        self.y = 1/2 * Gravity * self.clock**2 + sin(angle) * self.clock + self.basey

        self.clock += self.speed


class technoblade:
    def __init__(self):
        print("")

