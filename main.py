import pygame
from player import Player
from constants import *




def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    # Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add player to groups
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in updateable:
            sprite.draw(screen)
        
        for sprite in drawable:
            sprite.update(dt)


        pygame.display.flip()
        delta = Clock.tick(60)
        dt = delta / 1000

    


if __name__ == "__main__":
    main()
