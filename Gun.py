class Gun:
    bullet_speed: float
    bullet_damage: float #How many radians in either idrection the bullet can spread
    bullet_spread: float
    ammo: int
    reload_per_tick: int
    bullet_size: int

class MachineGun(Gun):
    def __init__(self):
        self.bullet_spread = 0.5
        self.bullet_damage = 1
        self.bullet_speed = 1
        self.ammo = 20
        self.reload_per_tick = 0.25
        self.bullet_size= 5