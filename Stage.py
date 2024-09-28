from Enemy import Enemy
class Stage:
    enemies: list[Enemy]

    def __init__(self):
        enemies = []

    
    def spawn_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.handle_movements()

