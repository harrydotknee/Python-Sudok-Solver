from Square import Square
class Block:
    def __init__(self, squares):
        self.squares = squares

    def squares_arr(self):
        value_arr = []
        for i in self.squares:
            for j in i:
                value_arr.append(j)
        return value_arr

    def is_valid(self):
        checked = []
        for i in self.squares_arr():
            if i.value in checked:
                return False
            if i.value != 0:
                checked.append(i.value)
        return True
