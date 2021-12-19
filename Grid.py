from Block import Block
from Row import Row
from Column import Column
from Square import Square

class Grid:
    def __init__(self, values):
        self.values = values

    def squares(self):
        squares = []
        for row in self.values:
            new_row = []
            for value in row:
                new_row.append(Square(value))
            squares.append(new_row)
        return squares

    def convert_value_array_to_squares(self, array):
        output = []
        for value in array:
            output.append(Square(value))
        return output

    def block_row(self, triple_row):
        return [
            Block([triple_row[0][:3],triple_row[1][:3], triple_row[2][:3]]),
            Block([triple_row[0][3:6], triple_row[1][3:6], triple_row[2][3:6]]),
            Block([triple_row[0][6:9], triple_row[1][6:9], triple_row[2][6:9]])
        ]

    def blocks(self):
        return (
            self.block_row(self.squares()[:3]) +
            self.block_row(self.squares()[3:6]) +
            self.block_row(self.squares()[6:9])
        )
    def rows(self):
        grid_of_rows = []
        for i in self.squares():
            grid_of_rows.append(Row(i))
        return grid_of_rows

    def columns(self):
        grid_of_columns = []
        for x in range(0, 9): # for each in row
            column = []
            for y in range(0,9): # for each in column
                column.append(self.squares()[y][x])
            grid_of_columns.append(Column(column))
        return grid_of_columns

    def is_block_valid(self):
        for block in self.blocks():
            if block.is_valid() == False:
                return False
        return True

    def is_row_valid(self):
        for row in self.rows():
            if row.is_valid() == False:
                return False
        return True

    def is_column_valid(self):
        for column in self.columns():
            if column.is_valid() == False:
                return False
        return True

    def is_valid(self):
        if self.is_row_valid() and self.is_column_valid() and self.is_block_valid():
            return True
        return False

    def is_complete(self):
        if self.is_valid():
            for row in self.rows():
                for square in row.squares:
                    if square.value == 0:
                        return False
            return True
        return False
