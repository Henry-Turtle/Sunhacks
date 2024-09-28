import pygame
from Game import Game
from Enemy import Enemy
from Stage import Stage

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
game = Game()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for enemy in game.stage.enemies:
        pygame.draw.rect(screen, pygame.Color(255, 0, 0, 0), pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()