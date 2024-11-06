from operator import add
file = open("input")
moves = [l.split() for l in file.readlines()]
for i in moves: 
    i[1] = int(i[1])
    if(i[0] == "R"):
        i[0] = [0, 1]
    elif(i[0] == "L"):
        i[0] = [0, -1]
    elif(i[0] == "D"):
        i[0] = [1, 0]
    elif(i[0] == "U"):
        i[0] = [-1, 0]
visited = {(4,0)}
rope = [[4, 0] for i in range(10)]
for m in moves:
    dir = m[0]
    for i in range(m[1]):
        # Move the head
        rope[0] = list(map(add, rope[0], dir))
        for j in range(len(rope)-1):
            dist_i = rope[j][0]-rope[j+1][0]
            dist_j = rope[j][1]-rope[j+1][1]
            # One coordinate aligned
            if((dist_i==0) != (dist_j==0)):
                # Move the knot straight towards the next
                if(abs(dist_i)>1): rope[j+1][0] += 1 if dist_i > 0 else -1
                if(abs(dist_j)>1): rope[j+1][1] += 1 if dist_j > 0 else -1
            # Both coordinates misaligned
            elif(dist_i!=0 and dist_j!=0):
                # Move the knot diagonally towards the next
                if(abs(dist_i)>1 or abs(dist_j)>1): 
                    rope[j+1][0] += 1 if dist_i > 0 else -1
                    rope[j+1][1] += 1 if dist_j > 0 else -1
        visited.add(tuple(rope[-1]))
print(len(visited))