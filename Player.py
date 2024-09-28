import pygame
class Player:
    def __init__(self):
        pass
    
    def getCrosshair(self, cursor: tuple[int]) -> pygame.Rect:
        x, y = cursor
        return pygame.Rect(x-10, y-10, 20, 20)

