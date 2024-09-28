import pygame, math

class Enemy:

    side = 0

    def __init__(self, speed: float, dmg: float, x: float, y: float, width: float, height: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Enemy [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}, {self.width}, {self.height}]"
    
    def handle_movement(self, target: tuple) -> None:

        directionx = (self.x_pos - target[0])/(((self.x_pos**2) + (self.y_pos**2))**0.5)
        directiony = (self.y_pos - target[1])/(((self.x_pos**2) + (self.y_pos**2))**0.5)
        self.x_pos += self.speed * directionx
        self.y_pos += self.speed * directiony

    def draw(self, screen: pygame.Surface, target: tuple):
        
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(self.x_pos - (self.width/2), self.y_pos - (self.height/2), self.width, self.height))


class Triangle(Enemy):

    def __init__(self, speed: float, dmg: float, x: float, y: float, side: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.side = side

    def __str__(self) -> str:
        return f"Triangle [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}]"
    
    def draw(self, screen: pygame.Surface, center: tuple, target: tuple):

        centroid = (self.x_pos, self.y_pos)
        
        

        pygame.draw.polygon(screen, pygame.Color(255, 0, 0) [vertex1, vertex2, vertex3])
        pygame.draw.polygon()
        


class Rectangle(Enemy):

    def __str__(self) -> str:
        return super().__str__()


class Pentagon(Enemy):

    def __init__(self, speed: float, dmg: float, x: float, y: float, side: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.side = side

    def __str__(self) -> str:
        return f"Enemy [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}]" 
