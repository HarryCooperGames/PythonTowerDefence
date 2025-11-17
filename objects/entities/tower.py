import pygame

from objects.object import *

class Tower(Object):
    def __init__(self, x, y, w, h, colour, cost, damage, attack_speed):
        super().__init__(x, y, w, h, colour)
        self.cost = cost
        self.damage = damage
        self.attack_speed = attack_speed
    def place_tower(self):
        pass
    def enemy_in_range(self):
        pass
    def attack(self):
        pass

