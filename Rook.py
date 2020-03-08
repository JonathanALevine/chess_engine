

from ChessColour import *
from ChessPieces import *
import Piece

class Rook(Piece.Piece):
	def __init__(self, colour):
		super().__init__(ChessPieces.ROOK, colour)

	def isLegalMove(self, chessboard, source, destination):
		return True

