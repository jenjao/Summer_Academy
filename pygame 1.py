# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:32:24 2020

@author: user
"""

'''
    design some basic gameplay:
    - goal is to avoid obstacles
        - player starts on the left side of screen
        - obstacles enter randomly from the right
    - player can move left, right, up, down to avoid obstacles
    - player can't move off screen
    - game ends when player is hit or when user closes window

    some things that won't be covered:
        - no multiple lives
        - no score keeping
        - no player attack capabilities
        - no advancing levels
        - no boss characters
'''

# import pygame module

import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP, 
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,    
)

# initialize pygame
pygame.init()

# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create screen object
# size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

### Settng up the game loop

'''
    game loop:
        - processes the user input
        - updates state of all game object
        - updates the display and audio output
        - maintains the speed of the game
'''

'''
    frame - every cycle of the game loop
    
    end game loop:
        - player collides with obstacle
        - player closes the window
'''

### Processing Events

'''
    access list of all active events in the queue - pygame.event.get()
'''

# Variable to keep the main loop running
running = True

# main loop
while running:
    # look at every event in the queue
    for event in pygame.event.get():
        # if user hits a key
        if event.type == KEYDOWN:
            # if esc is hit, loop stops
            if event.key == K_ESCAPE:
                running = False
        
        # if user clicks the close window button, stop loop
        elif event.type == QUIT:
            running = False



pygame.quit()





























