# Space WARS GAME
## Team members: Feridun Mujde
<img src="https://user-images.githubusercontent.com/73741033/102718259-6c92d800-4311-11eb-8ada-3126240d9757.png">

## Explanation of the game
###### It's a score game
###### You have to stay alive in space with running away from your enemies
###### First your enemies are a few than it gets harder
###### At the beginning, you have just 3 lives. When you die, your live gets less(-1)
###### Sometimes you have to shoot bullet to your enemies (If the bullet hits your enemy, it dies) for not die
###### Randomly comes bullet and live from your dead enemies and that bullet and live packets increase your bullet and live

# Codes

## colors
```
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
```
## initialising screen 
```
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shmup")
clock = pygame.time.Clock()
```
## assets
```
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
```

## scoretext
```
font_name = pygame.font.match_font('arial')
def draw_score(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midbottom = (x, y)
    surf.blit(text_surface, text_rect)
```

## live pics
```
def draw_lives(surf, x, y, lives, player_sprite_lives):
    for i in range(lives):
        player_sprite_lives_rect = player_sprite_lives.get_rect()
        player_sprite_lives_rect.x = x + 25 * i
        player_sprite_lives_rect.y = y
        surf.blit(player_sprite_lives, player_sprite_lives_rect)
```

## entity's
```
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 16
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 60
        self.speedx = 0
        self.shot_delay = 300
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power_lvl = 1

    def update(self):
        self.speedx = 0
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (WIDTH / 2, HEIGHT - 60)

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 5
        if (keystate[pygame.K_LEFT] or keystate[pygame.K_a]) and (keystate[pygame.K_RIGHT]or keystate[pygame.K_d]):
            self.speedx = 0
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        now = pygame.time.get_ticks()
        if self.power_lvl == 1 and now - self.last_shot > self.shot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
        if self.power_lvl == 2 and now - self.last_shot > self.shot_delay:
            self.last_shot = now
            bullet1 = Bullet1(self.rect.centerx, self.rect.top)
            bullet2 = Bullet2(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet1)
            bullets.add(bullet2)
        if self.power_lvl == 3 and now - self.last_shot > self.shot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet1 = Bullet1(self.rect.centerx, self.rect.top)
            bullet2 = Bullet2(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet)
            bullets.add(bullet1)
            bullets.add(bullet2)
        if self.power_lvl == 4 and now - self.last_shot > self.shot_delay:
            self.last_shot = now
            bullet1 = Bullet1(self.rect.centerx, self.rect.top)
            bullet2 = Bullet2(self.rect.centerx, self.rect.top)
            bullet3 = Bullet3(self.rect.centerx, self.rect.top)
            bullet4 = Bullet4(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            all_sprites.add(bullet3)
            all_sprites.add(bullet4)
            bullets.add(bullet1)
            bullets.add(bullet2)
            bullets.add(bullet3)
            bullets.add(bullet4)
        if self.power_lvl == 5 and now - self.last_shot > self.shot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet1 = Bullet1(self.rect.centerx, self.rect.top)
            bullet2 = Bullet2(self.rect.centerx, self.rect.top)
            bullet3 = Bullet3(self.rect.centerx, self.rect.top)
            bullet4 = Bullet4(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            all_sprites.add(bullet3)
            all_sprites.add(bullet4)
            bullets.add(bullet)
            bullets.add(bullet1)
            bullets.add(bullet2)
            bullets.add(bullet3)
            bullets.add(bullet4)

    def hide(self):
        #hide the player while "dead"
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT - 3000)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy1_sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 17
        self.rect.x = random.randrange (WIDTH - self.rect.width)
        self.rect.y = random.randrange (-100, -25)
        self.speedy = random.randrange (1, 8)
        self.speedx = random.randrange (-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 30 or self.rect.right > WIDTH + 30:
            self.rect.x = random.randrange (WIDTH - self.rect.width)
            self.rect.y = random.randrange (-100, -25)
            self.speedy = random.randrange (1, 8)
            self.speedx = random.randrange (-3, 3)
        if player.hidden:
            self.rect.y +=2000

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom <= 100 :
            self.kill

class Bullet1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = -1

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.bottom < 0 :
            self.kill

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = 1

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.bottom < 0 :
            self.kill

class Bullet3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = -2

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0 :
            self.kill

class Bullet4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_sprite
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = 2

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0 :
            self.kill

class Powerups(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['gun','lives'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.center = center
        self.speedy = 4
    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT + 10:
            self.kill


class Backgroundstar1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "star.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speedy = 3
        self.rect.x = random.randrange (WIDTH - self.rect.width)
        self.rect.y = random.randrange (-1000, -10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange (WIDTH - self.rect.width)
            self.rect.y = random.randrange (-1000, -10)

class Deathexplosion(pygame.sprite.Sprite):
    def __init__(self, center, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.image = death_anim[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        if death_anim[self.type] == death_anim['player']:
            self.frame_rate = 80
        else:
            self.frame_rate = 50
    def update(self):

        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(death_anim[self.type]):
                self.kill()
            else:
                center = self.rect.center
                self.image = death_anim[self.type][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
```

