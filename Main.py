from ChessColour import *
from ChessPieces import *
import Piece
from Queen import *
from Square import *
from Pawn import *
from Coordinate import *
from ChessBoard import *

test = ChessBoard()
print(test)
print(test.move(Coordinate("b1"), Coordinate("c3")))
print(test)
print(test.move(Coordinate("d7"), Coordinate("d5")))
print(test)
print(test.move(Coordinate("c3"), Coordinate("d5")))
print(test)
print(test.move(Coordinate("d8"), Coordinate("d5")))
print(test)
