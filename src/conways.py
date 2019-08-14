import pygame, random
import time

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 505

# dict with on/off state for each coordinate
cur_states = {'x': {205: 1, 230: 1, 255: 1}, 'y': {205: 1}}
next_states = {'x': {205: 1}, 'y': {205: 1, 230: 1, 255: 1}}

pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

s = 1
states = cur_states

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    x = 5
    while x < 500:
        y = 5
        while y < 500:
            if x in states['x'] and y in states['y']:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
            else:
                pygame.draw.rect(screen, GRAY, pygame.Rect(x, y, 20, 20))
            y += 25
        x += 25
        if x == 505:
            if s == 1:
                states = next_states
                s = 0
            else:
                states = cur_states
                s = 1
            x = 5
        time.sleep(1)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
