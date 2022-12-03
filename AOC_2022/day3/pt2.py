#parse
f = open("input.txt").read().splitlines()
data = []
for i in f:
    data.append(i)

total = 0
i = 0
while (i < (len(data)-2)):
    curr1 = data[i]
    curr2 = data[i+1]
    curr3 = data[i+2]
    shared = set(curr1).intersection(curr2).intersection(curr3)
    print(shared)
    #A = 65
    #a = 97
    ascii = ord(list(shared)[0])
    if (ascii >= 97): 
        total += ascii - 96
    else:
        total += ascii - 38
    i += 3

print(total)