from pygame.locals import * # import pygame modules

def readFile(path):
  f = open(path, "r")
  arr = []
  while(True):
    tempLine = f.readline()
  
    if tempLine == "": 
      break
  
    temparr = []
    for t in tempLine:
      temparr.append(t)
    arr.append(temparr)
  f.close()
  return arr;

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile['rect']):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'checkpoint': False, 'top': False, 'bottom': False, 'right': False, 'left': False, 'goal': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
      if tile['type'] == '4':
        collision_types['checkpoint'] = True
        continue;
      if tile['type'] == '3':
        collision_types['goal'] = True;
      if movement[0] > 0:#moving right
        rect.right = tile['rect'].left
        collision_types['right'] = True
      elif movement[0] < 0:#moving left
        rect.left = tile['rect'].right
        collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
      if tile['type'] == '4':
        collision_types['checkpoint'] = True
        continue;
      if tile['type'] == '3':
        collision_types['goal'] = True;
      if movement[1] > 0:#going up
          rect.bottom = tile['rect'].top
          collision_types['bottom'] = True
      elif movement[1] < 0:#going down
          rect.top = tile['rect'].bottom
          collision_types['top'] = True
    return rect, collision_types

def setMomentum(moving_right, moving_left, player_y_momentum):
  player_movement = [0, 0]
  if moving_right:
      player_movement[0] += 2
  if moving_left:
      player_movement[0] -= 2
  return player_movement