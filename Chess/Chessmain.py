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
    pieces = ["WhiteRook","WhiteKnight","WhiteBishop","WhiteKing","WhiteQueen","WhitePawn","BlackRook","BlackKnight","BlackBishop","BlackKing","BlackQueen","BlackPawn"]
    for piece in pieces:
        Load_Images[piece] = pygame.transform.scale(pygame.image.load("/Users/pawel/PycharmProjects/ChessGame/Chess/Chess images/" + piece + ".png"), (Square_size, Square_size))
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
    while infiniteloop:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                infiniteloop = False
                main_menu_screen = pygame.display.set_mode((1280, 720))

        creategamestate(displaysize, gamestate)
        game_clock.tick(Fps_Limit)
        pygame.display.flip()
# Function to create the game state on the screen
def creategamestate(displaysize, gamestate):
    createBoard(displaysize)
    createPieces(displaysize, gamestate.board)
# Function to create the chess board on the screen
def createBoard(displaysize):
    #makes a darker green throug the RGB values (Red green Blue)
    darker_green = pygame.Color(0, 100, 0)
    # Define the colours of the squares
    colours = [pygame.Color("White"), darker_green]

    # Loop through each row and column of the board
    for r in range(Dimension_Screen):
        for c in range(Dimension_Screen):
            # Determine the colour of the square based on its position on the board, which uses coordinates
            colour = colours[((r + c) % 2)]

            # Draws a rectangle on the display with the appropriate colour and size
            # The rectangle's position and size are based on the row and column and the size of the squares
            pygame.draw.rect(displaysize, colour, pygame.Rect(c * Square_size, r * Square_size, Square_size, Square_size))


# Function to create the chess pieces on the screen
def createPieces(displaysize, board):
    pass


