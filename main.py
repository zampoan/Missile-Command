import pygame
import entities

SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 900

backgroundImage = pygame.image.load('missile-command-assets/2D/bg.png') # Img size is 1200 x 900
backgroundImageRect = backgroundImage.get_rect()

def backgroundMovement(screen, cursorX):
    """
    Make a moving background according to mouse position
    """
     # Calculate background position
    backgroundX = 0 
    backgroundY = 0

    # Adjust screen based off cursor position
    if cursorX < SCREEN_WIDTH / 2:

        # Ratio is 50:550, for every 11 px of screen, move 1 px of bg
        screenMovement= cursorX - SCREEN_WIDTH / 2

        ratio = screenMovement / 11
        
        backgroundX = int(ratio)
        
    elif cursorX > SCREEN_WIDTH / 2:
        
        screenMovement = cursorX - SCREEN_WIDTH / 2
        ratio = screenMovement / 11
        
        backgroundX = int(ratio)
    
    
    screen.blit(backgroundImage, (backgroundX, backgroundY))


def main(screen):
    clock = pygame.time.Clock()

    pygame.display.set_caption('Missile Command')

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        # Get mouse position on screen for each frame
        cursorX, cursorY = pygame.mouse.get_pos()

        # screen.blit(backgroundImage, (backgroundX, backgroundY))
        backgroundMovement(screen, cursorX)

        pygame.display.update()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    main(screen)
