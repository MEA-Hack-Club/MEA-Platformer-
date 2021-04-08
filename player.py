from pygame.image import load
from pygame.locals import *
from settings import *
from helpers import *
import pygame

class Player:
  def __init__(self, rect):
    self.rect = rect
    self.air_timer = 0
    self.movement = 0
    self.moving_right = False
    self.moving_left = False
    self.y_momentum = 0
    self.current_health = 100
    self.max_health = 100
    self.health_bar_length = 100
    self.projectiles = []
    
  def move_projectiles(self,display):
    for projectile in self.projectiles:
      projectile.move()
      projectile.draw(display)
      if projectile.x > 400 or projectile.x < 0:
        self.projectiles.remove(projectile)

  def draw_health_bar(self, display):
    percentage = self.current_health/self.max_health
    health_bar = pygame.Rect(10, 150, percentage*self.health_bar_length, 20)
    pygame.draw.rect(display, RED, health_bar)

  def do_damage(self,damage):
    if(self.current_health <= 0):
      self.current_health = 0;
    else:
      self.current_health -= damage

  def heal(self, amount):
    if(self.current_health<=self.max_health):
      self.current_health+=amount
    if(self.current_health>self.max_health):
      self.current_health = self.max_health
  
  def collides(self, rect):
    return self.rect.colliderect(rect);

  def move(self, map):
    self.movement = [0, 0]
    if self.moving_right :
        self.movement[0] += PLAYER_VELOCITY
    if self.moving_left :
        self.movement[0] -= PLAYER_VELOCITY

    self.movement[1] += self.y_momentum
    self.y_momentum = TERMINAL_VELOCITY if self.y_momentum>TERMINAL_VELOCITY else self.y_momentum+GRAVITY

    self.rect, collisions = move(self.rect, self.movement, map.tiles)

    if(collisions['goal']):
      map.switchMap('map1')

    if collisions ['checkpoint']:
      self.heal(1)
      
    if collisions['bottom']:
      self.y_momentum = 0
      self.air_timer = 0
    else:
        self.air_timer += 1

  def getMovementInput(self, event):
    if event.type == KEYDOWN:
        if event.key == K_d:
            self.moving_right = True
        elif event.key == K_a:
            self.moving_left = True
        elif event.key == K_w:
            if self.air_timer < 6:
                self.y_momentum = -5
    elif event.type == KEYUP:
      if event.key == K_d:
        self.moving_right = False
      if event.key == K_a:
        self.moving_left = False