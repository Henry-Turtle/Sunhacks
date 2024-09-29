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
        if self.player.current_gun.ammo < 1:
            return
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

        self.player.current_gun.current_shoot_delay_ticks = self.player.current_gun.shoot_delay_ticks
        self.player.current_gun.ammo -= 1
        

        


    def do_collisions(self):
        enemy_rects:tuple[pygame.Rect] = [e.getRect() for e in self.stage.enemies]
        
        for bullet in self.stage.bullets:
            damaged_enemies: tuple = bullet.get_rect().collidelistall(enemy_rects)
            for enemy_index in damaged_enemies:
                self.damage(self.stage.enemies[enemy_index], bullet.damage)
                self.destroy_bullet(bullet)

    def destroy_enemy(self, enemy: Enemy)->None:
        self.stage.enemies.remove(enemy)

    def destroy_bullet(self, bullet: Bullet)->None:
        self.stage.bullets.remove(bullet)
            

    def damage(self, enemy: Enemy, damage: float):
        enemy.hp -= damage
        if enemy.hp <= 0:
            self.destroy_enemy(enemy)
            