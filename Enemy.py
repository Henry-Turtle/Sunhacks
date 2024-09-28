class Enemy:

    def __init__(self, type: str, speed: float, dmg: float, x: float, y: float) -> None:
        self.type = type
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y

    def __str__(self) -> str:
        return f"Enemy ['{type}', {self.speed}, {self.damage}]"
    
    def handle_movement():
        pass
