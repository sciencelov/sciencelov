# main.py

import pygame
from pathlib import Path
import sys
from ball_simulation import Ball  # Make sure to import check_collision


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

# Parse the command line argument for the number of balls
num_balls = int(sys.argv[1]) if len(sys.argv) > 1 else 1
num_balls = 3

# Set the initial position for the first ball
initial_x = 100
initial_y = 150

# Set the vertical distance between each ball
vertical_distance = 70

# Create a list of Ball objects with vertical spacing
balls = [
    Ball(initial_x, initial_y + i * vertical_distance, 0, 0, 30, (35, 161, 224)) for i in range(num_balls)
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
    for i, ball in enumerate(balls):
        ball.update_position(GRAVITY_Y, DT, screen)

        # Check for collisions with other balls
        for other_ball in balls[i + 1:]:
            if ball.check_collision(other_ball):
                ball.resolve_collision(other_ball)

    pygame.display.flip()  # Update the display of the full screen
    clock.tick(60)  # Cap the frame rate at 60 frames per second

# End of the main loop
pygame.quit()  # Close Pygame
sys.exit()  # Exit the script

