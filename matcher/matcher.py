# Images were created using img2go.com
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
WHITE = (255, 255, 255)
NAME = ''
Questions = []
Answers = []
counter = 0


file = open ('data/personalinfo', 'r')
content = file.readlines()
file.close()
data = False
ques = False
answ = False
#print(content)
for line in content:
    if 'ID\n' == line:
        data = True
    if 'QUESTIONS\n' == line:
        ques = True
    if 'ANSWERS\n' == line:
        answ = True
    if answ and line != 'ANSWERS\n' and line != '\n':
        Answers.append(line[:len(line)-1])
    elif ques and line != 'QUESTIONS\n' and line != '\n':
        Questions.append(line[:len(line)-1])
    elif data and line != '\n':
        test = 1


# Create the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perfect Match")

# Load images
background = pygame.image.load('data/back.png')
background = pygame.transform.scale(background, (width, height))  # Resize the image

name = "What is your name?"
age = "How old are you?"
gender = "What gender do you identify as?"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw Background
    screen.blit(background, (0, 0))

    font = pygame.font.SysFont(None, 36)
    score = str(Questions[counter])
    caption_text = font.render(score, True, (0, 0, 0))
    screen.blit(caption_text, (width // 2 - caption_text.get_width() // 2, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


