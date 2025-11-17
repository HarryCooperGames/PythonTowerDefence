import pygame
class Object:
    def __init__(self, colour,  x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.w, self.h))