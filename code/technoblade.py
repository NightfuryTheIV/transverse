import pygame
from math import sin, cos, pi
Gravity = 9.81

run_1 = pygame.image.load('../image/character/run/run1.png')
run_2 = pygame.image.load('../image/character/run/run2.png')
run_3 = pygame.image.load('../image/character/run/run3.png')
run_4 = pygame.image.load('../image/character/run/run4.png')
run_5 = pygame.image.load('../image/character/run/run5.png')
run_6 = pygame.image.load('../image/character/run/run6.png')
run_7 = pygame.image.load('../image/character/run left/RUN_L_1.png')
run_8 = pygame.image.load('../image/character/run left/RUN_L_2.png')
run_9 = pygame.image.load('../image/character/run left/RUN_L_3.png')
run_10 = pygame.image.load('../image/character/run left/RUN_L_4.png')
run_11 = pygame.image.load('../image/character/run left/RUN_L_5.png')
jump_1 = pygame.image.load('../image/character/jump/JUMP1.png')
jump_2 = pygame.image.load('../image/character/jump/JUMP2.png')
jump_3 = pygame.image.load('../image/character/jump/JUMP3.png')
jump_4 = pygame.image.load('../image/character/jump/JUMP4.png')
jump_5 = pygame.image.load('../image/character/jump/JUMP5.png')
jump_6 = pygame.image.load('../image/character/jump/JUMP6.png')
jump_7 = pygame.image.load('../image/character/jump/JUMP7.png')


run_r=[run_1,run_2,run_3,run_4,run_5,run_6]
run_l= [run_7,run_8,run_9,run_10,run_11]
run_j= [jump_1,jump_2,jump_3,jump_4,jump_5,jump_6,jump_7]


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()#All characteristic of character
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 5
        self.yspeed = 0
        self.image = pygame.image.load('../image/character/run/run1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 660
        self.is_running = False
        self.is_running_left = False
        self.is_jumping = False
        self.is_jumpingL = False
        self.animationR_index = 0
        self.animationL_index = 0
        self.animationJ_index = 0
        self.air_time = 0
        self.jump_delay = 1
        self.keys = {}

    def jump(self):
        if self.rect.y > 680:
            self.yspeed = -8
        else:
            self.yspeed += 0.4
        self.rect.y += self.yspeed
        print(f"pos y : {self.rect.y}, velocity : {self.yspeed}")

    def gravity(self):
        self.yspeed += 0.4
        self.rect.y += self.yspeed
        print(f"pos y : {self.rect.y}, velocity : {self.yspeed}")

    def update(self):
        if self.is_running:
            # Update animation
            self.image = run_r[self.animationR_index]
            self.animationR_index = (self.animationR_index + 1) % len(run_r)
        elif self.is_running_left:
            self.image = run_l[self.animationL_index]
            self.animationL_index = (self.animationL_index + 1) % len(run_l)
        elif self.is_jumping:
            # Delay the jumping animation
            if self.air_time % self.jump_delay == 0:
                self.image = run_j[self.animationJ_index]
                self.animationJ_index = (self.animationJ_index + 1) % len(run_j)
            self.air_time += 1
        else:
            # Set default image if not running
            self.image = pygame.image.load('../image/character/run/run1.png')

        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:
            if self.rect.x > -1:
                self.rect.x -= self.speed
        if self.keys[pygame.K_RIGHT]:
            if self.rect.x < 1250:
                self.rect.x += self.speed
        if self.keys[pygame.K_SPACE]:
            self.jump()
        else:
            if self.rect.y < 680:
                self.gravity()

    def start_runningL(self):
        self.is_running_left = True
    def stop_runningL(self):
        self.is_running_left = False
    def start_runningR(self):
        self.is_running = True
    def stop_runningR(self):
        self.is_running = False
    def start_jumping(self):
        self.is_jumping = True
    def stop_jumping(self):
        self.is_jumping = False


player = Player()


class Projectile:
    def __init__(self, name, type, velocity, speed):
        self.player = player
        self.name = name
        self.type = type  # We might use different types of arrows for diffreent levels in the future
        self.velocity = velocity  # the actual at which the arrow is flying
        self.speed = speed  # the speed at which the flight trajectory is refreshed (between 0.1 and 1)
        self.clock = 0  # This will be used inside the trajectory equations
        self.image = pygame.image.load('../image/elements/test.jpg')
        self.rect = self.image.get_rect()
        self.basex = player.rect.x
        self.rect.x = 0
        self.basey = player.rect.y
        self.rect.y = 0
        self.angle = pi

    def firing_angle(self):
        if player.keys[pygame.K_UP]:
            self.angle += pi/180
        if player.keys[pygame.K_DOWN]:
            self.angle -= pi/180

    def flight(self, angle):
        self.rect.x = self.velocity * cos(angle) * self.clock + self.basex
        self.rect.y = 1/2 * Gravity * self.clock**2 + sin(angle) * self.clock + self.basey

        self.clock += self.speed