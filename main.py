import pygame
from Game import Game
from Enemy import Enemy
from Stage import Stage


# pygame setup
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
game = Game()
game.stage.spawn_enemy(Enemy(1.0, 100.0, 100, 50, 50, 50))
mouseX, mouseY = pygame.mouse.get_pos()
CENTER = (WIDTH/2, HEIGHT/2)

while running:
    keys = pygame.key.get_pressed()  # Checking pressed keys
    if keys[pygame.K_w]:
        game.player.move(-1, 0)
        
    if keys[pygame.K_a]:
        game.player.move(0, 1)
    if keys[pygame.K_s]:
        game.player.move()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    #*Render all enemies
    for enemy in game.stage.enemies:
        enemy.handle_movement(CENTER[0], CENTER[1])
        #pygame.draw.rect(screen, pygame.Color(255, 0, 0, 0), pygame.Rect(enemy.x_pos, enemy.y_pos, enemy.width, enemy.height))
        enemy.draw(screen)

    #*render the player

    game.player.draw(screen)



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()