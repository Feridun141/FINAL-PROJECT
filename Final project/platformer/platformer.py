import os, sys
import pygame

#debug errors and shit
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')
if not pygame.image.get_extended(): print ('Warning, images disabled')

#store the path to our shit for the functions
main_dir = os.path.split(os.path.abspath(__file__))[0]
clock = pygame.time.Clock() 
#above should be in main process

SCREENRECT = pygame.Rect(0, 0, 640, 480)
BLACK = (0,0,0)
WHITE = (255,255,255)

"""***********************
Game functions
***********************"""
class NoneSound:
	def play(self): pass

def load_music(file):
	"loads a sound file, prepares it for play"
	class NoneSound:
		def play(self): pass
	if not pygame.mixer:
		return NoneSound()
	music_to_load = os.path.join(main_dir, 'data', file)
	try:
		music_export = pygame.mixer.music.load(music_to_load)
	except pygame.error as message:
		print ('Cannot load music file')
		print ('tried to load the following;')
		print (music_to_load)
		print ('Error message:')
		raise SystemExit(message)
	return music_export

def load_sound(file):
	if not pygame.mixer: return NoneSound()
	file = os.path.join(main_dir, 'data', file)
	try:
		sound = pygame.mixer.Sound(file=file)
		return sound
	except pygame.error:
		print ('Warning, unable to load, %s' % file)
	return NoneSound()

def load_image(file):
	"loads an unfiltered image"
	if not pygame.image.get_extended(): 
		raise SystemExit("extended images not available")
	image_to_load = os.path.join(main_dir, 'data', file)
	try:
		image_export = pygame.image.load(image_to_load)
	except pygame.error as message:
		print ('Could not load image')
		raise SystemExit(message)
	return image_export, image_export.get_rect()
	
def load_sprite(file, colorkey=-1):
	"loads an image, prepares it for play"
	if not pygame.image.get_extended(): 
		raise SystemExit("Could not load image; extended images not available")
	image_to_load = os.path.join(main_dir, 'data', file)
	try:
		image_export = pygame.image.load(image_to_load)
	except pygame.error as message:
		print ('Could not load image')
		raise SystemExit(message)
	image_export = image_export.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image_export.get_at((0,0))
		image_export.set_colorkey(colorkey)
	return image_export, image_export.get_rect()
	
"""***********************
classes & sprites
***********************"""

