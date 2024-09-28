import pygame
class Player:
    def __init__(self):

        self.x = 50
        self.y = 50
        self.speed = 5

    #*x and y should either be 1 or -1 to indicate direction
    def move(self, x: int, y: int):
        self.x += x * self.speed
        self.y += y * self.speed

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, pygame.Color("green"), (self.x, self.y), 20)


