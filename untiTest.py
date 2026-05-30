import main as m,bishop as b,chess as c,position as p,pionRook as pr, player as pl
import time as t
def testBoardPiece():
    pieces = [m.Piece(0,(0,0)),m.Piece(0,(1,0)),m.Piece(1,(3,0)),]
    print("Creating pieces OK")
    t.sleep(0.5)
    print(pieces)
    board = m.Board(pieces)
    print("Creating board OK")
    t.sleep(0.5)
    board.display() #should display the board
    t.sleep(0.5)
    print(board.get_piece((0,0))) #should display a black piece
    print(board.get_piece((3,0))) #should display a white piece
    print("Getting pieces OK")
    t.sleep(0.5)
    board.set_piece(m.Piece("B",(1,1)))
    print('Setting pieces OK')
    t.sleep(0.5)
    print(board.get_piece((1,1)))
    print("Getting set pieces OK")
    t.sleep(0.5)


print("Testing Board")
testBoardPiece()
