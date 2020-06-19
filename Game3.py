# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:26:44 2020

@author: user
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:07:16 2020

@author: jenileejao
"""


# import pygame module
import pygame


# import random for random numbers
import random

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


# define a player object by extending pygame.sprite.Sprite
# the surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    #######$$$$$$$$$$$$$$ INSERT LATER WHEN PROMPTED
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
                
    ###########$$$$$$$$$$$$$$$ INSERT LATER WHEN PROMPTED
    # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# define the enemy object by extending pygame.sprite.Sprite
# the surface you draw on the screen is now an attribute of enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
        
     # move the sprite based on speed
     # remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
# initialize pygame
pygame.init()


# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create screen object
# size is determined by the constant SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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

    #######$$$$$$$$$$$$$$ INSERT LATER WHEN ASKED
    pressed_keys = pygame.key.get_pressed()


    #######$$$$$$$$ INSERT LATER WHEN ASKED
    player.update(pressed_keys)
    
    
### Drawing on the Screen

    # fill the screen with white 
    screen.fill((0, 0, 0))
    

### SPRITES

    # draw player on screen
    screen.blit(player.surf, player.rect)
    
    #update display
    pygame.display.flip()

############################ CONTINUATION ###########################
    
'''
    so far, we've learned how to set up pygame and draw objects on the screen
    now the real fun starts. we'll make the player controllable
    using the keyboard
    
    in earlier lectures you saw that pygame.event.get()
    returns a list of the events in the event queue, which we scan
    for KEYDOWN event types.
    
    well that's not the only way to read keypresses
    
    pygame also provides pygame.event.get_pressed(), which returns
    a dictionary containing all the current KEYDOWN events in the queue
    
'''

###########$$$$$$$$$$$$$$$ PUT THIS AFTER FOR LOOP BUT PART OF WHILE LOOP

''' 
        pressed_keys = pygame.key.get_pressed()
'''

##################$$$$$$$$$$ THEN THIS AFTER CLASS PLAYER 
        ########### IN LINE WITH DEF __init__
'''
        def update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
'''
    
'''
        K UP, K DOWN, LEFT AND RIGHT correspond to the arrow keys 
        on the keyboard
        if the dictionary entry for that key is True, then that key is down,
        and you move the player .rect in the proper direction
        
        here you use .move_ip which stands for MOVE IN PLACE to move
        the current rect
        
        then we can call .update every frame to move the player sprite 
        in response to keypresses
        
'''
    
###########$$$$$$$$$$$$$$$$$ ADD AFTER pressed_keys = .get_pressed()
'''
        player.update(pressed_keys)
'''    

'''
    but you might notice two small problems:
        - player rect can move very fast if a key is held down.
            well work on that later
        - player rect can move off screen. lets solve that now
'''

'''
    to keep player on screen, we need to add some logic to detect
    if the rect is going to move off screen.
    to do that, we need to check whether the rect coordinates
    have moved beyond the screens boundary.
    
    if so, then we instruct the program to move it back to the edge
'''

##########$$$$$$$$$$$$$$$$$ ADD AFTER def update
'''
        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
'''

'''
    here instead of using .move, you just change the corresponding 
    coordinates of .top, bottom, etc.
    
    so lets test it
    
    yay so it works
'''
    
#pygame.quit()

### ENEMIES

'''
    so now lets add some enemies.
    
    whats a game without enemies right?
    
    so we'll use the techniques weve already learned
    to creat a basic enemy class, then create a lot of 
    them for your player to avoid.
    
    first, we import the random library
'''

###########$$$$$$$$$$$$$$$ INSERT AFTER import pygame
'''
        # import random for random numbers
        import random
'''

##############$$$$$$$$$$$$$ INSERT AFTER class PLAYER
'''
# define the enemy object by extending pygame.sprite.Sprite
# the surface you draw on the screen is now an attribute of enemy
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.Surface((20, 10))
            self.surf.fill((255, 255, 255))
            self.rect = self.surf.get_rect(
                center = (
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                )
            )
            self.speed = random.randint(5, 20)
            
            # move the sprite based on speed
            # remove the sprite when it passes the left edge of the screen
            def update(self):
                self.rect.move_ip(-self.speed, 0)
                if self.rect.right < 0:
                    self.kill()
'''

pygame.quit()





























