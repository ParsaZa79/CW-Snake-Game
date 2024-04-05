import pygame
import random

pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

snake_block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(window_width / 2, window_height / 2)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, direction):
        if self.length > 1 and (direction == self.direction or (direction + self.direction) in [pygame.K_UP + pygame.K_DOWN, pygame.K_LEFT + pygame.K_RIGHT]):
            return
        self.direction = direction

    def move(self):
        cur = self.get_head_position()
        x, y = cur
        if self.direction == pygame.K_UP:
            y -= snake_block_size
        elif self.direction == pygame.K_DOWN:
            y += snake_block_size
        elif self.direction == pygame.K_LEFT:
            x -= snake_block_size
        elif self.direction == pygame.K_RIGHT:
            x += snake_block_size
        new = (x, y)
        if new in self.positions[1:]:
            return True  # Snake collided with itself
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return False  # Snake did not collide with itself

    def reset(self):
        self.length = 1
        self.positions = [(window_width / 2, window_height / 2)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, green, pygame.Rect(p[0], p[1], snake_block_size, snake_block_size))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(pygame.K_UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(pygame.K_DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(pygame.K_LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(pygame.K_RIGHT)
               
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, window_width - snake_block_size) // snake_block_size * snake_block_size,
                         random.randint(0, window_height - snake_block_size) // snake_block_size * snake_block_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], snake_block_size, snake_block_size))
        
def game_loop():
    game_over = False
    game_close = False

    snake = Snake()
    food = Food()

    while not game_over:
        while game_close:
            window.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        snake.handle_keys()
        window.fill(black)

        if snake.move():
            game_close = True
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        snake.draw(window)
        food.draw(window)

        pygame.display.update()

        if snake.get_head_position()[0] >= window_width or snake.get_head_position()[0] < 0 or snake.get_head_position()[1] >= window_height or snake.get_head_position()[1] < 0:
            game_close = True

        pygame.time.delay(100)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])

game_loop()