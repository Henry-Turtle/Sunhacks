import pygame
from Game import Game
from Enemy import *
from Stage import Stage
import math
from Bullet import *
from Gun import *
import sys
import random

class main:

    actions = [0, 0, 0, 0]

    def __init__(self):
# pygame setup
        pygame.init()
        pygame.font.init() 
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)

        self.big_font = pygame.font.SysFont('Ariel', 80)
        self.medium_font = pygame.font.SysFont('Ariel', 60)
        self.WIDTH = 1400
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game = Game((self.WIDTH, self.HEIGHT))
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.CENTER = (self.WIDTH/2, self.HEIGHT/2)
        self.BOX_SIZE = 40
        self.BOX_SPACE = 25
        self.state = "playing"
        self.flag = False
        self.round = 1

        self.RED = pygame.Color(255,73,79)
        self.WHITE = pygame.Color("white")
        self.guns = [MachineGun(), Shotgun(), SniperRifle(), GrenadeLauncher()]

        self.reload_cost = 100
        self.width_cost = 50
        self.radius_cost = 150
        self.damage_cost = 50


    def handle_start(self):
        self.__init__()
        pass

    def handle_playing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                self.mouseX, self.mouseY = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and self.game.player.current_gun.can_fire():
                self.game.shoot((self.mouseX, self.mouseY))
                fired = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game.player.swap_gun(0)
                if event.key == pygame.K_2:
                    self.game.player.swap_gun(1)
                    print(True)
                if event.key == pygame.K_3:
                    self.game.player.swap_gun(2)
                if event.key == pygame.K_4:
                    self.game.player.swap_gun(3)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.actions[1] = 1
        if keys[pygame.K_d]:
            self.actions[0] = 1
        if keys[pygame.K_w]:
            self.actions[3] = 1
        if keys[pygame.K_s]:
            self.actions[2] = 1
        #actions = pygame.key.get_pressed()
        self.game.player.handle_movement(self.actions[0], self.actions[1], self.actions[2], self.actions[3])
        if self.game.player.pos_x > self.WIDTH:
            self.game.player.pos_x = self.WIDTH
        if self.game.player.pos_x < 0:
            self.game.player.pos_x = 0
        if self.game.player.pos_y > self.HEIGHT:
            self.game.player.pos_y = self.HEIGHT
        if self.game.player.pos_y < 0:
            self.game.player.pos_y = 0
        


        self.actions = [0, 0, 0, 0] 
        if pygame.mouse.get_pressed()[0] and self.game.player.current_gun.autofire and self.game.player.current_gun.can_fire():
            self.game.shoot((self.mouseX, self.mouseY))

        # self.game.player.current_gun.draw(self.screen)
        # fill the self.screen with a color to wipe away anything from last frame
        self.screen.fill("black")

        self.game.do_collisions()
        # RENDER YOUR GAME HERE
        for obj in self.game.stage.temporary_objects:
            obj.draw(self.screen)
            self.game.stage.decay_temporary_object(obj)
        
        

        #*render the homebase
        # pygame.draw.rect(self.screen, pygame.Color("green"), pygame.Rect(self.WIDTH/2 - 15, self.HEIGHT/2 - 15, 30, 30))
        pygame.draw.rect(self.screen, pygame.Color("green"), pygame.Rect(self.game.player.pos_x - 15, self.game.player.pos_y - 15, 30, 30))

        self.game.spawn_enemies()
        #*Render all enemies
        for enemy in self.game.stage.enemies:
            self.game.stage.handle_enemy_movement(enemy, (self.game.player.pos_x - 15, self.game.player.pos_y - 15))
            enemy.draw(self.screen, self.CENTER)
            # if enemy.getRect().colliderect(pygame.Rect(self.WIDTH/2 - 15, self.HEIGHT/2 - 15, 30, 30)):
            if enemy.getRect().colliderect(self.game.player.get_rect()):
                self.game.player.current_health -= enemy.damage
                self.game.destroy_enemy(enemy, False)
            if self.game.player.current_health <= 0:
                self.state = "gameover"
                self.game.destroy_enemy(enemy)

        if len(self.game.stage.enemies) == 0 and self.game.stage.enemies_spawned >= self.game.stage.max_enemies:
            print("Round Over")
            self.state = "skilltree"


        
        #*Render and process all bullets

        for bullet in self.game.stage.bullets:
            bullet.handle_movement()
            if bullet.pos_x > self.WIDTH or bullet.pos_x < 0 or bullet.pos_y < 0 or bullet.pos_y > self.HEIGHT:
                self.game.stage.bullets.remove(bullet)
            if bullet.type == "grenade":
                bullet.ticks_loaded += 1
                if bullet.ticks_loaded > 180:
                    self.game.explode_grenade(bullet)
                bullet.speed = math.e **(2.5-bullet.ticks_loaded/30)
            elif bullet.type == "shotgun":
                bullet.ticks_loaded += 1
            bullet.draw(self.screen)


        #* Draw the UI
        for i in range(len(self.game.player.guns)):
            color =self.RED
            #image = self.game.player.guns[i].get_image()
            if self.game.player.current_gun == self.game.player.guns[i]:
                color = pygame.Color("green")
            pygame.draw.rect(self.screen, color, pygame.Rect(30+i*(40+self.BOX_SPACE), self.HEIGHT-30-self.BOX_SIZE, self.BOX_SIZE, self.BOX_SIZE), 2)
            pygame.draw.rect(self.screen, color, pygame.Rect(30+i*(40+self.BOX_SPACE), self.HEIGHT-30-self.BOX_SIZE+(self.BOX_SIZE*(1-self.game.player.guns[i].ammo_percentage())), self.BOX_SIZE, self.BOX_SIZE*self.game.player.guns[i].ammo_percentage()))

        color = self.RED
        pygame.draw.rect(self.screen, color, pygame.Rect(30, 30, 150*(self.game.player.current_health/self.game.player.max_health), 30))
        color = pygame.Color("white")
        pygame.draw.rect(self.screen, color, pygame.Rect(30, 30, 150, 30), 2)
        text = "$" + str(round(self.game.money,2)) + f"Round {self.round}".rjust(50)
        moneytext = self.medium_font.render(text, False, color)
        self.screen.blit(moneytext, (30+150+30, 30))
        
        #*Handle any misc operations
        self.game.player.current_gun.shoot_delay_tick_down()

        for gun in self.game.player.guns:
            if gun != self.game.player.current_gun:
                gun.reload()
                gun.shoot_delay_tick_down()
        self.game.player.current_gun.draw(self.screen)
        #for tempobj in self.game.stage.temporary_objects:
            #pass



        # flip() the display to put your work on self.screen
        pygame.display.flip()
        self.game.ticks+=1  

    def handle_gameover(self):
        gameover: pygame.Surface = self.big_font.render("GAME OVER", False, pygame.Color("white"), self.RED)
        click: pygame.Surface = self.medium_font.render("CLICK TO CONTINUE", False, pygame.Color("white"), self.RED)

        self.screen.blit(gameover, (self.WIDTH/2-gameover.get_width()/2, self.HEIGHT/2-gameover.get_height()/2))
        self.screen.blit(click, (self.WIDTH/2-click.get_width()/2, self.HEIGHT/2-click.get_height()/2+100))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEMOTION:
                self.mouseX, self.mouseY = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "start"
                print(True)
                return

    def handle_skilltree(self):
        self.screen.fill(pygame.Color("black"))

        money = self.big_font.render("Cash: $" + str(round(self.game.money, 2)), False, self.WHITE)
        self.screen.blit(money, (50, 75))
        newgame = self.medium_font.render("Next Round", False, self.WHITE, self.RED)
        self.screen.blit(newgame, (self.WIDTH - 20-newgame.get_width(), self.HEIGHT - 20-newgame.get_height()))
        newgame_rect = pygame.Rect(self.WIDTH - 20 - newgame.get_width(), self.HEIGHT - 20 - newgame.get_height(), newgame.get_width(), newgame.get_height())

        reload = self.medium_font.render("Upgrade Reload: $" + str(self.reload_cost), False, self.WHITE, self.RED)
        reload_rect = reload.get_rect()
        reload_rect.top = self.HEIGHT/2-200
        reload_rect.left = self.WIDTH/2-200
        
        damage = self.medium_font.render("Upgrade Damage: $" + str(self.damage_cost), False, self.WHITE, self.RED)
        damage_rect = damage.get_rect()
        damage_rect.top = self.HEIGHT/2
        damage_rect.left = self.WIDTH/2-200

        if not self.flag:
            self.check = random.randrange(2)
            self.flag = True

        if not self.check:
            size = self.medium_font.render("Upgrade Attack Size: $" + str(self.width_cost), False, self.WHITE, self.RED)
            size_rect = size.get_rect()
            size_rect.top = self.HEIGHT/2+200
            size_rect.left = self.WIDTH/2-200
            self.screen.blits([(reload, (self.WIDTH/2-200, self.HEIGHT/2-200)), (damage, (self.WIDTH/2-200, self.HEIGHT/2)), (size, (self.WIDTH/2-200, self.HEIGHT/2+200))])
        
        else:
            radius = self.medium_font.render("Upgrade Bomb Radius: $" + str(self.radius_cost), False, self.WHITE, self.RED)
            radius_rect = radius.get_rect()
            radius_rect.top = self.HEIGHT/2+200
            radius_rect.left = self.WIDTH/2-200


            self.screen.blits([(reload, (self.WIDTH/2-200, self.HEIGHT/2-200)), (damage, (self.WIDTH/2-200, self.HEIGHT/2)), (radius, (self.WIDTH/2-200, self.HEIGHT/2+200))])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEMOTION:
                self.mouseX, self.mouseY = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if newgame_rect.collidepoint(self.mouseX, self.mouseY):
                    self.game.max_enemies = int(self.game.max_enemies * 1.5)
                    self.game.stage.enemies_spawned = 0
                    self.game.reset(self.guns)
                    self.state = "playing"
                    self.flag = False
                    print(self.game.stage.max_enemies, self.game.stage.enemies_spawned)
                    self.round += 1
                    print(self.game.stage.max_enemies, self.game.stage.enemies_spawned)


                if reload_rect.collidepoint(self.mouseX, self.mouseY) and self.game.money >= self.reload_cost:
                    print("BOUGHT RELOAD")
                    self.game.money -= self.reload_cost
                    self.reload_cost = self.reload_cost * 2
                    for gun in self.guns:
                        gun.reload_per_tick = gun.reload_per_tick * 2
                    
                if damage_rect.collidepoint(self.mouseX, self.mouseY) and self.game.money >= self.damage_cost:
                    print("BOUGHT DAMAGE")
                    for gun in self.guns:
                        gun.bullet_damage = gun.bullet_damage + 5
                    self.game.money -= self.damage_cost
                    self.damage_cost = self.damage_cost * 2

                if not self.check:
                    if size_rect.collidepoint(self.mouseX, self.mouseY) and self.game.money >= self.width_cost:
                        print("BOUGHT SIZE")
                        for gun in self.guns:
                            gun.bullet_size = gun.bullet_size + 3
                        self.game.money -= self.width_cost
                        self.width_cost = self.width_cost * 2

                elif radius_rect.collidepoint(self.mouseX, self.mouseY) and self.game.money >= self.radius_cost:
                    print("BOUGHT RADIUS")
                    self.game.grenade_radius += 10
                    self.game.money -= self.radius_cost
                    self.radius_cost = self.radius_cost * 2
                    

                    
        pygame.display.flip()

    def loop(self):
        while self.running:
            self.clock.tick(60)  # limits FPS to 60
            if self.state == "start":
                pygame.mouse.set_visible(False)
                self.flag = False
                self.handle_start()
            elif self.state == "playing":
                self.flag = False
                pygame.mouse.set_visible(False)
                self.handle_playing()
            elif self.state == "gameover":
                self.flag = False
                pygame.mouse.set_visible(True)
                self.handle_gameover()
            elif self.state == "skilltree":
                pygame.mouse.set_visible(True)
                self.handle_skilltree()

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        
        
        pygame.quit()

instance = main()
instance.loop()


