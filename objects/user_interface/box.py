import pygame
from objects.object import Object

class Box(Object):
    def __init__(self, colour, x, y, w, h, outline_width):
        super().__init__(colour, x, y, w, h)
        self.outline_width = outline_width
        self.rect = pygame.Rect(x, y, w, h)
    def draw_outline(self, surface):
        pygame.draw.rect(surface,self.colour,(self.x,self.y,self.w,self.h), self.outline_width)