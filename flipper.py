# flipper.py

import pygame

class Flipper:
    def __init__(self, x, y, width, height, color, key):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.angle = 0  # Initial angle of the flipper
        self.rotation_speed = 5  # Adjust as needed
        self.key = key

    def rotate(self, direction):
        # Rotate the flipper clockwise or counterclockwise based on the direction
        self.angle += direction * self.rotation_speed
        self.angle = max(0, min(self.angle, 45))  # Limit the rotation angle

    def handle_input(self):
        # Handle user input for flippers
        keys = pygame.key.get_pressed()
        if keys[self.key]:
            self.rotate(-1)  # Rotate counterclockwise when the key is pressed
        else:
            self.rotate(1)  # Rotate clockwise when the key is not pressed

    def update(self):
        # Update the flipper state (e.g., based on user input)
        pass  # No additional update logic for now

    def draw(self, screen):
        # Draw the flipper on the screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))




