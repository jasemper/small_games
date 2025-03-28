# Images were created using img2go.com (except for the brick. The brick is from adobe)
import pygame
import sys
from random import randint

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 700
CHAR_WIDTH, CHAR_HEIGHT = 100, 100
CHAR_SPEED = 0.5
TEXT_COLOR = (0, 0, 0)
WORDS = {"man":"Mann", "men":"Männer", "woman":"Frau", "women":"Frauen", "child":"Kind", "children":"Kinder", "kitchen":"Küche", "bathroom":"Bad", "cat":"Katze", "dog":"Hund"}
TUTORIAL = "There will always be three\nbricks falling towards the\nground.\nUse the left and right arrow\nkeys to move me beneath\nthe brick, that has the\ncorrect translation for the\nword on th top, in order to\nsurvive.."

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Word Runner')  # Change the caption here

# Set up font
font = pygame.font.SysFont(None, 36)

# Character variables
char_x = (WIDTH - CHAR_WIDTH) // 2  # Start character in the middle
char_y = HEIGHT - CHAR_HEIGHT      # Start character at the bottom

# Initialize Pygame mixer and load the MP3 file
pygame.mixer.init()
pygame.mixer.music.load('data/NCS_Music.mp3')

# Load character image
character_img0 = pygame.image.load('data/char1.png')
character_img0 = pygame.transform.scale(character_img0, (CHAR_WIDTH*1.5, CHAR_HEIGHT*1.5))  # Resize the image
character_img1 = pygame.image.load('data/char1.png')
character_img1 = pygame.transform.scale(character_img1, (CHAR_WIDTH, CHAR_HEIGHT))  # Resize the image
character_img2 = pygame.image.load('data/char2.png')
character_img2 = pygame.transform.scale(character_img2, (CHAR_WIDTH, CHAR_HEIGHT))  # Resize the image
background_game = pygame.image.load('data/background.jpeg')
background_game = pygame.transform.scale(background_game, (WIDTH, HEIGHT))  # Resize the image
background_menu = pygame.image.load('data/start.jpeg')
background_menu = pygame.transform.scale(background_menu, (WIDTH, HEIGHT))  # Resize the image
brick = pygame.image.load('data/brick.png')
brick = pygame.transform.scale(brick, (CHAR_WIDTH*1.5, CHAR_HEIGHT))  # Resize the image
brokenbrick = pygame.image.load('data/brickbroken.png')
brokenbrick = pygame.transform.scale(brokenbrick, (CHAR_WIDTH*1.5, CHAR_HEIGHT))  # Resize the image
bubble = pygame.image.load('data/bubble.png')


# Play the loaded music file in an infinite loop (-1)
pygame.mixer.music.play(-1)

