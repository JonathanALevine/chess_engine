
from ChessColour import *
from ChessPieces import *
import Piece

class Bishop(Piece.Piece):
	def __init__(self, colour):
		super().__init__(ChessPieces.BISHOP, colour)

	def isLegalMove(self, chessboard, source, destination):
		return True