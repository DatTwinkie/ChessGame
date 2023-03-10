# Modules that are being used
import pygame
import sys
from Chess.button import Button
from Chess.Chessmain import main

# Initialising pygame
pygame.init()
# Program size and name
display_size = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
# Background image
Background = pygame.image.load("/Users/pawel/PycharmProjects/ChessGame/messi ronaldo chess.png")
# Define a function that loads a font and returns it with the given size
def get_font(size):
    return pygame.font.Font("/Users/pawel/PycharmProjects/ChessGame/Roboto-Black.ttf", size)


# Create a new function for the Play button
def game_selection():
    select_screen = pygame.image.load("/Users/pawel/PycharmProjects/ChessGame/messi ronaldo chess.png")
    button1 = pygame.image.load("/Users/pawel/PycharmProjects/ChessGame/pvp22.png")
    # Start an infinite loop for the "Play" screen
    while True:
        # Get the position of the mouse on the screen
        play_mouse_pos = pygame.mouse.get_pos()
        # Fill the screen with black colour
        display_size.blit(select_screen, (0, 0))
        # Create the game mode selection
        # Blit the text surface onto the screen
        Select_PVP1 = Button(image=button1, pos=(384, 310),
                             text_input=None, font=get_font(45), base_colour="white", highlight_colour="Green")
        Select_PVP1.changeColour(play_mouse_pos)
        Select_PVP1.update(display_size)
        # Create a "BACK" button and update it on the screen
        Back_Button = Button(image=None, pos=(50, 50),
                           text_input="BACK", font=get_font(25), base_colour="white", highlight_colour="Red")
        Back_Button.changeColour(play_mouse_pos)
        Back_Button.update(display_size)

        # Handle Pygame events
        for event in pygame.event.get():
            # If the "X" button is clicked, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If the mouse button is clicked, check if it's inside the "BACK" button and go back to the main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.checkForInput(play_mouse_pos):
                    main_menu()
                if Select_PVP1.checkForInput(play_mouse_pos):
                    main()

        # Update the Pygame display
        pygame.display.update()


# Define the main menu function
def main_menu():
    # Set the caption of the Pygame window
    pygame.display.set_caption("menu")

    # Draw the background image at (0, 0)
    display_size.blit(Background, (0, 0))

    # Run the main menu loop
    while True:
        # Get the current mouse position
        mouse_position_menu = pygame.mouse.get_pos()

        # Render the "Main Menu" text and create a rectangle for it
        Menu_Text = get_font(100).render("Main Menu", True, "#b68f40")
        Menu_Rectangle = Menu_Text.get_rect(center=(640, 100))

        # Create three Button objects for "PLAY" and "QUIT"
        Game_selection_button = Button(image=pygame.image.load("/Users/pawel/PycharmProjects/ChessGame/Play Rect.png"), pos=(640, 250),
                                       text_input="PLAY", font=get_font(75), base_colour="#d7fcd4",
                                       highlight_colour="Green")
        quit_button = Button(image=pygame.image.load("/Users/pawel/PycharmProjects/ChessGame/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_colour="#d7fcd4", highlight_colour="Red")

        # Draw the "Main Menu" text at the center of the screen
        display_size.blit(Menu_Text, Menu_Rectangle)

        # Loop through the three Button objects
        for button in [Game_selection_button, quit_button]:
            # Change the colour of the button's text if the mouse is hovering over it
            button.changeColour(mouse_position_menu)
            # Draw the button on the screen
            button.update(display_size)

        # Handle events
        for event in pygame.event.get():
            # If the "X" button is clicked, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If the mouse button is clicked, check if it's inside a button and execute the appropriate function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Game_selection_button.checkForInput(mouse_position_menu):
                    game_selection()
                if quit_button.checkForInput(mouse_position_menu):
                    pygame.quit()
                    sys.exit()

        # Update the display
        pygame.display.update()


# Call the main menu function to start the game
main_menu()
