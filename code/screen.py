import sys
from technoblade import player
from objects import *
from technoblade import Platform
from technoblade import menu
from technoblade import Projectile

class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Technoblade Trinity")
        pygame.display.set_icon(icon_image)
        self.clock = pygame.time.Clock()
        self.framerate = 120

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


def zoomimg_menu_levels(scale):
    menu_i = pygame.transform.scale(menu_im, (int(menu_im.get_width() * scale), int(menu_im.get_height() * scale)))
    screen.blit(menu_i, (525, 280))
    pygame.display.flip()
    clock.tick(frame_rate)
    pygame.display.update()


def zoomimg_player(scale_a, scale_b):
    screen.blit(player.image_knew, player.rect)
    player.update()


def zoomimg_wight(image,scale_a,scale_b,x,y):
    rescaled_image = pygame.transform.scale(image, (scale_a, scale_b))
    screen.blit(rescaled_image, (x, y))


def zoomimg(image,scale,x,y):
    zommimg = pygame.transform.scale(image, (int(background.get_width() * scale), int(image.get_height() * scale)))
    screen.blit(zommimg, (x, y))


def zoomimg_backgrounds(image,scale,x,y):
    zommimg = pygame.transform.scale(image, (int(Title.get_width() * scale), int(Title.get_width() * scale)))
    screen.blit(zommimg, (x, y))

def life_update():
    if player.health == 30:
        zoomimg(green,0.2,1110,10)
    elif player.health == 20:
        zoomimg(yellow, 0.2,1110,10)
    elif player.health == 10:
        zoomimg(red, 0.2,1110,10)


def buttons(bt1: Button, bt2: Button, bt3: Button, bt4: Button, arg1, arg2, arg3, arg4):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if bt1.is_clicked(mouse_x, mouse_y):
                    bt1.function(arg1)
                elif bt2.is_clicked(mouse_x, mouse_y):
                    bt2.function(arg2)
                elif bt3.is_clicked(mouse_x, mouse_y):
                    bt3.function(arg3)
                elif bt4.is_clicked(mouse_x, mouse_y):
                    bt4.function(arg4)

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
            zoomimg(background,1.7,0,0)
            zoomimg_menu_levels(scale2)
            zoomimg_backgrounds(Title,0.7,450,-30)
            zoomimg(arrow_images[i], 0.3, 900, 500)
            screen.blit(player.image, (960, 300))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)
            pygame.time.delay(1)  # Add a delay between each animation step

        # Reset animation flags after the loop
        player.anim1 = False
        player.anim2 = False
        player.anim3 = False

        anim_menu(False)

def menu_check():
    if menu(True):
        Menu(True)


def Menu(cond):
    if cond:
        pygame.mixer.music.load(menu_music)
        pygame.mixer.music.play(-1)  # Play the menu music in an infinite loop
        player.rect.x = 0
        player.rect.y = 650
        anim_menu(True)

        easy = Button(525, 275, 210, 70, "Easy", level1, 0, 0, 0, 255)
        medium = Button(525, 365, 210, 70, "Medium", level2, 0, 0, 0, 255)
        hard = Button(525, 460, 210, 70, "Hard", level3, 0, 0, 0, 255)
        insane = Button(525, 550, 210, 70, "Insane", level4, 0, 0, 0, 255)

        # Display buttons
        pygame.display.update()

        # Handle button events
        buttons(easy, medium, hard, insane, True, True, True, True)

    else:
        # Stop the music if the menu is deactivated
        pygame.mixer.music.stop()


def restarts(level):
    player.rect.x = 10
    player.rect.y = 660
    player.health = 30
    v = level1
    pause(v, False)
    level(True)


