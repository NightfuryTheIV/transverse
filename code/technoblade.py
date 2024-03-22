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


class Button:
    def __init__(self, x, y, length, height, text, r, g, b, alpha=255):
        self.length = length
        self.height = height
        self.text = text
        self.rect = self
        self.color = (r, g, b)
        self.surface = pygame.Surface((length, height), pygame.SRCALPHA)
        self.surface.set_alpha(alpha)

        font = pygame.font.Font(None, 24)
        text_act = font.render(self.text, True, (self.color[0], self.color[1], self.color[2], alpha))
        text_rect = text_act.get_rect(center=(self.surface.get_width() / 2, self.surface.get_height() / 2))
        self.button_rect = pygame.Rect(x, y, length, height)  # Adjust the position as needed

        self.surface.blit(text_act, text_rect)

        # Draw the button on the screen

    def pressed_check(self):
        clock.tick(60)

        for events in pygame.event.get():
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                if self.button_rect.collidepoint(events.pos):
                    print(self.text)

        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.surface, self.color, (1, 1, self.length - 2, self.height - 2))
            print(self.text)
        else:
            pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.length, self.height))
            pygame.draw.rect(self.surface, (255, 255, 255), (1, 1, self.length - 2, self.height - 2))
            pygame.draw.rect(self.surface, (0, 0, 0), (1, 1, self.length - 2, 1), 2)
            pygame.draw.rect(self.surface, (0, 100, 0), (1, 48, self.length - 2, 10), 2)

        pygame.display.update()

        # DOES NOT DISPLAY THE BUTTON !!

class technoblade:
    def __init__(self):
        self.player = Player()
        self.pressed = {}

