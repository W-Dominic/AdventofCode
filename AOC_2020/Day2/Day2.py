def foo():
    #reads input
    f = open("/home/dom/Programming/AOC_2020/Day2/input.txt")
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
    valid = 0

    for i in L:
        s = i.split("-")
        min = s[0]
        s2 = s[1].split(" ")
        max = int(s2[0])
        min = int(min)

        char = s2[1].replace(":", "")
        passwd = s2[2]
        
        #PYTHON HAS XOR
        if (passwd[min-1] == char) ^ (passwd[max-1] == char):
            valid +=1 
    
    return valid

        

