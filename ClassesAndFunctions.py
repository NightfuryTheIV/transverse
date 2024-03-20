import pygame
import sys


class Button:
    def __init__(self, x, y,  length, height, font_size, text, r, g, b):
        self.length = length
        self.height = height
        self.text = text
        self.rect = self
        self.color = (r, g, b)
        self.font_size = font_size

        self.surface = pygame.Surface((length, height))

        font = pygame.font.Font(None, self.font_size)
        text_act = font.render(self.text, True, self.color)
        text_rect = text_act.get_rect(center=(self.surface.get_width() / 2, self.surface.get_height() / 2))
        self.button_rect = pygame.Rect(x, y, length, height)  # Adjust the position as needed

        # Shwo the button text
        self.surface.blit(text_act, text_rect)

        # Draw the button on the screen
        screen.blit(self.surface, (self.button_rect.x, self.button_rect.y))

    def pressed_check(self):
        clock.tick(60)
        screen.fill((0, 200, 255))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    print("YOOOOOOOOOOOOOOOOOOO")

        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(self.surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(self.surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(self.surface, (0, 100, 0), (1, 48, 148, 10), 2)

        pygame.display.update()

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Create a Pygame window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Clickable Button')

buttonss = Button(10, 10, 250, 150, 25, "hee hee", 0, 255, 255)
while True:
    buttonss.pressed_check()

