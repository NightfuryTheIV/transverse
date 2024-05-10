from math import sin, cos, pi
from objects import *
pygame.mixer.init()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # All characteristics of character
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 2
        self.yspeed = 0
        self.image = pygame.image.load('../image/character/run/run1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 674
        self.is_running = False
        self.is_running_left = False
        self.is_jumping = False
        self.is_jumpingL = False
        self.is_dead = False
        self.dead_screen = False
        self.animationR_index = 0
        self.animationL_index = 0
        self.animationJ_index = 0
        self.animationJL_index = 0
        self.animationD_index = 0
        self.air_time = 0
        self.jump_delay = 10
        self.keys = {}
        self.menu_anim = False
        self.anim1 = False
        self.anim2 = False
        self.anim3 = False

    def update2(self):
        if self.anim1 :
            self.image = pygame.image.load('../image/character/run/run3.png')
        elif self.anim2 :
            self.image = pygame.image.load('../image/character/run left/RUN_L_5.png')
        elif self.anim3 :
            self.image = pygame.image.load('../image/character/jump/JUMP2.png')




    def jump(self):
        if self.rect.y > 674:
            self.yspeed = -10
        else:
            self.yspeed += 0.4
        self.rect.y += self.yspeed

    def gravity(self):
        self.yspeed += 0.4
        self.rect.y += self.yspeed

    def update(self):
        if not player.is_dead:
            if self.is_running and not self.is_jumping:
                # Update animation
                self.image = run_r[self.animationR_index]
                self.animationR_index = (self.animationR_index + 1) % len(run_r)
            elif self.is_running_left and not self.is_jumping:
                self.image = run_l[self.animationL_index]
                self.animationL_index = (self.animationL_index + 1) % len(run_l)
            elif self.is_jumping:
                if self.is_running:
                    # Jumping and running right animation
                    self.image = run_j[self.animationJ_index]
                elif self.is_running_left:
                    # Jumping and running left animation
                    self.image = jump_l[self.animationJL_index]
                else:
                    self.image = run_j[self.animationJ_index]
                if self.air_time % self.jump_delay == 0:
                    if self.is_running:
                        self.animationJ_index = (self.animationJ_index + 1) % len(run_j)
                    elif self.is_running_left:
                        self.animationJL_index = (self.animationJL_index + 1) % len(jump_l)
                    else:
                        self.animationJ_index = (self.animationJ_index + 1) % len(run_j)
                self.air_time += 1
            else:
                # Set default image if not running
                self.image = pygame.image.load('../image/character/run/run1.png')
        else :
            if self.animationD_index < len(death) - 1:  # Check if animationD_index is less than the total number of death frames
                self.image = death[self.animationD_index]
                self.animationD_index = (self.animationD_index + 1) % len(death)
            else:
                # Animation loop completed, reset animationD_index
                self.animationD_index = 0
                player.is_dead = False
                self.dead_screen = True





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
            if self.rect.y < 674:
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

