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
    
    def handle_movement(self, targetx: float, targety: float) -> None:

        directionx = (self.x_pos - targetx)/(((self.x_pos**2) + (self.y_pos**2))**0.5)
        directiony = (self.y_pos - targety)/(((self.x_pos**2) + (self.y_pos**2))**0.5)
        self.x_pos += self.speed * directionx
        self.y_pos += self.speed * directiony

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