## death animation
```
death_anim = {}
death_anim['enemy'] = []
death_anim['player'] = []
for i in range(5):
    filename = 'explosion{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    death_anim['enemy'].append(img)
    img_player = pygame.transform.scale(img, (60, 60))
    death_anim['player'].append(img_player)

powerup_images = {}
powerup_images['gun'] = pygame.image.load(os.path.join(img_folder, "powerup_bullet.png")).convert()
powerup_images['lives'] = pygame.image.load(os.path.join(img_folder, "powerup_lives.png")).convert()

```

## sprites
```
bullet_sprite = pygame.image.load(os.path.join(img_folder, "bullet.png")).convert()
enemy1_sprite = pygame.image.load(os.path.join(img_folder, "enemy1.png")).convert()
player_sprite = pygame.image.load(os.path.join(img_folder, "ship.png")).convert()
player_sprite_lives = pygame.transform.scale(player_sprite, (20, 20))
player_sprite_lives.set_colorkey(BLACK)
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
player = Player()
stars = pygame.sprite.Group()
all_sprites.add(player)
```

## enemy and backgroundstar spawns
```
for i in range(8):
    E = Enemy()
    all_sprites.add(E)
    enemies.add(E)
for i in range(50):
    B = Backgroundstar1()
    stars.add(B)
    all_sprites.add(B)
```

## score
```
score = 0
```

## game
```
running = True
while running:
```

## clock
```
clock.tick(FPS)
```

## updates
```
all_sprites.update()
```

## collision enemy bullet
```
bullethit = pygame.sprite.groupcollide(enemies, bullets, True, True, pygame.sprite.collide_circle)
    for hit in bullethit:
        score += 10
        E = Enemy()
        enemies.add(E)
        if random.random() > 0.95:
            powerup = Powerups(hit.rect.center)
            all_sprites.add(powerup)
            powerups.add(powerup)
        death = Deathexplosion(hit.rect.center, 'enemy')
        all_sprites.add(E, death)
```

## collision enemy player
```
hit = pygame.sprite.spritecollide(player,enemies, True, pygame.sprite.collide_circle)
    if hit:
        death = Deathexplosion(player.rect.center, 'player')
        all_sprites.add(death)
        player.hide()
        player.lives -= 1
        player.power_lvl = 1
```

## collision with powerups
```
poweruphit = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
    for hit in poweruphit:
        if hit.type == 'lives':
            player.lives += 1
            if player.lives >= 5:
                player.lives = 5
                score += 500
        if hit.type == 'gun':
            player.power_lvl += 1
            if player.power_lvl >= 5:
                player.power_lvl = 5
                score += 500
```

## check if the player sprite and the explosion are gone before closing
```
if player.lives == 0 and not death.alive():
        running = False
```

## input and events
```
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

## draw
```
 screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_score(screen,("score: "+str(score)), 24, WIDTH/2, HEIGHT-10)
    draw_lives(screen, WIDTH -150 , HEIGHT- 30, player.lives, player_sprite_lives)

```

## after drawing flip
```
    pygame.display.flip()

pygame.quit()
```
