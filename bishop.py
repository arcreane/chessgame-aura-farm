from main import Board

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

class Bishop(Piece):
    def __init__(self,color,position):
        if self.color == 0:
            self.symbol = '♗'
        if self.color == 1:
            self.symbol='♝'
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



