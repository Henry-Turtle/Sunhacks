class Enemy:

    def __init__(self, type: str, speed: float, dmg: float) -> None:
        self.type = type
        self.speed = speed
        self.damage = dmg

    def __str__(self) -> str:
        return f"Enemy ['{type}', {self.speed}, {self.damage}]"

