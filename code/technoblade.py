import pygame,sys


class Player(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_healf = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('../image/perso.png')
        self.rect= self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity




class technoblade:
    def __init__(self):
        self.player = Player()
        self.pressed = {}



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

    def pressed_check(self):
        clock.tick(60)
        screen.fill((0, 200, 255))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    print("YOOOOOOOOOOOOOOOOOOO")

        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.surface, self.color, (1, 1, self.length - 2, self.height - 2))
        else:
            pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.length, self.height))
            pygame.draw.rect(self.surface, (255, 255, 255), (1, 1, self.length - 2, self.height - 2))
            pygame.draw.rect(self.surface, (0, 0, 0), (1, 1, self.length - 2, 1), 2)
            pygame.draw.rect(self.surface, (0, 100, 0), (1, 48, self.length - 2, 10), 2)

        pygame.display.update()

        # DOES NOT DISPLAY THE BUTTON !!