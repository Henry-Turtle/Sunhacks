import pygame
from Gun import *
from Bullet import Bullet
class Player:
    current_gun: Gun
    guns: list[Gun]

    def __init__(self):
        self.guns = []
        self.guns.append(MachineGun())

        self.current_gun = self.guns[0]
    
    def create_bullet(self, x: float, y: float, direction: list[float]) -> Bullet:
        return Bullet(self, x, y, direction, self.current_gun.bullet_speed, self.current_gun.bullet_damage, self.current_gun.bullet_size)


