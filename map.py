from helpers import readFile
from settings import *
import pygame

class Map:
  def __init__(self, mapPath):
    self.gameMapArr = readFile('maps/'+mapPath)
    self.mapPath = mapPath
  
  def switchMap(self, mapPath):
    mapPath = mapPath[:3]+str((int(mapPath[3])+1));
    self.gameMapArr = readFile('maps/'+mapPath);
    self.mapPath = mapPath;

  def draw(self, display, sprites):
    tiles = []
    TILE_SIZE = sprites.grass.get_width()
    for y in range(0, len(self.gameMapArr)):
      for x in range (0, len(self.gameMapArr[y])):
        tile = self.gameMapArr[y][x]
        if tile == '1':
            display.blit(sprites.dirt, (x * TILE_SIZE, y * TILE_SIZE))
        elif tile == '2':
            display.blit(sprites.grass, (x * TILE_SIZE, y * TILE_SIZE))
        elif tile == '3':
            display.blit(sprites.flag, (x * TILE_SIZE, y * TILE_SIZE))
        if tile != '0':
            tiles.append({'type': tile, 'rect': pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)})
    self.tiles = tiles