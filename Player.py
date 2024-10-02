import pygame
from Gun import *
from Bullet import *
class Player:
    current_gun: Gun
    guns: list[Gun]
    pos_x: int
    pos_y: int
    speed: int
    health: float

    def __init__(self, guns: tuple[Gun], speed: int = 2, pos_x: float = 700, pos_y: float = 400):
        self.guns = []
        for gun in guns:
            self.guns.append(gun)

        self.current_gun = self.guns[0]
        self.current_health = 300
        self.max_health = 300
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def create_bullet(self, x: float, y: float, direction: list[float], blast_radius: int = 100) -> Bullet:
        if isinstance(self.current_gun, GrenadeLauncher):
            return GrenadeBullet(x, y, direction, self.current_gun.bullet_speed,self.current_gun.bullet_damage, self.current_gun.bullet_size, blast_radius)
        elif isinstance(self.current_gun, Shotgun):
            return ShotgunBullet(x, y, direction, self.current_gun.bullet_speed, self.current_gun.bullet_damage, self.current_gun.bullet_size)
        return Bullet(x, y, direction, self.current_gun.bullet_speed, self.current_gun.bullet_damage, self.current_gun.bullet_size)

    def swap_gun(self, i: int)->None:
        self.current_gun = self.guns[i]

    def handle_movement(self, left: int, right: int, up: int, down: int):
        v = [(left - right), (up - down)]
        magnitude = (((v[0]**2) + (v[1]**2))**0.5)
        if magnitude != 0:
            self.pos_x += self.speed * (v[0]/magnitude)
            self.pos_y += self.speed * (v[1]/magnitude)            
        
        # self.pos_x += left * self.speed
        # self.pos_y += up * self.speed
        # self.pos_x -= right * self.speed
        # self.pos_y -= down * self.speed

    def get_rect(self):
        return pygame.Rect(self.pos_x - 15, self.pos_y - 15, 30, 30)

    
