import pygame, sys # import pygame and sys
pygame.init() # initiate pygame
from enemy import Enemy
from player import Player
from projectile import Projectile
from map import Map
from pygame.locals import * # import pygame modules
from helpers import *
from settings import *
# from map_scripts.map1 import map1

clock = pygame.time.Clock() # set up the clock
pygame.display.set_caption(WINDOW_NAME)# set the window name
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen
display = pygame.Surface((300, 200))

import sprites;
map = Map("map1")
player = Player(pygame.Rect(50, 50, sprites.player.get_width(), sprites.player.get_height()))
enemy = Enemy(pygame.Rect(50, 50, sprites.enemy.get_width(), sprites.enemy.get_height()))

while True: # game loop
  #display stuff
  display.fill((146,244,255))
  map.draw(display, sprites)
  display.blit(sprites.player, (player.rect.x, player.rect.y))
  display.blit(sprites.enemy, (enemy.rect.x, enemy.rect.y))
  player.draw_health_bar(display)

  if(int(pygame.time.get_ticks()*0.001)%5==0):
    player.heal(1)

  #movement
  player.move_projectiles(display)
  for event in pygame.event.get(): # event loop
    if event.type == KEYDOWN and event.key == K_SPACE: 
      projectile = Projectile(10, player.rect.x, player.rect.y, 1 if player.moving_right == True else -1, BLACK)
      player.projectiles.append(projectile)

    if event.type == QUIT: # check for window quit
        pygame.quit() # stop pygame
        sys.exit() # stop script
    else:
      player.getMovementInput(event)#get WASD input
  player.move(map)
  enemy.moveRoutine(pygame, map, player)
        
  surf = pygame.transform.scale(display, WINDOW_SIZE)
  screen.blit(surf, (0, 0))
  pygame.display.update() # update display
  clock.tick(FPS) # maintain 60 f