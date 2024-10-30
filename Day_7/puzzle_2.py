from collections import defaultdict
def dfs(current, current_path, dirs):
    for d in current[2]:
        dirs[current_path + d + "/"] += dfs(current[2][d], current_path + d + "/", dirs)
    return sum([i[1] for i in current[1]]) + sum([dirs[current_path + d + "/"] for d in current[2]])

file = open("input")
log = [i.split() for i in file.readlines()]
# node[parent, [(filename, size), ... ], {dirname: node, ...}]
root_node = [None, [], {}]
current_node = root_node
# Go over the log and fill the tree
while(len(log) > 0):
    line = log.pop(0)
    # Command
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current_node = current_node[0]
            else:
                if(line[2] not in current_node[2]):
                    # Add node to the tree if it doesn't exist and move to it
                    new_node = [current_node, [], {}]
                    current_node[2][line[2]] = new_node
                    current_node = new_node
                else:
                    # Otherwise just move to it
                    current_node = current_node[2][line[2]]
        elif line[1] == "ls":
            # Listed items
            while(len(log) > 0 and log[0][0] != "$"):
                item = log.pop(0)
                if(item[0] == "dir"):
                    if(item[1] not in current_node):
                        current_node[2][item[1]] = [current_node, [], {}]
                else:
                    current_node[1].append((item[1], int(item[0])))
dirs = defaultdict(int)
# Now do a depth-first search and add up the size of each directory
dfs(root_node, "", dirs)
required = 30000000 - (70000000 - dirs["//"])
print(min([dirs[i] for i in dirs if dirs[i] >= required]))