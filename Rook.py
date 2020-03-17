

from ChessColour import *
from ChessPieces import *
import Piece

class Rook(Piece.Piece):
	def __init__(self, colour):
		super().__init__(ChessPieces.ROOK, colour)

	def isLegalMove(self, chessboard, source, destination):
		# Source square coordinates
		source_column = source.getColumnNumber()
		source_row = source.getRowNumber()
		# Destination square coordinates
		destination_column = destination.getColumnNumber()
		destination_row = destination.getRowNumber()


		# when a rook moves it, the following is true
		# (1) The row changes but the column does not change
		# (2) The column changes but the row does not change
		# (3) Cannot jump over a piece
		

		return True

