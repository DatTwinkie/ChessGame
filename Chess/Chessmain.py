#Responsbile  for handling user input and displaying current gamestate information
import pygame
import pygame.draw
import pygame.time
from Chess import Chessengine


# Setting up screen dimensions and other game variables
Width_Screen = 800
Height_Screen = 800
Dimension_Screen = 8
Square_size = Height_Screen // Dimension_Screen
Fps_Limit = 30
Load_Images = {}

#initialise a global dictionary of images. this will be called once in the main"

def startImages():
    pieces = ["WR","WN","WB","WK","WQ","WP","BR","BN","BB","BK","BQ","BP"]
    for chess_piece in pieces:
        Load_Images[chess_piece] = pygame.transform.scale(pygame.image.load("/Users/pawel/PycharmProjects/ChessGame/Chess/Chess images/" + chess_piece + ".png"), (float(Square_size*0.97), float(Square_size*0.97)))

    #allows me to access an image by saying 'images['WhiteRook']'

    #handle user input and graphics
def main():
    pygame.init()
    displaysize = pygame.display.set_mode((Width_Screen,Height_Screen))
    game_clock = pygame.time.Clock()
    displaysize.fill(pygame.Color("white"))
    #calling constructor from the other code, which allows  access  to the  board
    gamestate = Chessengine.GameState()
    # Initialize the game state and load images
    startImages()
    infiniteloop = True
    # holds which square is clicked on
    square_Select = ()
    user_Click = []

    # main game loop
    while infiniteloop:
        for event in pygame.event.get():
            # checks if user clicked on quit button
            if event.type == pygame.QUIT:
                infiniteloop = False
                main_menu_screen = pygame.display.set_mode((1280, 720))
            # checks if user clicked on the board
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # gets the location of the mouse click
                mouse_location = pygame.mouse.get_pos()
                # calculates which row and column the user clicked on
                column = mouse_location[0] // Square_size
                row = mouse_location[1] // Square_size

                # if user clicked on the same square again
                if square_Select == (row, column):
                    # deselect the square
                    square_Select = ()
                    user_Click = []
                else:
                    # select the square and add it to user_Click
                    square_Select = (row, column)
                    user_Click.append(square_Select)

                # if the user has selected two squares
                if len(user_Click) == 2:
                    # Create a Chess_Move object for the player's move
                    player_move = Chessengine.Chess_Move(user_Click[0], user_Click[1],gamestate.board)
                    # Print the notation of the move that was made
                    print(player_move.create_Chess_Notation())
                    # Make the move on the gamestate board
                    gamestate.moveMaking(player_move)
                    # Reset the selected square
                    square_Select = ()
                    # Reset the user's click
                    user_Click = []

        creategamestate(displaysize, gamestate)
        game_clock.tick(Fps_Limit)
        pygame.display.flip()
# Function to create the game state on the screen
def creategamestate(displaysize, gamestate):
    createBoard(displaysize)
    createPieces(displaysize, gamestate.board)
# Function to create the chess board on the screen
def createBoard(displaysize):
    #makes a darker green through the RGB values (Red green Blue)
    darker_green = pygame.Color(0, 100, 0)
    # Define the colours of the squares
    colours = [pygame.Color("White"), darker_green]

    # Loop through each row and column of the board
    for row in range(Dimension_Screen):
        for column in range(Dimension_Screen):
            # Determine the colour of the square based on its position on the board, which uses coordinates
            colour = colours[((row + column) % 2)]

            # Draws a rectangle on the display with the appropriate colour and size
            # The rectangle's position and size are based on the row and column and the size of the squares
            pygame.draw.rect(displaysize, colour, pygame.Rect(column * Square_size, row * Square_size, Square_size, Square_size))


# Function to create the chess pieces on the screen
def createPieces(displaysize, board):
    # Loop through each row and column of the board
    for row in range(Dimension_Screen):
        for column in range(Dimension_Screen):
            # Get the chess piece at the current row and column
            chess_piece = board[row][column]
            # If there is a piece at this location on the board
            if chess_piece != "--":
                # Draw the image of the chess piece on the display surface at the appropriate location and size
                displaysize.blit(Load_Images[chess_piece], pygame.Rect(column*Square_size, row*Square_size, Square_size, Square_size))
