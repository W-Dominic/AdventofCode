f = open("input.txt").read().splitlines()
data = []
for i in f:
    
    data.append(i.split(" "))

hmap = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}
hmap2 = {
    (0,'A'): 3, # S + 0
    (0,'B'): 1, # R 
    (0,'C'): 2, # P   
    (3,'A'): 4, # R + 3
    (3,'B'): 5, # P 
    (3,'C'): 6, # S 
    (6,'A'): 8, # P + 6
    (6,'B'): 9, # S
    (6,'C'): 7, # R  
}

total = 0 
for i in data:
    theirs = i[0]
    res = i[1]

    key = (hmap[res], theirs)
    #print(key)
    score = hmap2[key]
    #print(score)
    total += score
 
print(total)