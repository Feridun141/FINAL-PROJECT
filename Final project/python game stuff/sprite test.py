
# pygame stuff
import pygame
import random
import os

WIDTH = 600
HEIGHT = 400
FPS = 30

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
#assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
	# player Sprite
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, "ship.png")).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
	def update(self):
		self.rect.y += -5
		if self.rect.bottom > HEIGHT:
			self.rect.top = 0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shmup")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# game
running = True
while running:

	# clock
	clock.tick(FPS)

	#inputs and events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#sprite updates
	all_sprites.update()

	#draw
	screen.fill(BLACK)
	all_sprites.draw(screen)
	#after drawing flip
	pygame.display.flip()

pygame.quit()
