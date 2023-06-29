import time,pygame,sys
from pygame.locals import *
pygame.init()

class Game:
  def __init__(self,clock,game_font=None):
    self.screen = pygame.display.get_surface()
    self.clock = clock
    self.font = game_font
    
  def flip(self,fps=0):
    pygame.display.flip()
    self.clock.tick(fps)

  def exit(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
        pygame.quit()
        sys.exit()

  # Credtis to Clear Code
  def deltatime(self,previous_time):
    self.dt = time.time() - previous_time
    previous_time = time.time()
    return self.dt,previous_time

  def debug(self,info,y_pos=10,x_pos=10):
    font = pygame.font.Font(None,30)
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info),True,'White')
    debug_rect = debug_surf.get_rect(topleft=(x_pos,y_pos))
    pygame.draw.rect(display_surf,'Black',debug_rect)
    display_surf.blit(debug_surf,debug_rect)

  # Credits to Thefluffypotato
  def Font(self,path,information,location,surface,scale=[1,1]):
    # ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']'''
    
    def clip(surf,x,y,x_size,y_size):
      handle_surf = surf.copy()
      clipR = pygame.Rect(x,y,x_size,y_size)
      handle_surf.set_clip(clipR)
      image = surf.subsurface(handle_surf.get_clip())
      return image.copy()
    def render(surf,loc,scale):
      x_offset = 0
      for char in information:
        if char != " ":
          surf.blit(pygame.transform.scale_by(self.characters[char],scale),(loc[0]+x_offset,loc[1])) 
          x_offset += self.characters[char].get_width() + self.spacing
        else:
          x_offset += self.spacing_width + self.spacing

    # info = information
    scale = scale
    loc = location
    surf = surface
    self.spacing = 1
    font_img = pygame.image.load(path).convert()
    font_img.set_colorkey((0,0,0))
    char_width = 0
    self.char_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
    self.characters = {}
    char_count = 0
    
    for x in range(font_img.get_width()):
      c = font_img.get_at((x,0))
      if c[0] == 127:
        char_img = clip(font_img, x - char_width, 0, char_width, font_img.get_height())
        self.characters[self.char_order[char_count]] = char_img.copy()
        char_count += 1
        char_width = 0
      else:
        char_width += 1
    self.spacing_width = self.characters['A'].get_width()
    render(surf,loc,scale)
  
  def spritestack(self,images,postion,rotation,scale=[1,1],spread=1):
    img  = images
    pos = postion
    rot = rotation
    scale = scale
    spread = scale[0] * spread 
    def render(images,pos,rot,scale,spread=1):
      for i,img in enumerate(images):
        rotated_img = pygame.transform.rotate(pygame.transform.scale_by(img,scale),rot)
        self.screen.blit(rotated_img,(pos[0]-rotated_img.get_width()//2,pos[1]-rotated_img.get_width()//2 - i*spread))

    render(img,pos,rot,scale,spread)

    # self.rect.center = pygame.mouse.get_pos()    

  def outline(self,Surf,pos,color):
    surf_mask = pygame.mask.from_surface(Surf)
    for point in surf_mask.outline():
      x = point[0] + pos[0]
      y = point[1]+ pos[1]
      pygame.draw.circle(self.screen,color,(x,y),1)