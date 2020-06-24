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

#import random for random numbers
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
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
# size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)


# instantiate player. Right now, it's just a rectangle
player = Player()

# create groups to hold enemy sprites and all sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

        # add a new enemy
        elif event.type == ADDENEMY:
            # create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
    pressed_keys = pygame.key.get_pressed()
    
    player.update(pressed_keys)
    
    # update enemy position
    enemies.update()

### drawing on the screen
    '''
        - screen.fill()
        - pygame.draw.circle()
        
        surface
    '''

    # fill the screen with white
    screen.fill((0, 0, 0))
    
    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # draw player on screen
    # screen.blit(player.surf, player.rect)
    pygame.display.flip()
    
### SPRITES
    
    '''
        - collided 
        - flies off the screen
        - background
        - animated
        
        sprite - 2D representation of something on the screen
    '''

# pygame.event.get()
# pygame.event.get_pressed()


### SPRITE GROUPS
'''
    two different group object:
        - will hold every sprite in the game
        - will hold just the enemy objects
'''

### CUSTOM EVENTS
'''
    two things:
        - create a new enemy
        - add it to all_sprites and enemies
'''

pygame.quit()
































            