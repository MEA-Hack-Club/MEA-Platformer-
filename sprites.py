import pygame;

player = pygame.image.load('img/player2.png')
enemy = pygame.image.load('img/yeti.png')

flag = pygame.transform.scale(pygame.image.load('img/goal.png'), (16, 16))
dirt = pygame.image.load('img/dirt.png')
grass = pygame.image.load('img/grass.png')
checkpoint = pygame.image.load('img/Checkpoint.gif')