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
        #tacks whoevers turn it is
        self.whiteMove = True
        #keeps track of the games special moves
        self.Move_Log =[]
