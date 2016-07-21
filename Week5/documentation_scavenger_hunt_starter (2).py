"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PINK = (255,150,150)



pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE









# -------- Main Program Loop -----------
x_speed = 5
y_speed = 3
xpos = 350
ypos = 250
c = random.randint(5,90)
color_list = [BLACK , WHITE , GREEN , RED , BLUE , GREY , PINK]
index = 3


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    xpos+= x_speed
    ypos+= y_speed 

    # --- Game logic should go here
   
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here
    
    
    pygame.draw.circle(screen, color_list[index] , [x,y], size, 0)
    
    if xpos > 700:
        x_speed = -x_speed
        index = random.randint(0,6)
    if xpos < 0:
        x_speed = -x_speed
        index = random.randint(0,6)
    if ypos < 0:
        y_speed = -y_speed
        index = random.randint(0,6)
    if ypos > 500:
        y_speed = -y_speed
        index = random.randint(0,6)

        
    
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
