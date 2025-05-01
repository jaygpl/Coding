# random is used for the food placement in the game
import random

import pygame

# this will initialize all imported Pygame modules
pygame.init()

# this will create 
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# this will determine the colouring in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# changes the speed of the game, the size of one segment of the snake and how fast the snake will move
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# this is used to render text for the messages and score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

# shows the current score whilst playing the game at the top-left of the screen
def your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [10, 10])

# this draws each part of the snake's body using a green rectangle
def our_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block, block])

# this will show the "game over" message on the screen if the player dies
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# this ends the game and triggers the "you lost" screen
def gameLoop():
    game_over = False
    game_close = False

# this will set the starting position for the snake and control its movement direction
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

# this keeps track of snake segments and helps with placing the food in random positions
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# this loop runs until the player quits
    while not game_over:
        # this will display the game over message and score
        while game_close:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # the user can press q the quit or c to restart on their keyboard
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # this will quit the game or change the snake's direction based on the arrow key that is pressed
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

        # updates the snake's position
        x1 += x1_change
        y1 += y1_change

        # ends the game if the snake goes out of bounds
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # this draws the food at its current position
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # updates the snake's body and adds the head position of the snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # removes the tail segment if the snake doesn't just eat food
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # ends game if the snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # draws the snake and the current score
        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        # when snake eats food, a new food is spawned and the snake grows in length
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # determines how fast the game loop runs
        clock.tick(snake_speed)

    # this ends the Pygame session and closes the program entirely
    pygame.quit()
    quit()

# this starts the game
gameLoop()

