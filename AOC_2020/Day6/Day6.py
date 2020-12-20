def input():
    f = open("/home/dom/Programming/AOC/AOC_2020/Day6/input.txt")
    f = f.read()
    L = []
    s = ""
    for i in f:
        if (i == "\n"):
            L.append(s)
            s=""
        else:
            s += i

    List = []
    Sub  = []
    i = 0
    j = 1
    k = 2
    while (k<len(L)-2):
        s1 = L[i]
        s2 = L[j]
        s3 = L[k]
        if (s3 == "") and (s1 == ""):
            List.append([s2])
        elif (not(s1 == "")) and (s2 == ""): 
            Sub.append([s1])
            List.append(Sub)
            Sub = []
        elif ((not(s2 == "")) and (not(s1 == ""))):
            Sub.append([s1])
        i += 1 
        j += 1
        k += 1
    return List

def unique(L):
    return "".join(set(L))

def pt1():
    L = input()
    sum = 0
    for i in L:
        s = unique(i)
        sum += len(s)
        print (s,sum)
    return sum

def pt2():
    L = input()
    sum = 0 
    for i in L:
        if (len(i) == 1):
            s = i[0][0]
            sum  += len(s)
        elif (len(i) > 1):
            sum += LOLcontains(i)
        else:
            sum += 0
    return sum

def LOLcontains(L):
    common = ""
    for i in L:
        for j in i:
            for k in j:
                if not(k in common):
                    common += k

    for x in common:
        for y in L:
            for z in y:
                if not(x in z):
                    common = common.replace(x,"")
    print (common, len(common))
    return len(common)