def pause(level, cond):
    resume = Button(517, 290, 115, 110, "Resume", level, 0, 0, 0, 255)
    restart = Button(660, 290, 115, 110, "Restart", restarts, 0, 0, 0, 255)
    back2menu = Button(660, 440, 115, 110, "Back to Menu", Menu, 0, 0, 0, 255)
    useless_button = Button(0, 0, 1, 1, "Hello There!", print, 0, 0, 0, 255)

    if cond:
        # Display the pause screen
        zoomimg(background,1.7,0,0)
        screen.blit(pause_im, (400, 150))
        pygame.display.flip()
        clock.tick(frame_rate)
        buttons(resume, restart, back2menu, useless_button, True, level, True, True)

    while cond:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if resume.is_clicked(mouse_x, mouse_y):
                    pause(level, False)  # Resume the game
                    resume.function(True)
                elif restart.is_clicked(mouse_x, mouse_y):
                    restart.function(True, level)
                elif useless_button.is_clicked(mouse_x, mouse_y):
                    pass
                elif back2menu.is_clicked(mouse_x, mouse_y):
                    back2menu.function(True)
                elif event.key == pygame.K_n:
                    get_mouse_position()



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
    player.rect.x = 60
    player.rect.y = 430
    play_level_music(level1_music, False)

    sol = Platform(-50, 670, block_long_l1, 1400, 100)

    platform2 = Platform(60, 490, block_long_l1, 120, 180)
    platform3 = Platform(0, 310, block_long_l1, 60, 700)
    platform4 = Platform(60, 310, block_long_l1, 120, 60)
    platform5 = Platform(180, 490, block_court_l1, 60, 60)
    platform6 = Platform(420, 370, block_court_l1, 60, 600)
    platform7 = Platform(660, 310, block_court_l1, 60, 600)
    platform8 = Platform(900, 370, block_court_l1, 60, 60)
    platform9 = Platform(1020, 370, block_long_l1, 300, 800)
    platform10 = Platform(1140, 310, block_court_l1, 100, 60)
    platform11 = Platform(1220, 200, block_court_l1, 60, 1000)
    platform12 = Platform(900, 130, block_court_l1, 180, 60)

    spike1 = Platform(180, 610, spike, 240, 60)
    spike2 = Platform(480, 610, spike, 180, 60)
    spike3 = Platform(720, 610, spike, 300, 60)
    spike4 = Platform(1020, 310, spike, 120, 60)

    laser_launcher_g = Platform(0, 250, laser_launcher1, 60, 60)
    door = Platform(960, 70, door1, 60, 60)


    while cond:
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
                elif event.key == pygame.K_v:
                    victory(True)


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.stop_runningR()
                elif event.key == pygame.K_LEFT:
                    player.stop_runningL()
                elif event.key == pygame.K_SPACE:
                    player.stop_jumping()

        if player.dead_screen:
            pygame.mixer.music.stop()
            dead_screen(level1, True)
        else:
            player.update()
            sol.handle_collision(player)

            platform2.handle_collision(player)
            platform3.handle_collision(player)
            platform4.handle_collision(player)
            platform5.handle_collision(player)
            platform6.handle_collision(player)
            platform7.handle_collision(player)
            platform8.handle_collision(player)
            platform9.handle_collision(player)
            platform10.handle_collision(player)
            platform11.handle_collision(player)
            platform12.handle_collision(player)

            spike1.handle_collision(player)
            spike2.handle_collision(player)
            spike3.handle_collision(player)
            spike4.handle_collision(player)

            laser_launcher_g.handle_collision(player)
            door.handle_collision(player)

            zoomimg_backgrounds(level1_im, 2.6, 0, -250)
            zoomimg_player(60, 60)
            po = Projectile("a", "r", 10, 10)
            po.show_projectile()
            po.update_kunai()
            sol.draw()

            platform2.draw()
            platform3.draw()
            platform4.draw()
            platform5.draw()
            platform6.draw()
            platform7.draw()
            platform8.draw()
            platform9.draw()
            platform10.draw()
            platform11.draw()
            platform12.draw()

            spike1.draw()
            spike2.draw()
            spike3.draw()
            spike4.draw()

            laser_launcher_g.draw()
            door.draw()

            pygame.draw.rect(screen, (255, 255, 255), player.rect, 2)
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
            dead_screen(level2, True),
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
            zoomimg_backgrounds(level2_im, 2.6, 0, -490)
            zoomimg_player(60, 60)
            life_update()
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)


def level3(cond):
    Menu(False)
    '''play_level_music(level3_music, False)'''

    sol = Platform(-50, 670, block_mid_l4, 1400, 100)


    laser_launcher_g = Platform(0, 250, laser_launcher1, 60, 60)
    door = Platform(960, 70, door3, 60, 60)

    while cond:
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
                elif event.key == pygame.K_v:
                    victory(True)


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.stop_runningR()
                elif event.key == pygame.K_LEFT:
                    player.stop_runningL()
                elif event.key == pygame.K_SPACE:
                    player.stop_jumping()

        if player.dead_screen:
            pygame.mixer.music.stop()
            dead_screen(level3, True)
        else:
            player.update()
            sol.handle_collision(player)

            laser_launcher_g.handle_collision(player)
            door.handle_collision(player)

            zoomimg_backgrounds(level3_im, 2.6, 0, -250)
            zoomimg_player(60, 60)
            sol.draw()

            laser_launcher_g.draw()
            door.draw()

            pygame.draw.rect(screen, (255, 255, 255), player.rect, 2)
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
            zoomimg_backgrounds(level4_im, 2.6, 0, -500)
            zoomimg_player(60, 60)
            life_update()
            pygame.display.flip()
            pygame.display.update()
            clock.tick(frame_rate)
