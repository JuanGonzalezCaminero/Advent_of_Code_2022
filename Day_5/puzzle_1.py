file = open("input")
crates,instructions = file.read().rstrip().split("\n\n")
crates = crates.split("\n")
crates.pop(-1)
crates = [[i[j:j+4].strip().strip("[]") for j in range(0, len(i), 4)] for i in crates]
crates = [[j for j in i if j!=""] for i in zip(*crates)]
instructions = [[int(j) for j in i.split() if j.isdigit()] for i in instructions.split("\n")]
for inst in instructions:
    for i in range(inst[0]):
        crates[inst[2]-1].insert(0, crates[inst[1]-1].pop(0))
for i in crates:
    print(i[0], end="")
print()