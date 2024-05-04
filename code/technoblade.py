import pygame
import sys
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 1  # Set your desired frame rate here


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()#All characteristic of character
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2.5
        self.image = pygame.image.load('../image/character/run/Xnip2024-05-04_18-25-53-removebg-preview.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 670
        self.pressed = {"UP": False, "LEFT": False, "RIGHT": False}

    def move_up(self):
        # Gravitational constant
        g = 9.81
        # Initial eight
        h0 = 0
        # Initial speed
        Vc = 50
        #Real angle timme and angle time max
        temps_angle_reel = 2
        temps_angle_max = 5
        # Calcul de V0y
        V0y = (temps_angle_reel / temps_angle_max) * Vc
        V0y = min(V0y, Vc)  # Max speed
        # Trajectory calculator
        def trajectory_calculator(t):
            return V0y * t - 0.5 * g * t**2 + h0

        self.rect.y -= trajectory_calculator(1)
    def update(self):
        if self.pressed["RIGHT"]:
            self.rect.x += self.velocity
        if self.pressed["LEFT"]:
            self.rect.x -= self.velocity
        if self.pressed["UP"]:
            self.move_up()



class technoblade:
    def __init__(self):
        print

