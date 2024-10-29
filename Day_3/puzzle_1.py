file = open("input")
rucksacks = [[i[:int(len(i)/2)], i[int(len(i)/2):]] for i in file.readlines()]

result = 0
for r in rucksacks:
    item = set(r[0]).intersection(set(r[1])).pop()
    # Convert to priority and add to result
    result += 1 + (ord(item) - ord("a") if ord(item) > ord("a") else ord(item) - ord("A") + 26)

print(result)