
class Coordinate:

    def __init__(self, coordinate):

        # The column must be between "a" and "h"
        # The column must be a letter ..... to be implemented
        if ord(coordinate[0]) >= 97+8:
            raise ValueError
        # The row must be between 1 and 8 
        if int(coordinate[1]) > 8 or int(coordinate[1]) < 1:
            raise ValueError
        # The row must be number ..... to be implemented

        # Instantiate the coordinate
        self.coordinate = coordinate
        # Instatiate the column and the row based on the coordinate
        # Ex: "a1" => column = "a", row = "1"
        self.column = coordinate[0]
        self.row = coordinate[1]

    # Get the column
    def getColumn(self):
        return self.column

    # Get the row
    def getRow(self):
        return self.row

    def getColumnNumber(self):
        return ord(self.getColumn()) - 97

    def getRowNumber(self):
        return int(self.getRow()) - 1

    # String Function
    def __str__(self):
        return "({},{})".format(self.getColumn(), self.getRow())

    def name(self):
        return "{}{}".format(self.getColumn(), self.getRow())
