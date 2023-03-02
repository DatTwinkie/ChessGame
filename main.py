# Modules that are being used
import pygame
import sys
from button import Button

# Initialising pygame
pygame.init()
# Program size and name
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
# Background image
Background = pygame.image.load("messi ronaldo chess.png")


# Define a function that loads a font and returns it with the given size
def get_font(size):
    return pygame.font.Font("Roboto-Black.ttf", size)


# Create a new function for the Play button
def play():
    # Start an infinite loop for the "Play" screen
    while True:
        # Get the position of the mouse on the screen
        play_mouse_pos = pygame.mouse.get_pos()
        # Fill the screen with black colour
        screen.fill("black")
        # Create the game on top of this code


        # Blit the text surface onto the screen

        # Create a "BACK" button and update it on the screen
        Play_Back = Button(image=None, pos=(50, 50),
                           text_input="BACK", font=get_font(25), base_colour="white", highlight_colour="Red")
        Play_Back.changeColour(play_mouse_pos)
        Play_Back.update(screen)

        # Handle Pygame events
        for event in pygame.event.get():
            # If the "X" button is clicked, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If the mouse button is clicked, check if it's inside the "BACK" button and go back to the main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_Back.checkForInput(play_mouse_pos):
                    main_menu()

        # Update the Pygame display
        pygame.display.update()


# Define the main menu function
def main_menu():
    # Set the caption of the Pygame window
    pygame.display.set_caption("menu")

    # Draw the background image at (0, 0)
    screen.blit(Background, (0, 0))

    # Run the main menu loop
    while True:
        # Get the current mouse position
        Menu_Mouse_Pos = pygame.mouse.get_pos()

        # Render the "Main Menu" text and create a rectangle for it
        Menu_Text = get_font(100).render("Main Menu", True, "#b68f40")
        Menu_Rectangle = Menu_Text.get_rect(center=(640, 100))

        # Create three Button objects for "PLAY", "OPTIONS", and "QUIT"
        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_colour="#d7fcd4", highlight_colour="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_colour="#d7fcd4", highlight_colour="White")

        # Draw the "Main Menu" text at the center of the screen
        screen.blit(Menu_Text, Menu_Rectangle)

        # Loop through the three Button objects
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            # Change the colour of the button's text if the mouse is hovering over it
            button.changeColour(Menu_Mouse_Pos)
            # Draw the button on the screen
            button.update(screen)

        # Handle events
        for event in pygame.event.get():
            # If the "X" button is clicked, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If the mouse button is clicked, check if it's inside a button and execute the appropriate function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(Menu_Mouse_Pos):
                    play()
                if QUIT_BUTTON.checkForInput(Menu_Mouse_Pos):
                    pygame.quit()
                    sys.exit()

        # Update the display
        pygame.display.update()


# Call the main menu function to start the game
main_menu()
