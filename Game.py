from Stage import Stage
from Player import Player

class Game:
    stage: Stage
    player: Player
    def __init__(self):
        self.stage = Stage()
        self.player = Player()
    
