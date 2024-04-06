import pygame
# from technoblade import Button
Title = pygame.image.load('../image/TITLE.png')
menu = pygame.image.load('../image/menu.png')
background = pygame.image.load('../image/Fond.png')
pygame.display.set_caption("Technoblade Trinity")
scale=1.7
scale2=1
scale3=0.7
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 120  # Set your desired frame rate here

class Screen:

    def __init__(self):
        self.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Technoblade Trinity")
        self.clock =pygame.time.Clock()
        self.framerate = 60
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.display.fill((0, 0, 0))

    def get_size(self):
        return self.display.get_size()
    def get_display(self):
        return self.display


def zoomimg(scale):
    zommimg = pygame.transform.scale(background, (
    int(background.get_width() * scale), int(background.get_height() * scale)))
    screen.blit(zommimg, (0, 0))
    pygame.display.flip()
def zoomimg2(scale):
    Menu_im = pygame.transform.scale(menu, (int(menu.get_width() * scale2), int(menu.get_height() * scale2)))
    screen.blit(Menu_im, (525, 280))
    pygame.display.flip()
    clock.tick(frame_rate)
    pygame.display.update()
def zoomimg3(scale):
    Title_im = pygame.transform.scale(Title,
                                      (int(Title.get_width() * scale3), int(Title.get_height() * scale3)))
    screen.blit(Title_im, (450, -30))
    pygame.display.flip()
    clock.tick(frame_rate)
    pygame.display.update()


class Button:
    def __init__(self, x, y, length, height, text, r, g, b, alpha=255):
        self.length = length
        self.height = height
        self.text = text
        self.rect = self
        self.color = (r, g, b)
        self.surface = pygame.Surface((length, height), pygame.SRCALPHA)
        self.surface.set_alpha(alpha)

        font = pygame.font.Font(None, 0)
        text_act = font.render(self.text, True, (self.color[0], self.color[1], self.color[2], alpha))
        text_rect = text_act.get_rect(center=(self.surface.get_width() / 2, self.surface.get_height() / 2))
        self.button_rect = pygame.Rect(x, y, length, height)  # Adjust the position as needed

        self.surface.blit(text_act, text_rect)

        # Draw the button on the screen
        screen.blit(self.surface, (self.button_rect.x, self.button_rect.y))

    def pressed_check(self, mouse_x, mouse_y):
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("MMMMMMM")
                if self.button_rect.collidepoint(mouse_x, mouse_y):
                    print(self.text)

        print(mouse_x, mouse_y)


"""
            # DOES NOT DISPLAY THE BUTTON !
            pygame.display.update()
"""


def Menu(cond):
    if cond:
        zoomimg(scale)
        zoomimg2(scale2)
        zoomimg3(scale3)
        easy = Button(525, 275, 210, 70, "Easy", 0, 0, 0,255)
        medium = Button(525, 365, 210, 70, "Medium", 0, 0, 0,255)
        hard = Button(525, 460, 210, 70, "Hard", 0, 0, 0,255)
        insane = Button(525, 550, 210, 70, "Insane", 0, 0, 0,255)

        for i in range(50):
            easy.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            medium.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            hard.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            insane.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
