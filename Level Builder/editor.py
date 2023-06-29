import pygame,sys
from pygame.locals import *
from settings import *
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_button
from pygame.mouse import get_pos as mouse_pos


class Editor:
  def __init__(self):
    # Main Setup
    self.display_surface = pygame.display.get_surface()

    # Navigation
    self.origin = vector()
    self.pan_active = False
    self.pan_offset = vector()
  # Input
  def event_loop(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
          pygame.quit()
          sys.exit()
        self.pan_input(event)

  def pan_input(self,event):
    if event.type == pygame.MOUSEBUTTONDOWN and mouse_button()[2]:
      self.pan_active = True
      self.pan_offset = vector(mouse_pos()) - self.origin
    if not mouse_button()[2]:
      self.pan_active = False
      
    # Panning 
    if self.pan_active:
      self.origin = vector(mouse_pos()) - self.pan_offset
      
    # Mouse wheel
    if event.type == pygame.MOUSEWHEEL:
      if pygame.key.get_pressed()[pygame.K_LCTRL]:
        self.origin.y -= event.y*50
        
      else:
        self.origin.x -= event.y*50
        
  def draw_tile_markers(self):
    cols = WINDOW_WIDTH // TILE_SIZE 
    row = WINDOW_HEIGHT // TILE_SIZE
    # Support Line Surf
    self.line_surf = pygame.Surface((self.display_surface.get_width(),self.display_surface.get_height()))
    self.line_surf.fill('Black')
    self.line_surf.set_alpha(50)
    
    # Offset vector
    offset_vector = vector(x = self.origin.x - int(self.origin.x/TILE_SIZE)*TILE_SIZE,y=self.origin.y - int(self.origin.y/TILE_SIZE)*TILE_SIZE)
    
    for col in range(cols+1):
      x = offset_vector.x + col * TILE_SIZE
      pygame.draw.line(self.line_surf,LINE_COLOUR,(x,0),(x,WINDOW_HEIGHT))

    for row in range(row+1):
      x = offset_vector.y + row * TILE_SIZE
      pygame.draw.line(self.line_surf,LINE_COLOUR,(0,x),(WINDOW_WIDTH,x))
    self.display_surface.blit(self.line_surf,(0,0))
  def run(self,dt):
    self.display_surface.fill('Black')
    self.event_loop()
    self.draw_tile_markers()
    pygame.draw.circle(self.display_surface,'red',self.origin,10)