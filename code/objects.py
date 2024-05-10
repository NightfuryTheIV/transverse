import pygame
pygame.mixer.init()

# Menu images and settings :
icon_image = pygame.image.load('../image/menu/game_image.jpg')
Title = pygame.image.load('../image/menu/TITLE.png')
menu = pygame.image.load('../image/menu/menu.png')
background = pygame.image.load('../image/menu/Fond.png')
pygame.display.set_caption("Technoblade Trinity")

# Levels background images :
level1_im = pygame.image.load('../image/levels/niv 1 jour.png')
level2_im = pygame.image.load('../image/levels/level2.png')
level3_im = pygame.image.load('../image/levels/level3.png')
level4_im = pygame.image.load('../image/levels/level4.png')

# Health bar :
green = pygame.image.load('../image/elements/life bar/health_bar_green.png')
yellow = pygame.image.load('../image/elements/life bar/health_bar_yellow.png')
red = pygame.image.load('../image/elements/life bar/health_barred.png')

# Pause buttons image:
pause_im = pygame.image.load('../image/menu/pause.png')

# Y ou are dead images :
yad = pygame.image.load('../image/character/death/you_are_dead.jpeg')
button = pygame.image.load('../image/character/death/button.png')

# Menu game arrows :
arrow_1 = pygame.image.load('../image/menu/1.png')
arrow_2 = pygame.image.load('../image/menu/2.png')
arrow_3 = pygame.image.load('../image/menu/3.png')
arrow_4 = pygame.image.load('../image/menu/4.png')

# Scales :
scale = 1.7
scale2 = 1
scale3 = 0.7
scale4 = 2.6
scale5 = 0.1
scale6 = 2.6
scale7 = 2.6
scale8 = 2.6

# Musics :
death_music = "../music/death_music.mp3"
menu_music = "../music/Menu_music.mp3"
level1_music = "../music/Easy_music.mp3"
level2_music = "../music/Medium_music.mp3"
level3_music = "../music/Hard_music.mp3"
level4_music = "../music/Insane_music.mp3"

# Screen settings :
screen = pygame.display.set_mode((1280, 730))
clock = pygame.time.Clock()  # Creating a clock object for controlling the frame rate
frame_rate = 120  # Set your desired frame rate here

# Run images :
run_1 = pygame.image.load('../image/character/run/run1.png')
run_2 = pygame.image.load('../image/character/run/run2.png')
run_3 = pygame.image.load('../image/character/run/run3.png')
run_4 = pygame.image.load('../image/character/run/run4.png')
run_5 = pygame.image.load('../image/character/run/run5.png')
run_6 = pygame.image.load('../image/character/run/run6.png')

# Run left images :
run_7 = pygame.image.load('../image/character/run left/RUN_L_1.png')
run_8 = pygame.image.load('../image/character/run left/RUN_L_2.png')
run_9 = pygame.image.load('../image/character/run left/RUN_L_3.png')
run_10 = pygame.image.load('../image/character/run left/RUN_L_4.png')
run_11 = pygame.image.load('../image/character/run left/RUN_L_5.png')

# Jump right images :
jump_1 = pygame.image.load('../image/character/jump/JUMP1.png')
jump_2 = pygame.image.load('../image/character/jump/JUMP2.png')
jump_3 = pygame.image.load('../image/character/jump/JUMP3.png')
jump_4 = pygame.image.load('../image/character/jump/JUMP4.png')
jump_5 = pygame.image.load('../image/character/jump/JUMP5.png')
jump_6 = pygame.image.load('../image/character/jump/JUMP6.png')
jump_77 = pygame.image.load('../image/character/jump/JUMP7.png')

# Jump left images :
jump_7 = pygame.image.load('../image/character/JUMP_L/image (1).png')
jump_8 = pygame.image.load('../image/character/JUMP_L/image (2).png')
jump_9 = pygame.image.load('../image/character/JUMP_L/image (3).png')
jump_10 =pygame.image.load('../image/character/JUMP_L/image (4).png')
jump_11 = pygame.image.load('../image/character/JUMP_L/image (5).png')
jump_12 = pygame.image.load('../image/character/JUMP_L/image (6).png')
jump_13 = pygame.image.load('../image/character/JUMP_L/image (7).png')

# Death images :
death_1 = pygame.image.load('../image/character/death/death1.png')
death_2 = pygame.image.load('../image/character/death/death2.png')
death_3 = pygame.image.load('../image/character/death/death3.png')
death_4 = pygame.image.load('../image/character/death/death4.png')
death_5 = pygame.image.load('../image/character/death/death5.png')
death_6 = pygame.image.load('../image/character/death/death6.png')
death_7 = pygame.image.load('../image/character/death/death7.png')
death_8 = pygame.image.load('../image/character/death/death8.png')
death_9 = pygame.image.load('../image/character/death/death9.png')

# Animations dictionaries :
run_r=[run_1,run_2,run_3,run_4,run_5,run_6]
run_l= [run_7,run_8,run_9,run_10,run_11]
run_j= [jump_1,jump_2,jump_3,jump_4,jump_5,jump_6,jump_77]
jump_l = [jump_7,jump_8,jump_9,jump_10,jump_11,jump_12,jump_13]
death = [death_1,death_1,death_1,death_2,death_2,death_2,death_3,death_3,death_3,death_4,death_4,death_4,death_5,death_5,death_5,death_6,death_6,death_6,death_7,death_7,death_7,death_8,death_8,death_9,death_9,death_9]
Gravity = 9.81

TEST = pygame.image.load('../image/character/image (1).jpg')