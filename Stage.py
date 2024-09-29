from Enemy import Enemy
from Bullet import Bullet
from Gun import *
from TemporaryObject import TemporaryObject
class Stage:
    enemies: list[Enemy]
    bullets: list[Bullet]
    temporary_objects: list[TemporaryObject]

    def __init__(self):
        self.enemies = []
        self.bullets = []
        self.temporary_objects = []

    
    def spawn_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.handle_movement()
    
    def spawn_bullet(self, bullet: Bullet):
        self.bullets.append(bullet)

    def handle_enemy_movement(self, enemy: Enemy, center: tuple[float, float]):
        enemy.handle_movement(center)
    
    

    #@enemy_array_position is the position of the enemy in the "enemies" array. This will be much faster
    def destroy_enemy(self, enemy_array_position: int):
        self.enemies.pop[enemy_array_position]
    def decay_temporary_object(self, obj: TemporaryObject):
        obj.color = [c-obj.decay_speed for c in obj.color]
        if obj.color[0] < 0 or obj.color[1]<0 or obj.color[2]<0:
            self.temporary_objects.remove(obj)

    def spawn_temporary_object(self, obj: TemporaryObject):
        self.temporary_objects.append(obj)
