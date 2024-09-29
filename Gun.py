class Gun:
    bullet_speed: float
    bullet_damage: float #How many radians in either idrection the bullet can spread
    bullet_spread: float
    ammo: int
    reload_per_tick: int
    bullet_size: int
    autofire: bool
    shoot_delay_ticks: int
    current_shoot_delay_ticks: int = 0

    def shoot_delay_tick_down(self):
        if self.current_shoot_delay_ticks > 0:
            self.current_shoot_delay_ticks -= 1
            return

    def reload(self):
        self.ammo += self.reload_per_tick
    
    def can_fire(self)->bool:
        return self.current_shoot_delay_ticks == 0

class MachineGun(Gun):
    def __init__(self):
        self.bullet_spread = 0.5
        self.bullet_damage = 20
        self.bullet_speed = 7
        self.ammo = 20
        self.reload_per_tick = 1/30
        self.bullet_size= 5
        self.autofire = True
        self.shoot_delay_ticks = 10