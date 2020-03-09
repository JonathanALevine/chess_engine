

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
		# Knights can jump over pieces
		# Types of moves for knights
		# (1): Column changes by 1 and row changes by 2
		# (2): Column changes by 2 and row changes by 1
		if(abs(destination_column - source_column == 1) and abs(destination_row-source_row == 2)):
			return True
		elif(abs(destination_column - source_column == 2) and abs(destination_row-source_row == 1)):
			return True
		else:
			return False