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
    ######$$$$$$$$$$$$ INSERT LATER
    RLEACCEL,
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
        ##########$$$$$$$$$$$ INSERT LATER
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
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
        #####$$$$$$$$INSERT LATER
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
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
        
##############$$$$$$$$$$$$$$$$ INSERT LATER
# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
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
#########$$$$$$$$$$$$ INSERT LATER
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player. right now, this is just a rectangle.
player = Player()


# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
######$$$$$$$$$$ INSERT LATER
clouds = pygame.sprite.Group()
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
            
        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            
            
    pressed_keys = pygame.key.get_pressed()


    player.update(pressed_keys)
    
    # update enemy position
    enemies.update()
    
    clouds.update()

    # fill the screen with white 
    #screen.fill((0, 0, 0))
    screen.fill((135, 206, 250))

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
    and the enemies are too fast, we can't really avoid them
    
    so lets solve these problems one by one.
    
    first, lets replace all those boring white rectangles with some
    cooler images that will make the game feel like an actual game.
    
    So i want to use a jet and a missile for my images. you can download
    an image or make your own.  
'''

'''
    talk about how it needs to be in one folder
'''

'''
    talk about where to find images:
        we need:
            - player
            - enemy
            - background photo, like clouds, grass, whatever you want
            - if you do find an image you like for player, enemy or cloud,
              make sure it has .png
              extension and make sure it has a plain background because
              what we're gonna do is make the background invisible,
              so it can't have a patterend bacground
        
        we can all use the audio that I have but you are free to also
        look for the game audio that you want
        
        I want you to take the rest of the time alloted for today's lecture
        to start looking for one
            
'''
#############$$$$$$$$$$$$ INSERT BEFORE BEFORE BEFORE K_UP in pygame locals
'''
    from pygame.locals import (
        RLEACCEL,
        K_UP, ETC
    )
    
    This RLEACCEL is an optional parameter that helps pygame render
    more quickly on non-accelerated displays
'''

###########$$$$$$$$$$$$$$$$ INSERT IN PLAYER CLASS, AFTER super(player,self)

'''
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                super(Player, self) etc
    ####INSERT: self.surf = pygame.image.load("jet.png").convert()
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)
                
    COMMENT OUT: self.surf.fill AND self.surf = pygame.Surface
                
    First line pygame.image.load loads an image from the disk. 
    you pass it a path to the file.
    it returns a surface and the .convert call optimizes
    the surface, making future .blit() calls faster
    
    second line uses .set_colorkey() to indicate the color pygame
    will render as transparent.
    
    in this case, we'll choose white because that's the background
    color of the jet image.
    
    nothing else needs to change. the image is still a surface
    except now it has a picture painted on it.  

'''

######################$$$$$$$$$$$$ INSERT IN ENEMY CLASS after super(Enemy)
'''
    heres similar changes to the Enemy class
    
    self.surf = pygame.image.load("missile.png").convert()
    self.surf.set_colorkey((255, 255, 255), RLEACCEL)
    
    COMMENT OUT: self.surf.fill AND self.surf = pygame.Surface
    
    when we run this now, it should show that this is the same game
    we had before but except now, we've added some nice graphics skins
    with images
    
    ******************** RUN HERE

    but why stop at just making the player and enemy sprites look nice?
    lets add a few clouds going past to give the impression
    of a jet flying thru the sky
'''

### ADDING BACKGROUND IMAGES
'''
    For background clouds, you use the same principles as you did for 
    Player and Enemy:

    - Create the Cloud class.
    - Add an image of a cloud to it.
    - Create a method .update() that moves the cloud toward the left side 
    of the screen.
    - Create a custom event and handler to create new cloud objects 
    at a set time interval.
    - Add the newly created cloud objects to a new Group called clouds.
    - Update and draw the clouds in your game loop.

'''

############$$$$$$$$$$ INSERT AFTER ENEMY CLASS
'''
        # Define the cloud object extending pygame.sprite.Sprite
        # Use an image for a better looking sprite
        class Cloud(pygame.sprite.Sprite):
            def __init__(self):
                super(Cloud, self).__init__()
                self.surf = pygame.image.load("cloud.png").convert()
                self.surf.set_colorkey((0, 0, 0), RLEACCEL)
                # The starting position is randomly generated
                self.rect = self.surf.get_rect(
                    center=(
                        random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                        random.randint(0, SCREEN_HEIGHT),
                    )
                )
        
            # Move the cloud based on a constant speed
            # Remove it when it passes the left edge of the screen
            def update(self):
                self.rect.move_ip(-5, 0)
                if self.rect.right < 0:
                    self.kill()
'''

'''
    This should all look familiar it's pretty much the same as enemy
    
    to have clouds appear at certain intervals, we'll use event creation
    code similar to what we used to create new enemies
   
    
'''

#######$$$$$$$$$$$$$$$ INSERT AFTER pygame.time.set_timer(ADDENEMY, 250)
'''
            ADDCLOUD = pygame.USEREVENT + 2
            pygame.time.set_timer(ADDCLOUD, 1000)
        
    this says to wait 1000 milliseconds or one second
    before creating the next cloud
'''

'''
    next create a new group to hold each newly created cloud

'''

###$$$$$$$$$$$$$$$$$$$ INSERT AFTER enemies = pygame.sprite.Group()
'''
                clouds = pygame.sprite.Group()
'''

'''
    next add a handler for the new ADDCLOUD event in the event handler
'''

#$#############$$$$$$$$$$ INSERT AFTER LAST ELIF
'''
        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

'''

'''
    finally make sure clouds are updated every frame
'''

###########$$$$$$$$$$$$$ INSERT AFTER enemies.update()
'''
        clouds.update()
'''

'''
        then change screen.fill((135, 206, 250))
        sky blue
        
        you can change it to something else
        
        note that each new cloud and enemy are added to all_sprites
        as well as cloud and enemies
        
        this is done because each group is used for a separate purpose:
            - rendering is done using all_sprites
            - position updates are done using clouds and enemies
            - collision detection is done using enemies
            
        we create multiple groups so that we can change the way sprites
        move or behave without impacting the movement or behavior 
        of the other sprites
'''


pygame.quit()





























