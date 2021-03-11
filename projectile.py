import pygame

class Projectile:
  def __init__(self,radius,x,y,direction,color):
    self.velocity = 8 * direction
    self.radius = radius
    self.x = x
    self.y = y
    self.direction = direction
    self.color = color

  def draw(self, display):
    pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)
    
  def move(self):
    self.x  += self.velocity