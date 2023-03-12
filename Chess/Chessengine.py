#responsible for storing information about the current state of game
#and also looking at valid moves, and also be able to edit moves

class GameState():
    def __init__(self):
        #2 dimensional list to store the chess board
        self.board = [
            ["BR","BN","BB","BQ","BK","BB","BN","BR"],
            ["BP","BP","BP","BP","BP","BP","BP","BP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["WP","WP","WP","WP","WP","WP","WP","WP"],
            ["WR","WN","WB","WQ","WK","WB","WN","WR"]]
        #tracks whoevers turn it is
        self.whiteMove = True
        #keeps track of the games special moves
        self.Move_Log =[]

    def moveMaking(self, MovePiece):
        # Sets the starting square of the moved piece to an empty square
        self.board[MovePiece.startingRow][MovePiece.startingColumn] = "--"
        # Sets the ending square of the moved piece to the moved piece
        self.board[MovePiece.EndingRow][MovePiece.EndingColumn] = MovePiece.movedPiece
        # Adds the move to the Move_Log so it can be undone later
        self.Move_Log.append(MovePiece)
        self.Move_Log.append(MovePiece)
        # Toggles the value of self.whiteMove to swap the player
        self.whiteMove = not self.whiteMove


class Chess_Move():
    # Maps row numbers to row numbers
    ranks_to_row = {"1": 7, "2": 6, "3": 5, "4": 4,
                    "5": 3, "6": 2, "7": 1, "8": 0}
    # Maps row numbers to row numbers
    rows_to_ranks = {v: k for k, v in ranks_to_row.items()}
    # Maps file letters to column numbers
    file_to_column = {"a": 0, "b": 1, "c": 2, "d": 3,
                     "e": 4, "f": 5, "g": 6, "h": 7}
    # Maps index numbers to file lettersx
    column_to_files = {v: k for k, v in file_to_column.items()}

    def __init__(self, Starting_Square, Ending_Square, board):
        # Extract the starting row and column from the starting square
        self.startingRow = Starting_Square[0]
        self.startingColumn = Starting_Square[1]
        # Extract the ending row and column from the ending square
        self.EndingRow = Ending_Square[0]
        self.EndingColumn = Ending_Square[1]
        # Store the piece that was moved
        self.movedPiece = board[self.startingRow][self.startingColumn]
        # Store the piece that was captured (if any)
        self.capturedPiece = board[self.EndingRow][self.EndingColumn]

    def create_Chess_Notation(self):
        # Returns the starting square and ending square in chess notation
        return self.create_Rank_File(self.startingRow, self.startingColumn) + self.create_Rank_File(self.EndingRow, self.EndingColumn)

    def create_Rank_File(self, Row, Column):
        # Converts row and column indices to a chess square
        return self.column_to_files[Column] + self.rows_to_ranks[Row]
