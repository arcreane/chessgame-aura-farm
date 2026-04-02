class Board:
    def __init__(self,board,pieces):
        self.board = board
        self.pieces = pieces

    def displayBoard(self):
        loadedboard = []
        for row in range(8):
            line = []
            for column in range(8):
                line.append(self.pieces[row][column].symbol)

    def updateBoard(self):
        pass

    def getPosition(self, neededpiece):
        for piece in self.pieces:
            if piece == neededpiece:
                return piece.position

    def getPiece(self, neededpos):
        for piece in self.pieces:
            if piece.position == neededpos:
                return piece

