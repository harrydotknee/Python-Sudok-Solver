from Block import Block
class Grid:
    def __init__(self, values):
        self.values = values

    def values(self):
        return self.values
    
    def make_blocks(self):
        row_of_blocks_1 = self.values[:2]
        row_of_blocks_2 = self.values[3:6]
        row_of_blocks_3 = self.values[6:9]
        block = [[]]
        for row in self.values:
            block_row =  [row[:2], row[3:6], row[6:9]]
            block.append(block_row)

