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
        for i in range(8):
            for j in range(8):
                for piece in self.pieces:
                    if piece.position == [i,j]:
                        drawnboard[i][j] = piece.symbol
                    else:
                        drawnboard[i][j] = '_'

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
                for position in movement:
                    for piece in pieces:
                        if position == piece.getposition():
                            opposition.append(position)
                            del movement[movement.index(position):]

            moveset = downleft + downright + upleft + upright
            downleft = downright = upleft = upright = []
            possiblecaptures = []

            for position in opposition:
                if position.getpiece().color != self.color:
                    moveset.append(position)
                    possiblecaptures.append(position)

        destination = [ord(move[1])-97,move[2]]
        for possibility in moveset:
            if destination == possibility:
                return True
            else:
                return False

