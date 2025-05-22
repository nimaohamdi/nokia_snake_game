import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Window size
width = 600
height = 400

# Create game window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Nokia Snake Game')

# Game clock
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Display score
def score_display(score):
    value = score_font.render("Score: " + str(score), True, green)
    win.blit(value, [0, 0])

# Draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

# Game over message
def game_over_message():
    msg = font_style.render("You Lost! Press R to Restart or Q to Quit", True, red)
    win.blit(msg, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(blue)
            game_over_message()
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check wall collision
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(blue)
        pygame.draw.rect(win, green, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
