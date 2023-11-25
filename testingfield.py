from pygame import init, font, display, image, transform, fastevent, gfxdraw, mixer, time
from pymunk import Body, Poly, Space, pygame_util, constraints, PinJoint
from random import randint
from math import degrees, atan2

init()
fastevent.init()
screen = display.set_mode((1600, 900))
options = pygame_util.DrawOptions(screen)
space = Space()
space.gravity = 0, 600
clock = pygame.time.Clock()  # Use pygame.time.Clock() instead of time.Clock()
white = (255, 255, 255)
red = (255, 0, 0)

# Load images
bg = image.load("bg.png").convert()
base_bat_img = image.load("basebat_blue.png").convert_alpha()

# Load sounds
base_bat_sound = mixer.Sound("basebat_sound.mp3")

class Base_bat:
    def __init__(self, x, y, a, vect):
        self.body = Body(1, 1, Body.KINEMATIC)
        self.body.position = x, y
        self.body.angle = a
        shape = Poly(self.body, vect)
        shape.elasticity = 0.5
        shape.friction = 0.5
        shape.collision_type = 1  # hard_c_t
        space.add(self.body, shape)

    def check_movement(self, down, motion, x_check, angle_vel_u, angle_vel_d):
        if x_check:
            self.body.angular_velocity = angle_vel_u if down or motion else angle_vel_d
            if down:
                base_bat_sound.play()

    def animation(self, img, limit_u, limit_d):
        if self.body.angle <= limit_u:
            self.body.angular_velocity = 0
        if self.body.angle >= limit_d:
            self.body.angular_velocity = 0
        if self.body.angle <= limit_u - 0.2:
            self.body.angle = limit_u
        if self.body.angle >= limit_d + 0.2:
            self.body.angle = limit_d
        rotated_img = transform.rotate(img, -degrees(self.body.angle))
        screen.blit(rotated_img, (self.body.position[0] - rotated_img.get_width() // 2,
                                  self.body.position[1] - rotated_img.get_height() // 2))

# Create instances and run the game loop...

while True:
    screen.blit(bg, (0, 0))
    for ev in fastevent.get():
        # Handle events...
        pass

    # Update and render game elements...

    display.update()
    clock.tick(60)

