import pygame
class Object:
    def __init__(self, x, y, w, h, colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.w, self.h))