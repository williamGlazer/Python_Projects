import pygame

# -------------------------------------------------------------------
#                           CONSTANTS
# -------------------------------------------------------------------

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TITLE = "My Game"
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


# -------------------------------------------------------------------
#                           CLASSES
# -------------------------------------------------------------------


class Game:

    FPS = 60
    is_game_over = False

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE)
        pygame.display.set_caption(title)

    def run_game_loop(self, level):

        won = False

        is_game_over = False
        direction = 0
        player_character = Player('Player.png', 350, 780, 80, 80)

        enenemy_0 = Enemy('Enemy.png', 20, 400, 50, 50)
        enenemy_0.SPEED *= level

        enenemy_1 = Enemy('Enemy.png', 780, 500, 50, 50)
        enenemy_1.SPEED *= level*0.75

        enenemy_2 = Enemy('Enemy.png', 500, 200, 50, 50)
        enenemy_2.SPEED *= level

        goal = GameObject('Treasure.png', 300, 50, 200, 200)

        while not is_game_over:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    is_game_over = True

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        is_game_over = True

                    down_press = event.key == pygame.K_UP
                    up_press = event.key == pygame.K_DOWN

                    if down_press and up_press:
                        direction = 0

                    elif down_press:
                        if direction == -1:
                            direction = 0
                        else:
                            direction = 1

                    elif up_press:
                        if direction == 1:
                            direction = 0
                        else:
                            direction = -1

                elif event.type == pygame.KEYUP:
                    down_press = event.key == pygame.K_UP
                    up_press = event.key == pygame.K_DOWN

                    if down_press or up_press:
                        direction = 0

                print(event)

            self.game_screen.fill(WHITE)

            goal.draw(self.game_screen)

            player_character.move(direction)
            player_character.draw(self.game_screen)

            enenemy_0.move(self.game_screen)
            enenemy_0.draw(self.game_screen)

            if level >= 2:
                enenemy_1.move(self.game_screen)
                enenemy_1.draw(self.game_screen)
            if level >= 3:
                enenemy_2.move(self.game_screen)
                enenemy_2.draw(self.game_screen)

            if player_character.detect_collision(enenemy_0) or player_character.detect_collision(enenemy_1) or player_character.detect_collision(enenemy_2):
                is_game_over = True
                won = False
                text = font.render('You suck', True, BLACK)
                self.game_screen.blit(text, (300, 300))
                pygame.display.update()
                clock.tick(1)
                break

            if player_character.detect_collision(goal):
                is_game_over = True
                won = True
                text = font.render('...', True, BLACK)
                self.game_screen.blit(text, (370, 300))
                pygame.display.update()
                clock.tick(1)
                break

            pygame.display.update()
            clock.tick(self.FPS)

        if won:
            self.run_game_loop(level + 0.25)


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

        self.object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.object_image, (width, height))

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class Player(GameObject):

    SPEED = 7

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction):

        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= SCREEN_HEIGHT - self.height or self.y_pos <= 0:
            self.y_pos = SCREEN_HEIGHT - self.height

    def detect_collision(self, other_entity):
        if self.y_pos >= other_entity.y_pos + other_entity.height:
            return False
        elif self.y_pos + self.height < other_entity.y_pos:
            return False

        if self.x_pos >= other_entity.x_pos + other_entity.width:
            return False
        elif self.x_pos + self.width < other_entity.x_pos:
            return False

        return True


class Enemy(GameObject):

    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, game_screen):

        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)

        elif self.x_pos >= game_screen.get_width() - 70:
            self.SPEED = -abs(self.SPEED)

        self.x_pos += self.SPEED

# -------------------------------------------------------------------
#                           RUN
# -------------------------------------------------------------------


pygame.init()


new_game = Game(TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)


pygame.quit()
