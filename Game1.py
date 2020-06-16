#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:25:36 2020

@author: jenileejao
"""

''' By the end of this program, you'll be able to 
    - draw items on your screen
    - play sound effects and music
    - handle user input
    - implement even loops
    - describe how game programming differs from standard procedural 
      python programming
'''

### Basic PyGame Program

''' before all the specifics, let's take a look at a basin pygame program
    --- here we will create a window, fill the background with white
        and draw a blue cirle in the middle of it
'''

# import and initialize the pygame library

import pygame
pygame.init()

'''
    without these, theres no pygame
'''


# set up the drawing window
screen = pygame.display.set_mode([500, 500])
'''
    sets up programs display window
    
    you provide either a list or tuple that specifies the width and height
    of the window to create
    
    this program uses a list to create a square window with 500 pix 
    on each side
'''


# run until the user asks to quit
running = True
while running:
    
    '''
        set up a game loop to control when the program ends
    '''
    
    # User clicks the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    '''
        scan and handle events within the game loop
        we'll get to events a bit later
        
        in this case the only event handled is pygame.quit
        and this occurs when the user clicks the close window button
    '''
            
    
    # Fill background with white
    screen.fill((255, 255, 255))
    
    '''
        fills window with a solid color.
        screen.fill accepts either list or tuple specifying
        the RGB values. 
        
        Change RGB colors (153, 50, 204)
    '''
    
    
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    
    '''
        draws a circle in the window using the ff parameters:
            - screen: window on which to draw
            - (0,0,225): tuple containing RGB color values
                ** change to (255, 192, 203) ***
            - (250, 250): tuple specifying hte center coordinates of circle
            - 75: radius of the circle in pixels
    '''
    
    
    # Flip the display
    pygame.display.flip()
    
    '''
        updates the contents of the display to the screen
        
        without this call, nothing will appear in the window
    '''
    
# Quit
pygame.quit()
'''
    exits pygame when loop finishes
'''    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    