data = open("input.txt").read().splitlines()

curr = 0
sums = []
for i in data:
    if i == "":
        sums.append(curr)
        curr = 0
    else : 
        curr += int(i)
sums.append(curr)

max1 = max(sums)
sums.remove(max1)
max2 = max(sums)
sums.remove(max2)
max3 = max(sums)
sums.remove(max3)
print(max1, max2, max3)
print(max1 + max2 + max3)

