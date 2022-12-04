#parse
f = open("input2.txt").read().splitlines()
data = []
for i in f:
    data.append(i)

total = 0
for i in data:
    parsed = i.split(",")
    #print(parsed)
    nums1 = parsed[0].split("-")
    nums1 = [int(x) for x in nums1]
    nums2 = parsed[1].split("-")
    nums2 = [int(x) for x in nums2]    
    #print(nums1, nums2)
    set1 = [x for x in range(nums1[0], nums1[1]+1)]
    set2 = [x for x in range(nums2[0], nums2[1]+1)]

    intersect = set(set1).intersection(set2)
    if (len(intersect) == len(set1) or len(intersect) == len(set2)):
        total += 1
    
print(total)