from Enemy import Enemy
from Bullet import Bullet
class Stage:
    enemies: list[Enemy]
    bullets: list[Bullet]

    def __init__(self):
        self.enemies = []
        self.bullets = []

    
    def spawn_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.handle_movement()
    
    def spawn_bullet(self, bullet: Bullet):
        self.bullets.append(bullet)

    #@enemy_array_position is the position of the enemy in the "enemies" array. This will be much faster
    def destroy_enemy(self, enemy_array_position: int):
        self.enemies.pop[enemy_array_position]
