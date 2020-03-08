

from ChessColour import *
from ChessPieces import *
import Piece

class Pawn(Piece.Piece):
	def __init__(self, colour):
		# Instatiate the pawn from piece class with inheritance
		# Inherite all methods from the piece class by using super
		super().__init__(ChessPieces.PAWN, colour)
		# Instatiate the pawn's first move
		self.first_move = True

	def isLegalMove(self, chessboard, source, destination):
		# The pawns rules are different depending on if its in its first move or not 
		# If the pawn is on its first move
		if(self.first_move):

			# Source square coordinates
			source_column = source.getColumnNumber()
			source_row = source.getRowNumber()
			# Destination square coordinates
			destination_column = destination.getColumnNumber()
			destination_row = destination.getRowNumber()

			# Rules change depending on if capturing a piece
			

			# Set the first move to False
			self.first_move = False
		else:
			pass

		return True