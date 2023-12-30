import pygame
import math

class Ball:
    def __init__(self, x, y, vx, vy, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.friction = 0.98  # Adjust the friction factor as needed

    def update_position(self, gravity_y, dt, screen, balls=None):
        self.vy = self.vy + gravity_y * dt

        if self.y >= screen.get_height():
            self.vy = self.vy * (-1)

        # Apply air friction
        self.vx *= self.friction
        self.vy *= self.friction

        self.y = self.y + self.vy * dt + 0.5 * gravity_y * dt**2
        self.x = self.x + self.vx * dt

        self.check_boundary_collision(screen)

        if balls:
            self.check_ball_collision(balls)

        pygame.draw.circle(screen, self.color, [int(self.x), int(self.y)], self.radius)

    def check_boundary_collision(self, screen):
        if self.y >= screen.get_height() - self.radius:
            self.y = screen.get_height() - self.radius
            self.vy = self.vy * (-1)

    def check_ball_collision(self, balls):
        for ball in balls:
            if ball != self and self.check_collision(ball):
                self.resolve_collision(ball)

    def check_collision(self, ball):
        distance = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
        return distance < self.radius + ball.radius

    def resolve_collision(self, ball):
        # Calculate collision normal
        collision_normal = [ball.x - self.x, ball.y - self.y]
        magnitude = math.sqrt(collision_normal[0]**2 + collision_normal[1]**2)

        # Check if magnitude is non-zero before dividing
        if magnitude != 0:
            collision_normal = [collision_normal[0] / magnitude, collision_normal[1] / magnitude]
        else:
            # Handle the case where magnitude is zero
            # For example, set a default collision_normal or skip the collision resolution
            return

        # Calculate relative velocity
        relative_velocity = [ball.vx - self.vx, ball.vy - self.vy]

        # Calculate impulse
        impulse = 2 * (relative_velocity[0] * collision_normal[0] + relative_velocity[1] * collision_normal[1]) / (1 / self.radius + 1 / ball.radius)

        # Update velocities
       # Update velocities with negative impulse
        self.vx -= impulse * collision_normal[0] / self.radius
        self.vy -= impulse * collision_normal[1] / self.radius
        ball.vx += impulse * collision_normal[0] / ball.radius
        ball.vy += impulse * collision_normal[1] / ball.radius


