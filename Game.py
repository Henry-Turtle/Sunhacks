from Stage import Stage
from Player import Player
import pygame
from Bullet import *
from Enemy import Enemy
from Gun import *
from TemporaryObject import *
import math
import random


class Game:
    stage: Stage
    player: Player
    center: list[int, int]
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
        elif (isinstance(self.player.current_gun, Shotgun)):
            self.shoot_shotgun(mouse_pos)
        elif (isinstance(self.player.current_gun, MachineGun)):
            self.shoot_machinegun(mouse_pos)
        elif (isinstance(self.player.current_gun, GrenadeLauncher)):
            self.shoot_grenadelauncher(mouse_pos)

            
        self.player.current_gun.current_shoot_delay_ticks = self.player.current_gun.shoot_delay_ticks
        self.player.current_gun.ammo -= 1
        
    def shoot_machinegun(self, mouse_pos: tuple[int, int]):
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
        
    def shoot_shotgun(self, mouse_pos: tuple[int, int]):
        x, y = mouse_pos
        dx = x - self.center[0]
        dy = (y - self.center[1])*-1
        
        magnitude = (dx**2 + dy**2)**0.5

        v = [(dx/magnitude), (dy/magnitude)]

        theta = math.atan2(v[1], v[0])
        rand = random.Random()
        for i in range(5):
            random_angle = theta + rand.random()*self.player.current_gun.bullet_spread - self.player.current_gun.bullet_spread/2
            cos = math.cos(random_angle)
            sin = math.sin(random_angle)
            print(theta, random_angle, cos, sin)

            self.stage.spawn_bullet(self.player.create_bullet(
                    self.center[0] + cos*self.bullet_spawn_radius,
                    self.center[1] + sin*self.bullet_spawn_radius*-1,
                    [cos, sin]
                    ))

    def shoot_sniper(self, mouse_pos: tuple):
        x, y = mouse_pos
        dx = x - self.center[0]
        dy = (y - self.center[1])*-1
        
        magnitude = (dx**2 + dy**2)**0.5

        v = [dx*900/magnitude, dy*900/magnitude] #900 is enough to cover entire screen
        enemy_collisions = [b.getRect() for b in self.stage.enemies]
        damaged_enemies = []
        for i in range(len(enemy_collisions)):
            if enemy_collisions[i].clipline(self.center, [v[0]+self.center[0], -1*v[1]+self.center[1]]):
                damaged_enemies.append(self.stage.enemies[i])
        
        for enemy in damaged_enemies:
            self.damage(enemy, self.player.current_gun.bullet_damage)
        
        self.stage.spawn_temporary_object(SniperTrail(self.center, v))

    def shoot_grenadelauncher(self, mouse_pos: tuple):
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


    def explode_grenade(self, bullet: GrenadeBullet):
        for enemy in self.stage.enemies:
            dist = math.dist([enemy.x_pos + enemy.width, enemy.y_pos + enemy.height], [bullet.pos_x, bullet.pos_y])
            if dist <= bullet.explosion_radius:
                self.damage(enemy, bullet.damage)
        self.stage.spawn_temporary_object(GrenadeExplosion((bullet.pos_x, bullet.pos_y), bullet.explosion_radius))
        self.stage.bullets.remove(bullet)
        pass


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
        if bullet.type == "grenade":
            self.explode_grenade(bullet)
            return
        self.stage.bullets.remove(bullet)
            

    def damage(self, enemy: Enemy, damage: float):
        enemy.hp -= damage
        if enemy.hp <= 0:
            self.destroy_enemy(enemy)
            