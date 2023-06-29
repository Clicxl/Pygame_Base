import pygame
from pygame.locals import *
from settings import *
from editor import *

class Main:
  def __init__(self):
    self.display_surf = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    self.clock =  pygame.time.Clock()
    self.editor = Editor()
  
  def run(self):
    while True:
      dt = self.clock.tick()/1000
          
      self.editor.run(dt)
      pygame.display.flip()
  
if __name__ == '__main__':
  Game = Main()
  Game.run()