from math import sin, cos, sqrt, atan2, degrees, radians

import pygame.mouse

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
        self.stand = False
        self.platfrom = False

    def jump(self):
        if self.stand:
            self.yspeed = -15
        self.yspeed += 0.2
        self.rect.y += self.yspeed
        self.stand = False

    def gravity(self):
        self.yspeed += 0.4
        self.rect.y += self.yspeed

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

            self.keys = pygame.key.get_pressed()

            # Adjust the direction based on key press
            if self.keys[pygame.K_LEFT]:
                self.xdirection = -3
            elif self.keys[pygame.K_RIGHT]:
                self.xdirection = 3
            else:
                self.xdirection = 0

            # Update character position only if within screen limits
            if 0 <= self.rect.x + self.xdirection <= 1250:
                self.rect.x += self.xdirection

            elif self.platfrom:
                self.stand = True
            elif not self.platfrom:
                self.stand = False

            # Apply gravity
            self.gravity()

            # Check for jumping and apply jump only when standing on a platform
            if self.keys[pygame.K_SPACE] and self.stand == True:
                self.jump()

            self.spike_interaction(spikelist)

    def no_slide(self):
        self.xmomentum = 600
        base_momentum = self.xmomentum
        while self.xmomentum != 0 and self.xmomentum > base_momentum/10000:
            print(self.xmomentum, self.xdirection)
            self.rect.x = self.rect.x - (self.xdirection/5) * (self.xmomentum/10)
            self.xmomentum *= 3/5

    def update2(self):
        if self.anim1:
            self.image = pygame.image.load('../image/character/run/run3.png')
        elif self.anim2:
            self.image = pygame.image.load('../image/character/run left/RUN_L_5.png')
        elif self.anim3:
            self.image = pygame.image.load('../image/character/jump/JUMP2.png')

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
    def __init__(self, name, type):
        self.player = player
        self.name = name
        self.type = type  # We might use different types of arrows for diffreent levels in the future
        self.velocity = 1  # the actual at which the arrow is flying
        self.speed = 0.1  # the speed at which the flight trajectory is refreshed (between 0.1 and 1)
        self.clock = 0  # This will be used inside the trajectory equations
        self.kunai_image = pygame.transform.scale(kunai, (60, 60))
        self.rect = self.kunai_image.get_rect()
        self.basex = player.rect.x
        self.rect.x = 0
        self.basey = player.rect.y
        self.rect.y = 0
        self.angle = 0
        self.kunai_rect = self.kunai_image.get_rect(center=(self.rect.x, self.rect.y))

    def show_projectile(self):
        screen.blit(self.kunai_image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    def get_distance(self, mousex, mousey):
        xcenter = abs(self.rect.bottom - self.rect.top)/2
        ycenter = abs(self.rect.right - self.rect.left)/2
        return round(sqrt((xcenter - mousex)**2 + (ycenter - mousey)**2))

    def flight(self, angle):
        g = 0.001
        self.rect.x = (self.velocity * cos(radians(angle)) * self.clock)*3 + self.basex
        self.rect.y = 1/2 * g * self.clock**2 + self.basey + sin(angle) * self.clock

        self.clock += self.speed
        self.kunai_rect.center = (self.rect.x, self.rect.y)
        print(self.rect.x, self.rect.y, cos(angle), sin(angle), self.clock, angle)

    def update_kunai(self):
        rotated_kunai = pygame.transform.rotate(self.kunai_image, 0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.rect.center = player.rect.center
                self.clock = 0
                self.basex = player.rect.centerx
                self.basey = player.rect.centery

                player_rect = self.rect
                dx, dy = mouse_x - player_rect.centerx, player_rect.centery - mouse_y
                self.angle = 1*degrees(atan2(-dy, dx))

                # Rotate the kunai image
                rotated_kunai = pygame.transform.rotate(self.kunai_image, self.angle)
                rotated_kunai_rect = rotated_kunai.get_rect(center=self.rect.center)

                # Set the initial velocity based on the angle
                self.velocity = abs(self.rect.centerx - mouse_x) / 1000

                # Now you can use 'rotated_kunai' and 'self.velocity' in your game logic
                # ...

                while 0 < self.rect.x < 1280 and 0 < self.rect.y < 720:
                    self.flight(self.angle)
                    screen.blit(rotated_kunai, self.kunai_rect)

        return rotated_kunai


def menu(cond):
    if cond:
        pass
    else:
        cond = False

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale_a, scale_b):
        super().__init__()
        self.image_name = image
        self.check = True
        self.image = pygame.transform.scale(image, (scale_a, scale_b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def name (self):
        if self.image_name == door1 :
            self.image_name = "door1"
        elif self.image_name == door2 :
            self.image_name = "door2"
        elif self.image_name == door3 :
            self.image_name = "door3"
        elif self.image_name == door4 :
            self.image_name = "door4"

    '''    def win(self,cond):
        if cond == True:

            pygame.mixer.music.load(win_music)
            pygame.mixer.music.play(-1)
            zommimg = pygame.transform.scale(victory,(int(victory.get_width() * 1.7), int(victory.get_height() * 1.7)))
            screen.blit(zommimg, (-20, -120))
        while cond == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Check if it's a keyboard event
                    if event.key == pygame.K_RETURN:
                        cond = False
                        menu_im(True)'''


    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self, player_rect):
        # Ajout d'une marge pour la détection de collision
        margin = 0
        # Vérifier si le rectangle du joueur chevauche le rectangle de la plateforme en ajoutant une marge
        return self.rect.colliderect(
            pygame.Rect(player_rect.left + margin, player_rect.top + margin, player_rect.width - margin * 2,
                        player_rect.height - margin * 2))

    def handle_collision(self, player):
        self.name()
        if self.check_collision(player.rect):
            # Si le joueur est en collision avec la plateforme depuis le bas et en train de tomber
            if player.yspeed >= 0 and player.rect.bottom >= self.rect.top > player.rect.top:
                player.rect.bottom = self.rect.top
                player.yspeed = 0
                player.platfrom = True
                player.stand = True
            elif not player.rect.bottom >= self.rect.top > player.rect.top:
                player.platfrom = False
            # Si le joueur est en collision avec la plateforme depuis le haut, arrêter son mouvement vertical
            elif player.yspeed < 0 and player.rect.bottom <= self.rect.top:
                player.rect.top = self.rect.bottom
                player.yspeed = 0
                player.platfrom = False
            # Si le joueur est en collision avec la plateforme depuis la gauche, arrêter son mouvement horizontal vers la droite
            if player.rect.colliderect(self.rect):
                # Check if player is moving right and collides from the left side of the platform
                if player.xdirection > 0 and player.rect.right >= self.rect.left > player.rect.left:
                    print("lol")
                    player.rect.right = self.rect.left
                    player.xdirection = 0
                    player.is_running = False

                # Check if player is moving left and collides from the right side of the platform
                elif player.xdirection < 0 and player.rect.left <= self.rect.right < player.rect.right:
                    print("lol")
                    player.rect.left = self.rect.right
                    player.xdirection = 0
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


