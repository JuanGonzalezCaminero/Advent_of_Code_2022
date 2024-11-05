from operator import add
from itertools import product
def check_visible(house_height, row):
    visible=0
    for tree in row[1:]:
        visible+=1
        if tree >= house_height:
            break
    return visible

file = open("input")
grid = [[int(j) for j in list(i.strip())] for i in file.readlines()]
grid_size = len(grid)
current_max = 0
#Go over every tree
for (i,j) in product(range(grid_size), range(grid_size)):
    tree_score = 1
    # Count in all directions
    # left
    tree_score *= check_visible(grid[i][j], grid[i][j::-1])
    # right
    tree_score *= check_visible(grid[i][j], grid[i][j:grid_size])
    # up
    tree_score *= check_visible(grid[i][j], [grid[k][j] for k in range(i, -1, -1)])
    # down
    tree_score *= check_visible(grid[i][j], [grid[k][j] for k in range(i, grid_size)])
    if(tree_score > current_max):
        current_max = tree_score

print(current_max)