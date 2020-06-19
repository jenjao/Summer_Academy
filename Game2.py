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

### ********************* INSERT THIS LATER WHEN IT SAYS TO INSERT

'''
    SKIP SKIP SKIP
'''

# define a player object by extending pygame.sprite.Sprite
# the surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


############# SKIP ABOVE FIRST
    '''
        THEN ADD THE ONES WITH ###$$$$$$$$$$$$$$$
    '''

"""
"""


# initialize pygame
pygame.init()


# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# create screen object
# size is determined by the constant SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#############$$$$$$$$$$$$ SKIP THIS FOR NOW UNTIL LATER AFTER
''' SKIP SKIP SKIP '''

# Instantiate player. right now, this is just a rectangle.
player = Player()



### Setting Up the Game Loop


### Processing Events


# Variable to keep the main loop running
running = True


# Main loop
while running:
    #pygame.event.wait()
    
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
    
    #################$$$$$$$$$$$$$$$ CHANGE AFTER MAKING CLASS PLAYER
    """
        change screen to black (0, 0, 0)
    """
    
    # fill the screen with white
    #screen.fill((255, 255, 255))  #########$$$$$ CHANGE TO BLACK  
    screen.fill((0, 0, 0))
    
    
    ############# COMMENT LINES BETWEEN ####^^^^^^^^^
    
    """
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
    """
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
    
    """
    
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
    """
    
#pygame.quit()

    '''
        the reason why the image looks so off-center is that .blit() puts
        the top-left corner of surf at the location given.
        if you want surf to be centered, then youll have to do some math
        to shift it up and to the left. 
        
        you can do this by subtracting the width and the height of surf
        from the width and height of the screen, dividing each
        by 2 to locate the center, and then passing those numbers
        as arguments to screen.blit()
    '''
    
    
    ############^^^^^^^^^^^^^^^^^^ COMMENT AGAIN
    '''
    # put the center of surf at the center of the display
    surf_center = (
        (SCREEN_WIDTH - surf.get_width())/2,
        (SCREEN_HEIGHT - surf.get_height())/2
    )
    
    # Draw surf at the new coordinates
    screen.blit(surf, surf_center)
    pygame.display.flip()
    '''
    ########^^^^^^^^^^^^^^^^^^^^^^^
    
    '''
        ***** RUN ******
        ############ comment the pygame.display.flip() above to see both
        squares, then comment first screen.blit ###################
    '''
    
    '''
        notice the call to pygame.display.flip() after the call
        to blit(). this updates the entire screen with everything
        that's been drawn since the last flip
        
        without the call to .flip, nothing will be shown
    '''

    ''' *********** RUN ************* '''

#pygame.quit()


### SPRITES

    ''' 
    in our design, the player starts on the left and the obstacles come 
    from the right. we can represent all the obstacles with surface objects
    to make drawing everything easier, but how do we know where to draw them?
    
    how do we know if an obstacle has collided with the player?
    what happens when the obstacle flies off the screen?
    what if we want to draw background images that also move?
    what if we want our images to be animated?
    
    we can handle all these situation and more with SPRITES.
    
    in programming terms, sprite is a 2D representation of something on 
    the screen. Essentially its a picture.
    
    pygame provides a sprite class, which is designed to hold one
    or several graphical representations of any game object that we want
    to display on the screen.
    
    to use it, we can create a new class that extends sprite.
    
    this will allow us to use its built-in methods

    how will we use sprite objects with the current game to define the player?
    
    '''
    
################$$$$$$$$$$$$$$$ INSERT CODE BEFORE PYGAME.INIT
    '''
            class Player(pygame.sprite.Sprite):
                def __init__(self):
                super(Player, self).__init__()
                self.surf = pygame.Surface((75, 25))
                self.surf.fill((255, 255, 255))
                self.rect = self.surf.get_rect()
    '''
    '''
        we first define player by extending pygame.sprite.Sprite
        then .__init__() uses .super() to call the .__init__() method 
        for sprite.
        
        next, we define and initialize .surf to hold the image display,
        which is currently a white box. 
        
        we also define and initialize .rect, which we'll use to draw
        the player later. to use this new class, we need to create 
        a new object and change the drawing code as well.
    '''
    
##################$$$$$$$$$$$ INSERT AFTER screen = pygame.display.set
    '''
            # Instantiate player. right now, this is just a rectangle.
            player = Player()
    '''

#############$$$$$$$$$$$$ then change screen.fill to black
    
    
    
#######$$$$$$$$$$$$ then comment all screen.blit and continue:


    # draw player on screen
    #screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(player.surf, player.rect)
    
    #update display
    pygame.display.flip()

    ###### then change (SCREEN_WIDTH/2, SCREEN_HEIGHT/2) to 
                    # player.rect

    ''' 
        when we pass a rect to .blit, it uses the coordinates
        of the top left corner to draw the surface.
        
        we'll use this later to make our player move
    '''

pygame.quit()

































