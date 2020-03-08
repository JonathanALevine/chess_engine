
from ChessColour import *
from ChessPieces import *

class Piece:

	def __init__(self, piece, colour):
		self.colour = colour
		self.name = piece
		self.shortName = self.name.getShortName()

		# If the piece is black, the name is lower case
		if self.colour is ChessColour.BLACK:
			self.shortName = self.shortName.lower()

	def getShortName(self):
		return self.shortName

	def getColour(self):
		return self.colour

	def getName(self):
		return self.name

	def isLegalMove(self, chessboard, source, destination):
		if(chessboard.getSquare(source).getPiece().isLegalMove(chessboard, source, destination)): return True
		else: return False 

	# String function
	def __str__(self):
		return "{} {}".format(self.getColour().name, self.getName().name)