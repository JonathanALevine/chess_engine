
from enum import Enum

# Enumeration class sets the shortnames of the pieces
class ChessPieces(Enum):
	# Shortnames of the pieces
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

