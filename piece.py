#git add --all, then git status

class Piece:
    def __init__(self, position, colour):
        self.position = position    #for the placement
        self.colour = colour        #for either black or white. Thinking of making it binary.
    def isValidMove(self, newPosition, board):
        pass
    def __str__(self):
        return '?'


class King(Piece):
    def __str__(self):
        return 'K'
    def isValidMove(self, newPosition, board):
        pass

class Queen(Piece):
    def __str__(self):
        return 'Q'
    def isValidMove(self, newPosition, board):
        pass

class Bishop(Piece):
    def __str__(self):
        return 'B'
    def isValidMove(self, newPosition, board):
        return True

class Rook(Piece):
    def __str__(self):
        return 'R'
    def isValidMove(self, newPosition, board):
        return True

class Knight(Piece):
    def __str__(self):
        return 'Kn'
    def isValidMove(self, newPosition, board):
        return True

class Pawn(Piece):
    def __str__(self):
        return 'P'
    def isValidMove(self, newPosition, board):
        return True
