import pygame  # This imports the pygame functions
import time  # This imports the time functions
import random  # This imports the random functions
import pygame.mixer  # This imports the pygame.mixer function
import imageio  # Imports imageio, used for the easter egg


from moviepy.editor import VideoFileClip  # Imports the VideoFileClip function

sounds = pygame.mixer  # This simplifies the prefix pygame.mixer to sounds
sounds.init()  # This initializes the mixer module
pygame.init()  # This initializes the pygame module
display_width = 800  # This is the width of the window
display_height = 600  # This is the height of the window

# Selection of colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

dark_red = (150, 0, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

# This is defines the displays used for all of the game windows
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ultimate Hangman')
clock = pygame.time.Clock()


def text_objects(text, font, color):  # This function renders the text, font and color/Joey
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def text(msg, x, y, size, color):  # This function draws text/Joey
    smallText = pygame.font.Font("freesansbold.ttf", size)
    textSurf, textRect = text_objects(msg, smallText, color)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)


def button(msg, x, y, w, h, ic, ac, action=None):  # This function creates the buttons/Joey
    s_button = sounds.Sound("button.wav")  # This is a variable for the click sound
    mouse = pygame.mouse.get_pos()  # This variable senses the position of the mouse
    click = pygame.mouse.get_pressed()  # This variable senses if the mouse is clicked
    if x + w > mouse[0] > x and y + h > mouse[
        1] > y:  # This if statement senses when the mouse is hovering over the button
        pygame.draw.rect(gameDisplay, ac, (x - 10, y - 10, w + 20, h + 20))  # This draws the active button
        if click[0] == 1 and action != None:  # This senses if the mouse is clicked
            s_button.play()  # This plays the click sound
            if action == "intro":  # This runs the intro screen if the button value is "intro"
                game_intro()
            elif action == "play":  # This runs the game select screen if the button value is "play"
                game_select()
            elif action == "option":  # This runs the options screen if the button value is "option"
                option()
            elif action == "quit":  # This exits the game if the button value is "quit"
                pygame.quit()
                quit()
            elif action == "enter":  # This returns the value enter if the enter button is clicked
                return "enter"
            elif action == "eazy" or action == "medium" or action == "hard":  # This runs the gameplay screen if the button value is a difficulty
                gameloop(action)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))  # This draws the inactive button

    smallText = pygame.font.Font("freesansbold.ttf", 20)  # Text font
    textSurf, textRect = text_objects(msg, smallText, red)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():  # This is the function for the intro screen/Joey
    pygame.mixer.music.load('opening.wav')
    pygame.mixer.music.play(-1)  # This plays the opening music
    logo = pygame.image.load("supreme_logo.png")  # This loads the title
    hanging_knuckles = pygame.image.load("sad.png")  # This loads the knuckles image
    while True:  # This is a loop
        for event in pygame.event.get():  # This senses the user's actions
            if event.type == pygame.QUIT:  # This quits pygame if the user closes the window
                pygame.quit()
                quit()
        gameDisplay.fill(white)  # This fills the window with white color
        gameDisplay.blit(logo, (30, -30))  # This draws the game logo
        gameDisplay.blit(hanging_knuckles, (450, 250))  # This draws knuckles
        pygame.draw.line(gameDisplay, bright_red, (586, 150), (586, 250), 8)
        button("Play", 100, 250, 200, 50, green, bright_green, "play")  # This button leads to the difficulty screen
        button("Options", 100, 350, 200, 50, green, bright_green, "option")  # This button leads to the option screen
        button("Exit", 100, 450, 200, 50, green, bright_green, "quit")  # This button exits the game
        pygame.display.update()  # This updates the window
        clock.tick(200)  # This function runs 200 game frames per second


