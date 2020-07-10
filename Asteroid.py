import pygame, random

class Asteroid(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load("asteroid.png")
    self.image = pygame.transform.smoothscale(self.image,(random.randint(20, 100), random.randint(20, 100)))
    self.rect = self.image.get_rect()     
    self.rect.center = pos 
    self.speed = pygame.math.Vector2(0, 3)
    self.speed.rotate_ip(random.randint(0, 360))

  def update(self):
    self.rect.move_ip(self.speed)
    screen_info = pygame.display.Info() 
    if self.rect.right > screen_info.current_w or self.rect.left < 0:
      self.speed[0] *= -1
      self.image = pygame.transform.flip(self.image, True, False)
      self.rect.move_ip(self.speed[0], 0)
    if self.rect.top < 0 or self.rect.bottom >  screen_info.current_h:
      self.speed[1] *= -1
      self.image = pygame.transform.flip(self.image, False, True)
      self.rect.move_ip(0, self.speed[1])
