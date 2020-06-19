# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:26:44 2020

@author: user
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


###########$$$$$$$$$$$$$$ INSERT WHEN PROMPTED

# create custom even for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. right now, this is just a rectangle.
player = Player()


#############$$$$$$$$$$$$$$$$$$ INSERT LATER

# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


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

        #############$$$$$$$$$$$ INSERT LATER
        # add a new enemy
        elif event.type == ADDENEMY:
            # create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            
            
    pressed_keys = pygame.key.get_pressed()


    player.update(pressed_keys)
    
    ########$$$$$$$$$$$$$$$$ INSERT LATER
    # update enemy position
    enemies.update()
    
### Drawing on the Screen

    # fill the screen with white 
    screen.fill((0, 0, 0))


#################$$$$$$$$$$$$$$$ INSERT LATER
    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

### SPRITES

    # draw player on screen
    #screen.blit(player.surf, player.rect)
    
    #update display
    pygame.display.flip()


### ENEMIES

############################ CONTINUATION ###########################
    
'''
# define the enemy object by extending pygame.sprite.Sprite
# the surface you draw on the screen is now an attribute of enemy
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.Surface((20, 10))
            self.surf.fill((255, 255, 255))
            
            %% self.rect = self.surf.get_rect(
                center = (
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                )
            %%)
            
            ^^ self.speed = random.randint(5, 20)
            
            # move the sprite based on speed
            # remove the sprite when it passes the left edge of the screen
            &&def update(self):
                self.rect.move_ip(-self.speed, 0)
                @@if self.rect.right < 0:
                    self.kill()
'''

'''
    there are four notable differences btween enemy and player
        - lines %%
            - you update rect to be a random location along the right
            edge of the screen.
            its located at some position between 20 and 100 pixels
            away from the right edge and somewhere between
            the top and bottom edges
        - line ^^
            - you define .speed as a random number between 5 and 20
            this specifies how fast this enemy moves toward the player
        - line && down
            - you define .update 
            it takes no arguments since enemies move automatically.
            instead, .update moves the enemy toward the left side
            of the screen at the .speed defined when it was created
        - line @@
            - you check whether the enemy has moved off screen
            - to make sure the enemy is fully off the screen and wont 
            disappear while sttill visible,
            you check that the right side of the .rect has gone past
            the left side of the screen.
            once the enemy is off screen, you can call .kill
            to prevent it from being processed futher.
        
        so what does .kill do? to figure this out, we'll have to 
        talk about sprite groups
    
'''

### SPRITE GROUPS
'''
    another super useful class that pygame provides is the sprite groups
    this is an object that hlds a group of sprite objects.
    so why use it?
    cant you just track your sprite objects in a list instead?
    well, you can but the advantage of using a goroup lies in the methods
    it exposes. 
    these methods help to detect whether an enemy has collided with the player
    which makes updates much easier
    
    lets see how to create sprite groups.
    
    youll create two different group objects:
        - first group will hold every sprite in the game
        - second will hold just the enemy objects
'''

#################$$$$$$$$$$$$$$$$ INSERT AFTER player = Player()
'''
        # create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        enemies = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
'''

'''
    when we call .kill, the sprite is removed from every group to which 
    it belongs. this removes the references to the sprite as well,
    which allows python's garbage collector to reclaim the memory
    as necessary
    
    now that you have all_sprites group, you can change how objects
    are drawn. instead of calling .blit on just Player,
    you can iterate over everything in all_sprites:
'''

################$$$$$$$$$$$$$$ INSERT AFTER screen.fill((0,0,0))
'''
        # draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            
        COMMENT OUT 
        scrren.blit(player.surf, player.rect)
'''

'''
    now anything put into all_sprites will be drawn with every frame,
    whether its an enemy or the player
    
    theres just one problem, you dont have enemies!
    you could create a bunch of enemies at the beginning of the game
    but the game would quickly become boring
    when they all left the screen a few seconds later.
    
    instead, lets explore how to keep a steady supply of enemies
    coming as the game progresses
'''

### CUSTOM EVENTS

'''
    The design calls for enemies to appear at regular intervals. 
    This means that at set intervals, you need to do two things:
        - Create a new Enemy.
        - Add it to all_sprites and enemies.

    You already have code that handles random events. The event loop 
    is designed to look for random events occurring every frame 
    and deal with them appropriately. Luckily, pygame doesn’t 
    restrict you to using only the event types it has defined. 
    You can define your own events to handle as you see fit.
    
    Let’s see how to create a custom event that’s generated every few seconds.
    You can create a custom event by naming it:
'''

########$$$$$$$$$$$$$$$$$$ INSERT "BEFORE" player = Player()
'''
        # create custom even for adding a new enemy        
        ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDENEMY, 250)
'''

'''
    pygame defines events internally as integers, so you need to define a 
    new event with a unique integer. The last event pygame reserves 
    is called USEREVENT, so defining ADDENEMY = pygame.USEREVENT + 1 
    on ensures it’s unique.

    Next, you need to insert this new event into the event queue at regular
    intervals throughout the game. That’s where the time module comes in.
    Line 84 fires the new ADDENEMY event every 250 milliseconds, 
    or four times per second. You call .set_timer() outside the game loop
    since you only need one timer, but it will fire throughout the entire game.
'''

##############$$$$$$$$$$$$$$$$$$$$$ INSERT AFTER ELIF, UNDER FOR LOOP
'''
        # add a new enemy
        elif event.type == ADDENEMY:
            # create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
'''

################$$$$$$$$$$$$$$$ INSERT AFTER player.update(pressed_keys)
'''
        # update enemy position
        enemies.update()
'''

'''
    Whenever the event handler sees the new ADDENEMY event on elif event.type 
    it creates an Enemy and adds it to enemies and all_sprites.
    Since Enemy is in all_sprites, it will get drawn every frame.
    You also need to call enemies.update() 
     which updates everything in enemies, to ensure they move properly:
'''

'''
    however thats not the only reason theres a group for just enemies
    we'll talk more about it tomorrow
'''
pygame.quit()





























