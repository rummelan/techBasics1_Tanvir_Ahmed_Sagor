import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Assignment 8")

clock = pygame.time.Clock()

class MovingImage:
    def __init__(self, image_file):
        self.image = pygame.image.load(image_file)

        # Random size
        size = random.randint(50, 120)
        self.image = pygame.transform.scale(self.image, (size, size))

        # Random position
        self.x = random.randint(0, WIDTH - size)
        self.y = random.randint(0, HEIGHT - size)

        # Random speed
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= WIDTH - self.image.get_width():
            self.speed_x *= -1

        if self.y <= 0 or self.y >= HEIGHT - self.image.get_height():
            self.speed_y *= -1

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

images = []

for i in range(5):
    images.append(MovingImage("favorite_image.png"))

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 220, 255))

    for img in images:
        img.move()
        img.draw()

    pygame.display.update()

pygame.quit()
