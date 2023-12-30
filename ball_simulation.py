import pygame
import math

class BaseObject(object):
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def update_position(self, gravity_y, dt, screen, entities=None):
        pass

    def check_boundary_collision(self, screen):
        pass

    def check_collision(self, entity):
        for entity in entities:
            if entity != self and self.check_collision(entity):
                self.resolve_collision(entity)

    def check_collision(self, entity):
        return False

    def resolve_collision(self, entity):
        pass



class Ball(BaseObject):
    def __init__(self, x, y, vx, vy, radius, color):
        super().__init__(x,y,vx, vy,color)
        self.radius = radius
        self.friction = 0.98  # Adjust the friction factor as needed
        
    def update_position(self, gravity_y, dt, screen, entities=None):
        super().update_position(gravity_y, dt, screen,entities)
        self.vy = self.vy + gravity_y * dt

        if self.y >= screen.get_height():
            self.vy = self.vy * (-1)

        # Apply air friction
        self.vx *= self.friction
        self.vy *= self.friction

        self.y = self.y + self.vy * dt + 0.5 * gravity_y * dt**2
        self.x = self.x + self.vx * dt

        self.check_boundary_collision(screen)

       # if balls:
          #  self.check_ball_collision(balls)

        pygame.draw.circle(screen, self.color, [int(self.x), int(self.y)], self.radius)

  # def check_boundary_collision(self, screen):
       # if self.y >= screen.get_height() - self.radius:
          #  self.y = screen.get_height() - self.radius
            #self.vy = self.vy * (-1)


    def check_collision(self, entity):
        super().check_collision(entity)
        distance = math.sqrt((self.x -entity.x)**2 + (self.y - entity.y)**2)
        return distance < self.radius + entity.radius

    def resolve_collision(self, entity):
        super().check_collision(entity)
        # Calculate collision normal
        collision_normal = [entity.x - self.x, entity.y - self.y]
        magnitude = math.sqrt(collision_normal[0]**2 + collision_normal[1]**2)

        # Check if magnitude is non-zero before dividing
        if magnitude != 0:
            collision_normal = [collision_normal[0] / magnitude, collision_normal[1] / magnitude]
        else:
            # Handle the case where magnitude is zero
            # For example, set a default collision_normal or skip the collision resolution
            return

        # Calculate relative velocity
        relative_velocity = [entity.vx - self.vx, entity.vy - self.vy]

        # Calculate impulse
        impulse = 2 * (relative_velocity[0] * collision_normal[0] + relative_velocity[1] * collision_normal[1]) / (1 / self.radius + 1 / entity.radius)

        # Update velocities
       # Update velocities with negative impulse
        self.vx -= impulse * collision_normal[0] / self.radius
        self.vy -= impulse * collision_normal[1] / self.radius
        entity.vx += impulse * collision_normal[0] / entity.radius
        entity.vy += impulse * collision_normal[1] / entity.radius


class Square(BaseObject):
    def __init__(self, x, y, vx, vy, radius, color):
        super().__init__(x,y,vx, vy,color)
        self.radius = radius
        self.friction = 0.98  # Adjust the friction factor as needed
        
    def update_position(self, gravity_y, dt, screen, entities=None):
        super().update_position(gravity_y, dt, screen,entities)
        self.vy = self.vy + gravity_y * dt

        if self.y >= screen.get_height():
            self.vy = self.vy * (-1)

        # Apply air friction
        self.vx *= self.friction
        self.vy *= self.friction

        #self.y = self.y + self.vy * dt + 0.5 * gravity_y * dt**2
        #self.x = self.x + self.vx * dt

        self.check_boundary_collision(screen)

       # if balls:
          #  self.check_ball_collision(balls)

        pygame.draw.rect(screen, self.color,pygame.Rect(int(self.x-25), int(self.y-25), int(25), int(25)))

  # def check_boundary_collision(self, screen):
       # if self.y >= screen.get_height() - self.radius:
          #  self.y = screen.get_height() - self.radius
            #self.vy = self.vy * (-1)


    def check_collision(self, entity):
        super().check_collision(entity)
        distance = math.sqrt((self.x -entity.x)**2 + (self.y - entity.y)**2)
        return distance < self.radius + entity.radius

    def resolve_collision(self, entity):
        super().check_collision(entity)
        # Calculate collision normal
        collision_normal = [entity.x - self.x, entity.y - self.y]
        magnitude = math.sqrt(collision_normal[0]**2 + collision_normal[1]**2)

        # Check if magnitude is non-zero before dividing
        if magnitude != 0:
            collision_normal = [collision_normal[0] / magnitude, collision_normal[1] / magnitude]
        else:
            # Handle the case where magnitude is zero
            # For example, set a default collision_normal or skip the collision resolution
            return

        # Calculate relative velocity
        relative_velocity = [entity.vx - self.vx, entity.vy - self.vy]

        # Calculate impulse
        impulse = 2 * (relative_velocity[0] * collision_normal[0] + relative_velocity[1] * collision_normal[1]) / (1 / self.radius + 1 / entity.radius)

        # Update velocities
       # Update velocities with negative impulse
        self.vx -= impulse * collision_normal[0] / self.radius
        self.vy -= impulse * collision_normal[1] / self.radius
        entity.vx += impulse * collision_normal[0] / entity.radius
        entity.vy += impulse * collision_normal[1] / entity.radius