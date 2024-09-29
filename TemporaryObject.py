class TemporaryObject:
    color: tuple[int, int, int]
    speed: int
    def __init__(self):
        color = (255, 255, 255)
    
    def draw(self, screen):
        pass
    
    def tick_down(self):
        pass

class SniperTrail(TemporaryObject):
    
 def __init__(self, color=(255, 255, 255), speed=0):
        super().__init__(color, speed)
        # SniperTrail specific initialization, if any
        pass
        
        
class ChainSaw(TemporaryObject):
    
    def __init__(self, color=(245, 245, 245), speed=0):
        super().__init__(color, speed)
    # SniperTrail specific initialization, if any
    pass


class JackHammer(TemporaryObject):
    
    def __init__(self, color=(235, 235, 235), speed=0):
        super().__init__(color, speed)
    # SniperTrail specific initialization, if any
    pass
    
    
    class ShortGun(TemporaryObject):
        
        def __init__(self, color=(225, 225, 225), speed=0):
            super().__init__(color, speed)
    # SniperTrail specific initialization, if any
    pass
    
    
    
