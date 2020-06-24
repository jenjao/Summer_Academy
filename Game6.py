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
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
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
            
            
# setup for sounds. 
pygame.mixer.init()
            
# initialize pygame
pygame.init()

############$$$$$$$$$$$$$ INSERT LATER
# setup the clock for a decent framerate
clock = pygame.time.Clock()

# define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create screen object
# size is determined by the constant SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# create custom even for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player. right now, this is just a rectangle.
player = Player()


# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")
                
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
        
    # check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # if so, then remove the player and stop the loop
        player.kill()
        
        # stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        
        running = False
    
    #update display
    pygame.display.flip()
    
    # ensures program maintains a rate of 30 frames per second
    clock.tick(30)

####################### CONTINUATION ###########################
 
'''
While testing the game you may have noticed that the enemies move 
a little fast. If not, then that’s okay, as different machines will see 
different results at this point.

The reason for this is that the game loop processes frames as fast 
as the processor and environment will allow. Since all the sprites move 
once per frame, they can move hundreds of times each second. 
The number of frames handled each second is called the frame rate, 
and getting this right is the difference between a playable game and 
a forgettable one.

Normally, you want as high a frame rate as possible, but for this game, 
you need to slow it down a bit for the game to be playable. 
Fortunately, the module time contains a Clock which is designed 
exactly for this purpose.

Using Clock to establish a playable frame rate requires 
just two lines of code. The first creates a new Clock before 
the game loop begins:
'''

########$$$$$$$$$$$$$$$$$$$$ INSERT AFTER pygame.init
'''
            # setup the clock for a decent framerate
            clock = pygame.time.Clock()

    the second calls .tick to inform pygame that the program
    has reached the end of the frame
'''

###########$$$$$$$$$$$$$ INSERT AFTER pygame.display.flip()
'''
            # ensures program maintains a rate of 30 frames per second
            clock.tick(30)
            
    
    The argument passed to .tick() establishes the desired frame rate. 
    To do this, .tick() calculates the number of milliseconds 
    each frame should take, based on the desired frame rate. 
    Then, it compares that number to the number of milliseconds that 
    have passed since the last time .tick() was called. 
    If not enough time has passed, then .tick() delays processing 
    to ensure that it never exceeds the specified frame rate.
    
    Passing in a smaller frame rate will result in more time in each 
    frame for calculations, while a larger frame rate provides smoother 
    (and possibly faster) gameplay:
        
    Play around with this number to see what feels best for you
    if you're using a mac, youll notice that it moves
    significantly slower, so you can adjust it and
    see how it changes

    *************** RUN HERE
'''



### SOUND EFFECTS

'''
    So far, you’ve focused on gameplay and the visual aspects of your game. 
    Now let’s explore giving your game some auditory flavor as well. 
    pygame provides mixer to handle all sound-related activities. 
    You’ll use this module’s classes and methods to provide background 
    music and sound effects for various actions.

    The name mixer refers to the fact that the module mixes various 
    sounds into a cohesive whole. Using the music sub-module, you can stream 
    individual sound files in a variety of formats, such as MP3, Ogg, and Mod.
    You can also use Sound to hold a single sound effect to be played, 
    in either Ogg or uncompressed WAV formats. All playback happens in 
    the background, so when you play a Sound, the method returns 
    immediately as the sound plays.
    
    As with most things pygame, using mixer starts with an 
    initialization step. Luckily, this is already handled by pygame.init().
    You only need to call pygame.mixer.init() if you want 
    to change the defaults:
'''


###########$$$$$$$$$$$$ INSERT BEFORE BEFORE BEFORE pygame.init()
'''
                # setup for sounds. 
                pygame.mixer.init()

    pygame.mixer.init() accepts a number of arguments, but the defaults 
    work fine in most cases. Note that if you want to change the defaults,
    you need to call pygame.mixer.init() before calling pygame.init(). 
    Otherwise, the defaults will be in effect regardless of your changes.

    After the system is initialized, you can get your sounds and 
    background music setup:
'''

#########$$$$$$$$$$$$ INSERT AFTER all_sprites.add(player)
'''
                # Load and play background music
                # Sound source: http://ccmixter.org/files/Apoxode/59262
                # License: https://creativecommons.org/licenses/by/3.0/
                pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
                pygame.mixer.music.play(loops=-1)
                
                # Load all sound files
                # Sound sources: Jon Fincher
                move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
                move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
                collision_sound = pygame.mixer.Sound("Collision.ogg")
'''

'''
    
    First and second lines load a background sound clip and begin playing it.
    You can tell the sound clip to loop and never end by setting the named 
    parameter loops=-1.

    Last three lines load three sounds you’ll use for various sound effects. 
    The first two are rising and falling sounds, which are played when the 
    player moves up or down. The last is the sound used whenever there 
    is a collision. You can add other sounds as well, such as a sound 
    for whenever an Enemy is created, or a final sound for when the game ends.

    ************* RUN
    
    So, how do you use the sound effects? You want to play each sound when 
    a certain event occurs. For example, when the ship moves up, you want 
    to play move_up_sound. Therefore, you add a call to .play() whenever 
    you handle that event. In the design, that means adding the following 
    calls to .update() for Player:
'''

#########$$$$$$$$$$$$$$ INSERT UNDER PLAYER def update(self, pressed_keys)
'''
            def update(self, pressed_keys):
                if pressed_keys[K_UP]:
                    self.rect.move_ip(0, -5)
#########INSERT     move_up_sound.play()
                if pressed_keys[K_DOWN]:
                    self.rect.move_ip(0, 5)
#########INSERT     move_down_sound.play()

'''

'''
    for a collision b/w the player and the enemy, you play the sound
    for when collisions are detected
'''

#############$$$$$$$$$$$$ INSERT AFTER player.kill() 
########################  BEFORE running = False
'''
        # stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        
    
    Here, you stop any other sound effects first, 
    because in a collision the player is no longer moving.
    Then you play the collision sound and continue execution from there.

    Finally, when the game is over, all sounds should stop. 
    This is true whether the game ends due to a collision or the user
    exits manually. To do this, add the following lines at the end 
    of the program after the loop:
'''



# All done! Stop and quit the mixer.
pygame.mixer.music.stop()


pygame.quit()





























