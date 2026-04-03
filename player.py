class Player:
    def __init__(self, _name, _color):
        self._name = _name
        self._color = _color

    def AskMove(self):
        int(input("What is your move?"))



class HumanPlayer(Player):
    pass

class AiPlayer(Player):
    pass