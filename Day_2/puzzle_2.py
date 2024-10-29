file = open("input")
rounds = [i.strip().split(" ") for i in file.readlines()]

for i in rounds:
    # Change letters to 1, 2, 3
    i[0] = ord(i[0]) - 64
    i[1] = ord(i[1]) - 87

score = 0

for r in rounds:
    # Lose
    if(r[1] == 1):
        score += r[0] - 1 if r[0] - 1 > 0 else 3
    # Draw
    elif(r[1] == 2):
        score += 3 + r[0]
    # Win
    elif(r[1] == 3):
        score += 6 + (r[0] % 3) + 1

print(score)
        