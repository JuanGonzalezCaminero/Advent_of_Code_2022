file = open("input")
assignments = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in file.readlines()]
widths = [[j[1]-j[0] for j in i] for i in assignments]
result = 0
for i in range(len(widths)):
    larger = 1 if widths[i][1] > widths[i][0] else 0
    smaller = 1 - larger
    if(assignments[i][larger][0] <= assignments[i][smaller][0]):
        if(assignments[i][larger][1] >= assignments[i][smaller][1]):
            result += 1
print(result)