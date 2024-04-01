import pygame
from entities import *

SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 900

def backgroundMovement(screen, cursorX):
    """
    Make a moving background according to mouse position
    """

    backgroundImage = pygame.image.load('missile-command-assets/2D/bg.png') # Img size is 1200 x 900
    backgroundWater = pygame.image.load("missile-command-assets/2D/water.png")
    backgroundCrosshair = pygame.image.load("missile-command-assets/2D/bg_resequ_crosshair.png")

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
    screen.blit(backgroundCrosshair, (-50, 0))
    screen.blit(backgroundWater, (-50, SCREEN_HEIGHT - 50))

def spriteActivity():
    cityImgPath = [
        'missile-command-assets/2D/city01.png',
        'missile-command-assets/2D/city02.png',
        'missile-command-assets/2D/city03.png',
        'missile-command-assets/2D/city04.png',
        'missile-command-assets/2D/city05.png',
        'missile-command-assets/2D/bridge.png'
        ]

    citySprites = pygame.sprite.Group()
    enemyMissileSprites = pygame.sprite.Group()
    playerMissileSprites = pygame.sprite.Group()

    # Sprite activity
    # Cities
    city1 = City(cityImgPath[0], 20, SCREEN_HEIGHT - 105)
    city2 = City(cityImgPath[1], 275, SCREEN_HEIGHT - 125)
    city3 = City(cityImgPath[2], 450, SCREEN_HEIGHT - 100)
    city4 = City(cityImgPath[3], 630, SCREEN_HEIGHT - 120)
    city5 = City(cityImgPath[4], 900, SCREEN_HEIGHT - 100)
    bridge1 = City(cityImgPath[5], 110, SCREEN_HEIGHT - 100)
    citySprites.add(bridge1, city1, city2, city4, city3, city5, )

    # Player Missiles
    pMissile1 = PlayerMissile(90, SCREEN_HEIGHT - 55)
    pMissile2 = PlayerMissile(345, SCREEN_HEIGHT - 75)
    pMissile3 = PlayerMissile(520, SCREEN_HEIGHT - 50)
    pMissile4 = PlayerMissile(700, SCREEN_HEIGHT - 70)
    pMissile5 = PlayerMissile(970, SCREEN_HEIGHT - 50)
    playerMissileSprites.add(pMissile1, pMissile2, pMissile3, pMissile4, pMissile5)

    return citySprites, enemyMissileSprites, playerMissileSprites


def main(screen):

    clock = pygame.time.Clock()
    pygame.display.set_caption('Missile Command')
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    # All sprites stores here
    citySprites, enemyMissileSprites, playerMissileSprites = spriteActivity()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        # Get mouse position on screen for each frame
        cursorX, cursorY = pygame.mouse.get_pos()
        print(cursorX, cursorY)

        # Responsible for moving background
        backgroundMovement(screen, cursorX)

        # Update sprites
        citySprites.update()
        enemyMissileSprites.update()
        playerMissileSprites.update()

        # Draw sprites
        citySprites.draw(screen)
        enemyMissileSprites.draw(screen)
        playerMissileSprites.draw(screen)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    main(screen)
