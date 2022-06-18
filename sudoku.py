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

GRID_REFERENCE = [ [3, 0, 6, 5, 0, 8, 0, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

def print_grid(grid):
    for row in grid:
        print(row)

def valid_square(grid, row, column, value):
    if grid[row][column] == value:
        return False

    for square in grid[row]:
        if square == value:
            return False

    for j in range(0, GRID_SIZE):
        if grid[j][column] == value:
            return False

    return True


def solve(grid, row, column):
    if row == GRID_SIZE - 1 and column == GRID_SIZE:
        print("done")
        return True

    if column == GRID_SIZE:
        row += 1
        column = 0

    if GRID_REFERENCE[row][column] != 0:
        solve(grid, row, column + 1)

    square_valid = False

    for i in range(1, GRID_SIZE + 1):
        if valid_square(grid, row, column, i):
            grid[row][column] = i
            square_valid = True
            solve(grid, row, column + 1)
    if not square_valid:
        grid[row][column] = 0
        if column > 0:
            while(GRID_REFERENCE[row][column - 1] != 0):
                if column == 0:
                    row -= 1
                    column = GRID_SIZE - 1
                else:
                    column -= 1
        
        solve(grid, row, column - 1)
    return False


if solve(GRID, 0, 0):
    print_grid(GRID)

print("donezo")
