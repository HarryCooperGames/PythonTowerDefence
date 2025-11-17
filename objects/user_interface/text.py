import pygame
class Text:
  #initialise class
  def __init__(self,text,text_col,x,y, size):
    self.text = text
    self.text_col = text_col
    self.x = x
    self.y = y
    self.size = size
  #draw text function
  def draw_text(self, surface):
    text_font = pygame.font.SysFont("Arial", self.size)
    img = text_font.render(self.text,True,self.text_col)
    text_center = img.get_rect(center = (self.x,self.y))
    surface.blit(img, text_center)