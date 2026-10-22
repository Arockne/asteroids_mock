import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    #System info
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #containers
    Player.containers = (updatable, drawable)

    #initialized objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #game loop
    while True:
        log_state()
        #check for player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update game world
        screen.fill("black")
        updatable.update(dt)

        #draw game on screen
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        
        #limit to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
