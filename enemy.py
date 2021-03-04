from settings import *
from helpers import move
import pygame

class Enemy(pygame.sprite.Sprite):
  def __init__(self, rect, air_timer=0,movement=[0, 0], direction=0, y_momentum=0):
    super().__init__()
    self.movement = movement
    self.direction = direction
    self.y_momentum = y_momentum
    self.air_timer = air_timer
    self.rect = rect

  def moveRoutine(self, pygame, map, player):
    if(player.collides(self.rect)):
      self.y_momentum=-2;

    stage = int(0.001*pygame.time.get_ticks())%2
    if(stage==0):
      self.moveRight();
    else:
      self.moveLeft();
    self.move(map)

  def moveRight(self):
    self.direction=1;
  def moveLeft(self):
    self.direction=-1;
  def stopMovement(self):
    self.direction=0;


  def move(self, map):
    self.movement = [0, 0]
    if self.direction == 1:
        self.movement[0] += PLAYER_VELOCITY
    elif self.direction == -1:
        self.movement[0] -= PLAYER_VELOCITY

    self.movement[1] += self.y_momentum
    self.y_momentum = TERMINAL_VELOCITY if self.y_momentum>TERMINAL_VELOCITY else self.y_momentum+GRAVITY

    self.rect, collisions = move(self.rect, self.movement, map.tiles)

    if collisions['bottom']:
      self.y_momentum = 0
      self.air_timer = 0
    else:
        self.air_timer += 1