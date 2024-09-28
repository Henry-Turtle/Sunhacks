from Stage import Stage
from Player import Player
import pygame

class Game:
    stage: Stage
    player: Player
    
    def __init__(self):
        self.stage = Stage()
        self.player = Player()
    
    def shoot(self):
        damaged_enemies = self.player.getCrosshair().collidelistall(self.stage.enemies)

