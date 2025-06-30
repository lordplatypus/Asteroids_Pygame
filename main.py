import pygame
from constants import *
from player import Player

def main():
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update
        updatable.update(delta_time)

        # Draw
        surface.fill("black")

        for element in drawable:
            element.draw(surface)

        pygame.display.flip()

        # Delta Time / Framerate
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()