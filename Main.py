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
print(test.move(Coordinate("a2"), Coordinate("a4")))
print(test)
print(test.move(Coordinate("e7"), Coordinate("e5")))
print(test)
print(test.move(Coordinate("a4"), Coordinate("a5")))
print(test)
print(test.move(Coordinate("e5"), Coordinate("e4")))
print(test)