import pygame
from Game import Game
from Enemy import *
from Stage import Stage
import math


# pygame setup
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
game = Game((WIDTH, HEIGHT))
game.stage.spawn_enemy(Rectangle(1, 100.0, 100, 50, 25, 50, 100))
game.stage.spawn_enemy(EnemySpiral(1, 100.0, 400, 700, 25, 50, 100))
mouseX, mouseY = pygame.mouse.get_pos()
CENTER = (WIDTH/2, HEIGHT/2)
BOX_SIZE = 40
BOX_SPACE = 25
for i in range(100):
    game.stage.spawn_bullet(game.player.create_bullet(500, 500, [math.sin(i),math.cos(i)]))


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))



while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and game.player.current_gun.can_fire():
            game.shoot((mouseX, mouseY))
            fired = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game.player.swap_gun(0)
            if event.key == pygame.K_2:
                game.player.swap_gun(1)
                print(True)
            if event.key == pygame.K_3:
                game.player.swap_gun(2)
            if event.key == pygame.K_4:
                game.player.swap_gun(3)
    actions = pygame.key.get_pressed()
    #game.player.handle_movement(actions[pygame.K_a], actions[pygame.K_d], actions[pygame.K_w], actions[pygame.K_s])
    if pygame.mouse.get_pressed()[0] and game.player.current_gun.autofire and game.player.current_gun.can_fire():
        game.shoot((mouseX, mouseY))
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    #*render the homebase
    pygame.draw.rect(screen, pygame.Color("green"), pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30))

    #*Render all enemies
    for enemy in game.stage.enemies:
        game.stage.handle_enemy_movement(enemy, CENTER)
        #pygame.draw.rect(screen, pygame.Color(255, 0, 0, 0), pygame.Rect(enemy.x_pos, enemy.y_pos, enemy.width, enemy.height))
        enemy.draw(screen, CENTER)

    
    #*Render all bullets

    for bullet in game.stage.bullets:
        bullet.handle_movement()
        bullet.draw(screen)

    game.do_collisions()

    #* Draw the UI
    for i in range(len(game.player.guns)):
        color = pygame.Color("red")
        #image = game.player.guns[i].get_image()
        if game.player.current_gun == game.player.guns[i]:
            color = pygame.Color("green")
        pygame.draw.rect(screen, color, pygame.Rect(30+i*(40+BOX_SPACE), HEIGHT-30-BOX_SIZE, BOX_SIZE, BOX_SIZE), 2)
        pygame.draw.rect(screen, color, pygame.Rect(30+i*(40+BOX_SPACE), HEIGHT-30-BOX_SIZE+(BOX_SIZE*(1-game.player.guns[i].ammo_percentage())), BOX_SIZE, BOX_SIZE*game.player.guns[i].ammo_percentage()))

    
    #*Handle any misc operations
    game.player.current_gun.shoot_delay_tick_down()

    for gun in game.player.guns:
        if gun != game.player.current_gun:
            gun.reload()
    #for tempobj in game.stage.temporary_objects:
        #pass



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


