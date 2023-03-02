"""
Complete game in Pygame Zero

This game demonstrates some of the more advanced features of
Pygame Zero, including:
- Using sprites to render complex graphics
- Handling user input
- Sound output

"""

# Import pgzrun allows the program to run in Python IDLE
# You can also run the program from the command line using:
#   `pgzrun pygame_zero_basic.py`
import pgzrun

# For type-hinting support
from typing import Tuple

# To randomize coin placement
from random import randint

# Set the width and height of your output window, in pixels
WIDTH = 1280
HEIGHT = 800

# Set up the player
player = Actor("alien_green_stand")  # noqa: F82
player_position = WIDTH // 2, HEIGHT // 2
player.center = player_position

# Set up the coins to collect
COIN_COUNT = 9
coin_list = list()

SPIKE_COUN = 2
spike_list = list()
# Set up a timer to create new coins
coin_countdown = 2
coin_interval = 0.1

# Setup a timer for create new spike
spike_countdown = 4
spike_interval = 0.5

# Score is initially zero
score = 0
# Health is 5
health = 5
def add_spike():
    """should damage actor while touching
    """
    global spike_countdown
    
    new_spike = Actor(  # edited
        "spike", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)) # done
    )
    # Adds spike to a list
    spike_list.append(new_spike)
    
    if len(spike_list) < 3:
        spike_countdown -= spike_interval
    if spike_countdown < 1:
       spike_countdown = 50
       
    # Schedule the next spike addition
    clock.schedule(add_spike, spike_countdown) 

def add_coin():
    """Adds a new coin to playfield, then
    schedules the next coin to be added
    """
    global coin_countdown

    # Create a new coin Actor at a random location
    new_coin = Actor(  # noqa: F821
        "coin_gold", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10))
    )

    # Add it to the global coin list
    coin_list.append(new_coin)
    
    # Decrease the time between coin appearances if there are # fewer than three coins on the screen.
    if len(coin_list) < 3:
        coin_countdown -= coin_interval

    # Make sure you don't go too quickly
    if coin_countdown < 0.3:
        coin_countdown = 0.347

    # Schedule the next coin addition
    clock.schedule(add_coin, coin_countdown)  # noqa: F821


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

color_ = "white"

def update(delta_time: float):
    """Called every frame to update game objects

    Arguments:
        delta_time {float} -- Time since the last frame
    """
    global score
    global health 
    global color_

    # Update the player position
    player.center = player_position

    # Check if the player has collided with a coin or a spike
    # First, setting up a list of coins or a spike to remove 
    coin_remove_list = []
    spike_remove_list = []

    # Check each coin in the list for a collision
    for coin in coin_list:
        if player.colliderect(coin):
            sounds.coin_pickup.play()  # noqa: F821
            coin_remove_list.append(coin)
            score += 10

    # Check each spike in the list for a collision
    for spike in spike_list:
        if player.colliderect(spike):
            sounds.eep.play()  # edited
            spike_remove_list.append(spike)
            score -= 50
            health -=1
            if health > 3:
                color_ = "white"
            if health == 3:
                color_ = "yellow"
            elif health == 2:
                color_ = "orange"
            elif health == 1:
                color_ = "red"
        if len(spike_list) > 6:
                spike_remove_list.append(spike)          

    # Remove any coins with which you collided
    for coin in coin_remove_list:
        coin_list.remove(coin)
    # Remove any spike with which you collided
    for spike in spike_remove_list:
        spike_list.remove(spike)

    # The game is over when there are too many coins on the screen
    if len(coin_list) >= COIN_COUNT:
        # Stop making new coins
        clock.unschedule(add_coin)  # noqa: F821
        clock.unschedule(add_spike)
    elif health <=0:
        clock.unschedule(add_coin)
        clock.unschedule(add_spike)

        # Print the final score and exit the game
        print(f"Game over! Final score: {score}")
        exit()


def draw():
    """Render everything on the screen once per frame"""

    # Clear the screen first
    screen.clear()  # noqa: F821

    # Set the background color to pink
    screen.fill("pink")  # noqa: F821
    if len(coin_list) == 5:
        screen.fill("yellow")
    elif len(coin_list) == 6:
        screen.fill("orange")
    elif len(coin_list) == 7:
        screen.fill("red")
    elif len(coin_list) >= 8:
        screen.fill("black")
    
    # Draw the player
    player.draw()

    # Draw the remaining coins
    for coin in coin_list:
        coin.draw()
    for spike in spike_list:
        spike.draw()

    # Draw the current score at the bottom
    
    screen.draw.text(  # edited
        f"Score: {score}",
        (48, HEIGHT - 50),
        fontsize=60, shadow=(2,2), scolor="#202020",
        color="white", 
    )

    screen.draw.text(f"HP: {health}",
        (100, 100),
        fontsize=60,
        color=color_,
    )
   
    

# Schedule the first coin to appear
clock.schedule(add_coin, coin_countdown)  # noqa: F821
# Schedule the first spike to appear
clock.schedule(add_spike, spike_countdown) 
# Run the program
pgzrun.go()
