GRID_SIZE = 9

GRID = [ [3, 0, 6, 5, 0, 8, 0, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

def solve(grid, row, column):
    if row == GRID_SIZE - 1 and column == GRID_SIZE:
        return False
    if column == GRID_SIZE:
        row += 1
        column = 0
    print(grid[row][column])
    solve(grid, row, column + 1)


    return False

solve(GRID, 0, 0)
