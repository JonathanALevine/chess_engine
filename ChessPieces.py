
from enum import Enum

class ChessPieces(Enum):

	PAWN = "P"
	KNIGHT = "N"
	BISHOP = "B"
	ROOK = "R"
	QUEEN = "Q"
	KING = "K"

	def __init__(self, shortName):
		self.shortName = shortName

	def getShortName(self):
		return self.shortName

