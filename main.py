import pygame
from Game import Game
from Enemy import Enemy
from Stage import Stage


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
running = True
mygame = Game()
mygame.stage.spawn_enemy(Enemy(1.0, 100.0, 100, 50, 50, 50))
mouseX, mouseY = pygame.mouse.get_pos()

while running:
    # poll for events   jk 
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
    for enemy in mygame.stage.enemies:
        enemy.handle_movement(screen.get_width()/2, screen.get_height()/2)
        #pygame.draw.rect(screen, pygame.Color(255, 0, 0, 0), pygame.Rect(enemy.x_pos, enemy.y_pos, enemy.width, enemy.height))
        enemy.draw(screen)

    #*render the crosshairs

    pygame.draw.circle(screen, pygame.Color("blue"), (mouseX, mouseY), 50, 1)



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()