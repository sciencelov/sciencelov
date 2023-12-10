# main.py

import pygame
from pathlib import Path
import sys
from ball_simulation import Ball

# Initialize PyGame
pygame.init()

# Initial window size
s_width = 600
s_height = 800

# Define spacetime 
GRAVITY_Y = 0.3
DT = 1  # ms (discretization of time)

# Making display screen
screen = pygame.display.set_mode((s_width, s_height), pygame.RESIZABLE)
bg_orig = pygame.image.load(Path(__file__).parents[0] / Path("bkg.jpg")).convert()
clock = pygame.time.Clock()

# Setup 
running = True

# Parse command-line arguments to determine the number of balls and their properties
num_balls = int(sys.argv[1]) if len(sys.argv) > 1 else 1
balls = [
    Ball(100 + i * 50, 150, 0, 0, 30, (35, 161, 224)) for i in range(num_balls)
]

# Main event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # End the loop when the ESC key is pressed

    # Adjust screen size and redraw background image
    s_width, s_height = screen.get_width(), screen.get_height()
    bg = pygame.transform.scale(bg_orig, (s_width, s_height))
    screen.blit(bg, (0, 0))  # redraws background image

    # Update and draw all balls
    for ball in balls:
        ball.update_position(GRAVITY_Y, DT, screen)

    pygame.display.flip()  # Update the display of the full screen
    clock.tick(60)  # Cap the frame rate at 60 frames per second

# End of the main loop
pygame.quit()  # Close Pygame
sys.exit()  # Exit the script
