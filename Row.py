class Row:
    def __init__(self, values):
        self.values = values

    def is_valid(self):
        checked = []
        for i in self.values:
            if i in checked:
                return False
            checked.append(i)
        return True
