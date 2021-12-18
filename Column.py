class Column:
    def __init__(self, values):
        self.values = values

    def is_valid(self):
        checked = []
        for i in self.values:
            if i in checked:
                return False
            if i != 0:
                checked.append(i)
        return True
