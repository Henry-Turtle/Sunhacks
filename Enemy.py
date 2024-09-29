import pygame
import math
class Enemy:

    def __init__(self, speed: float, dmg: float, x: float, y: float, width: float, height: float, hp: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height
        self.hp = hp
        self.max_hp = hp

    def __str__(self) -> str:
        return f"Enemy [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}, {self.width}, {self.height}]"
    
    def handle_movement(self, target: tuple) -> None:
        pass

    def draw(self, screen: pygame.Surface, target: tuple):
        color = [85, 85, 85]
        if self.hp/self.max_hp > 0.75:
            color = [255, 0, 0]
        elif self.hp/self.max_hp > 0.50:
            color = [191, 32, 32]
        elif self.hp/self.max_hp > 0.25:
            color = [127, 64, 64]
        elif self.hp/self.max_hp > 0:
            color = [85, 85, 85]
        pygame.draw.rect(screen, pygame.Color(color[0], color[1], color[2]), pygame.Rect(self.x_pos - (self.width/2), self.y_pos - (self.height/2), self.width, self.height))

    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x_pos - (self.width/2), self.y_pos - (self.height/2), self.width, self.height)
    

class Rectangle(Enemy):
    def handle_movement(self, target: tuple) -> None:
            v = [self.x_pos - target[0], self.y_pos - target[1]]
            magnitude = (v[0]**2 + v[1]**2)**0.5
            v[0] = v[0] / magnitude
            v[1] = v[1] / magnitude

            self.x_pos -= self.speed * v[0]
            self.y_pos -= self.speed * v[1]

    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
    

    def draw(self, screen: pygame.Surface, target: tuple):

        color = [255-170*(1-self.hp/self.max_hp), 85*(1-self.hp/self.max_hp), 85*(1-self.hp/self.max_hp)]

        pygame.draw.rect(screen, pygame.Color(int(color[0]), int(color[1]), int(color[2])), pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))

class EnemySpiral(Enemy):

    def __init__(self, speed: float, dmg: float, x: float, y: float, width: float, height: float, hp: float) -> None:
        super().__init__(speed, dmg, x, y, width, height, hp)

    def handle_movement(self, target: tuple) -> None:

        actual_x = self.x_pos - target[0]
        actual_y = self.y_pos - target[1]

        # Calculate the current radius and angle of the object in polar coordinates
        radius = math.sqrt(actual_x**2 + actual_y**2)
        angle = math.atan2(actual_y, actual_x)

        # Update the angle and radius to create spiral movement
        angle -= 0.005 * self.speed  # Slightly change the angle for spiral effect
        radius -= 0.5*self.speed  # Decrease radius to move inward

        # Convert polar coordinates back to cartesian coordinates
        new_x = radius * math.cos(angle)
        new_y = radius * math.sin(angle)

        # Update the object's position
        self.x_pos = target[0] + new_x
        self.y_pos = target[1] + new_y


class EnemyDodge(Enemy):
    pass