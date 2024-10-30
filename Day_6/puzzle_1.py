file = open("input")
data = file.read().strip()
sop_length = 4
answer = sop_length
window = [0, sop_length]
for i in range(len(data) - sop_length):
    if(len(set(data[window[0]:window[1]])) == sop_length):
        print(answer)
        exit()
    window = [i+1 for i in window]
    answer+=1