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

        v = [self.x_pos - target[0], self.y_pos - target[1]]
        magnitude = (v[0]**2 + v[1]**2)**0.5
        v[0] = v[0] / magnitude
        v[1] = v[1] / magnitude

        self.x_pos -= self.speed * v[0]
        self.y_pos -= self.speed * v[1]

    def draw(self, screen: pygame.Surface, target: tuple):
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))

    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

class Triangle(Enemy):

    def __init__(self, speed: float, dmg: float, x: float, y: float, side: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.side = side

    def __str__(self) -> str:
        return f"Triangle [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}]"
    
    def draw(self, screen: pygame.Surface, target: tuple):

        centroid = (self.x_pos, self.y_pos)
        distance = ((self.x_pos**2)+(self.y_pos**2))**0.5
        vertexes = [None, None, None]
        median = self.side*(3**0.5)/2
        angle_to_origin = math.atan((centroid[1] - target[1])/(centroid[0] - target[0]))
        # vertex1 = [centroid[0]-((median*(2/3))*math.)]

        for i in range(3):
            vertexes[i] = [centroid[0] - (median*(2/3)*math.cos(angle_to_origin + ((math.pi/3)*i))), centroid[1] + (median*(2/3)*math.cos(angle_to_origin + ((math.pi/3)*i)))]
        

        pygame.draw.polygon(screen, pygame.Color(255, 0, 0), vertexes)
        


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
