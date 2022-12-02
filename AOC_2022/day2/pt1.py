f = open("input.txt").read().splitlines()
data = []
for i in f:
    
    data.append(i.split(" "))

hmap = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3 
}

total = 0 
for i in data:
    score = 0
    yours = i[1]
    theirs = i[0]
    score += hmap[yours]

    if (theirs == "A" and yours == "X") or (theirs == "B" and yours == "Y") or (theirs == "C" and yours == "Z"):
        score += 3 
    elif (theirs == "B" and yours == "Z") or (theirs == "C" and yours == "X") or (theirs == "A" and yours == "Y"):
        score += 6
    total += score
    print(score)

print(total)