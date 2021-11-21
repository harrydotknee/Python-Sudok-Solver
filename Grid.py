from Block import Block
from Row import Row
from Column import Column

class Grid:
    def __init__(self, values):
        self.values = values

    def values(self):
        return self.values

    def block_row(self, triple_row):
        return [
            Block([triple_row[0][:3], triple_row[1][:3], triple_row[2][:3]]),
            Block([triple_row[0][3:6], triple_row[1][3:6], triple_row[2][3:6]]),
            Block([triple_row[0][6:9], triple_row[1][6:9], triple_row[2][6:9]])
        ]

    def blocks(self):
        return [
            self.block_row(self.values[:3]),
            self.block_row(self.values[3:6]),
            self.block_row(self.values[6:9])
        ]
    def rows(self):
        grid_of_rows = []
        for i in self.values:
            grid_of_rows.append(Row(i))
        return grid_of_rows

    def columns(self):
        grid_of_columns = []
        for i in range(0, len(self.values)):
            column = []
            for j in range(len(self.values[i])):
                column.append(self.values[j])
            grid_of_columns.append(Column(column))
                
        return grid_of_columns

    def is_block_valid(self):
        for block_row in self.blocks():
            for block in block_row:
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



