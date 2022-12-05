def move_procedure(stacks, command):
    res = [int(i) for i in command.split() if i.isdigit()]
    #print(res)
    
    num = res[0]
    FROM = res[1]-1
    TARGET = res[2]-1

    moved = []
    while(num > 0):
        moved.append(stacks[FROM][-1])
        stacks[FROM].pop()
        num -= 1
    # move num from FROM to TARGET
    moved.reverse()
    stacks[TARGET] = stacks[TARGET] + moved
    return stacks

# for every 4 spaces in a row, make 1
def normalize(lst):
    count = 0
    res = []
    for i in lst:
        if count == 3 and i == "":
            count = 0
            res.append("")  
        elif i == "":
            count += 1
        else:
            count = 0
            res.append(i)
    return res

if __name__ == "__main__":
    f = open("input.txt").read().splitlines()
    data = []
    for i in f:
        
        data.append(i.split(" "))

    cache = []
    commands = []
    for i in range(len(data)):
        if data[i][0] == "move":
            commands = data[i:] 
            break
        cache.append(data[i])
    
    #find out how many stacks
    stacks = []
    for i in cache[-2]:
        if i != "":
            stacks.append([])

    #fill the stacks
    i = len(cache)-3
    while(i >= 0):
        res = normalize(cache[i])
        for x in range(len(res)):
            if res[x] != "":
                stacks[x].append(res[x][1])
        i -= 1
    
    print(stacks)
    #loop through commands and update stack
    #print(commands)
    for c in commands:   
        cmd = " ".join(c)
        stacks = move_procedure(stacks, cmd)
    
    for i in stacks:
        print(i[-1], end="")
    print("")