def game_select():  # This is the function for the difficulty screen/Richard
    i_sleep = pygame.image.load("i_sleep.png")  # Different PNG of the difficulty settings
    real = pygame.image.load("real.png")
    power_of_god_and_anime = pygame.image.load("power_of_god_and_anime.png")
    while True:  # This is a loop
        for event in pygame.event.get():  # This senses the user's actions
            if event.type == pygame.QUIT:  # Quits the program if the player clicks 'exit'
                pygame.quit()
                quit()
        gameDisplay.fill(white)  # fills the game background with white
        text("Choose your difficulty", (display_width / 2), (150), 50, red)  # text with choosing difficulty
        gameDisplay.blit(i_sleep,
                         (display_width * 0.1, 250))  # The next three lines show the display format of the pictures
        gameDisplay.blit(real, (display_width * 0.38, 250))
        gameDisplay.blit(power_of_god_and_anime, (display_width * 0.7 - 10, 250))
        button("EAZY", display_width * 0.1 - 20, 450, 200, 50, green, bright_green,
               "eazy")  # The next 3 lines show the difficulty buttons
        button("MEDIUM", display_width * 0.38, 450, 200, 50, green, bright_green, "medium")
        button("EXPERTS ONLY", display_width * 0.7 - 20, 450, 200, 50, green, bright_green, "hard")
        pygame.display.update()  # Updates the window
        clock.tick(200)  # Runs 200 ticks per second


def option():  # Function for the options tab/Joey
    knuckles = pygame.image.load("knuckles.png")  # PNG for the tab
    while True:  # Loop for the options menu
        for event in pygame.event.get():  # In case the user clicks off the program
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)  # Background colour
        gameDisplay.blit(knuckles, (0, 0))  # Positioning of the picture
        text("THIS IS NOT DA WEI", int(display_width / 2), int(display_height / 2), 50, green)  # Text for the menu
        button("ABORT", display_width * 0.43, 450, 120, 50, green, bright_green,
               "intro")  # Button to go back to main menu
        pygame.display.update()  # Updates the window
        clock.tick(200)  # Running 200 ticks per second


def death_screen(t, s):  # death screen function/Devin
    pygame.mixer.music.load('lose_music.wav')  # loads the following wav file
    pygame.mixer.music.play(-1)  # plays the wav file in a loop
    lost_image = pygame.image.load("lost_image.png")  # death image
    while True:
        for event in pygame.event.get():  # if the user X's out, then the program quits
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)  # fills background white
        gameDisplay.blit(lost_image, (0, 0))  # transfer the death image onto the screen
        text("NO SUPREME FOR YOU", int(display_width / 2), int(display_height / 3), 50,
             red)  # the following text is displayed
        text("Time: " + str(int(t)) + " seconds", int(display_width / 2), int(display_height / 3 + 70), 25,
             red)  # displays the time spent in a text
        text("Score: " + str(s) + " fails", int(display_width / 2), int(display_height / 3 + 100), 25,
             red)  # displays the score and number of tries
        button("Quit", 150, 450, 120, 50, green, bright_green, "quit")  # button for quit
        button("Menu", 550, 450, 120, 50, green, bright_green, "intro")  # button for menu
        pygame.display.update()
        clock.tick(200)


def end_screen(t, s):  # end screen function/Richard
    winning = pygame.image.load("winning.png")  # loads the following image
    while True:
        for event in pygame.event.get():  # if user X's out, then the program quits
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(blue)  # fills background blue
        gameDisplay.blit(winning, (170, 15))  # transfer the image onto the screen
        text("SUPREME WIN", int(display_width / 2), int(display_height / 3 + 150), 50,
             green)  # the following text appears onto the screen
        text("Time: " + str(int(t)) + " seconds", int(display_width / 2), int(display_height / 3 + 190), 25,
             green)  # displays amount of time taken
        text("Score: " + str(s) + " fails", int(display_width / 2), int(display_height / 3 + 220), 25,
             green)  # displays the score and attemps/fails
        button("Quit", 150, 450, 120, 50, green, bright_green, "quit")  # button for quit
        button("Menu", 550, 450, 120, 50, green, bright_green, "intro")  # button for menu
        pygame.display.update()
        clock.tick(200)


