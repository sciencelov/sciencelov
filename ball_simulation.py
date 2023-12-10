# ball_simulation.py

import pygame

class Ball:
    def __init__(self, x, y, vx, vy, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

    def update_position(self, gravity_y, dt, screen):
        self.vy = self.vy + gravity_y * dt

        if self.y >= screen.get_height():
            self.vy = self.vy * (-1)

        self.y = self.y + self.vy * dt + 0.5 * gravity_y * dt**2

        pygame.draw.circle(screen, self.color, [int(self.x), int(self.y)], self.radius)
