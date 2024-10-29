file = open("input")
rucksacks = [i.strip() for i in file.readlines()]

result = 0
for r in range(0, len(rucksacks), 3):
    item = set(rucksacks[r]).intersection(set(rucksacks[r+1])).intersection(set(rucksacks[r+2])).pop()
    # Convert to priority and add to result
    result += 1 + (ord(item) - ord("a") if ord(item) > ord("a") else ord(item) - ord("A") + 26)

print(result)