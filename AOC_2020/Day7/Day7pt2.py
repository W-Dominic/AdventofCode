import re
from Day7pt1 import pt1 as pt1

def input():
    f = open("/home/dom/Programming/AOC/AOC_2020/Day7/input.txt")
    f = f.read().splitlines()
    return f

def pt2():
    L = input()
    #splits into individual colors
    for i in range(len(L)):
        L[i]=L[i].replace("contain","").replace("bag", "").replace(" s ","").replace(" s.","").replace(" s,","").replace(",","").replace(" ", "").replace("noother","").replace(".","")
        L[i]=L[i].replace("1"," 1").replace("2"," 2").replace("3"," 3").replace("4"," 4").replace("5"," 5").replace("6"," 6").replace("7"," 7").replace("8"," 8").replace("9"," 9")           
    #splits based on spaces
    for i in range(len(L)):
        L[i] = L[i].split(" ")
    Lnums = L
    L = pt1()
    return chain(Lnums,["shinygold"])
#recursively finds the elements of the parent given
def find(input,lst):
    if (len(lst) == 0):
        return []
    found = []
    for i in input:
        for j in range(len(i)):
            if (lst[0] in i[0]):
                for k in range (len(i)):
                    if (not(k==0)):
                        found.append(i[k])
    return found + find(input,lst[1:])
#chains together to find the number of bags, iterating through levels recursively 
def chain(input,lst):
    l = set(find(input,lst))
    if (len(l) == 0):
        return 0
    else:
        bags = 0
        for i in l:
            bags += int(i[0]) + int(i[0])*chain(input,[i[1:]])
    return bags
        
