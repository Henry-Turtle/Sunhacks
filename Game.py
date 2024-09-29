from Stage import Stage
from Player import Player
from Bullet import Bullet
import pygame

class Game:
    stage: Stage
    player: Player
    center: list[int]
    bullet_spawn_radius: int
    
    def __init__(self, dimensions: tuple[int]):
        self.stage = Stage()
        self.player = Player()

        x, y = dimensions
        self.center = [x/2, y/2]

        self.bullet_spawn_radius = 30
    

    def shoot(self, mouse_pos: tuple):
        x, y = mouse_pos
        dx = x - self.center[0]
        dy = (y - self.center[1])*-1
        
        magnitude = (dx**2 + dy**2)**0.5

        v = [(dx/magnitude), (dy/magnitude)]

        self.stage.spawn_bullet(Bullet(
            v[0]*self.bullet_spawn_radius+self.center[0],
              v[1]*self.bullet_spawn_radius*-1+self.center[1],
                v, self.player.current_gun.bullet_speed,
                  self.player.current_gun.bullet_damage))
        print(v)

        


    def do_collisions(self):
        enemy_rects = [e.getRect() for e in self.stage.enemies]
        damaged_enemies = self.player.getCrosshair().collidelistall(enemy_rects)
        print(len(damaged_enemies))

