from Stage import Stage
from Player import Player
import pygame
from Bullet import Bullet
from Enemy import Enemy
from Gun import *

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
        if not self.player.current_gun.can_fire():
            return
        if (isinstance(self.player.current_gun, SniperRifle)):
            self.shoot_sniper(mouse_pos)
            
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
        

    def shoot_sniper(self, mouse_pos: tuple):
        x, y = mouse_pos
        dx = x - self.center[0]
        dy = (y - self.center[1])*-1
        
        magnitude = (dx**2 + dy**2)**0.5

        v = [dx*900/magnitude, dy*900/magnitude] #900 is enough to cover entire screen

        enemy_collisions = [b.getRect() for b in self.stage.enemies]
        damaged_enemies = []
        for i in range(len(enemy_collisions)):
            if enemy_collisions[i].clipline(0, 0, v[0], v[1]) == ():
                damaged_enemies.append(enemy_collisions[i])
        
        for enemy in damaged_enemies:
            self.damage(enemy, self.player.current_gun.bullet_damage)
        
        

        


    def do_collisions(self):
        enemy_rects:tuple[pygame.Rect] = [e.getRect() for e in self.stage.enemies]
        enemystack:tuple[Enemy] = []
        for bullet in self.stage.bullets:
            damaged_enemies: tuple = bullet.get_rect().collidelistall(enemy_rects)
            if len(damaged_enemies) > 0:
                self.destroy_bullet(bullet)
            for enemy_index in damaged_enemies:
                enemystack.append(self.stage.enemies[enemy_index])

        for enemy in enemystack:   
            self.damage(enemy, bullet.damage)


    def destroy_enemy(self, enemy: Enemy)->None:
        self.stage.enemies.remove(enemy)

    def destroy_bullet(self, bullet: Bullet)->None:
        self.stage.bullets.remove(bullet)
            

    def damage(self, enemy: Enemy, damage: float):
        enemy.hp -= damage
        if enemy.hp <= 0:
            self.destroy_enemy(enemy)
            