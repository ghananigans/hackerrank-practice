import sys

# Return True if something around this location
# is a bomb (including itself)
def check(grid, R, C, i, j):
    return (grid[i][j] == "O") or \
        (i + 1 < R and grid[i + 1][j] == "O") or \
        (i - 1 >= 0 and grid[i - 1][j] == "O") or \
        (j + 1 < C and grid[i][j + 1] == "O") or \
        (j - 1 >= 0 and grid[i][j - 1] == "O")

R, C, N = [int(temp) for temp in input().split(' ')]
grid = []

for i in range(R):
    grid.append(list(input()))
    assert(len(grid[-1]) == C)

assert(len(grid) == R)

for i in range(R):
    row = grid[i]

    for j in range(C):
        if N == 1:
            # 1
            sys.stdout.write(row[j])
        elif N % 2 == 0:
            # 2, 4, 6, 8
            sys.stdout.write("O")
        elif N % 4 == 1:
            if check(grid, R, C, i, j):
                # In 2 steps, this location is empty, so check to see
                # if any of the locations around this location would
                # have a bomb in 2 steps. If it does, then this place
                # will be empty after another 2 steps, otherwis
                # plant a bomb
                if (i + 1 < R and not check(grid, R, C, i + 1, j)) or \
                    (i - 1 >= 0 and not check(grid, R, C, i - 1, j)) or \
                    (j + 1 < C and not check(grid, R, C, i, j + 1)) or \
                    (j - 1 >= 0 and not check(grid, R, C, i, j - 1)):
                    # If any of the
                    sys.stdout.write(".")
                else:
                    sys.stdout.write("O")
            else:
                # in 2 steps, this location would have a bomb planted
                # so in 2 more steps, this location would be empty
                sys.stdout.write(".")
        elif N % 4 == 3:
            # 4, 8, 12
            if check(grid, R, C, i, j):
                # Something around this location is a bomb
                # so this place is empty
                sys.stdout.write(".")
            else:
                # Nothing around this location is a bomb
                # so plant a bomb
                sys.stdout.write("O")
        else:
            assert(False)

    sys.stdout.write("\n")
