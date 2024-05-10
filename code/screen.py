import sys
from technoblade import player
from objects import *


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Technoblade Trinity")
        pygame.display.set_icon(icon_image)
        self.clock = pygame.time.Clock()
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


class Button:
    def __init__(self, x, y, length, height, text, function, r, g, b, alpha=255):
        self.length = length
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x, y, length, height)
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

    def is_clicked(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)


def zoomimg_menu_background(scale):
    zommimg = pygame.transform.scale(background, (int(background.get_width() * scale), int(background.get_height() * scale)))
    screen.blit(zommimg, (0, 0))
    pygame.display.flip()


def zoomimg_menu_levels(scale):
    menu_im = pygame.transform.scale(menu, (int(menu.get_width() * scale), int(menu.get_height() * scale)))
    screen.blit(menu_im, (525, 280))
    pygame.display.flip()
    clock.tick(frame_rate)
    pygame.display.update()


def zoomimg_menu_title(scale):
    title_im = pygame.transform.scale(Title, (int(Title.get_width() * scale), int(Title.get_height() * scale)))
    screen.blit(title_im, (450, -30))


def zoomimg_player_old(scale):
    player_im = pygame.transform.scale(player.image, (int(Title.get_width() * scale), int(Title.get_height() * scale)))
    screen.blit(player_im, player.rect)


def zoomimg_level1_background(scale):
    Level1_im = pygame.transform.scale(level1_im, (int(Title.get_width() * scale), int(Title.get_height() * scale)))
    screen.blit(Level1_im, (0, -250))


def zoomimg_level2_background(scale):
    Level2_im = pygame.transform.scale(level2_im, (int(Title.get_width() * scale), int(Title.get_height() * scale)))
    screen.blit(Level2_im, (0, -490))


def zoomimg_level3_background(scale):
    Level3_im = pygame.transform.scale(level3_im, (int(Title.get_width() * scale), int(Title.get_height() * scale)))
    screen.blit(Level3_im, (0, -300))


def zoomimg_level4_background(scale):
    Level4_im = pygame.transform.scale(level4_im, (int(Title.get_width() * scale), int(Title.get_height() * scale)))
    screen.blit(Level4_im, (0, -500))

def zoomimg_player(scale_a, scale_b):
    rescaled_image1 = pygame.transform.scale(player.image, (scale_a, scale_b))
    screen.blit(rescaled_image1,player.rect)


def zoomimg_wight(image,scale_a,scale_b,x,y):
    rescaled_image = pygame.transform.scale(image, (scale_a, scale_b))
    screen.blit(rescaled_image, (x, y))


def zoomimg(image,scale,x,y):
    zommimg = pygame.transform.scale(image, (int(background.get_width() * scale), int(image.get_height() * scale)))
    screen.blit(zommimg, (x, y))

def life_update():
    if player.health == 100:
        zoomimg(green,0.2,1110,10)
    elif player.health == 67 :
        zoomimg(yellow, 0.2,1110,10)
    elif player.health == 34:
        zoomimg(red, 0.2,1110,10)


def buttons(bt1: Button, bt2: Button, bt3: Button, bt4: Button):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if bt1.is_clicked(mouse_x, mouse_y):
                    bt1.function(True)
                elif bt2.is_clicked(mouse_x, mouse_y):
                    bt2.function(True)
                elif bt3.is_clicked(mouse_x, mouse_y):
                    bt3.function(True)
                elif bt4.is_clicked(mouse_x, mouse_y):
                    bt4.function(True)

        pygame.display.update()
        clock.tick(frame_rate)


def anim_menu(cond):
    if cond:
        arrow_images = [arrow_1, arrow_2, arrow_3, arrow_4]
        for i in range(4):  # Loop through each animation step
            if i == 0:
                zoomimg(arrow_images[i], 0.3, 900, 500)
            elif i == 1:
                player.anim1 = False
                player.anim2 = False
                player.anim3 = True

            elif i == 2:
                player.anim3 = False
                player.anim1 = False
                player.anim2 = True
            elif i == 3:
                player.anim2 = False
                player.anim3 = False
                player.anim1 = True

            player.update2()
            zoomimg_menu_background(scale)
            zoomimg_menu_levels(scale2)
            zoomimg_menu_title(scale3)
            zoomimg(arrow_images[i], 0.3, 900, 500)
            screen.blit(player.image, (960, 300))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)
            pygame.time.delay(10)  # Add a delay between each animation step

        # Reset animation flags after the loop
        player.anim1 = False
        player.anim2 = False
        player.anim3 = False

        anim_menu(False)


def Menu(cond):
    if cond:
        pygame.mixer.music.load(menu_music)
        pygame.mixer.music.play(-1)  # Play the menu music in an infinite loop
        player.rect.x = 0
        player.rect.y = 660
        anim_menu(True)


        easy = Button(525, 275, 210, 70, "Easy", level1, 0, 0, 0, 255)
        medium = Button(525, 365, 210, 70, "Medium", level2, 0, 0, 0, 255)
        hard = Button(525, 460, 210, 70, "Hard", level3, 0, 0, 0, 255)
        insane = Button(525, 550, 210, 70, "Insane", level4, 0, 0, 0, 255)

        # Display buttons
        pygame.display.update()

        # Handle button events
        buttons(easy, medium, hard, insane)

    else:
        # Stop the music if the menu is deactivated
        pygame.mixer.music.stop()


