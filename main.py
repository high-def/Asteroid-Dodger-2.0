import pygame, pandas as pd
from pygame.locals import *
from Ship import *
from Asteroid import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)

color = (50, 0, 100)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

df = pd.read_csv('game_info.csv')
numlevels = df['LevelNum'].max()         
current_level = df['LevelNum'].min()
level_data = df.iloc[current_level]
asteroid_count = level_data['AsteroidCount']
player = Ship((level_data['PlayerX'], level_data['PlayerY']))
asteroids = pygame.sprite.Group()



def init():
  global current_level, asteroid_count
  level_data = df.iloc[current_level]
  player.reset((level_data['PlayerX'], level_data['PlayerY']))
  asteroid_count = level_data['AsteroidCount']
  asteroids.empty()
  for i in range(asteroid_count):
    asteroids.add(Asteroid((random.randint(0, 800), random.randint(0, 600))))
  
def win():
  font = pygame.font.SysFont(None, 70)
  text = font.render("You escaped the asteroid field!", True, (100, 100, 100))
  text_rect = text.get_rect()
  text_rect.center = (screen_info.current_w //2, screen_info.current_h //2)
  while True:
    screen.fill(color)
    screen.blit(text, text_rect)
    pygame.display.flip()

def main():
  global current_level
  init()
  while current_level <= numlevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          player.speed[0] = 10
        if event.key == pygame.K_LEFT:
          player.speed[0] = -10
        if event.key == pygame.K_UP:
          player.speed[1] = -10
        if event.key == pygame.K_DOWN:
          player.speed[1] = 10
      else:
        player.speed[0] = 0
        player.speed[1] = 0                              
    screen.fill(color)
    asteroids.draw(screen)
    player.update()
    asteroids.update()
    gets_hit = pygame.sprite.spritecollide(player, asteroids, False)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    if player.check_reset(screen_info.current_w):
      if current_level == numlevels:
       break
      else:
        current_level += 1
        init()
    elif gets_hit:
      player.reset((20, 300))
  win()

if __name__ == "__main__":
  main()
             