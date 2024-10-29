file = open("input")
rounds = [i.strip().split(" ") for i in file.readlines()]
for i in rounds:
    # Change letters to 1, 2, 3
    i[0] = ord(i[0]) - 64
    i[1] = ord(i[1]) - 87

score = 0

for r in rounds:
    # If win
    if(r[1] == r[0]%3 + 1):
        score += 6
    # If draw
    elif(r[1] == r[0]):
        score += 3
    score += r[1]

print(score)
        