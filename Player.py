import pygame
from Gun import *
class Player:
    current_gun: Gun
    guns: list[Gun]

    def __init__(self):
        self.guns = []
        self.guns.append(MachineGun())

        self.current_gun = self.guns[0]
    

