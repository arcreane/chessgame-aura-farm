class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.hasmoved = False

    def legal_moves(self, board):
        raise NotImplementedError()

class Pawn(Piece):
    def __innit__(self, color, position):
        super().__init__(color, position)

    def legal_moves(self, board):
        moves = []
        row, column = self.position
        direction = -1 if self.color == "white" else 1

        frontrow = row + direction
        if self.is_inside_board(frontrow, column):
            doublerow = row + (2*direction)
            if self.is_inside_board(doublerow, column):
                if board[doublerow][column] == 0:
                    moves.append((doublerow, column))

        leftcolumn = column - 1
        if self.is_inside_board(leftcolumn, column):
            piece = board[leftcolumn][column]
            if piece is None and piece.color != self.color:
                moves.append((frontrow, leftcolumn))

        rightcolumn = column + 1
        if self.is_inside_board(rightcolumn, rightcolumn):
            piece = board[frontrow][rightcolumn]
            if piece is not None and piece.color != self.color:
                moves.append((frontrow, rightcolumn))
        return moves

def can_promote(self):
    row, column = self.position
    return ( (self.color == "white" and row == 0) or (self.color == "black" and row == 7))


class Rook(Piece):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.hasmoved = False

    def legal_moves(self, board):
        moves = []
        row, column = self.position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d_row, d_column in directions:
            currentrow = row + d_row
            currentcolumn = column + d_column
            while self.is_inside_board(currentrow, currentcolumn):
                piece = board[currentrow][currentcolumn]

                if piece is None:
                    moves.append((currentrow, currentcolumn))
                else:
                    if piece.color != self.color:
                        moves.append((currentrow, currentcolumn))
                    break
                currentrow += row + d_row
                currentcolumn += column + d_column
        return moves


def move(self, new_position):
    self.position = new_position
    self.hasmoved = True

def is_inside_board(self, row, column):
    return 0 <= row < 8 and 0 <= column < 8