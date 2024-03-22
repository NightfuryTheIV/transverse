import pygame
import sys
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 1  # Set your desired frame rate here


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_healf = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('../image/perso.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity


class Button:
    def __init__(self, x, y, length, height, text, r, g, b):
        self.length = length
        self.height = height
        self.text = text
        self.rect = self
        self.color = (r, g, b)
        self.surface = pygame.Surface((length, height))

        font = pygame.font.Font(None, 24)
        text_act = font.render(self.text, True, self.color)
        text_rect = text_act.get_rect(center=(self.surface.get_width() / 2, self.surface.get_height() / 2))
        self.button_rect = pygame.Rect(x, y, length, height)  # Adjust the position as needed

        self.surface.blit(text_act, text_rect)

        # Draw the button on the screen
        screen.blit(self.surface, (self.button_rect.x, self.button_rect.y))

        easy = Button(525, 250, 210, 70, "Easy", 0, 0, 0)
        medium = Button(525, 350, 210, 70, "Medium", 0, 0, 0)
        hard = Button(525, 450, 210, 70, "Hard", 0, 0, 0)
        insane = Button(525, 550, 210, 70, "Insane", 0, 0, 0)
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

