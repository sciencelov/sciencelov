import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
BALL_SPEED = 5
PADDLE_SPEED = 7
GRAVITY = 0.2
FRICTION = 0.98

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game class
class PinballGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pinball Game")
        self.clock = pygame.time.Clock()

        self.balls = [Ball(WIDTH // 2, HEIGHT // 2)]
        self.paddles = [Paddle(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)]
        self.obstacles = [Obstacle(100, 100, 50, 50), Obstacle(300, 200, 50, 50), MovingObstacle(500, 300, 50, 50)]

        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        for ball in self.balls:
            ball.update()

        for paddle in self.paddles:
            paddle.update()

        for obstacle in self.obstacles:
            obstacle.update()

        self.check_collisions()

    def check_collisions(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.collides_with(paddle):
                    ball.bounce_up()
                    self.score += 10

            for obstacle in self.obstacles:
                if ball.collides_with(obstacle):
                    ball.bounce()

    def run(self):
        while True:
            self.handle_events()
            self.update()

            self.screen.fill(BLACK)

            for ball in self.balls:
                ball.draw(self.screen)

            for paddle in self.paddles:
                paddle.draw(self.screen)

            for obstacle in self.obstacles:
                obstacle.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

# Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BALL_RADIUS
        self.speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
        self.speed_y = BALL_SPEED

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Gravity
        self.speed_y += GRAVITY

        # Friction
        self.speed_x *= FRICTION

        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1

        # Ball falls through the hole at the bottom
        if self.y - self.radius >= HEIGHT:
            self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
        self.speed_y = BALL_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

    def collides_with(self, other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distance < self.radius + other.radius

    def bounce_up(self):
        self.speed_y = -BALL_SPEED

    def bounce(self):
        self.speed_x *= -1
        self.speed_y *= -1

# Paddle class
class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = min(width, height) // 2  # Set radius to half the minimum dimension

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and self.x + self.width < WIDTH:
            self.x += PADDLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

# Obstacle class
class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = min(width, height) // 2  # Set radius to half the minimum dimension

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))


# MovingObstacle class
class MovingObstacle(Obstacle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 3

    def update(self):
        self.x += self.speed
        if self.x <= 0 or self.x + self.width >= WIDTH:
            self.speed *= -1

# Run the game
if __name__ == "__main__":
    game = PinballGame()
    game.run()
