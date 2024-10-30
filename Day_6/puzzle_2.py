file = open("input")
data = file.read().strip()
som_length = 14
answer = som_length
window = [0, som_length]
for i in range(len(data) - som_length):
    if(len(set(data[window[0]:window[1]])) == som_length):
        print(answer)
        exit()
    window = [i+1 for i in window]
    answer+=1