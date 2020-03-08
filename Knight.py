

from ChessColour import *
from ChessPieces import *
import Piece

class Knight(Piece.Piece):
	def __init__(self, colour):
		super().__init__(ChessPieces.KNIGHT, colour)

	def isLegalMove(self, chessboard, source, destination):
		return True
