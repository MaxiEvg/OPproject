from typing import Tuple
import pgzrun


WIDTH = 1280
HEIGHT = 800



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




def draw_level():
    """Render everything on the screen once per frame"""

    # Clear the screen first
    screen.clear()  # noqa: F821

    # Set the background color to pink
    screen.fill("pink")  # noqa: F821


    level1 = Actor("level1", (150, 300) )
    level2 = Actor("level2", (500, 300) )
    level3 = Actor("level3", (850, 300) )
    levels = [level1, level2, level3]
    for i in levels:
        i.draw()
                




pgzrun.go()