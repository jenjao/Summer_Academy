#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:14:43 2020

@author: jenileejao
"""

''' 
    before writing code, its always good practice to have
    some design in place
    
    lets design some basic gameplay:
    - goal is to avoid obstacles
        - player starts on left side of screen
        - obstacles enter randomply from right
            and move left in a straight line
    - player can move left, right, up, down to avoid obstacles
    - player cant move off screen
    - game ends when player is hit or when user closes window
    
    here is some thing that wont be covered:
        - no multiple lives
        - no score keeping
        - no player attack capabilities
        - no advancing levels
        - no boss characters
'''

'''
    after importing, youll also need to initialize it
    
    this will allow pygame to connect its abstractions
    to your specific hardware
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

'''
    pygame library defines many things besides modules and classes
    it also defines some local constants for things like
    keystrokes, mouse movements, and display attributes
    
'''

'''
    now we need something to draw on
    
    so we create a screen
'''


# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# create screen object
# size is determined by the constant SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
''' 
    here you create the scrren to use by calling pygame.display.set_mode
    and passing a tuple or list with desired width and height
    
    in this case, the window is 800x600
    
    this returns a surface which represents the inside dimension of 
    the window and this is the portion of the window you can control
'''

'''
    if we run this code now, you'll see a window pop up breifly and
    then immediately disappear as the program exits.
    
    next, we'll focus on the main game loop to ensure that our program
    exits only when given the correct input
'''

#pygame.quit()


### Setting Up the Game Loop

''' every game from Pong to Fortnite uses a game loop to control gameplay
    the game loop does 4 very important things:
        - processes user input
        - updates state of all game object
        - updates the display and audio output
        - maintains the speed of the game
'''

'''
    every cycle of the game loop is called a frame
    and the quicker you can do things each cycle,
    the faster your game will run.
    
    frames will continue to occur until some condition to exit the game
    is met. in this design, there are two conditions that end
    the game loop:
        - player collides with obstacle
        - player closes window
'''

''' 
    the first thing the game loop does is process user input 
    to allow the player to move around the screen
    
    thus you need some way to capture and process a variety of input
    so we do this by using the pygame event system
'''


### Processing Events

''' 
    Key presses, mouse movements, and even joystick movements are some 
    of the ways in which a user can provide input. 
    All user input results in an event being generated. 
    Events can happen at any time and often (but not always) 
    originate outside the program. 
    All events in pygame are placed in the event queue,
    which can then be accessed and manipulated. 
    Dealing with events is referred to as handling them, 
    and the code to do so is called an event handler.

    Every event in pygame has an event type associated with it.
    For this game, the event types we'll focus on are keypresses 
    and window closure. 
    Keypress events have the event type KEYDOWN, 
    and the window closure event has the type QUIT.
    Different event types may also have other data associated with them. 
    For example, the KEYDOWN event type also has a variable called key 
    to indicate which key was pressed.

    You access the list of all active events in the queue 
    by calling pygame.event.get(). 
    You then loop through this list, 
    inspect each event type, and respond accordingly:
'''

# Variable to keep the main loop running
running = True

'''
    sets up a control variable for the game loop
    to exit the loop and the game, you set running = False
'''


# Main loop
while running:
    '''
        starts the event handler, walking thru every event currently
        in the even queue, if there are no events, 
        then list is empty and handler wont do anything
    '''
    # look at every event in the queue
    for event in pygame.event.get():
        
        #if user hit a key
        if event.type == KEYDOWN:
            #if esc is hit, stops the loop
            if event.key == K_ESCAPE:
                running = False
            '''
             check if the current event.type is a KEYDOWN event
             if it is, the program checks which key was pressed
             by looking at the event.key attribute
             
             if the key is the esc key, indicated by K_ESCAPE,
             then it exits the game loop by setting running to false
             '''
         
        #if user clicks the window close button, stop loop
        elif event.type == QUIT:
            running = False
        '''
            does a similar check for the event type called QUIT
            this event only occurs when the user clicks the 
            close window button or use any action to close the window
        '''
    
        '''
            here youll see a blank screen and it won't disappear
            until you press the esc key or trigger a quit event
        '''
    
    
pygame.quit()
    






































