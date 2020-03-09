
from Square import *
from Coordinate import *

from ChessColour import *
from ChessPieces import *

import Piece
from Queen import *
from Rook import *
from Pawn import *
from King import *
from Bishop import *
from Knight import * 

class ChessBoard:

	# WHITE is the first move
	__activeColour__ = ChessColour.WHITE
	# Move count starts at 1
	# Increment after black has replied with their move
	__fullMove__ = 1	 

	def __init__(self):
		self.reset()

	def initilizeFromPieces(self, positions, pieces):
		pass

	# Sets the default state of the chess board
	def reset(self):

		# Instantiate the chessboard 
		self.chessboard = [[0,0,0,0,0,0,0,0],
						   [0,0,0,0,0,0,0,0],
						   [0,0,0,0,0,0,0,0],
						   [0,0,0,0,0,0,0,0],
						   [0,0,0,0,0,0,0,0],
						   [0,0,0,0,0,0,0,0],
						   [0,0,0,0,0,0,0,0],
						   [0,0,0,0,0,0,0,0]]

		# Set the board pieces
		# White Main Pieces
		self.chessboard[0][0] = Square(Coordinate("a1"), Rook(ChessColour.WHITE))
		self.chessboard[1][0] = Square(Coordinate("b1"), Knight(ChessColour.WHITE))
		self.chessboard[2][0] = Square(Coordinate("c1"), Bishop(ChessColour.WHITE))
		self.chessboard[3][0] = Square(Coordinate("d1"), Queen(ChessColour.WHITE))
		self.chessboard[4][0] = Square(Coordinate("e1"), King(ChessColour.WHITE))
		self.chessboard[5][0] = Square(Coordinate("f1"), Bishop(ChessColour.WHITE))
		self.chessboard[6][0] = Square(Coordinate("g1"), Knight(ChessColour.WHITE))
		self.chessboard[7][0] = Square(Coordinate("h1"), Rook(ChessColour.WHITE))

		# White Pawns
		self.chessboard[0][1] = Square(Coordinate("a2"), Pawn(ChessColour.WHITE))
		self.chessboard[1][1] = Square(Coordinate("b2"), Pawn(ChessColour.WHITE))
		self.chessboard[2][1] = Square(Coordinate("c2"), Pawn(ChessColour.WHITE))
		self.chessboard[3][1] = Square(Coordinate("d2"), Pawn(ChessColour.WHITE))
		self.chessboard[4][1] = Square(Coordinate("e2"), Pawn(ChessColour.WHITE))
		self.chessboard[5][1] = Square(Coordinate("f2"), Pawn(ChessColour.WHITE))
		self.chessboard[6][1] = Square(Coordinate("g2"), Pawn(ChessColour.WHITE))
		self.chessboard[7][1] = Square(Coordinate("h2"), Pawn(ChessColour.WHITE))

		# The blank squares
		for j in range(0, 8):
			for i in range(2, 6):
				self.chessboard[j][i] = Square(Coordinate("{}{}".format(chr(j+97),i+1)), None)		

		# Black Main Pieces
		self.chessboard[0][7] = Square(Coordinate("a8"), Rook(ChessColour.BLACK))
		self.chessboard[1][7] = Square(Coordinate("b8"), Knight(ChessColour.BLACK))
		self.chessboard[2][7] = Square(Coordinate("c8"), Bishop(ChessColour.BLACK))
		self.chessboard[3][7] = Square(Coordinate("d8"), Queen(ChessColour.BLACK))
		self.chessboard[4][7] = Square(Coordinate("e8"), King(ChessColour.BLACK))
		self.chessboard[5][7] = Square(Coordinate("f8"), Bishop(ChessColour.BLACK))
		self.chessboard[6][7] = Square(Coordinate("g8"), Knight(ChessColour.BLACK))
		self.chessboard[7][7] = Square(Coordinate("h8"), Rook(ChessColour.BLACK))

		# Black Pawns
		self.chessboard[0][6] = Square(Coordinate("a7"), Pawn(ChessColour.BLACK))
		self.chessboard[1][6] = Square(Coordinate("b7"), Pawn(ChessColour.BLACK))
		self.chessboard[2][6]= Square(Coordinate("c7"), Pawn(ChessColour.BLACK))
		self.chessboard[3][6] = Square(Coordinate("d7"), Pawn(ChessColour.BLACK))
		self.chessboard[4][6] = Square(Coordinate("e7"), Pawn(ChessColour.BLACK))
		self.chessboard[5][6] = Square(Coordinate("f7"), Pawn(ChessColour.BLACK))
		self.chessboard[6][6] = Square(Coordinate("g7"), Pawn(ChessColour.BLACK))
		self.chessboard[7][6] = Square(Coordinate("h7"), Pawn(ChessColour.BLACK))

	# Return the square based on the passed coordinate 
	def getSquare(self, coordinate):
		# return the square
		return self.chessboard[coordinate.getColumnNumber()][coordinate.getRowNumber()]

	# Move method
	def move(self, source, destination):
		# The source square coordinate
		source_column = source.getColumnNumber()
		source_row = source.getRowNumber()

		# The destination square coordinate
		destination_column = destination.getColumnNumber()
		destination_row = destination.getRowNumber()

		# If the source square is empty, return False
		if(self.getSquare(source).getPiece() is None): 
			return False

		# If the piece on the destination square is the same colour as the active piece colour, return FALSE
		if(self.getSquare(destination).isOccupied() and self.getSquare(destination).getPiece().getColour() 
			is ChessBoard.__activeColour__):
			return False

		# If the move on the source piece is a legal move
		if(self.getSquare(source).getPiece().isLegalMove(self,source, destination)):
			# If the move is not on the active colour's turn return False
			if(self.getSquare(source).getPiece().getColour() is not ChessBoard.__activeColour__):
				return False

			# Do the move
			# change the active colour
			# increment the move number
			self.getSquare(destination).addPiece(self.getSquare(source).deletePiece())

			# change the active colour 
			if(ChessBoard.__activeColour__ is ChessColour.WHITE):
				ChessBoard.__activeColour__ = ChessColour.BLACK
			else:
				ChessBoard.__activeColour__ = ChessColour.WHITE
				ChessBoard.__fullMove__ = ChessBoard.__fullMove__ + 1
			# RETURN TRUE (THE MOVE WAS DONE)
			return True
		# RETURN FALSE (THE MOVE COULD NOT BE DONE)
		else:
			return False

	# String function 
	# Print the board in BOARD mode
	# White pieces at the bottom
	def __str__(self):
		out = "Board:Board\n"
		for i in range(7, -1, -1):
			for j in range (0,8):
				if self.chessboard[j][i].getPiece() is None:
					if j == 7:
						out += " "
					else:
						out += " _"
				else:
					if j == 7:
						out += "{}".format(self.chessboard[j][i].getPiece().getShortName())

					else:
						out += "{}_".format(self.chessboard[j][i].getPiece().getShortName())
			out += "\n"
		return out

	# Print the board in FEN mode
	# White Pieces on the left
	def toFEN(self):
		pass
