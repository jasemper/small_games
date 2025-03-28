# Images were created using img2go.com
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 500
PLAYER_SPEED = 7
OBSTACLE_SPEED = 5
WHITE = (255, 255, 255)
tick_counter = 0
i = -1

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy bird")

# Load images
background = pygame.image.load('back.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Resize the image
bird1 = pygame.image.load('bird1.png')
bird1 = pygame.transform.scale(bird1, (PLAYER_SIZE, PLAYER_SIZE))  # Resize the image
bird2 = pygame.image.load('bird2.png')
bird2 = pygame.transform.scale(bird2, (PLAYER_SIZE, PLAYER_SIZE))  # Resize the image
obstacle_image1 = pygame.image.load('pipe1.png')
obstacle_image1 = pygame.transform.scale(obstacle_image1, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))  # Resize the image
obstacle_image2 = pygame.image.load('pipe2.png')
obstacle_image2 = pygame.transform.scale(obstacle_image2, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))  # Resize the image
#obstacle_image1 = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT), pygame.SRCALPHA)
#pygame.draw.rect(obstacle_image1, (255, 0, 0), (0, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
#obstacle_image2 = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT), pygame.SRCALPHA)
#pygame.draw.rect(obstacle_image2, (255, 0, 0), (0, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

# Game variables
player_x = WIDTH // 3 - PLAYER_SIZE // 2
player_y = HEIGHT // 2 - PLAYER_SIZE // 2
obstacles1 = []
obstacles2 = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Movement of the character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_y > 0:
        player_y -= PLAYER_SPEED * 1.5
    elif player_y < HEIGHT - PLAYER_SIZE:
        player_y += PLAYER_SPEED * 1.5

    # Generate obstacles
    if tick_counter == 0:
        obstacle_y = random.randint(300, (300 + HEIGHT / 2))
        obstacle_x = WIDTH + OBSTACLE_WIDTH
        obstacles2.append((obstacle_x, obstacle_y))
        obstacle_y = obstacle_y - 150 - OBSTACLE_HEIGHT
        obstacles1.append((obstacle_x, obstacle_y))

    # Update obstacle positions
    obstacles1 = [(x - OBSTACLE_SPEED, y) for x, y in obstacles1 if y < HEIGHT]
    obstacles2 = [(x - OBSTACLE_SPEED, y) for x, y in obstacles2 if y < HEIGHT]

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    for obstacle_x, obstacle_y in obstacles1:
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        if player_rect.colliderect(obstacle_rect):
            print("Game Over!")
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw Background
    screen.blit(background, (0, 0))

    # Draw player
    if (tick_counter%15) // 2 < 3:
        screen.blit(bird1, (player_x, player_y))
    else:
        screen.blit(bird2, (player_x, player_y))

    # Draw obstacles
    for obstacle_x, obstacle_y in obstacles1:
        screen.blit(obstacle_image1, (obstacle_x, obstacle_y))
    for obstacle_x, obstacle_y in obstacles2:
        screen.blit(obstacle_image2, (obstacle_x, obstacle_y))

    font = pygame.font.SysFont(None, 36)
    score = str(i)
    caption_text = font.render(score, True, (0, 0, 0))
    screen.blit(caption_text, (WIDTH - 22, 0))

    # Update the display
    pygame.display.flip()

    # Increment the tick counter
    tick_counter += 1

    # Reset the tick counter to 0 after 15 ticks
    if tick_counter == 60:
        tick_counter = 0
        i += 1

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
