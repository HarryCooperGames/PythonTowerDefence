import pygame

from objects.object import Object  # absolute import from parent package

class Enemy(Object):
    def __init__(self, x, y, w, h, colour, damage, speed, health):
        super().__init__(x, y, w, h, colour)
        self.damage = damage
        self.speed = speed
        self.health = health
    def move(self):
        pass
    def update_health(self):
        pass