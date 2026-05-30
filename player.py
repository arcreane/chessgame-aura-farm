import random

class player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def AskMove(self, legal_moves):
        raise


class human_player(player):
    def play(self, legal_moves):
        print(f"\n{self.name}'s turn ({self.color})")
        while True:
            start = input("start square")
            end = input("end square")
            move = (start, end)
            if move in legal_moves:
                return move
            print("impossible move")


class ai_player(player):
    def play(self, legal_moves):
        print(f"\n{self.name}'s turn")
        move = random.choice(legal_moves)
        print(f"{self.name} plays {move[0]} -> {move[1]}")
        return move
