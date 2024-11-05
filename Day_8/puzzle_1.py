from operator import add
def check_visible(visible, row, coords, axis):
    previous_tree=-1
    for tree in row:
        if previous_tree < tree:
            visible.add(tuple(coords))
            if tree == 9:
                return
            previous_tree = tree
        coords = list(map(add, coords, axis))

file = open("input")
grid = [[int(j) for j in list(i.strip())] for i in file.readlines()]
visible = set()
grid_size = len(grid)
# Count in all directions, assume square grid
for i in range(grid_size):
    #left
    check_visible(visible, grid[i], [i, 0], [0, 1])
    # right
    check_visible(visible, grid[i][::-1], [i, grid_size-1], [0, -1])
    # top
    check_visible(visible, [grid[j][i] for j in range(grid_size)], [0, i], [1, 0])
    # bottom
    check_visible(visible, [grid[j][i] for j in range(grid_size)][::-1], [grid_size-1, i], [-1, 0])

print(len(visible))