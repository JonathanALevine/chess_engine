

from ChessColour import *
from ChessPieces import *
import Piece

class King(Piece.Piece):
	def __init__(self, colour):
		super().__init__(ChessPieces.KING, colour)

	def isLegalMove(self, chessboard, source, destination):
		return True