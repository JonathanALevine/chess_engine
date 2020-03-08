

from Coordinate import *
from Piece import *

class Square:

	def __init__(self, coordinate, piece):
		self.coordinate = coordinate
		self.piece = piece

	def getCoordinate(self):
		return self.coordinate

	def getPiece(self):
		return self.piece

	def getColumn(self):
		return self.getCoordinate().getColumn()

	def getRow(self):
		return self.getCoordinate().getRow()

	# addPiece() stores the old piece in temp, sets the square piece
	# to the new piece and returns the old piece
	def addPiece(self, newPiece):
		temp = self.getPiece()
		self.piece = newPiece
		return temp

	# deletePiece() deletes the piece in the square by setting it to None
	def deletePiece(self):
		return self.addPiece(None)

	# isOccupied() returns false if the square is empty
	# returns true if the square is full
	def isOccupied(self):
		if (self.piece is None): return False
		else: return True

	# String function
	# Prints the piece
	# Checks if the square is occupied
	def __str__(self):
		# Filled Square
		if(self.isOccupied()):
			return "Square({},{}):{}".format(self.getColumn(), self.getRow(), self.getPiece())
		# Empty Square
		else:
			return "Square({},{}):None".format(self.getColumn(), self.getRow())		


