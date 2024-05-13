from math import sin, cos, pi
from objects import *
pygame.mixer.init()


spikelist = []


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # All characteristics of character
        self.health = 30
        self.max_health = 30
        self.attack = 10
        self.speed = 5
        self.yspeed = 0
        self.image = pygame.image.load('../image/character/run/run1.png')
        self.image_knew = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image_knew.get_rect()
        self.rect.x = 0
        self.rect.y = 670
        self.xdirection = 5
        self.yspeed = 0
        self.xmomentum = 0
        self.iframes = False
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
        if self.anim1:
            self.image = pygame.image.load('../image/character/run/run3.png')
        elif self.anim2:
            self.image = pygame.image.load('../image/character/run left/RUN_L_5.png')
        elif self.anim3:
            self.image = pygame.image.load('../image/character/jump/JUMP2.png')


    def on_platform(self):
        if self.rect.y > 670:
            return True
        else:
            return False

    def jump(self):
        if self.on_platform():
            self.yspeed = -10
        else:
            self.yspeed += 0.2
        self.rect.y += self.yspeed

    def gravity(self):
        self.yspeed += 0.4
        self.rect.y += self.yspeed

    def no_slide(self):
        self.xmomentum = 600
        base_momentum = self.xmomentum
        while self.xmomentum != 0 and self.xmomentum > base_momentum/10000:
            print(self.xmomentum, self.xdirection)
            self.rect.x = self.rect.x - (self.xdirection/5) * (self.xmomentum/10)
            self.xmomentum *= 3/5

    def spike_interaction(self, spikes):
        touches_spike = False
        i = 0

        while touches_spike is False and i < len(spikes):
            if spikes[i].touching():
                if not self.iframes:
                    self.health -= spikes[i].damage
                touches_spike = True
                self.iframes = True
            i += 1

        if touches_spike:
            self.no_slide()

    def update(self):
        if not player.is_dead:
            if self.is_running and not self.is_jumping:
                # Update animation
                self.image_knew = pygame.transform.scale(run_r[self.animationR_index], (60, 60))
                self.animationR_index = (self.animationR_index + 1) % len(run_r)
            elif self.is_running_left and not self.is_jumping:
                self.image_knew = pygame.transform.scale(run_l[self.animationL_index], (60, 60))
                self.animationL_index = (self.animationL_index + 1) % len(run_l)
            elif self.is_jumping:
                if self.is_running:
                    self.image_knew = pygame.transform.scale(run_j[self.animationJ_index], (60, 60))
                elif self.is_running_left:
                    self.image_knew = pygame.transform.scale(jump_l[self.animationJL_index], (60, 60))
                else:
                    self.image_knew = pygame.transform.scale(run_j[self.animationJ_index], (60, 60))
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
                self.image_knew = pygame.transform.scale(self.image, (60, 60))
        else:
            if self.animationD_index < len(death) - 1:
                self.image_knew = pygame.transform.scale(death[self.animationD_index], (60, 60))
                self.animationD_index = (self.animationD_index + 1) % len(death)
            else:
                player.is_dead = False
                self.dead_screen = True
        self.keys = pygame.key.get_pressed()

        # Adjust the direction based on key press
        if self.keys[pygame.K_LEFT]:
            self.xdirection = -5
        elif self.keys[pygame.K_RIGHT]:
            self.xdirection = 5
        else:
            self.xdirection = 0

        # Update character position only if within screen limits
        if 0 <= self.rect.x + self.xdirection <= 1250:
            self.rect.x += self.xdirection

        if self.keys[pygame.K_SPACE]:
            self.jump()
        else:
            if not self.on_platform():
                if self.rect.y < 668:
                    self.gravity()

        self.spike_interaction(spikelist)

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

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale_a, scale_b,):
        super().__init__()
        self.image = pygame.transform.scale(image, (scale_a, scale_b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self, player_rect):
        # Check if the player's rectangle overlaps with the platform's rectangle
        return self.rect.colliderect(player_rect)

    def handle_collision(self, player):
        if self.check_collision(player.rect):
            # If player is colliding with the platform from the bottom, stop their vertical movement
            if player.yspeed < 0 and player.rect.bottom <= self.rect.top:
                player.rect.bottom = self.rect.top
                player.yspeed = 0
            # If player is colliding with the platform from the top, stop their vertical movement
            elif player.yspeed > 0 and player.rect.top >= self.rect.bottom:
                player.rect.top = self.rect.bottom
                player.yspeed = 0
            # If player is colliding with the platform from the left, stop their horizontal movement
            elif player.rect.right > self.rect.left and player.rect.left < self.rect.right:
                player.rect.right = self.rect.left
                player.is_running = False
            # If player is colliding with the platform from the right, stop their horizontal movement
            elif player.rect.left < self.rect.right and player.rect.right > self.rect.left:
                player.rect.left = self.rect.right
                player.is_running_left = False


class GroundSpike:
    def __init__(self, x, y):
        self.damage = 10
        self.image = pygame.image.load('../image/elements/test.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 100
        self.rect.height = 10
        spikelist.append(self)

    def touching(self):
        if pygame.Rect.colliderect(self.rect, player.rect):
            return True
        else:
            return False


