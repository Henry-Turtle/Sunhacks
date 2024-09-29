import pygame
class Bullet:
    pos_x: float
    pos_y: float
     
    speed: float
    direction: list[float]
    damage: float
    size: int
    type: str

    def __init__(self, x: float, y: float, direction: list[float], speed: float, damage: float, bullet_size: int):
        self.pos_x = x
        self.pos_y = y
        self.speed = speed

        magnitude = (direction[0]**2 + direction[1]**2)**0.5
        self.direction = [direction[0]/magnitude, -1*direction[1]/magnitude]

        self.size = bullet_size
        self.damage = damage
        self.type = "bullet"

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, pygame.Color("white"), (self.pos_x, self.pos_y), self.size)

    def handle_movement(self):
        self.pos_x += self.direction[0]*self.speed
        self.pos_y += self.direction[1]*self.speed

    def get_rect(self)-> pygame.Rect:
        return pygame.Rect(self.pos_x - self.size/2, self.pos_y-self.size/2, self.size, self.size)

class ShotgunBullet(Bullet):
    ticks_loaded: int
    def __init__(self, x: float, y: float, direction: list[float], speed: float, damage: float, bullet_size: int):
        self.pos_x = x
        self.pos_y = y
        self.speed = speed

        magnitude = (direction[0]**2 + direction[1]**2)**0.5
        self.direction = [direction[0]/magnitude, -1*direction[1]/magnitude]

        self.size = bullet_size
        self.damage = damage

        self.ticks_loaded = 0
        self.type = "shotgun"

class GrenadeBullet(Bullet):
    tick_loaded: int
    def __init__(self, x: float, y: float, direction: list[float], speed: float, damage: float, bullet_size: int):
        self.pos_x = x
        self.pos_y = y
        self.speed = speed

        magnitude = (direction[0]**2 + direction[1]**2)**0.5
        self.direction = [direction[0]/magnitude, -1*direction[1]/magnitude]

        self.size = bullet_size
        self.damage = damage

        self.ticks_loaded = 0
        self.explosion_radius = 50
        self.type = "grenade"