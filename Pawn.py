
from ChessColour import *
from ChessPieces import *
import Piece
import math

class Pawn(Piece.Piece):
	# Constructor
	# Sets the first_move parameter to True
	def __init__(self, colour):
		# Instatiate the pawn from piece class with inheritance
		# Inherite all methods from the piece class by using super
		super().__init__(ChessPieces.PAWN, colour)
		# Instatiate the pawn's first move
		self.first_move = True
	# isLegalMove() method
	# Detects if the Pawn move is legal
	# Returns True or False depending
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
			# Not capturing a piece
			else:
				# If on the FIRST MOVE, pawns can advance two squares or one
				# Pawns cannot jump over other pieces
				if(self.first_move and ((destination_row - source_row == 1) or (destination_row - source_row == 2)) and
					(destination_column-source_column == 0) and not(chessboard.chessboard[source_column][source_row+1].isOccupied())):
					self.first_move = False
					return True
				elif(not(self.first_move) and (destination_row - source_row == 1) and (destination_column-source_column == 0)):
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
				# If on the FIRST MOVE, pawns can advance two squares or one
				# Pawns cannot jump over other pieces
				if(self.first_move and ((destination_row - source_row == -1) or (destination_row - source_row == -2)) and
					(destination_column-source_column == 0) and not(chessboard.chessboard[source_column][source_row-1].isOccupied())):
					self.first_move = False
					return True
				elif(not(self.first_move) and (destination_row - source_row == -1) and (destination_column-source_column == 0)):
					return True
				else:
					return False