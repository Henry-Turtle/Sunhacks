import pygame
from Gun import *
from Bullet import *
class Player:
    current_gun: Gun
    guns: list[Gun]
    pos_x: int
    pos_y: int
    speed: int

    def __init__(self):
        self.guns = []
        self.guns.append(MachineGun())
        self.guns.append(Shotgun())
        self.guns.append(SniperRifle())
        self.guns.append(GrenadeLauncher())

        self.current_gun = self.guns[0]
    
    def create_bullet(self, x: float, y: float, direction: list[float]) -> Bullet:
        if isinstance(self.current_gun, GrenadeLauncher):
            return GrenadeBullet(x, y, direction, self.current_gun.bullet_speed,self.current_gun.bullet_damage, self.current_gun.bullet_size)
        elif isinstance(self.current_gun, Shotgun):
            return ShotgunBullet(x, y, direction, self.current_gun.bullet_speed, self.current_gun.bullet_damage, self.current_gun.bullet_size)
        return Bullet(x, y, direction, self.current_gun.bullet_speed, self.current_gun.bullet_damage, self.current_gun.bullet_size)

    def swap_gun(self, i: int)->None:
        self.current_gun = self.guns[i]

    def handle_movement(self, left: bool, right: bool, up: bool, down: bool):
        v = [-1*left + 1*right, -1*up+1*down]
        magnitude = (v[0]**2 + v[1]**2)**0.5
        v = [(v[0]/magnitude)*self.speed, (v[1]/magnitude)*self.speed]
        self.pos_x += v[0]
        self.pos_y += v[1]
        

    
