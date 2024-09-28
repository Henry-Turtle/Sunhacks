import pygame

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

    def draw(screen: pygame.Surface):
        pass

class Triangle(Enemy):

    def __init__(self, speed: float, dmg: float, x: float, y: float, side: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.side = side

    def __str__(self) -> str:
        return f"Triangle [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}]"
    
    def draw(self, screen: pygame.Surface, center: tuple):

        points = []
        centroidx = self.x_pos
        centroidy = self.y_pos
        median = ((3**0.5)/2)*self.side
        point1 = (((median*0.67) + centroidy), (centroidx))
        point2 = ()
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
