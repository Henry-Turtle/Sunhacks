from Stage import Stage
from Player import Player
import pygame
from Bullet import Bullet
from Enemy import Enemy

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

        self.stage.spawn_bullet(self.player.create_bullet(
                v[0]*self.bullet_spawn_radius+self.center[0],
                v[1]*self.bullet_spawn_radius*-1+self.center[1],
                v
                ))


        


    def do_collisions(self):
        enemy_rects:tuple[pygame.Rect] = [e.getRect() for e in self.stage.enemies]
        bullet_rects: tuple[pygame.Rect] = [b.get_rect for b in self.stage.bullets]\
        
        for bullet in bullet_rects:
            damaged_enemies: tuple = bullet.collidelistall(enemy_rects)
            for enemy_index in damaged_enemies:
                damaged_enemies[enemy_index].damage(bullet.damage)
                self.destroy(bullet)
        damaged_enemies = self.player.getCrosshair().collidelistall(enemy_rects)
        print(len(damaged_enemies))

        def destroy(bullet: Bullet)->None:
            self.stage.bullets.remove(bullet)

        def destroy(enemy: Enemy)->None:
            self.stage.enemies.remove(enemy)
