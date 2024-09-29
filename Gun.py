import pygame

class Gun:
    bullet_speed: float
    bullet_damage: float #How many radians in either idrection the bullet can spread
    bullet_spread: float
    max_ammo: float
    ammo: float
    reload_per_tick: int
    bullet_size: int
    autofire: bool
    shoot_delay_ticks: int
    current_shoot_delay_ticks: int = 0

    def shoot_delay_tick_down(self):
        if self.current_shoot_delay_ticks > 0:
            self.current_shoot_delay_ticks -= 1
            return

    def reload(self) -> None:
        if self.ammo < self.max_ammo:
            self.ammo += self.reload_per_tick
            return
        if self.ammo > self.max_ammo:
            self.ammo = self.max_ammo
            return
        return
    
    def can_fire(self)->bool:
        return self.current_shoot_delay_ticks == 0 and self.ammo >= 1
    
    def ammo_percentage(self)->float:
        return self.ammo / self.max_ammo

    def draw(self, screen: pygame.Surface):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        pygame.draw.line(screen, pygame.Color(0, 150, 50), [mouse_x, mouse_y-4], [mouse_x, mouse_y-14], 3)
        pygame.draw.line(screen, pygame.Color(0, 150, 50), [mouse_x, mouse_y+4], [mouse_x, mouse_y+14], 3)
        pygame.draw.line(screen, pygame.Color(0, 150, 50), [mouse_x-4, mouse_y], [mouse_x-14, mouse_y], 3)
        pygame.draw.line(screen, pygame.Color(0, 150, 50), [mouse_x+4, mouse_y], [mouse_x+14, mouse_y], 3)

class MachineGun(Gun):
    def __init__(self):
        self.bullet_spread = 0.5
        self.bullet_damage = 20
        self.bullet_speed = 7
        self.max_ammo = 20
        self.ammo = 20
        self.reload_per_tick = 1/30
        self.bullet_size= 5
        self.autofire = True
        self.shoot_delay_ticks = 10

class SniperRifle(Gun):
    def __init__(self):
        self.bullet_spread = 0
        self.bullet_damage = 100
        self.bullet_speed = 20
        self.max_ammo = 2
        self.ammo = 2
        self.reload_per_tick = 1/240
        self.bullet_size = 2
        self.autofire = False
        self.shoot_delay_ticks = 60

class Shotgun(Gun):
    def __init__(self):
        self.bullet_spread = 0.5
        self.bullet_speed = 10
        self.bullet_damage = 30
        self.max_ammo = 4
        self.ammo = 4
        self.reload_per_tick = 1/120
        self.bullet_size = 6
        self.autofire = False
        self.shoot_delay_ticks = 30

    def draw(self, screen: pygame.Surface):
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, pygame.Color(0, 150, 50), [mouse_x, mouse_y], 15, 2)

class GrenadeLauncher(Gun):
    def __init__(self):
        self.bullet_spread = 0
        self.bullet_speed = 10
        self.bullet_damage = 80
        self.max_ammo = 5
        self.ammo = 5
        self.reload_per_tick = 1/150
        self.bullet_size = 10
        self.autofire = False
        self.shoot_delay_ticks = 20

    def draw(self, screen: pygame.Surface):
    
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, pygame.Color(0, 150, 50, 0), pygame.Rect(mouse_x-15, mouse_y-15, 30, 30), 2)
