from objects.object import *
import pygame
import math
from ui.main_ui import *


class Tower(Object):
    def __init__(self, x, y, w, h, colour, cost, damage, attack_speed, range):
        super().__init__(x, y, w, h, colour)
        self.cost = cost
        self.damage = damage
        self.attack_speed = attack_speed
        self.range = range
        self.rect = pygame.Rect((x, y, w, h))
        self.range = range
        self.hitbox = pygame.Rect((x - self.range, y - self.range, w + 2 * self.range, h + 2 * self.range))
        self.damage = damage
        # checks which enemy the tower will attack
        self.target = None
        # checks if the tower is selected
        self.selected = False
        # checks how many upgrades the tower has
        self.upgrade_count = 0
        # checks the initial cost of the tower which can be increased by upgrades
        self.cost = cost
        # draws tower on screen

    def draw_tower(self, path_list, surface, player_state):
        collision = False
        if self.rect.colliderect(tower_main_box) or self.rect.colliderect(health_box) or self.rect.colliderect(map_border1) or self.rect.colliderect(map_border2) or self.rect.colliderect(map_border3.rect) or self.rect.colliderect(wave_box):
            collision = True
        if not collision:
            for path in path_list:
                if self.rect.colliderect(path):
                    print("error")
                    collision = True
        if not collision:
            pygame.draw.rect(surface, self.colour, (self.x, self.y, self.w, self.h))
            player_state["money"] -= self.cost
        # checks if an enemy collides with the towers hitbox

    def hitbox_check(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.hitbox) and enemy == self.target_enemy():
                self.target_enemy(enemies).health -= self.damage

    def target_enemy(self, enemies):
        x = self.rect.center[0]
        y = self.rect.center[1]
        dist_list = []
        for enemy in enemies:
            x_dist = enemy.pos[0] - x
            y_dist = enemy.pos[1] - y
            # finds the enemies distance from the tower
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            dist_list.append(dist)
            if dist == min(dist_list):
                if enemy.rect.colliderect(self.hitbox):
                    return enemy
                else:
                    dist_list = []

