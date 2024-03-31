import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720



def main(screen):
    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill('green')

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    main(screen)
