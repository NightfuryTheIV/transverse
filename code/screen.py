import pygame
import sys
from technoblade import Player
from technoblade import technoblade
player = Player()
Title = pygame.image.load('../image/TITLE.png')
menu = pygame.image.load('../image/menu.png')
background = pygame.image.load('../image/Fond.png')
pygame.display.set_caption("Technoblade Trinity")
level1_im = pygame.image.load('../image/niv 1 jour.png')
scale=1.7
scale2=1
scale3=0.7
scale4=2.6
scale5=0.1
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 120  # Set your desired frame rate here
player = Player()
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
    Title_im = pygame.transform.scale(Title, (int(Title.get_width() * scale3), int(Title.get_height() * scale3)))
    screen.blit(Title_im, (450, -30))
    pygame.display.flip()
    clock.tick(frame_rate)
    pygame.display.update()
def zoomimg4(scale):
    Level_im = pygame.transform.scale(level1_im, (int(Title.get_width() * scale4), int(Title.get_height() * scale4)))
    screen.blit(Level_im, (0, 0))
    pygame.display.flip()
    clock.tick(frame_rate)
    pygame.display.update()
def zoomimg5(scale):
    player_im = pygame.transform.scale(player.image, (int(Title.get_width() * scale5), int(Title.get_height() * scale5)))
    screen.blit(player_im, player.rect)
    pygame.display.flip()
    clock.tick(frame_rate)
    pygame.display.update()
class Button:
    def __init__(self, x, y, length, height, text, function, r, g, b, alpha=255):
        self.length = length
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x, y, length, height)  # Rect representing button position and size
        self.function = function
        self.color = (r, g, b)
        self.surface = pygame.Surface((length, height), pygame.SRCALPHA)
        self.surface.set_alpha(alpha)

        font = pygame.font.Font(None, 0)
        text_act = font.render(self.text, True, (self.color[0], self.color[1], self.color[2], alpha))
        text_rect = text_act.get_rect(center=(self.surface.get_width() / 2, self.surface.get_height() / 2))
        self.surface.blit(text_act, text_rect)

        # Draw the button on the screen
        screen.blit(self.surface, (x, y))

    def pressed_check(self, mouse_x, mouse_y):
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect.collidepoint(mouse_x, mouse_y):
                        self.function(True)  # Call the button function
                        return True
        return False  # Return False if no events are handled


def buttons(bt1:Button, bt2:Button, bt3:Button, bt4:Button):
    p1, p2, p3, p4 = False, False, False, False  # These variables are used to determine when a button is clicked and will serve to break the loop

    while not p1 and not p2 and not p3 and not p4:
        p1 = bt1.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        p2 = bt2.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        p3 = bt3.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        p4 = bt4.pressed_check(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        # print(p1, p2, p3, p4)
def Menu(cond):
    if cond:
        zoomimg(scale)
        zoomimg2(scale2)
        zoomimg3(scale3)
        pygame.display.flip()

        easy = Button(525, 275, 210, 70, "Easy", level1, 0, 0, 0, 255)  # Example function print
        medium = Button(525, 365, 210, 70, "Medium", print, 0, 0, 0, 255)  # Example function print
        hard = Button(525, 460, 210, 70, "Hard", print, 0, 0, 0, 255)  # Example function print
        insane = Button(525, 550, 210, 70, "Insane", print, 0, 0, 0, 255)  # Example function print

        # Display buttons
        pygame.display.update()

        # Handle button events
        buttons(easy, medium, hard, insane)


def level1(cond):
    while cond:
        Menu(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Menu(True)
                level1(False)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.pressed["UP"] = True
                elif event.key == pygame.K_DOWN:
                    player.pressed["DOWN"] = True
                elif event.key == pygame.K_LEFT:
                    player.pressed["LEFT"] = True
                elif event.key == pygame.K_RIGHT:
                    player.pressed["RIGHT"] = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.pressed["UP"] = False
                elif event.key == pygame.K_DOWN:
                    player.pressed["DOWN"] = False
                elif event.key == pygame.K_LEFT:
                    player.pressed["LEFT"] = False
                elif event.key == pygame.K_RIGHT:
                    player.pressed["RIGHT"] = False

        # Update the screen
        zoomimg4(scale4)
        player.update()
        zoomimg5(scale5)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(frame_rate)

