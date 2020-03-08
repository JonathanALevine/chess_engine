

from ChessColour import *
from ChessPieces import *
import Piece

class Knight(Piece.Piece):
	def __init__(self, colour):
		super().__init__(ChessPieces.KNIGHT, colour)

	def isLegalMove(self, chessboard, source, destination):
		# Source square coordinates
		source_column = source.getColumnNumber()
		source_row = source.getRowNumber()
		# Destination square coordinates
		destination_column = destination.getColumnNumber()
		destination_row = destination.getRowNumber()

		return True
