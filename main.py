class Board:
    def __init__(self,pieces):
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

    def get_piece(self, neededPos):
        for piece in self.pieces:
            if piece.position == neededPos:
                return piece.symbol
            else:
                return None
        return 0

    def set_piece(self,board,addedpiece):
        self.pieces.append(addedpiece)

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        if self.color == 0:
            self.symbol = '♟'
        if self.color == 1:
            self.symbol = '♙'