file = open("input")
instructions = [i.split() for i in file.readlines()]
for i in instructions: 
    if(len(i)!=1): i[1]=int(i[1])
screen=[40*["."] for i in range(6)]
cycle=0
x=1
while(len(instructions)!=0):
    if(abs(x-(cycle%40))<=1):
        screen[cycle//40][cycle%40] = "#"
    instruction = instructions.pop(0)
    if(instruction[0] == "addx"):
        cycle+=1
        if(abs(x-(cycle%40))<=1):
            screen[cycle//40][cycle%40] = "#"
        x+=instruction[1]
    cycle+=1
for i in screen:
    print("".join(i))