def box(x1, x2, y1, y2, w):  # This is a function that draws an empty rectangular box/Devin
    pygame.draw.line(gameDisplay, black, (x1, y1), (x2, y1), w)
    pygame.draw.line(gameDisplay, black, (x2, y1), (x2, y2), w)
    pygame.draw.line(gameDisplay, black, (x2, y2), (x1, y2), w)
    pygame.draw.line(gameDisplay, black, (x1, y2), (x1, y1), w)


def stand(x, y):  # This is a function that draws the hang man stand/Devin
    pygame.draw.line(gameDisplay, black, (x, y), (x, y - 240), 5)
    pygame.draw.line(gameDisplay, black, (x - 40, y), (x + 80, y), 5)
    pygame.draw.line(gameDisplay, black, (x, y - 240), (x + 120, y - 240), 5)
    pygame.draw.line(gameDisplay, black, (x + 120, y - 240), (x + 120, y - 210), 5)


def man(x, y):  # This is a function that draws the body parts of the hangman/Devin
    pygame.draw.line(gameDisplay, black, (x, y - 55), (x, y), 5)  # Body
    pygame.draw.line(gameDisplay, black, (x, y - 40), (x - 25, y - 20), 5)  # left arm
    pygame.draw.line(gameDisplay, black, (x, y - 40), (x + 25, y - 20), 5)  # right arm
    pygame.draw.line(gameDisplay, black, (x, y), (x - 20, y + 35), 5)  # left leg
    pygame.draw.line(gameDisplay, black, (x, y), (x + 20, y + 35), 5)  # right leg


