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
        if self.pieces[neededPos(0)][neededPos(1)] == None:
            return None
        else:
            piece = self.pieces[neededPos(0),neededPos(1)].symbol
            return piece

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

class Bishop(Piece):
    def __init__(self,color,position):
        super().__init__(color,position)
        if self.color == 0:
            self.symbol = '♝'
        if self.color == 1:
            self.symbol= '♗'
    def __str__(self):
        return 'B'

    def isValidMove(self, move, pieces):
        if self.symbol == '♗' or self.symbol == '♝':
            downright = []
            downleft =[]
            upright = []
            upleft =[]
            counter = 0
            while counter <= 7:
                counter += 1
                if 1 <= self.position[0] + counter and self.position[0] + counter <=8 and 1 <= self.position[1] + counter and self.position[1] + counter <=8 :
                    downright.append([self.position[0] + counter, self.position[1] + counter])
                if 1 <= self.position[0] - counter and self.position[0] - counter <=8 and 1 <= self.position[1] - counter and self.position[1] - counter <=8 :
                    upleft.append([self.position[0] - counter, self.position[1] - counter])
                if 1 <= self.position[0] + counter and self.position[0] + counter <=8 and 1 <= self.position[1] - counter and self.position[1] - counter <=8 :
                    downleft.append([self.position[0] + counter, self.position[1] - counter])
                if 1 <= self.position[0] - counter and self.position[0] - counter <=8 and 1 <= self.position[1] + counter and self.position[1] + counter <=8 :
                    upright.append([self.position[0] - counter, self.position[1] + counter])

            moveset = [downright, downleft, upright, upleft]

            opposition = []

            for movement in moveset:
                for coordinates in movement:
                    for piece in pieces:
                        if coordinates == piece.position:
                            opposition.append(coordinates)
                            del movement[movement.index(coordinates):]

            moveset = downleft + downright + upleft + upright
            downleft = downright = upleft = upright = []

            for coordinates in opposition:
                for piece in pieces:
                    if piece.position == coordinates:
                        if piece.color != self.color:
                            moveset.append(coordinates)

        destination = [ord(move[1])-97,move[2]]
        for possibility in moveset:
            if destination == possibility:
                return True
            else:
                return False

WPawn = Piece(0,[2,1])
BPawn = Piece(1,[2,5])
WBishop = Bishop(0,[4,3])
pieces = [WPawn,BPawn,WBishop]
board = Board(pieces)

while True:
    Board.display(board)
    try:
        move = str(input('Enter your next move: '))
        if len(move) != 3 or type(move) != str:
            raise Exception('Invalid move')
        if move[0] != 'B':
            raise Exception('Non-bishop movement not supported yet')
    finally:
        pass

    if Bishop.isValidMove(WBishop,move,pieces):
        coords = [ord(move[1])-97,int(move[2])-1]
        for piece in pieces:
            if piece.position == coords:
                pieces.remove(piece)
        WBishop.position = coords