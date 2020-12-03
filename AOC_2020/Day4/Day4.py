def foo():
    f=open("/home/dom/Programming/AOC_2020/Day3/input.txt")
    f = f.read()
    L= []
    s= ""
    for i in f:
        if(i == "\n"):
            L.append(s)
            s = ""
        else:
        s += i
