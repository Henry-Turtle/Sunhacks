import pygame
class TemporaryObject:
    color: list[int, int, int]
    decay_speed: float
    pos: list[float, float]
    def __init__(self):
        color = (255, 255, 255)
    
    def draw(self, screen):
        pass
    



class SniperTrail(TemporaryObject):
    line: list[float, float]
    width: int
    def __init__(self, start: list[float, float], v: list[float, float]):
        self.color = (150, 150, 150)
        self.line = [v[0], -1*v[1]]
        self.pos = start
        self.decay_speed = 150/60
        self.width = width

    def draw(self, screen:pygame.display):
        pygame.draw.line(screen, self.color, self.pos, [self.pos[0]+self.line[0], self.pos[1]+self.line[1]])

        
class GrenadeExplosion(TemporaryObject):
    radius: float
    def __init__(self, position: list[float, float], radius: float):
        self.pos = position
        self.radius = radius
        self.color = (255, 255, 255)
        self.decay_speed = 255/60

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)