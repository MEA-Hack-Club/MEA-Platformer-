import pygame;

player = pygame.image.load('img/player2.png')

yeti_running = [
  pygame.image.load('img/yeti/running/yeti_0.png'), pygame.image.load('img/yeti/running/yeti_1.png')
  ]
yeti_standing = pygame.image.load('img/yeti/standing.png')

flag = pygame.transform.scale(pygame.image.load('img/goal.png'), (16, 16))
dirt = pygame.image.load('img/dirt.png')
ice_road = pygame.image.load('img/ice_road.png')
grass = pygame.image.load('img/grass.png')
checkpoint = pygame.image.load('img/checkpoint.gif')