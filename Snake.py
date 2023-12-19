import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake parameters
snake_block = 10
snake_speed = 15

# Snake function
def snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(display, green, [segment[0], segment[1], snake_block, snake_block])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0

    # Initial snake length
    snake_list = []
    length_of_snake = 1

    # Initial food position
    foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            # Game over screen
            display.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            display.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
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

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Check boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Draw food
        display.fill(black)
        pygame.draw.rect(display, white, [foodx, foody, snake_block, snake_block])

        # Draw snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake eats food
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Update display
        snake(snake_block, snake_list)
        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Set snake speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Run the game loop
game_loop()
