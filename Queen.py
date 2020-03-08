
from ChessColour import *
from ChessPieces import *
import Piece

class Queen(Piece.Piece):
	def __init__(self, colour):
		super().__init__(ChessPieces.QUEEN, colour)

	def isLegalMove(self, chessboard, source, destination):
		return True
