from typing import Tuple
import pgzrun
from random import randint
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


def on_mouse_down():
    print("Mouse button clicked")
def on_mouse_down(pos):
    print("Mouse button clicked at", pos)
def on_mouse_down(button):
    print("Mouse button", button, "clicked")
def on_mouse_down(pos, button):
    print("Mouse button", button, "clicked at", pos)

levels = list()

RED = 200, 0, 0
BOX = Rect((50, 300), (300, 150))

def draw():
    """Render everything on the screen once per frame"""

    # Clear the screen first
    screen.clear()  # noqa: F821

    # Set the background color to pink
    screen.fill("pink")  # noqa: F821


    level1 = Actor("level1", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)))
    level2 = Actor("level2", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)))
    level3 = Actor("level3", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)))
    level1.draw(), level2.draw(), level3.draw()
    




pgzrun.go()