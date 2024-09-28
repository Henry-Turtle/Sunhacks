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

        # points = []
        centroid = (self.x_pos, self.y_pos)
        # median = ((3**0.5)/2)*self.side
        # point1 = (((median*0.67) + centroidy), (centroidx))
        # point2 = ()

        angle_to_target = math.atan2(target[1] - centroid[1], target[0] - centroid[0])

        # Angles for the three vertices of the triangle
        angle1 = angle_to_target
        angle2 = angle1 + 2 * math.pi / 3
        angle3 = angle1 - 2 * math.pi / 3

        # Calculate the vertices based on the centroid and self.side
        vertex1 = (centroid[0] + self.side * math.cos(angle1), centroid[1] + self.side * math.sin(angle1))
        vertex2 = (centroid[0] + self.side * math.cos(angle2), centroid[1] + self.side * math.sin(angle2))
        vertex3 = (centroid[0] + self.side * math.cos(angle3), centroid[1] + self.side * math.sin(angle3))

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
