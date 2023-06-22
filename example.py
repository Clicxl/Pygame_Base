import pygame,os
from pygame.locals import *
from Base import *

clock = pygame.time.Clock()
pygame.init()
font = pygame.font.Font(None,30)
screen = pygame.display.set_mode((500,500))
caption = pygame.display.set_caption('Base')
previous_time = time.time()

#Eaxmple images for Sprite Stacking
Ex_imgs = [pygame.image.load("Stacking Sprites/"+img) for img in os.listdir("Stacking Sprites")]
rot_frame = 0

while True:
  # Module
  App = Game(screen,clock,font)
  #-------------------------------
  screen.fill('White')
  #-------------------------------
  # Framerate independency 
  dt,previous_time = App.deltatime(previous_time)
  rot_frame += 50*dt
  # Custom Font
  App.Font('Font Ex/small_font.png',"This is Kesh's Base game module",(100,100),screen)
  # Sprite Stacking
  App.spritestack(Ex_imgs,(150,75),rot_frame)
  # Debuging
  App.debug(dt)
  # Exit Handler
  App.exit()
  # Screen Updater
  App.flip()
  