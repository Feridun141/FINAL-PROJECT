import os, sys, pygame

#execfile('file.py')
main_dir = os.path.split(os.path.abspath(__file__))[0]
platformer_dir = os.path.join(main_dir, 'platformer')
platformer_file = platformer_dir + "\platformer.py"
space_dir = os.path.join(main_dir, 'python game stuff')
space_file =  space_dir + "\game.py"
pong_dir = os.path.join(main_dir, 'pong')
pong_file =  pong_dir + "\pong.py"
starjump_dir = os.path.join(main_dir, 'StarJump')
starjump_file =  starjump_dir + "\jumpstar.py"

clock = pygame.time.Clock() 
SCREENRECT = pygame.Rect(0, 0, 640, 480)
BLACK = (0,0,0)
WHITE = (255,255,255)

def launch_game(name):
	adjustedname = name + "_file"
	os.system(adjustedname)
		
def main(winstyle = 0):	
	pygame.init()
	pygame.display.set_caption('Kolor')
	bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	background = pygame.Surface(SCREENRECT.size)
	screen.fill(WHITE)
	background.fill(WHITE)
	screen.blit(background, (0,0))
	pygame.display.flip()

	
	if pygame.font:
		font = pygame.font.Font(None, 36)
		text = font.render("KOLOR", 1, (10, 10, 10))
		textpos = text.get_rect(centerx=background.get_width()/2)
		background.blit(text, textpos)
		
	while 1:
		
		#input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				return

		#Draw Everything
		screen.blit(background, (0, 0))
		pygame.display.flip()
		
		clock.tick(60)	
		
		
if __name__ == '__main__':
	main()