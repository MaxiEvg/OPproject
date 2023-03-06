from typing import Tuple
import pgzrun


WIDTH = 1280
HEIGHT = 800

levels = []
player = Actor('alien_green_stand') 
player_position = WIDTH // 4, HEIGHT // 4
player.center = player_position

def on_mouse_move(pos: Tuple):
    """Called whenever the mouse changes position

    Arguments:
        pos {Tuple} -- The current position of the mouse
    """
    global player_position

    # Set the player to the mouse position
    player_position = pos
    

    # Ensure the player doesn't move off the screen
    if player_position[0] < 0:
        player_position[0] = 0
    if player_position[0] > WIDTH:
        player_position[0] = WIDTH

    if player_position[1] < 0:
        player_position[1] = 0
    if player_position[1] > HEIGHT:
        player_position[1] = HEIGHT

def update():
    
    global coin_countdown
    global coin_interval
    global limit
    global lvl
    global diff
    global settings
    

    player.center = player_position
    
    for level in levels:
        if player.colliderect(level1):
            print('выбран 1 уровень') 

            with open('diff.py',"w") as f:
                f.write("coin_countdown1 = 4; coin_interval1 = 0.5; limit = 0.86; lvl = 1")

            break
        if player.colliderect(level2):
            print('выбран 2 уровень')

            with open('diff.py',"w") as f:
                f.write("coin_countdown1 = 2; coin_interval1 = 0.3; limit = 0.7; lvl = 2")

            break
        if player.colliderect(level3):

            print('выбран 3 уровень')

            with open('diff.py',"w") as f:
                f.write("coin_countdown1 = 1; coin_interval1 = 0.2; limit = 0.5; lvl = 3")

            break
        
            

def draw():
    """Render everything on the screen once per frame"""

    # Clear the screen first
    screen.clear()  # noqa: F821

    # Set the background color to pink
    screen.blit("bg", (0, 0))  # noqa: F821

    global levels
    global level1
    global level2
    global level3

    level1 = Actor("level1", (150, 300) )
    level2 = Actor("level2", (500, 300) )
    level3 = Actor("level3", (850, 300) )
    levels = [level1, level2, level3]
    for i in levels:
        i.draw()
    
                
pgzrun.go()