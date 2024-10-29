file = open("input")
assignments = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in file.readlines()]
result = 0
for i in assignments:
    i.sort(key=lambda a:a[0])
    if(i[0][1]>=i[1][0]):
        result+=1
print(result)