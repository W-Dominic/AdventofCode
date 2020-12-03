from functools import reduce

def add():
    f = open("/home/dom/Programming/AOC_2018/input.txt")
    f = (f.read().replace("+","").replace("\n"," "))
    s = ""
    Lints =[]
    for i in f:
        if(i == " ")and (s != ""):
            Lints.append(int(s)) 
            s = ""
        else:
            s += i
    
    sum = 0
    sums=[]
    for k in Lints:
        sum += k
        sums.append(sum)
        if (sums.count(sum) == 2):
            return sum
    return 0
    
