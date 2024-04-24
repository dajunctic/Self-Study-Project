from attribute import *
# from manager import Manager
from gameplay import Gameplay

if __name__ == '__main__':
    run = True

    game = Gameplay()

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        game.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        pygame.display.update()
    pygame.quit()
