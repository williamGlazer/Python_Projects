import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT= 800
SCREEN_SIZE  = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_TITLE = "My Game" 

WHITE = (255, 255, 255)
BLACK = (0,   0,   0  )

is_game_over = False

FPS = 60
clock = pygame.time.Clock()

game_screen = pygame.display.set_mode(SCREEN_SIZE)
game_screen.fill(WHITE)
pygame.display.set_caption(SCREEN_TITLE)


while not is_game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_game_over = True

        print(event)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()