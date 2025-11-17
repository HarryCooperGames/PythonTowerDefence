import pygame
from pygame import *

from objects.object import *

class Enemy(Object):
    def __init__(self, x, y, w, h, colour, damage, speed, health, waypoints, image, money_value, player_state, surface):
        super().__init__(x, y, w, h, colour)
        self.damage = damage
        self.speed = speed
        self.health = health
        self.waypoints = waypoints
        self.target_waypoint = 1
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (x+w/2, y+h/2)
        self.pos = self.rect.center
        self.money_value = money_value
        self.player_state = player_state
        self.surface = surface

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, waypoints, enemies, player_state, surface):
        self.health_check(enemies, waypoints, player_state)
        # defines the nextwaypoint the enemy will go to
        self.target = Vector2(self.waypoints[self.target_waypoint])
        # calculates displacement from the next waypoint
        self.movement = self.target - self.pos
        # calculate remaining distance to target
        distance = self.movement.length()
        # check if distance is greater the how much the enemy will move
        if distance >= self.speed:
            # move the enemy towards the next waypoint
            self.pos += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.pos += self.movement.normalize() * distance
            if len(waypoints) - 1 > self.target_waypoint:
                self.target_waypoint += 1
        # update the center to the position that is being moved
        self.rect.center = self.pos
        self.draw(surface)

    # checks if the enemy is still alive
    def health_check(self, enemies, waypoints, player_state):
        if self.health <= 0:
            enemies.remove(self)
            player_state["money"] += self.money_value
        if self.pos == waypoints[len(waypoints) - 1]:
            enemies.remove(self)
            player_state["player_health"] -= self.damage