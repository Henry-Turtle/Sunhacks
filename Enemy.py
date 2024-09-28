class Enemy:

    def __init__(self, speed: float, dmg: float, x: float, y: float, width: float, height: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Enemy [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}, {self.width}, {self.height}]"
    
    def handle_movement(self) -> None:

        self.x_pos = self.speed * (self.x_pos)
        self.y_pos = self.speed * (self.y_pos)

class Triangle(Enemy):

    def __init__(self, speed: float, dmg: float, x: float, y: float, side: float) -> None:
        self.speed = speed
        self.damage = dmg
        self.x_pos = x
        self.y_pos = y
        self.side = side

    def __str__(self) -> str:
        return f"Triangle [{self.x_pos}, {self.y_pos}, {self.speed}, {self.damage}]"


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