def pause(level,cond):
    if cond:
        # Display the pause screen
        zoomimg_menu_background(1.7)
        screen.blit(pause_im, (400, 150))
        pygame.display.flip()
        clock.tick(frame_rate)

    while cond:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Menu(True)  # Go back to the menu
                elif event.key == pygame.K_b:
                    player.rect.x = 0
                    player.rect.y = 660
                    pause(level,False)  # Resume the game
                    level(True)
                elif event.key == pygame.K_c:
                    pause(level,False)  # Resume the game
                    level(True)


def dead_screen(level, cond):
    if cond:
        level(False)
        pygame.mixer.music.load(death_music)
        pygame.mixer.music.play(-1)
        zoomimg(yad, 1.7, 0, -120)
        zoomimg(button,0.7,385,350)
        pygame.display.flip()
        clock.tick(frame_rate)
    else:
        pygame.mixer.music.stop()
    while cond:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Check if it's a keyboard event
                if event.key == pygame.K_RETURN:
                    player.dead_screen = False
                    player.is_dead = False
                    dead_screen(level, False)
                    Menu(True)


def play_level_music(level_music,cond):
    if not cond:
        pygame.mixer.music.load(level_music)  # Load the specified music file
        pygame.mixer.music.play(-1)  # Play the music in an infinite loop
        cond = True
    else:
        pass

def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)



def level1(cond):
    Menu(False)
    play_level_music(level1_music, False)
    while cond:
        if player.dead_screen:
            pygame.mixer.music.stop()
            dead_screen(level1, True)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Menu(True)
                    level1(False)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and not event.key == pygame.K_SPACE:
                        player.start_runningR()
                    elif event.key == pygame.K_LEFT and not event.key == pygame.K_SPACE:
                        player.start_runningL()
                    elif event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_ESCAPE:
                        pause(level1, True)
                    elif event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_LEFT and event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT:
                        player.start_jumping()
                        player.start_runningL()
                    elif event.key == pygame.K_m:
                        player.is_dead = True
                    elif event.key == pygame.K_n:
                        get_mouse_position()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player.stop_runningR()
                    elif event.key == pygame.K_LEFT:
                        player.stop_runningL()
                    elif event.key == pygame.K_SPACE:
                        player.stop_jumping()

            player.update()

            # Update the screen
            zoomimg_level1_background(scale4)
            zoomimg_player(60, 60)
            life_update()
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)



def level2(cond):
    Menu(False)
    play_level_music(level2_music, False)
    while cond:
        if player.dead_screen:
            pygame.mixer.music.stop()
            dead_screen(level2, True)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Menu(True)
                    level2(False)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and not event.key == pygame.K_SPACE:
                        player.start_runningR()
                    elif event.key == pygame.K_LEFT and not event.key == pygame.K_SPACE:
                        player.start_runningL()
                    elif event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_ESCAPE:
                        pause(level2, True)
                    elif event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_LEFT and event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT:
                        player.start_jumping()
                        player.start_runningL()
                    elif event.key == pygame.K_m:
                        player.is_dead = True
                    elif event.key == pygame.K_n:
                        get_mouse_position()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player.stop_runningR()
                    elif event.key == pygame.K_LEFT:
                        player.stop_runningL()
                    elif event.key == pygame.K_SPACE:
                        player.stop_jumping()

            player.update()
            zoomimg_level2_background(scale6)
            zoomimg_player(60, 60)
            life_update()
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)


def level3(cond):
    Menu(False)
    play_level_music(level3_music, False)
    while cond:
        if player.dead_screen:
            pygame.mixer.music.stop()
            dead_screen(level3, True)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Menu(True)
                    level3(False)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and not event.key == pygame.K_SPACE:
                        player.start_runningR()
                    elif event.key == pygame.K_LEFT and not event.key == pygame.K_SPACE:
                        player.start_runningL()
                    elif event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_ESCAPE:
                        pause(level3, True)
                    elif event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_LEFT and event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT:
                        player.start_jumping()
                        player.start_runningL()
                    elif event.key == pygame.K_m:
                        player.is_dead = True
                    elif event.key == pygame.K_n:
                        get_mouse_position()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player.stop_runningR()
                    elif event.key == pygame.K_LEFT:
                        player.stop_runningL()
                    elif event.key == pygame.K_SPACE:
                        player.stop_jumping()

            player.update()
            zoomimg_level3_background(scale4)
            zoomimg_player(60, 60)
            life_update()
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)


def level4(cond):
    Menu(False)
    play_level_music(level4_music, False)
    while cond:
        if player.dead_screen:
            pygame.mixer.music.stop()
            dead_screen(level4, True)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Menu(True)
                    level4(False)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and not event.key == pygame.K_SPACE:
                        player.start_runningR()
                    elif event.key == pygame.K_LEFT and not event.key == pygame.K_SPACE:
                        player.start_runningL()
                    elif event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_ESCAPE:
                        pause(level4, True)
                    elif event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE and not event.key == pygame.K_LEFT:
                        player.start_jumping()
                    elif event.key == pygame.K_LEFT and event.key == pygame.K_SPACE and not event.key == pygame.K_RIGHT:
                        player.start_jumping()
                        player.start_runningL()
                    elif event.key == pygame.K_m:
                        player.is_dead = True
                    elif event.key == pygame.K_n:
                        get_mouse_position()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player.stop_runningR()
                    elif event.key == pygame.K_LEFT:
                        player.stop_runningL()
                    elif event.key == pygame.K_SPACE:
                        player.stop_jumping()

            player.update()
            zoomimg_level4_background(scale4)
            zoomimg_player(60, 60)
            life_update()
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)
