import pygame
from pygame.locals import *

# This is only to import the Base module from the parent file 
import os,sys
parent_file = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_file)
from Base import *

clock = pygame.time.Clock()
pygame.init()
SCREEN = (1200,720)
screen = pygame.display.set_mode(SCREEN)
caption = pygame.display.set_caption('Sprites')
previous_time = time.time()
pygame.mouse.set_visible(False)
background = pygame.image.load('Sprites/BG.png')

# Sprite Group
# Dosent Work Currently
crosshair = Sprite('Sprites/crosshair.png')
crosshair_Group = pygame.sprite.Group()
crosshair_Group.add(crosshair)

while True:
  App = Game(screen,clock)
  screen.fill('Black')
  dt,previous_time = App.deltatime(previous_time)
  screen.blit(pygame.transform.scale(background,SCREEN),(0,0))
  # crosshair_Group.draw(screen) # TypeError: Source objects must be a surface
  App.exit()
  App.flip()