def gameloop(difficulty):  # This is the main gameloop
    pygame.mixer.music.load('wii.mp3')  # This plays the MP3 wii music/Joey
    pygame.mixer.music.play(-1)
    if difficulty == "eazy":  # if the difficulty selected is "eazy"/Richard
        words = (list('s t r i n g'), list('p l a n e t'), list('r a n d o m'), list('v e c t o r'),
                 # This is the word bank for the eazy selection
                 list('g e n i u s'), list('p y t h o n'), list('v o l u m e'), list('p o e t r y'))
        string = list("_ _ _ _ _ _")  # This represents the blank spots when guessing the word
        r = 6  # The word is 6 letters
    elif difficulty == "medium":  # Else If difficulty selected is "medium"/Richard
        words = (list('t r a m p o l i n e'), list('a f t e r s h o c k'), list('b a n k r u p t c y'),
                 list('m o n a r c h i s t'))  ##This is the word bank for the medium selection
        string = list("_ _ _ _ _ _ _ _ _ _")
        r = 10  # The word is 10 letters
    else:  # /Richard
        words = (list('m i s c o n j u g a t e d l y'),
                 list('d e r m a t o g l y p h i c s'))  # wordbank for the experts selection
        string = list("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        r = 15  # The word is 15 letters

    # /Joey
    lives = 7  # The user is able to have 7 failed attempts before losing
    guess = []  # This is a list that stores the user's input
    word = random.choice(words)  # This chooses a random word
    answer = ''.join(word).replace(" ", "")  # This reformats the correct word into a string
    x = 600
    y = 180
    NANI = False
    attempts = 0  # This is the number of fails that the player has made
    time = 0  # This sets the time to zero
    while True:  # /Joey
        for event in pygame.event.get():  # if the user X's out, then the program quits
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if len(guess) <= 21:  # the word guessed must be less than 21 letters
                    if event.key == pygame.K_BACKSPACE:  # if backspace is pressed
                        if len(guess) == 0:  # if there are no words to be deleted
                            continue  # continues program
                        else:
                            guess.pop(-1)  # Otherwise deletes one letter if user presses backspace
                    elif event.key == pygame.K_RETURN:  # Entering the Guess
                        attempts += 1  # accounting attempt
                        if len(guess) == 0:  # dismissing an empty list
                            continue
                        elif str(''.join(guess)) == "omae wa mou shindeiru":  # easter egg
                            attempts = -9999999999999999999999999999
                            NANI = True
                            continue
                        elif guess_str == answer:  # completes the list if the correct answer is guessed
                            attempts -= 1
                            for i in range(r):
                                string[2 * i] = word[2 * i]
                        else:  # checks the user's letter guess
                            for i in range(0, len(guess)):
                                guess.pop(-1)
                            for i in range(r):
                                if guess_str == word[2 * i]:
                                    attempts -= 1
                                    string[2 * i] = word[2 * i]
                    else:  # extracts the user's input
                        user_input = str(event)[30]
                        guess.append(user_input)
                        guess_str = ''.join(guess)

        gameDisplay.fill(white)  # Fills the background white
        time += 1 / 200  # This keeps track of the time in seconds
        box(50, 310, 230, 270, 5)  # Creates a box for the hangman
        box(display_width * 0.5, display_width - 25, 25, display_height - 250, 5)
        text("Guess the Word!", 180, 100, 30, red)  # Displays the following text
        text(''.join(guess), 180, 250, 20, red)
        text(''.join(string), display_width * 0.5, display_height - 100, 50, red)
        text("Time:", 538, 375, 20, red)  # displays the time in red
        text(str(int(time)), 625, 375, 20, red)  # Displays the time used in red
        text("Fails:", 540, 400, 20, red)  # Displays the attempts
        text(str(attempts) + "/" + str(lives), 640, 400, 20, red)  # Displays the attempts used
        stand(480, 305)
        if attempts >= 1:  # /Devin
            pygame.draw.circle(gameDisplay, black, (600, 120), 25, 5)  # Head
            if attempts >= 2:
                pygame.draw.line(gameDisplay, black, (600, 145), (600, 200), 5)  # Body
                if attempts >= 3:
                    pygame.draw.line(gameDisplay, black, (600, 160), (575, 180), 5)  # left arm
                    if attempts >= 4:
                        pygame.draw.line(gameDisplay, black, (600, 160), (625, 180), 5)  # right arm
                        if attempts >= 5:
                            pygame.draw.line(gameDisplay, black, (600, 200), (580, 235), 5)  # left leg
                            if attempts >= 6:
                                pygame.draw.line(gameDisplay, black, (600, 200), (620, 235), 5)  # right leg

        if button("Enter", 130, 300, 100, 50, green, bright_green, "enter") == "enter":  # Entering the Guess/Joey
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:  # This senses when the mouse is no longer clicked
                    attempts += 1  # the attempts increase if the player hits enter
                    if len(guess) == 0:  # dismissing an empty list
                        continue
                    for i in range(0, len(guess)):  # Resets all the letters to begin the game
                        guess.pop(-1)
                    if guess_str == answer:  # if the player guesses the word in one go
                        for i in range(r):  # In the total amount of letters in the word
                            string[2 * i] = word[2 * i]  # The program will auto fill all the corect letters
                    for i in range(r):  # If the player guesses one correct letter:
                        if guess_str == word[2 * i]:  # If it matches with one of the letters:
                            attempts -= 1  # It will not count for an attempt
                            string[2 * i] = word[2 * i]  # The program auto fills one letter

        if string == word:  # If the player matches the word/Joey
            end_screen(time, attempts)  # Displays the winning screen

        if attempts == lives:  # if the player loses all their lives/Richard
            death_screen(time, attempts)  # Displays the game over screen

        if NANI == True:  # Easter Egg #If the player enters the easter egg, this statement becomes true/Richard
            clip = VideoFileClip('movie.mp4')  # Plays the easter egg video
            clip.preview()  # Runs the video
            end_screen(time, attempts)  # The game then directly goes to the winning screen
        pygame.display.update()  # Updates the window
        clock.tick(200)  # Runs at 200 ticks per second


if __name__ == '__main__':
    game_intro()  # The program initiates the game


