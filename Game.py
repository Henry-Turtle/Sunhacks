from Stage import Stage
from Player import Player
import pygame
from Bullet import *
from Enemy import *
from Gun import *
from TemporaryObject import *
import math
import random


class Game:
    stage: Stage
    player: Player
    center: list[int, int]
    bullet_spawn_radius: int
    ticks: int
    seconds: int
    enemy_list = [Rectangle, EnemySpiral]
    money = 0
    
    def __init__(self, dimensions: tuple[int]):
        self.stage = Stage()
        self.player = Player([MachineGun(), Shotgun(), SniperRifle(), GrenadeLauncher()])

        x, y = dimensions
        self.center = [x/2, y/2]

        self.bullet_spawn_radius = 30
        self.grenade_radius = 100
        self.seconds = 0
        self.ticks = 0
    
    def reset(self, guns: tuple[Gun]):
        self.ticks = 0
        self.seconds = 0
        self.stage = Stage()
        self.player = Player(guns)

    def spawn_enemies(self):
        rand = random.Random()
        enemy: Enemy = self.enemy_list[random.randint(0, len(self.enemy_list)-1)]
        speed: float = (random.random())*(1+self.seconds/30)
        hp: float = (random.random()+1)*(30+self.seconds/15)
        dmg: float = (random.random()+1)*(30+self.seconds/15)
        size:float = (random.random())*30+30
        if self.ticks != 60:
            return
        self.ticks = 0
        self.seconds += 1
        num_enemies = int(self.seconds/60) + 1
        for i in range(num_enemies):
            side = (1 if random.randint(1, 2) == 1 else -1)
            parity = (1 if random.randint(1,2)==1 else -1)
            if side == 1:#Will spawn on left or right
                if parity == 1:#will spawn on left
                    self.stage.spawn_enemy(enemy(speed, dmg, -50-size, random.random()*self.center[1]*2, size, size, hp))
                else:#will spawn on right
                    self.stage.spawn_enemy(enemy(speed, dmg, self.center[0]*2+50+size, random.random()*self.center[1]*2, size, size, hp))
            else:#Will spawn on top or bottom
                if parity == 1:#Will spawn on bottom
                    self.stage.spawn_enemy(enemy(speed, dmg, random.random()*self.center[0]*2, -50-size, size, size, hp))
                else: #Will spawn on bottom
                    self.stage.spawn_enemy(enemy(speed, dmg, random.random()*self.center[0]*2, self.center[1]*2+50, size, size, hp))




        
        

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

        pygame.mixer.music.load("rifle.mp3")
        pygame.mixer.music.play()
        
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

            self.stage.spawn_bullet(self.player.create_bullet(
                    self.center[0] + cos*self.bullet_spawn_radius,
                    self.center[1] + sin*self.bullet_spawn_radius*-1,
                    [cos, sin]
                    ))
        
        pygame.mixer.music.load("shotgun.mp3")
        pygame.mixer.music.play()

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

        pygame.mixer.music.load("sniper.mp3")
        pygame.mixer.music.play()

    def shoot_grenadelauncher(self, mouse_pos: tuple):
        x, y = mouse_pos
        dx = x - self.center[0]
        dy = (y - self.center[1])*-1
        
        magnitude = (dx**2 + dy**2)**0.5

        v = [(dx/magnitude), (dy/magnitude)]

        self.stage.spawn_bullet(self.player.create_bullet(
                v[0]*self.bullet_spawn_radius+self.center[0],
                v[1]*self.bullet_spawn_radius*-1+self.center[1],
                v, self.grenade_radius
                ))
        
        pygame.mixer.music.load("grenade_launcher.mp3")
        pygame.mixer.music.play()

    def does_grenade_hit_enemy(self, enemy: Enemy, bullet: GrenadeBullet):
        rad = bullet.explosion_radius
        x = enemy.x_pos
        y = enemy.y_pos
        bullet_pos = [bullet.pos_x, bullet.pos_y]
        width = enemy.width
        height = enemy.height
        return math.dist([x, y], bullet_pos) <= rad or math.dist([x+width, y], bullet_pos) <= rad or math.dist([x, y+height], bullet_pos)<= rad or math.dist([x+width, y+height], bullet_pos)<= rad
    
    def explode_grenade(self, bullet: GrenadeBullet):
        enemy_list = []
        for enemy in self.stage.enemies:
            dist = math.dist([enemy.x_pos + enemy.width, enemy.y_pos + enemy.height], [bullet.pos_x, bullet.pos_y])
            if self.does_grenade_hit_enemy(enemy, bullet):
                enemy_list.append(enemy)
        pygame.mixer.music.load("explosion.mp3")
        pygame.mixer.music.play()
                
        self.stage.spawn_temporary_object(GrenadeExplosion((bullet.pos_x, bullet.pos_y), bullet.explosion_radius))
        for e in enemy_list:
            self.damage(e, bullet.damage)
        self.stage.bullets.remove(bullet)
        


    def do_collisions(self):
        for bullet in self.stage.bullets:
            enemystack:tuple[Enemy] = []
            enemy_rects:tuple[pygame.Rect] = [e.getRect() for e in self.stage.enemies]
            damaged_enemies: tuple = bullet.get_rect().collidelistall(enemy_rects)
            for enemy_index in damaged_enemies:
                enemystack.append(self.stage.enemies[enemy_index])
            for enemy in enemystack:   
                self.damage(enemy, bullet.damage)
            if len(damaged_enemies) > 0:
                self.destroy_bullet(bullet)


    def destroy_enemy(self, enemy: Enemy)->None:
        self.money += (enemy.damage + enemy.max_hp) / 10
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
            