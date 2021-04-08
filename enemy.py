from settings import *
from sprites import yeti_running
from helpers import move

class Enemy:
  def __init__(self, rect):
    self.movement = [0, 0]
    self.direction = 0
    self.y_momentum = 0
    self.air_timer = 0
    self.rect = rect
    self.sprite_index = 0
    self.sprite = None
    self.flipped = False

  def moveRoutine(self, pygame, map, player):
    ms_passed = pygame.time.get_ticks()
    if (ms_passed % 150) <= 15:
      self.sprite_index = (self.sprite_index+1) % len(yeti_running)

    if(player.collides(self.rect)):
      self.y_momentum=-2;
      player.do_damage(1)

    self.rect, collisions = move(self.rect, self.movement, map.tiles)

    if collisions['right']:
      self.direction = -1
      self.flipped = True
    if collisions ['left']:
      self.direction = 1
      self.flipped = False
  
    if self.direction == 1:
      self.moveRight()
    else:
      self.moveLeft()
    # stage = int(0.001*pygame.time.get_ticks())%2
    # if(stage==0):
    #   self.moveRight();
    # else:
    #   self.moveLeft();
    self.move(map, collisions)

  def moveRight(self):
    self.direction=1;
  def moveLeft(self):
    self.direction=-1;
  def stopMovement(self):
    self.direction=0;


  def move(self, map, collisions):
    self.movement = [0, 0]
    if self.direction == 1:
        self.movement[0] += PLAYER_VELOCITY
    elif self.direction == -1:
        self.movement[0] -= PLAYER_VELOCITY

    self.movement[1] += self.y_momentum
    self.y_momentum = TERMINAL_VELOCITY if self.y_momentum>TERMINAL_VELOCITY else self.y_momentum+GRAVITY

    if collisions['bottom']:
      self.y_momentum = 0
      self.air_timer = 0
    else:
        self.air_timer += 1