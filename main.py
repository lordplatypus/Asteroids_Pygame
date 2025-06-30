import pygame
from constants import *

def main():
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    while True:
        # Get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw
        surface.fill("black")
        pygame.display.flip()

        # Delta Time / Framerate
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()