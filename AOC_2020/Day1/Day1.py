def factor():
    f = open("/home/dom/Programming/AOC_2020/input.txt")
    f = f.read().replace("\n"," ")
    Lints= []
    s= ""
    for i in f:
        if(i == " ")and (s != ""):
            Lints.append(int(s))
            s = ""
        else:
            s += i
    

    #okay now we do something
    x =0
    j =0
    sum = 2020
    for i in Lints:
        for j in Lints:
            for k in Lints:
                if (i + j+k) == (sum):
                    return i*j*k


        





