from Square import Square
class Row:
    def __init__(self, squares):
        self.squares = squares

    def is_valid(self):
        checked = []
        for i in self.squares:
            if i.value in checked:
                return False
            if i.value != 0:
                checked.append(i.value)
        return True
