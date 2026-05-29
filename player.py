class Player:
    def __init__(self, name, color:str):
        self.name = name
        self.color = color

    def AskMove(self):
        piece = int(input("Which pawn do you want to move?"))
        position1 = int(input("Where is it?"))
        position2 = int(input("Where do you want it to go?"))




class HumanPlayer(Player):
    pass

class AiPlayer(Player):
    pass