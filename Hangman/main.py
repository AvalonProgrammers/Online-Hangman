import pygame
import os
import random
import math


# Opens and converts the words.txt file into a word lists consisting of strings of words
with open(file="words.txt") as words:
    words = list(words)
    for word in words:
        words = word.split(", ")

isClient = bool(input("Run as client?(True/False) "))
print(isClient)

# Initialize game window
pygame.init()

win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Hangman Game! (Online)")


# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


# Load Images
images = []
images.append(pygame.image.load(os.path.join("Assets", "hangman"+str(i)+".png" for i in range(7))))


# game variables
hangman_status = 0
word = random.choice(words).upper()
guessed = []


# Button constants
RADIUS = 20
GAP = 15

# Button variables
letters = [] 
startx = round((800 - (RADIUS * 2 + GAP) * 13) /2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Initialize Clock with frames per second
FPS = 60
clock = pygame.time.Clock()


def draw():
    win.fill(WHITE)

    # Draw title
    title = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(title, (400 - int(title.get_width()/2), 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "

    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - int(text.get_width()/2), int(y - text.get_height()/2)))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


# Define a function to see if the game is complete
def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (400 - int(text.get_width()/2), 200 - int(text.get_height()/2)))
    if message == "YOU LOSE! :(":
        ans = WORD_FONT.render(f"The word was {word} ", 1, BLACK)
        win.blit(ans, (400 - int(ans.get_width()/2), 280 - int(ans.get_height()/2)))
    pygame.display.update()
    pygame.time.delay(3000)


# Game loop
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if not ltr in word:
                            hangman_status += 1
    
    draw()

    won = True
    for letter in word:
        if letter not in guessed :
            won = False
            break
    
    if won:
        display_message("YOU WON! :)")
        run = False

    if hangman_status == 6:
        display_message("YOU LOSE! :(")
        run = False


pygame.quit()
