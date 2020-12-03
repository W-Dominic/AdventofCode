def trees(inc):
    f = open("/home/dom/Programming/AOC_2020/Day3/input.txt")
    f = f.read()
    L= []
    s= ""
    for i in f:
        if(i == "\n"):
            L.append(s)
            s = ""
        else:
                s += i

    #ok now we do something
    start = L[0]
    start = start[0]
    cnt = 0
    trees = 0
    for i in L:
        if (cnt >= len(i)):
            cnt = cnt - (len(i))
            currentS = i[cnt]
            if (currentS == "#"):
                trees +=1 
        else:
            currentS = i[cnt]
            if (currentS == "#"):
                trees += 1
        print(cnt,currentS)
        cnt += inc
        
    return trees

#for going down 2
def weirdTrees(inc): 
    f = open("/home/dom/Programming/AOC_2020/Day3/input.txt")
    f = f.read()
    L= []
    s= ""
    for i in f:
        if(i == "\n"):
            L.append(s)
            s = ""
        else:
                s += i

    #ok now we do something
    start = L[0]
    start = start[0]
    cnt = 0
    trees = 0
    i = 0
    while (i < len(L)):
        if (cnt >= len(L[i])):
            cnt = cnt - (len(L[i]))
            currentS = L[i][cnt]
            if (currentS == "#"):
                trees +=1 
        else:
            currentS = L[i][cnt]
            if (currentS == "#"):
                trees += 1
        print(cnt,currentS)
        cnt += inc
        i += 2
        
    return trees

def main():
    val = trees(1) * trees(3) * trees(5) * trees(7) * weirdTrees(1)
    return val
