import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50 ,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True

while running:
    # keep loop running at the right speed
    clock.tick (FPS)
    #process input (events)
    for event in pygame.event.get():
         # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    #Draw/render
    screen.fill(BLACK)
    all_sprites.draw()

    # *afer* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()