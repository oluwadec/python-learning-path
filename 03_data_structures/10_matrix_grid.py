"""10_matrix_grid.py - 2D lists as grids and matrices."""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Centre cell:", grid[1][1])
print("Last row:", grid[-1])

# Print the grid neatly
for row in grid:
    print(" ".join(str(n) for n in row))

# Sum of every row
row_sums = [sum(row) for row in grid]
print("Row sums:", row_sums)

# Transpose (rows become columns)
cols = list(zip(*grid))
print("Columns:", [list(c) for c in cols])

# Flatten into one list
flat = [n for row in grid for n in row]
print("Flat:", flat)
