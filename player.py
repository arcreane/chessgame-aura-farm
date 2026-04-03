class Player:
    def __init__(self, _name, _color):
        self._name = _name
        self._color = _color

    def AskMove(self):
        move = str(input("What is your move?"))
        #if isValidMove(move,board):




class HumanPlayer(Player):
    pass

class AiPlayer(Player):
    pass