import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
PLAYER_SPEED = 5
OBSTACLE_SPEED = 5
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subway Surfer")

# Load images
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(player_image, (0, 128, 255), (25, 25), 25)
obstacle_image = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE), pygame.SRCALPHA)
pygame.draw.rect(obstacle_image, (255, 0, 0), (0, 0, OBSTACLE_SIZE, OBSTACLE_SIZE))

# Game variables
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - 2 * PLAYER_SIZE
obstacles = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED

    # Generate obstacles
    if random.randint(0, 100) < 5:
        obstacle_x = random.randint(0, WIDTH - OBSTACLE_SIZE)
        obstacle_y = -OBSTACLE_SIZE
        obstacles.append((obstacle_x, obstacle_y))

    # Update obstacle positions
    obstacles = [(x, y + OBSTACLE_SPEED) for x, y in obstacles if y < HEIGHT]

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    for obstacle_x, obstacle_y in obstacles:
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_SIZE, OBSTACLE_SIZE)
        if player_rect.colliderect(obstacle_rect):
            print("Game Over!")
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Draw obstacles
    for obstacle_x, obstacle_y in obstacles:
        screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()

