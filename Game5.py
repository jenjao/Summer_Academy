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


# create custom even for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. right now, this is just a rectangle.
player = Player()


# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


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
    
    # update enemy position
    enemies.update()
    
    # fill the screen with white 
    screen.fill((0, 0, 0))

    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        
########$$$$$$$$$$$$$$$$$ INSERT LATER
    # check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # if so, then remove the player and stop the loop
        player.kill()
        running = False
    
    #update display
    pygame.display.flip()

####################### CONTINUATION ###########################
 
'''
   Your game design calls for the game to end whenever an enemy collides 
   with the player. Checking for collisions is a basic technique 
   of game programming, and usually requires some non-trivial math 
   to determine whether two sprites will overlap each other.
    
    This is where a framework like pygame comes in handy! Writing collision
    detection code is tedious, but pygame has a LOT of collision detection 
    methods available for you to use.
    
    We'll use a method called .spritecollideany(), which is read as 
    “sprite collide any.” This method accepts a Sprite and a Group as
    parameters. It looks at every object in the Group and checks if its 
    .rect intersects with the .rect of the Sprite. 
    If so, then it returns True. 
    Otherwise, it returns False. 
    This is perfect for this game since you need to check if the 
    single player collides with one of a Group of enemies.
'''

##############$$$$$$$$$$$$$$$ INSERT AFTER for entity in all_sprites
'''
        # check if any enemies have collided with the player
        @@if pygame.sprite.spritecollideany(player, enemies):
            # if so, then remove the player and stop the loop
            player.kill()
            running = False
'''

'''
    line @@
        - tests whether player has collided with any of the objects in enemies
         If so, then player.kill() is called to remove it from every group 
         to which it belongs. Since the only objects being rendered 
         are in all_sprites, the player will no longer be rendered. 
         
         Once the player has been killed, you need to exit the game as well
         so you set running = False to break out of the game loop 
'''
'''
    at this point, weve got the basic elements of a game in place
'''

'''
    now lets dress it up a bit, make it more playable and add some
    advanced capabilities to help it stand out
'''

### SPRITE IMAGES
'''
    alright, we have a game but lets be honest, its ugly
    the player and enemies are just white blocks on a black background
    
    so lets replace all those boring white rectangles with some
    cooler images that will make the game feel like an actual game.
    
    So i want to use a jet and a missile for my images. you can download
    an image or make your own.  
'''

pygame.quit()





























