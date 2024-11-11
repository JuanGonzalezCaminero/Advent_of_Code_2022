file = open("input")
instructions = [i.split() for i in file.readlines()]
for i in instructions: 
    if(len(i)!=1): i[1]=int(i[1])
cycle=0
x=1
next_check=20
result=0
while(len(instructions)!=0):
    cycle+=1
    next_check-=1
    if(next_check==0):
        result+=x*cycle
        next_check=40
    instruction = instructions.pop(0)
    if(instruction[0] == "addx"):
        cycle+=1
        next_check-=1
        if(next_check==0):
            result+=x*cycle
            next_check=40
        x+=instruction[1]
print(result)

