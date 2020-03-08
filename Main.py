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
test.move(Coordinate("e2"), Coordinate("e4"))
print(test)
test.move(Coordinate("b8"), Coordinate("c6"))
print(test)
test.move(Coordinate("a2"), Coordinate("a4"))
print(test)
