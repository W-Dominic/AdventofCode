#parse
f = open("input.txt").read().splitlines()
data = []
for i in f:
    data.append(i)

total = 0
for i in data:
    x = len(i)//2
    pt1 = i[:x]
    pt2 = i[x:]
    shared = set(pt1).intersection(pt2)
    #A = 65
    #a = 97
    ascii = ord(list(shared[i])
    if (ascii >= 97): 
        total += ascii - 96
    else:
        total += ascii - 40

print(total)