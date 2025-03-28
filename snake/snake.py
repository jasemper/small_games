import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Snake variables
snake_size = 20
snake_speed = 15
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
speed = [snake_size, 0]

# Food variables
food_pos = [random.randrange(1, (width//snake_size)) * snake_size,
            random.randrange(1, (height//snake_size)) * snake_size]
food_spawn = True

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 35)
    game_over_surface = my_font.render('Your Score is: ' + str(len(snake_body)), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2, height/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Main game function
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Change direction
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
        speed = [0, -snake_size]
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
        speed = [0, snake_size]
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
        speed = [-snake_size, 0]
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
        speed = [snake_size, 0]

    # Update snake position
    snake_pos[0] += speed[0]
    snake_pos[1] += speed[1]

    # Check if snake hits the boundaries
    if snake_pos[0] < 0 or snake_pos[0] > width - snake_size or snake_pos[1] < 0 or snake_pos[1] > height - snake_size:
        game_over()

    # Check if snake eats food
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.insert(0, list(snake_pos))
        if len(snake_body) > 1:
            snake_body.pop()
    
    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (width//snake_size)) * snake_size,
                    random.randrange(1, (height//snake_size)) * snake_size]
        food_spawn = True

    # Draw background
    screen.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # Draw food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    # Refresh screen
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(snake_speed)

