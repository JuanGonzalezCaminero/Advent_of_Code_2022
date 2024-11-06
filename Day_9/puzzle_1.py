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
visited = {(0,0)}
head = [0,0]
tail = [0,0]
for m in moves:
    dir = m[0]
    for i in range(m[1]):
        old_head = head
        # Move the head
        head = list(map(add, head, dir))
        # If distance>1, move the tail to the previous position of the head
        if(abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1):
            tail = old_head
            visited.add(tuple(tail))
print(len(visited))