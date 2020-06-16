#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:07:16 2020

@author: jenileejao
"""


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
# size is determined by the constant SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


### Setting Up the Game Loop


### Processing Events


# Variable to keep the main loop running
running = True


# Main loop
while running:
    # look at every event in the queue
    for event in pygame.event.get():
        
        #if user hit a key
        if event.type == KEYDOWN:
            #if esc is hit, stops the loop
            if event.key == K_ESCAPE:
                running = False
            
        #if user clicks the window close button, stop loop
        elif event.type == QUIT:
            running = False
    
    
############### CONTINUATION ####################

### Drawing on the Screen
'''
    we drew on the screen using
        - screen.fill() to fill the background
        - pygame.draw.circle() to draw a circle
        
    now youll learn about a third way to draw to the screen
    using a SURFACE
    
    Surface is a rectangular object on which you can draw
    like a blank sheet of paper
    the SCREEN object is a SURFACE and you can create
    your own SURFACE objects separate from the display screen

    lets see how that works
'''
    
# fill the screen with white
screen.fill((255, 255, 255))    

# create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))
'''
    new surface is created. this surface is 50 pixels wide
    50 pixels tall and assigned to surf
    
    at this point, you treat it just like the screen
'''


# give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()
'''
    we fill the surface with black and we can also access
    its underlying rect using .get_rect()
    this is stored as rect for later use
'''

### Using .blit() and .flip()

'''
    just creating a new surface is really not enough to see it on the screen
    to do this, we need to blit the surface onto another surface
    blit stands for block transfer and .blit() is how we copy
    the contents of one surface to another
    
    we can only .blit from one surface to another but since
    the screen is just another surface, its not a problem for this case

    heres how we draw surf on the screen
'''

# this line says "draw surf onto the screen at the center"
screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()
'''
    .blit() call takes two arguments:
        - the surface to draw
        - location at which to draw it on the source surface
    the coordinates (screenwidth and screenheight) tells the program
    to place surf in the exact center of the screen but it doesnt
    quite look that way
        *** run *** 
'''










































