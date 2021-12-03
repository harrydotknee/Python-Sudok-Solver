class Block:
    def __init__(self, values):
        self.values = values

    def values_arr(self):
        value_arr = []
        for i in self.values:
            for j in i:
                value_arr.append(j)
        return value_arr

    def is_valid(self):
        checked = []
        for i in self.values_arr():
            if i in checked:
                return False
            if i != 0:
                checked.append(i)
        return True
