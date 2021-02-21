from pygame.image import load
from pygame.locals import *
from settings import *
from helpers import *

class Player:
  def __init__(self, rect, air_timer=0,movement=[0, 0], direction=0, y_momentum=0):
    self.rect = rect
    self.movement = movement
    self.direction = direction #-1 = left, 1 = right, 0 = none
    self.y_momentum = y_momentum
    self.air_timer = air_timer

  def collides(self, rect):
    return self.rect.colliderect(rect);

  def move(self, map):
    self.movement = [0, 0]
    if self.direction == 1:
        self.movement[0] += PLAYER_VELOCITY
    elif self.direction == -1:
        self.movement[0] -= PLAYER_VELOCITY

    self.movement[1] += self.y_momentum
    self.y_momentum = TERMINAL_VELOCITY if self.y_momentum>TERMINAL_VELOCITY else self.y_momentum+GRAVITY

    self.rect, collisions = move(self.rect, self.movement, map.tiles)

    if(collisions['goal']):
      map.switchMap('map1')
      
    if collisions['bottom']:
      self.y_momentum = 0
      self.air_timer = 0
    else:
        self.air_timer += 1

  def getMovementInput(self, event):
    if event.type == KEYDOWN:
        if event.key == K_d:
            self.direction = 1
        elif event.key == K_a:
            self.direction = -1
        elif event.key == K_w:
            if self.air_timer < 6:
                self.y_momentum = -5
    elif event.type == KEYUP:
        self.direction = 0