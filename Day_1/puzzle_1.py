file = open("input")
data = map(lambda a: [int(j) for j in a], [i.split("\n") for i in file.read().split("\n\n")])
calories = [sum(i) for i in data]
print(max(calories))