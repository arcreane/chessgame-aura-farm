#The file that runs the whole chess game
import time as t
from player.py import AiPlayer, HumanPlayer
from board.py import Board

def initPlayer() -> tuple:
    print("Welcome to the chess game!")
    t.sleep(0.7)
    ready = False
    while not ready:
        print("Enter the names of the players, followed by their color (W/B)! Type 'AI' to choose an ai player")
        player1 = input("Player 1:")
        player2 = input("Player 2:")
        if player1 == "AI" and player2 == "AI":
            print("You can't make 2 AIs fight! ")
        else:
            player1 = player1.split()
            player2 = player2.split()
            if player1[1] not in ["W,B"] or player2[1] not in ["W,B"]:
                print("Please enter either W or B as a color! Format: '[NAME] [COLOR]' ")
            else:
                if player1[0] == "AI":
                    player1 = AiPlayer(player1[0], player1[1])
                    player2 = HumanPlayer(player2[0], player2[1])
                elif player2[0] == "AI":
                    player2 = AiPlayer(player2[0], player2[1])
                    player1 = HumanPlayer(player1[0], player1[1])
                else:
                    player1 = AiPlayer(player1[0], player1[1])
        return (player1, player2)


class Chess:
    def __init__(self):
        print('Initializing game....')
        self.board = Board()
        print("Board initialized!")
        self.players = self.initPlayers()
        print("Players ready!")
        self.currentPlayer = 0
        print(f"First player to play is {self.players[self.currentPlayer].name} who is playing {self.players[self.currentPlayer].color}")




    def switchPlayer(self):
        self.currentPlayer = (self.currentPlayer + 1)%2

    def initPlayers(self) -> tuple:
        players = initPlayer()
        if players[0].color == "W":
            self.currentPlayer = 0
        else:
            self.currentPlayer = 1
        return players

    def isCheckMate(self):
        return False

    def displayBoard(self):
        self.board.display()

    def isValidMove(self, move):