#Main game menu
menu = True
running = True
tutorial = False
while menu:
    screen.blit(background_menu, (0,0))
    screen.blit(character_img0, (WIDTH-200,HEIGHT-200))
    button_start = brick.get_rect(center=(WIDTH *0.75, HEIGHT *0.15))
    button_tut = brick.get_rect(center=(WIDTH *0.25, HEIGHT *0.15))
    screen.blit(brick, button_tut)
    show = font.render("TUTORIAL", True, TEXT_COLOR)
    screen.blit(show, (WIDTH *0.25-65, HEIGHT *0.15-5))
    screen.blit(brick, button_start)
    show = font.render("START", True, TEXT_COLOR)
    screen.blit(show, (WIDTH *0.75-44, HEIGHT *0.15-5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_start.collidepoint(event.pos):
                menu = False
            if button_tut.collidepoint(event.pos):
                tutorial = True
    pygame.display.flip()
    while tutorial:
        screen.blit(background_menu, (0,0))
        screen.blit(character_img1, (WIDTH / 2 ,125))
        screen.blit(bubble, (0,-3))
        
        lines = TUTORIAL.split("\n")
        i=300
        for line in lines:
            show = font.render(line, True, TEXT_COLOR)
            screen.blit(show, (60,i))
            i += show.get_height()

        button_back = brick.get_rect(center=(WIDTH /2, HEIGHT-75))
        screen.blit(brick, button_back)
        show = font.render("BACK", True, TEXT_COLOR)
        screen.blit(show, (WIDTH /2 - show.get_width()/2, HEIGHT-80))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                running = False
                tutorial = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.collidepoint(event.pos):
                    tutorial = False
        pygame.display.flip()

#Restart music
pygame.mixer.music.stop()
pygame.mixer.music.play(-1)

# Main game loop
counter = 4000
done = 0
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Select words
    if counter == 4000:
        counter = 0
        word1 = list(WORDS)[randint(0, len(WORDS)-1)]
        word2 = word1
        while word2 == word1:
            word2 = list(WORDS)[randint(0, len(WORDS)-1)]
        word3 = word1
        while word3 == word1 or word3 == word2:
            word3 = list(WORDS)[randint(0, len(WORDS)-1)]
        word_number = randint(1,3)
        match word_number:
            case 1:
                word = WORDS[word1]
            case 2:
                word = WORDS[word2]
            case 3:
                word = WORDS[word3]
    else:
        counter += 1

    # Check if the player is dead
    if counter == 2350:
        px = char_x
        if px < 150:
            player_number = 1
        elif px > 300:
            player_number = 3
        else:
            player_number = 2
        
        if word_number != player_number:
            running = False
        else:
            done += 1

    # Get all the keys currently held down
    keys = pygame.key.get_pressed()

    # Move character left or right
    if keys[pygame.K_LEFT] and char_x > 0:
        char_x -= CHAR_SPEED
    if keys[pygame.K_RIGHT] and char_x < WIDTH - CHAR_WIDTH:
        char_x += CHAR_SPEED

    # Update the screen
    screen.blit(background_game, (0,0))
    if int(counter/100)%2 == 0:
        screen.blit(character_img1, (char_x, char_y))
    else:
        screen.blit(character_img2, (char_x, char_y))

    # Moving words
    if counter <= 2350:
        w1 = font.render(word1, True, TEXT_COLOR)
        screen.blit(brick, ((WIDTH - brick.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2-50))
        screen.blit(w1, ((WIDTH - w1.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2))
        w2 = font.render(word2, True, TEXT_COLOR)
        screen.blit(brick, ((WIDTH - brick.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
        screen.blit(w2, ((WIDTH - w2.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
        w3 = font.render(word3, True, TEXT_COLOR)
        screen.blit(brick, ((WIDTH - brick.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
        screen.blit(w3, ((WIDTH - w3.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
    elif counter > 2350:
        match word_number:
            case 1:
                w1 = font.render(word1, True, TEXT_COLOR)
                screen.blit(brokenbrick, ((WIDTH - brick.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2-50))
                screen.blit(w1, ((WIDTH - w1.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2))
                w2 = font.render(word2, True, TEXT_COLOR)
                screen.blit(brick, ((WIDTH - brick.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
                screen.blit(w2, ((WIDTH - w2.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
                w3 = font.render(word3, True, TEXT_COLOR)
                screen.blit(brick, ((WIDTH - brick.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
                screen.blit(w3, ((WIDTH - w3.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
            case 2:
                w1 = font.render(word1, True, TEXT_COLOR)
                screen.blit(brick, ((WIDTH - brick.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2-50))
                screen.blit(w1, ((WIDTH - w1.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2))
                w2 = font.render(word2, True, TEXT_COLOR)
                screen.blit(brokenbrick, ((WIDTH - brick.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
                screen.blit(w2, ((WIDTH - w2.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
                w3 = font.render(word3, True, TEXT_COLOR)
                screen.blit(brick, ((WIDTH - brick.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
                screen.blit(w3, ((WIDTH - w3.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
            case 3:
                w1 = font.render(word1, True, TEXT_COLOR)
                screen.blit(brick, ((WIDTH - brick.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2-50))
                screen.blit(w1, ((WIDTH - w1.get_width()-300) / 2, (HEIGHT-HEIGHT + counter/2) / 2))
                w2 = font.render(word2, True, TEXT_COLOR)
                screen.blit(brick, ((WIDTH - brick.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
                screen.blit(w2, ((WIDTH - w2.get_width()) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
                w3 = font.render(word3, True, TEXT_COLOR)
                screen.blit(brokenbrick, ((WIDTH - brick.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2-50))
                screen.blit(w3, ((WIDTH - w3.get_width()+300) // 2, (HEIGHT-HEIGHT + counter/2) // 2))
        

    # Render and display caption text
    show_text = "What is: " + word
    caption_text = font.render(show_text, True, TEXT_COLOR)
    screen.blit(caption_text, ((WIDTH - caption_text.get_width()) // 2, 30))
    done_text = str(done)
    counter_text = font.render(done_text, True, TEXT_COLOR)
    screen.blit(counter_text, (400,30))

    # Refresh the display
    pygame.display.flip()

# Quit Pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit()

