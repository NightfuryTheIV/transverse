from math import sin, cos, pi, radians, degrees
import pygame

class Character:
    def __init__(self, name, speed, x_pos, y_pos):
        self.name = name
        self.speed = speed
        self.x = x_pos
        self.y = y_pos
        self.angle = 0

    def __str__(self):
        return f"{self.name}: {self.speed} m/s of speed. Currently at ({self.x}; {self.y}) position"

    def movement(self, friction, gravity): # friction et gravité de la map
        while True: # faudra changer quand on aura construit quelque chose avec des events
            velocity = 0 
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity += self.speed
                    if event.key == pygame.K_LEFT:
                        velocity -= self.speed
                    if event.key == pygame.K_UP:
                        for i in range(0, 100):
                            t = i/10
                            self.y = -1/2 * gravity * t**2 + sin(pi/3) * velocity + self.y
                    
                    velocity *= friction
                    self.x += velocity
                
                


class Bullet:
    def __init__(self, x_pos, y_pos, bullet_name, weight):
        self.x = x_pos
        self.y = y_pos
        self.bullet = bullet_name
        self.weight = weight

    def fire(self, initial_pos, angle, gravity): # initial position et angle du joueur, gravité de la map
        while True: # pareil, faudra faire un truc avec les events
            radians = radians(angle)
            for i in range(0, 100):
                t = i/10
                self.y = -0.5 * gravity * t**2 + sin(radians) * 1 + initial_pos # va falloir voir pour v0 ici
                self.x = cos(radians) * t


class Map:
    def __init__(self, map_name, friction, gravity):
        self.map = map_name
        self.friction = friction
        self.gravity = gravity


class Button:
    def __init__(self, command, fontsize, text = "Click!", pos=[0, 0], color = (255, 255, 255)):
        self.command = command
        self.fontsize = fontsize
        self.text = text
        self.pos = pos
        self.color = color


    def clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1:
                self.command()