class Player(pygame.sprite.Sprite):
	"""our player pentagon"""
	speed_x = 5
	speed_y = 2
	change_y = 0
	bounce = 48
	wall_list = []
	
	def __init__(self,passedimage,passedmidbottom):
		pygame.sprite.Sprite.__init__(self,self.containers) #call Sprite initializer
		self.image = passedimage
		self.rect = self.image.get_rect(midbottom=passedmidbottom)
		self.origtop = self.rect.top
		self.facing = -1
	
	def calc_grav(self):
		#Calculate effect of gravity.
		if self.change_y == 0:
			self.change_y = 9.8
		elif self.change_y >= -9.8:
			self.change_y -= .35
			print(self.change_y)
		else:
			self.change = -9.8
 
		# See if we are on the ground.
		if self.change_y >= 0:
			wall_collisions = pygame.sprite.spritecollide(self, self.wall_list, 0)
			for wall in (wall_collisions):
				self.change_y = 0
				self.rect.y = SCREENRECT.height - self.rect.height

	def move(self, direction):
		if direction: 
			self.facing = direction
		#moving left-to-right
		self.rect.move_ip(direction*self.speed_x, 0)
		self.rect = self.rect.clamp(SCREENRECT)
		self.rect.top = self.origtop - (self.rect.left//self.bounce%2)
		#gravity and jumping

	def jump(self):
		self.calc_grav()
		self.rect.move_ip(0,-self.speed_y*self.change_y)
		#self.rect.move_ip(0,-50)
			
class Wall(pygame.sprite.Sprite):
	#black rectangle, stops movement
	def __init__(self,passed):
		pygame.sprite.Sprite.__init__(self, self.containers) #call Sprite initializer
		passurface = passed[2], passed[3]
		self.image = pygame.Surface(passurface)
		self.rect = passed

class Floor(pygame.sprite.Sprite):
	#black rectangle, stops gravity (at some point)
	def __init__(self,passed):
		pygame.sprite.Sprite.__init__(self, self.containers) #call Sprite initializer
		passurface = passed[2], passed[3]
		self.image = pygame.Surface(passurface)
		self.rect = passed
		
class Pit(pygame.sprite.Sprite):
	#white (tansparent?) rectangle, allows movement
	mypit = (0,0,0)

"""***********************
Primary loop
***********************"""

#Shouldn't this be Main() or something?
def main(winstyle = 0):
	#Let's hit it!
	pygame.init()
	
	#set the icon. Must be done before set_mode.
	icon = load_image('avatar.png')# load theimage and rect
	scaled_icon = pygame.transform.scale2x(icon[0]) #select only the image and scale it up
	pygame.display.set_icon(scaled_icon) #set it as the icon of the screen
	
	#setup the screen.
	bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	background = pygame.Surface(SCREENRECT.size)
	screen.fill((255, 255, 255))
	background.fill((255, 255, 255))
	screen.blit(background, (0,0))
	pygame.display.flip()

	#stores width/height as vars... redundant?
	screenwidth, screenheight = pygame.display.get_surface().get_size()
	#other common vars for the map design
	commonheight = screenheight//10
	screenbottom = screenheight - commonheight
	#these *are* redundant since we can just use SCREENRECT modifiers i guess
	
	#initial states for variables
	gameover = False
	
	#apparently you should load images *after* you load the screen
	avatar = load_sprite('avatar.png', -1)
	
	#beautify the screen.
	pygame.display.set_caption('Kolor - Plato')
	
	#groups or something
	wall_list = pygame.sprite.Group()
	floor_list = pygame.sprite.Group()
	pits = pygame.sprite.Group()
	all = pygame.sprite.RenderUpdates()
	
	#i have no idea what i'm doing
	#"default groups for each sprite class"
	Player.containers = all
	Wall.containers = wall_list, all
	Floor.containers = floor_list, all
	Pit.containers = pits, all
	
	#initialize the sprites
	player = Player(avatar[0],SCREENRECT.midbottom)
	
	"""
	Leveldesign! Place walls by calling Wall() with a rectangle as argument
	Position from of the left face, position of the top face, width, height
	Use the first wall as an example. 
	could add an if statement here for multiple levels.
	"""
	
	Floor(pygame.Rect(SCREENRECT.left, SCREENRECT.bottom -1, SCREENRECT.right, SCREENRECT.bottom)) #Floor
	
	#doing these two like this so I can actually read it.
	#should probably write macros for SR.left and such
	rleft = SCREENRECT.left + 100
	rtop = SCREENRECT.bottom - 32
	wallrect = pygame.Rect(rleft,rtop,16,32)
	Wall(wallrect)
	
	rleft = SCREENRECT.right - 100
	rtop = SCREENRECT.bottom - 32
	wallrect = pygame.Rect(rleft,rtop,16,32)
	Wall(wallrect)
	
	load_music('cityruins.mp3')
	pygame.mixer.music.play(-1)
	
	#let's get looping
	while not gameover:
		
		all.clear(screen,background) #clean screen
		all.update() #reset sprites

		#Quitting the game with the [X] or escape
		for event in pygame.event.get():
			if event.type == pygame.QUIT or \
				(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					print("Recieved quit command.")
					load_sound('adios.ogg').play(0,1142)
					pygame.mixer.music.fadeout(1000)
					pygame.time.wait(1000)
					gameover = True
					
		#move the player
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_a] or pressed[pygame.K_LEFT] or pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
			if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
				direction = -1
			elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
				direction = 1
			else:
				direction = 0
			player.move(direction)
		
		if pressed[pygame.K_SPACE]:
			player.jump()
		
		#walls stop the player
		wall_collisions = pygame.sprite.spritecollide(player, wall_list, 0)
		for wall in (wall_collisions):
			player.move(-direction) #technically bounces him back as fast as he's moving
		
		#This should update the scene
		dirty = all.draw(screen)
		pygame.display.update(dirty)
		
		#framerate cap
		clock.tick(60)
		
if __name__ == '__main__': main()