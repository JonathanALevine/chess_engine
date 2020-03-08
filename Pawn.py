
from ChessColour import *
from ChessPieces import *
import Piece
import math

class Pawn(Piece.Piece):
	def __init__(self, colour):
		# Instatiate the pawn from piece class with inheritance
		# Inherite all methods from the piece class by using super
		super().__init__(ChessPieces.PAWN, colour)
		# Instatiate the pawn's first move
		self.first_move = True

	def isLegalMove(self, chessboard, source, destination):
		# Source square coordinates
		source_column = source.getColumnNumber()
		source_row = source.getRowNumber()
		# Destination square coordinates
		destination_column = destination.getColumnNumber()
		destination_row = destination.getRowNumber()
		# The rules of capture depend on if it is a WHITE Pawn or a BLACK Pawn
		# WHITE Pawn logic
		if(chessboard.getSquare(source).getPiece().getColour() is ChessColour.WHITE):
			# If the destination square is occupied
			# Capturing a piece
			if(chessboard.getSquare(destination).isOccupied()):
				# The destination row can only be +1 the source row
				# The destination column can only be +/-1 the source column
				if((destination_row - source_row == 1) and (abs(destination_column-source_column) == 1)):
					return True
				else:
					return False
			# Not occupied
			else:
				# If on the FIRST MOVE, pawns can advance two squares or one
				if(self.first_move and ((destination_row - source_row == 1) or (destination_row - source_row == 2)) and
					(abs(destination_column-source_column) == 0)):
					self.first_move = False
					return True
				else:
					return False
		# BLACK Pawn logic
		else:
			# If the destination square is occupied
			# Capturing a piece
			if(chessboard.getSquare(destination).isOccupied()):
				# The destination row can only be -1 the source row
				# The destination column can only be +/-1 the source column
				if((destination_row - source_row == -1) and (abs(destination_column-source_column) == 1)):
					return True
				else:
					return False
			# Not occupied
			else:
				# If on the FIRST MOVE, the pawns can advance two squares or one
				if(self.first_move and (destination_row - source_row == -1) or (destination_row - source_row == -2) and 
					(abs(destination_column-source_column) == 0)):
					self.first_move = False
					return True
				else:
					return False