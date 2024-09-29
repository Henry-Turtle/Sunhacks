import pygame
from Game import Game
from Enemy import *
from Stage import Stage


# pygame setup
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
game = Game((WIDTH, HEIGHT))
game.stage.spawn_enemy(Triangle(1, 100.0, 100, 50, 50))
game.stage.spawn_enemy(Triangle(1, 100.0, 400, 700, 50))
mouseX, mouseY = pygame.mouse.get_pos()
CENTER = (WIDTH/2, HEIGHT/2)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.shoot((mouseX, mouseY))


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    #*render the homebase
    pygame.draw.rect(screen, pygame.Color("green"), pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30))

    #*Render all enemies
    for enemy in game.stage.enemies:
        enemy.handle_movement(CENTER)
        #pygame.draw.rect(screen, pygame.Color(255, 0, 0, 0), pygame.Rect(enemy.x_pos, enemy.y_pos, enemy.width, enemy.height))
        enemy.draw(screen, CENTER)

    
    #*Render all bullets

    for bullet in game.stage.bullets:
        bullet.handle_movement()
        bullet.draw(screen)



    



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()