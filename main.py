class Board:
    def __init__(self,board,pieces):
        self.board = board
        self.pieces = pieces

    def display(self):
        drawnboard = [
            ['_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_'],
        ]
        for piece in self.pieces:
            drawnboard[piece.position[0]][piece.position[1]] = piece.symbol

        for line in drawnboard:
            print(line)


    def get_position(self, neededPiece):
        for piece in self.pieces:
            if piece == neededPiece:
                return piece.position

    def get_piece(self, neededPos):
        if self.pieces[neededPos(0)][neededPos(1)] == None:
            return None
        else:
            piece = self.pieces[neededPos(0),neededPos(1)].symbol
            return piece

    def set_piece(self,board,addedpiece,position):
        pass

